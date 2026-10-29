"""Explicit queries of research information models, never production recommendations."""
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys

import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.crawler.market_clock import KST, completed_price_cutoff
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.ohlcv_information import OHLCV_FEATURES, add_ohlcv_information
from src.features.price_learning_dataset import FEATURES, load_snapshots, make_features
from src.models.price_forecaster import json_text, logits, resolve_stock


def research_forecast(bundle, snapshots, code, arm='enriched', now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware inference is required.')
    now = now.astimezone(KST)
    metadata = bundle['metadata']
    if (metadata.get('schema') != 'research_ohlcv_information_v1'
            or metadata.get('recommendation_gate_passed') is not False
            or snapshots.attrs.get('feature_version') != HISTORY_FEATURE_VERSION):
        raise ValueError('This command only accepts the completed-history OHLCV research bundle.')
    if pd.Timestamp(metadata['trained_at']) > pd.Timestamp(now) or pd.Timestamp(metadata['as_of']).date() > now.date():
        raise ValueError('Cannot use a model before its fitting time.')
    columns = FEATURES + OHLCV_FEATURES if arm == 'enriched' else FEATURES
    model = bundle['models'][arm]
    if model['features'] != columns:
        raise ValueError('Research feature schema mismatch.')
    cutoff = pd.Timestamp(completed_price_cutoff(now))
    selected = snapshots[snapshots.stock_code.eq(code) & snapshots.signal_date.le(cutoff)
                         & snapshots.snapshot_date.le(cutoff)].copy()
    if selected.empty:
        raise ValueError('No completed history for this stock.')
    selected = add_ohlcv_information(selected)
    selected[FEATURES] = make_features(selected)
    row = selected.sort_values('signal_date').tail(1)
    if row[columns].isna().any(axis=None) or row.volume_ratio_20d.iloc[0] <= 0:
        raise ValueError('Insufficient active completed-price features.')
    with threadpool_limits(limits=2):
        probability = float(model['calibrator'].predict_proba(logits(model['classifier'], row[columns]))[0, 1])
        returns = float(model['regressor'].predict(row[columns])[0])
    if not np.isfinite(probability + returns) or not 0 <= probability <= 1:
        raise ValueError('Nonfinite research output.')
    origin = pd.Timestamp(row.signal_date.iloc[0])
    return dict(stock_code=code, signal_date=str(origin.date()), as_of=now.date().isoformat(),
                horizon_sessions=5, cost_assumption=.003, probability_above_cost=round(probability, 6),
                predicted_close_return=round(returns, 6), model_arm=arm,
                model_status='STALE_DATA' if (now.date() - origin.date()).days > 7 else 'RESEARCH_ONLY',
                recommendation='ABSTAIN', recommendation_ko='추천 보류',
                note='Experimental model estimate, not validated accuracy or investment advice. No production promotion.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run-dir', type=Path, required=True)
    parser.add_argument('--data-root', type=Path, required=True)
    parser.add_argument('--stock', required=True)
    parser.add_argument('--arm', choices=['baseline', 'enriched'], default='enriched')
    args = parser.parse_args()
    try:
        bundle = joblib.load(args.run_dir / 'research_models.joblib')
        prices, source = load_snapshots(args.data_root)
        if source.get('skipped_files') or prices.attrs.get('history_provenance', {}).get('failed_stocks', 0):
            raise ValueError('Incomplete input universe; finish collection first.')
        code = resolve_stock(args.stock, [ROOT, args.data_root])
        print(json_text(research_forecast(bundle, prices, code, args.arm)))
    except (ValueError, FileNotFoundError) as error:
        parser.exit(2, str(error) + '\n')
    except Exception as error:
        parser.exit(2, 'Research query failed: ' + type(error).__name__ + '\n')


if __name__ == '__main__':
    main()
