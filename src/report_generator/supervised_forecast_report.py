"""Export public, whitelisted ML forecasts without exposing model files or credentials."""
from __future__ import annotations

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import sys
import tempfile

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import grade_predictions
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.models.price_forecaster import (
    block_bootstrap_lower, forecast_row, json_text, load_bundle,
    load_model_snapshots, stock_catalog,
)


def forward_evidence(metadata, prices, ledger_dir, as_of, now):
    records, unreadable = [], 0
    for path in sorted(Path(ledger_dir).glob('ml_price_forecasts_forward_*.csv')):
        if '_eval_' in path.name:
            continue
        try:
            frame = pd.read_csv(path, dtype={'stock_code': str})
            required = {'model_dataset_sha256', 'model_trained_at', 'recorded_at', 'prediction_id',
                        'stock_code', 'signal_date', 'cost_assumption', 'horizon_sessions',
                        'probability_above_cost', 'predicted_close_return', 'validation_base_rate', 'origin_close'}
            if not required.issubset(frame):
                unreadable += 1
                continue
            matching = frame.model_dataset_sha256.eq(metadata['dataset_sha256']) & frame.model_trained_at.eq(metadata['trained_at'])
            records.append(frame[matching].copy())
        except (OSError, ValueError, pd.errors.ParserError):
            unreadable += 1
    ledger = pd.concat(records, ignore_index=True) if records else pd.DataFrame()
    result = {'recorded': len(ledger), 'resolved': 0, 'pending': 0, 'signal_dates': 0,
              'auc': None, 'brier': None, 'baseline_brier': None,
              'policy_cases': 0, 'policy_dates': 0, 'policy_net_lower_95': None,
              'integrity_issues': unreadable, 'passed': False}
    if ledger.empty:
        return result
    recorded = pd.to_datetime(ledger.recorded_at, errors='coerce', utc=True)
    trained = pd.Timestamp(metadata['trained_at'])
    valid = recorded.notna() & recorded.le(pd.Timestamp(now)) & recorded.ge(trained)
    valid &= pd.to_numeric(ledger.cost_assumption, errors='coerce').eq(metadata['cost_assumption'])
    valid &= pd.to_numeric(ledger.horizon_sessions, errors='coerce').eq(metadata['horizon_sessions'])
    valid &= pd.to_datetime(ledger.signal_date, errors='coerce').ge(pd.Timestamp(metadata['as_of']))
    valid &= ~ledger.duplicated(['stock_code', 'signal_date'], keep=False)
    valid &= ledger.prediction_id.notna() & ~ledger.prediction_id.duplicated(keep=False)
    result['integrity_issues'] += int((~valid).sum())
    ledger = ledger[valid].copy()
    if ledger.empty:
        return result
    try:
        summary, graded = grade_predictions(ledger, prices, as_of)
        resolved = graded[graded.outcome_state.eq('resolved')]
        result.update(resolved=summary['resolved'], pending=int(graded.outcome_state.eq('pending').sum()),
                      signal_dates=summary['resolved_signal_dates'], auc=summary['auc'],
                      brier=summary['brier_score'], baseline_brier=summary['frozen_baseline_brier'])
        result['integrity_issues'] += int((~graded.outcome_state.isin(['resolved', 'pending'])).sum())
        result['integrity_issues'] += int(resolved.get('origin_price_revised', pd.Series(dtype=bool)).fillna(False).sum())
        selected = resolved[(resolved.probability_above_cost.astype(float) >= metadata['probability_threshold'])
                            & (resolved.predicted_close_return.astype(float) > metadata['cost_assumption'])].copy()
        daily = (selected.observed_return.astype(float) - metadata['cost_assumption']).groupby(selected.signal_date).mean()
        result.update(policy_cases=len(selected), policy_dates=len(daily),
                      policy_net_lower_95=block_bootstrap_lower(daily.to_numpy()))
        result['passed'] = bool(result['integrity_issues'] == 0 and result['resolved'] >= 200
                                and result['signal_dates'] >= 60 and result['policy_cases'] >= 100
                                and result['policy_dates'] >= 20 and result['auc'] is not None
                                and result['auc'] >= .55 and result['brier'] < result['baseline_brier']
                                and result['policy_net_lower_95'] is not None and result['policy_net_lower_95'] > 0)
    except (ValueError, KeyError, TypeError, OverflowError):
        result['integrity_issues'] += 1
        result['passed'] = False
    return result


def build_payload(bundle, snapshots, roots, ledger_dir, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Forecast publication requires a timezone-aware clock.')
    now = now.astimezone(KST)
    metadata = bundle['metadata']
    if pd.Timestamp(metadata['trained_at']) > pd.Timestamp(now):
        raise ValueError('A model cannot publish predictions before it was trained.')
    if metadata['feature_version'] != HISTORY_FEATURE_VERSION:
        raise ValueError('The public ML panel requires the coherent completed-history absolute-return model.')
    if snapshots.attrs.get('feature_version') != HISTORY_FEATURE_VERSION:
        raise ValueError('Do not mix snapshot-price inputs with completed-history models.')
    cutoff = pd.Timestamp(completed_price_cutoff(now))
    prices = snapshots[(snapshots.signal_date <= cutoff) & (snapshots.snapshot_date <= cutoff)].copy()
    if prices.empty or prices.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('No unique completed price inputs.')
    aliases = {}
    for name, codes in stock_catalog(roots).items():
        for code in codes:
            aliases.setdefault(code, []).append(name)
    evidence = forward_evidence(metadata, prices, ledger_dir, cutoff, now)
    historical_gate = bool(metadata['test']['recommendation_gate_passed'])
    ready = historical_gate and evidence['passed']
    rows, skipped = [], 0
    latest = str(prices.signal_date.max().date())
    for _, row in prices.sort_values(['signal_date', 'stock_code']).drop_duplicates('stock_code', keep='last').iterrows():
        try:
            prediction = forecast_row(bundle, row, now.date())
        except ValueError:
            skipped += 1
            continue
        code = prediction['stock_code']
        names = sorted(set(aliases.get(code, [])))
        recommended = ready and prediction['recommendation'] == 'MONITOR_CANDIDATE' and prediction['signal_date'] == latest
        rows.append({'stock_code': code, 'stock_name': names[0] if names else code, 'aliases': names,
                     'signal_date': prediction['signal_date'], 'probability': prediction['probability_above_cost'],
                     'predicted_return': prediction['predicted_close_return'],
                     'stale': prediction['status'] == 'STALE_DATA', 'recommended': bool(recommended)})
    rows.sort(key=lambda row: (-row['probability'], row['stock_code']))
    if not rows:
        raise ValueError('No eligible ML forecasts; the last published data was not replaced.')
    current = [row for row in rows if not row['stale'] and row['signal_date'] == latest]
    recommendations = [row['stock_code'] for row in current if row['recommended']][:20]
    state = 'validated' if ready else 'research'
    if (pd.Timestamp(now.date()) - pd.Timestamp(latest)).days > 7:
        state = 'stale'
    return {'schema': 'public_price_forecast_v1', 'generated_at': now.isoformat(), 'price_date': latest,
            'model_state': state, 'recommendation_enabled': bool(ready and state != 'stale'),
            'horizon_sessions': int(metadata['horizon_sessions']), 'cost_assumption': float(metadata['cost_assumption']),
            'stock_count': len(rows), 'skipped_count': skipped,
            'forward': {key: evidence[key] for key in ['recorded', 'resolved', 'pending', 'signal_dates', 'passed', 'integrity_issues']},
            'recommendations': recommendations, 'watchlist': [row['stock_code'] for row in current[:5]], 'stocks': rows}


def write_payload(payload, output):
    output = Path(output)
    if payload.get('schema') == 'public_price_forecast_v1':
        new_date = datetime.strptime(payload['price_date'], '%Y-%m-%d').date()
        old_date = None
        try:
            previous = json.loads(output.read_text(encoding='utf-8'))
            if previous.get('schema') == 'public_price_forecast_v1':
                old_date = datetime.strptime(previous['price_date'], '%Y-%m-%d').date()
        except (OSError, ValueError, KeyError, TypeError):
            pass
        if old_date is not None and new_date < old_date:
            raise ValueError('Older price data cannot replace the current public forecast. Use a separate output for historical research.')
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', dir=output.parent, delete=False, encoding='utf-8') as handle:
            temporary = Path(handle.name)
            handle.write(json_text(payload) + '\n')
        os.replace(temporary, output)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description='Publish completed-history ML predictions for the dashboard.')
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_forecaster_expanded')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--ledger-dir', type=Path, default=ROOT / 'data/predictions')
    parser.add_argument('--output', type=Path, default=ROOT / 'docs/price_model.json')
    args = parser.parse_args()
    try:
        bundle = load_bundle(args.model_dir)
        data_root = args.data_root or Path(bundle['metadata']['data_root'])
        prices, source = load_model_snapshots(data_root, bundle['metadata'])
        if source.get('skipped_files'):
            raise ValueError('Some input series failed verification; public publication aborted.')
        payload = build_payload(bundle, prices, [ROOT, data_root], args.ledger_dir)
        write_payload(payload, args.output)
        print(json_text({key: payload[key] for key in ['model_state', 'price_date', 'stock_count', 'skipped_count', 'forward']}))
    except (FileNotFoundError, ValueError) as error:
        parser.exit(2, str(error) + '\n')
    except Exception as error:
        parser.exit(2, 'ML report failed: ' + type(error).__name__ + '\n')


if __name__ == '__main__':
    main()
