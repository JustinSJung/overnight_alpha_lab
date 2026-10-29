"""Immutable, timely forward records for the separately selected research model."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd

from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import valid_record_time
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.price_learning_dataset import load_snapshots
from src.models.price_forecaster import json_text
from src.models.selected_price_model import ROOT, load_selected, predict_values, prepare_selected_features


def freeze_selected(model_dir, data_root, output_dir, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware recording time required.')
    now = now.astimezone(KST)
    bundle = load_selected(model_dir, now)
    metadata = bundle['metadata']
    digest = metadata.get('dataset_sha256', '')
    if (len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest)
            or metadata.get('horizon_sessions') != 5 or metadata.get('cost_assumption') != .003):
        raise ValueError('A fingerprinted five-session research bundle is required.')
    raw, source = load_snapshots(data_root or metadata['data_root'])
    if (raw.attrs.get('feature_version') != HISTORY_FEATURE_VERSION or source.get('skipped_files')
            or raw.attrs.get('history_provenance', {}).get('failed_stocks', 0)):
        raise ValueError('Complete verified OHLCV history is required.')
    cutoff = pd.Timestamp(completed_price_cutoff(now))
    raw = raw[raw.signal_date.le(cutoff) & raw.snapshot_date.le(cutoff)].copy()
    if raw.empty:
        raise ValueError('No completed observations available.')
    origin = raw.signal_date.max()
    if pd.Timestamp(metadata['as_of']) >= origin:
        raise ValueError('Forward signal must follow the model fit as-of date.')
    if not valid_record_time(origin, pd.Timestamp(now)):
        return {'status': 'outside_recording_window_no_backdated_forecast', 'frozen_predictions': 0}
    latest = prepare_selected_features(raw, bundle['features'], metadata.get('market_min_stocks', 100))
    latest = latest[latest.signal_date.eq(origin)].copy()
    valid = np.isfinite(latest[bundle['features']]).all(axis=1) & latest.close.gt(0) & latest.volume_ratio_20d.gt(0)
    latest = latest[valid].sort_values('stock_code').reset_index(drop=True)
    if latest.empty or latest.stock_code.duplicated().any():
        raise ValueError('No unique eligible stock observations.')
    p, point, low, high = predict_values(bundle, latest[bundle['features']])
    ledger = latest[['stock_code', 'signal_date']].copy()
    ledger['signal_date'] = ledger.signal_date.dt.strftime('%Y-%m-%d')
    ledger['origin_close'] = latest.close.to_numpy()
    ledger['recorded_at'] = now.isoformat()
    ledger['as_of'] = now.date().isoformat()
    ledger['horizon_sessions'], ledger['cost_assumption'] = 5, .003
    ledger['probability_above_cost'], ledger['predicted_close_return'] = p, point
    ledger['empirical_return_lower'], ledger['empirical_return_upper'] = low, high
    ledger['model_dataset_sha256'], ledger['model_trained_at'] = digest, metadata['trained_at']
    ledger['validation_base_rate'] = bundle['baseline_probability']
    ledger['model_family'] = bundle['selected_name']
    ledger['status'], ledger['recommendation'] = 'RESEARCH_ONLY', 'ABSTAIN'
    ledger['prediction_id'] = [hashlib.sha256('|'.join(
        [code, str(origin.date()), digest, metadata['trained_at']]).encode()).hexdigest()[:20]
        for code in ledger.stock_code]
    key = hashlib.sha256((digest + metadata['trained_at']).encode()).hexdigest()[:16]
    output = Path(output_dir) / f'ml_selected_forward_{origin:%Y%m%d}_{key}.csv'
    output.parent.mkdir(parents=True, exist_ok=True)
    # Original predictions are immutable, including a repeated same-model/same-day run.
    with output.open('x', encoding='utf-8-sig') as handle:
        ledger.to_csv(handle, index=False)
    return {'status': 'awaiting_future_outcomes', 'frozen_predictions': len(ledger), 'ledger': str(output)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_forecaster_selected')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'data/predictions')
    args = parser.parse_args()
    try:
        print(json_text(freeze_selected(args.model_dir, args.data_root, args.output_dir)))
    except FileExistsError:
        parser.exit(2, 'Original same-day research predictions already exist; preserved without overwrite.\n')
    except (ValueError, FileNotFoundError) as error:
        parser.exit(2, str(error) + '\n')
    except Exception as error:
        parser.exit(2, 'Research forward recording failed: ' + type(error).__name__ + '\n')


if __name__ == '__main__':
    main()
