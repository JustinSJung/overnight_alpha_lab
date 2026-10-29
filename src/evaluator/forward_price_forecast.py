"""Freeze forward model predictions, then grade them separately as prices arrive."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd
from sklearn.metrics import brier_score_loss, roc_auc_score

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.crawler.market_clock import KST, completed_price_cutoff
from src.features.price_learning_dataset import load_snapshots
from src.models.price_forecaster import forecast_row, json_text, load_bundle, load_model_snapshots


def valid_record_time(origin, issued, first_session=None):
    if issued.tzinfo is None:
        return False
    origin = pd.Timestamp(origin).normalize()
    first_session = pd.Timestamp(first_session) if first_session is not None else origin + pd.offsets.BDay(1)
    closed = origin.tz_localize(KST) + pd.Timedelta(hours=16)
    next_open = first_session.normalize().tz_localize(KST) + pd.Timedelta(hours=9)
    return closed <= issued < next_open


def freeze_predictions(bundle, prices, output, now=None):
    now = now or datetime.now(KST)
    now = now.astimezone(KST)
    origin = prices['signal_date'].max()
    if origin.date() > completed_price_cutoff(now) or not valid_record_time(origin, pd.Timestamp(now)):
        raise ValueError('Record after the signal close buffer and before the next session opens.')
    rows = []
    for _, row in prices[prices['signal_date'] == origin].iterrows():
        try:
            prediction = forecast_row(bundle, row, now.date())
        except ValueError:
            continue
        identity = '|'.join([prediction['stock_code'], str(origin.date()),
                             bundle['metadata']['dataset_sha256'], bundle['metadata']['trained_at']])
        prediction.update({
            'prediction_id': hashlib.sha256(identity.encode()).hexdigest()[:20],
            'recorded_at': now.isoformat(), 'origin_close': float(row['close']),
            'model_dataset_sha256': bundle['metadata']['dataset_sha256'],
        })
        rows.append(prediction)
    if not rows:
        raise ValueError('No eligible fresh stock predictions to freeze.')
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Existing forecasts are never overwritten, including same-day reruns.
    with output.open('x', encoding='utf-8-sig') as handle:
        pd.DataFrame(rows).sort_values('stock_code').to_csv(handle, index=False)
    return pd.DataFrame(rows)


def grade_predictions(ledger, prices, as_of):
    prices = prices[prices['signal_date'] <= pd.Timestamp(as_of)].copy()
    calendar = sorted(prices['signal_date'].unique())
    rows = []
    for _, row in ledger.iterrows():
        result = row.to_dict()
        result.update({'outcome_state': 'pending', 'target_date': None, 'observed_return': None, 'target': None})
        origin = pd.to_datetime(row['signal_date'])
        issued = pd.Timestamp(row['recorded_at'])
        later = [pd.Timestamp(day) for day in calendar if pd.Timestamp(day) > origin]
        if not valid_record_time(origin, issued, later[0] if later else None):
            result['outcome_state'] = 'invalid_record_time'
            rows.append(result)
            continue
        horizon = int(row['horizon_sessions'])
        if horizon < 1:
            result['outcome_state'] = 'invalid_horizon'
        elif len(later) >= horizon:
            target_date = later[horizon - 1]
            stock = prices[prices['stock_code'].astype(str) == str(row['stock_code'])].set_index('signal_date')
            if origin not in stock.index or target_date not in stock.index:
                result['outcome_state'] = 'missing_prices'
            else:
                start = float(stock.loc[origin, 'close'])
                end = float(stock.loc[target_date, 'close'])
                if start <= 0 or not np.isfinite(start + end):
                    result['outcome_state'] = 'invalid_prices'
                else:
                    observed = end / start - 1
                    result.update({'outcome_state': 'resolved', 'target_date': str(target_date.date()),
                                   'observed_return': observed, 'target': int(observed > float(row['cost_assumption'])),
                                   'origin_price_revised': not np.isclose(start, float(row['origin_close']), rtol=1e-4)})
        rows.append(result)
    graded = pd.DataFrame(rows)
    resolved = graded[graded['outcome_state'] == 'resolved']
    summary = {'recorded_predictions': len(graded), 'resolved': len(resolved),
               'states': graded['outcome_state'].value_counts().to_dict(),
               'resolved_signal_dates': int(resolved['signal_date'].nunique()),
               'auc': None, 'brier_score': None, 'frozen_baseline_brier': None,
               'status': 'awaiting_future_outcomes' if resolved.empty else 'forward_results_available'}
    if not resolved.empty:
        y = resolved['target'].astype(int)
        probability = resolved['probability_above_cost'].astype(float)
        summary['brier_score'] = float(brier_score_loss(y, probability))
        summary['frozen_baseline_brier'] = float(brier_score_loss(y, resolved['validation_base_rate'].astype(float)))
        if y.nunique() == 2:
            summary['auc'] = float(roc_auc_score(y, probability))
    return summary, graded


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['freeze', 'grade'])
    parser.add_argument('--data-root', type=Path, required=True)
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_forecaster_history')
    parser.add_argument('--ledger', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.command == 'freeze':
        bundle = load_bundle(args.model_dir)
        prices, _ = load_model_snapshots(args.data_root, bundle['metadata'])
        frozen = freeze_predictions(bundle, prices, args.output)
        print(json_text({'frozen_predictions': len(frozen), 'ledger': args.output, 'status': 'awaiting_future_outcomes'}))
    else:
        prices, _ = load_snapshots(args.data_root)
        if args.ledger is None:
            parser.error('grade requires --ledger')
        if args.output.resolve() == args.ledger.resolve():
            parser.error('Grading must not overwrite the original prediction ledger.')
        ledger = pd.read_csv(args.ledger, dtype={'stock_code': str})
        summary, graded = grade_predictions(ledger, prices, completed_price_cutoff())
        args.output.parent.mkdir(parents=True, exist_ok=True)
        graded.to_csv(args.output, index=False, encoding='utf-8-sig')
        print(json_text(summary))


if __name__ == '__main__':
    main()
