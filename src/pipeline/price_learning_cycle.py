"""Publish current forecasts, freeze only timely originals, grade separately."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import freeze_predictions, grade_predictions, valid_record_time
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.models.price_forecaster import json_text, load_bundle, load_model_snapshots
from src.report_generator.supervised_forecast_report import build_payload, write_payload


def run_cycle(data_root, model_dir, ledger_dir, public_output, report_path, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('A timezone-aware recording clock is required.')
    now = now.astimezone(KST)
    bundle = load_bundle(model_dir)
    metadata = bundle['metadata']
    if metadata['feature_version'] != HISTORY_FEATURE_VERSION or pd.Timestamp(metadata['trained_at']) > pd.Timestamp(now):
        raise ValueError('Use an already-trained completed-history absolute forecast model.')
    prices, source = load_model_snapshots(data_root, metadata)
    if prices.attrs.get('feature_version') != HISTORY_FEATURE_VERSION:
        raise ValueError('Forward recording requires coherent completed-history inputs.')
    provenance = prices.attrs.get('history_provenance', {})
    if source.get('skipped_files') or provenance.get('failed_stocks', 0) or provenance.get('unreadable_stocks', 0):
        raise ValueError('Incomplete collection; preserve prior publication and retry failed stocks first.')
    cutoff = pd.Timestamp(completed_price_cutoff(now))
    prices = prices[(prices.signal_date <= cutoff) & (prices.snapshot_date <= cutoff)].copy()
    if prices.empty:
        raise ValueError('No completed price inputs.')
    origin = prices.signal_date.max()
    key = hashlib.sha256((metadata['dataset_sha256'] + '|' + metadata['trained_at']).encode()).hexdigest()[:12]
    ledger_dir = Path(ledger_dir)
    ledger = ledger_dir / f'ml_price_forecasts_forward_model_{origin:%Y%m%d}_{key}.csv'
    recorded = 0
    if ledger.exists():
        previous = pd.read_csv(ledger, dtype={'stock_code': str})
        if (previous.empty or not previous.model_dataset_sha256.eq(metadata['dataset_sha256']).all()
                or not previous.model_trained_at.eq(metadata['trained_at']).all()
                or not pd.to_datetime(previous.signal_date).eq(origin).all()):
            raise ValueError('Existing original ledger has conflicting model/date identity; it was not overwritten.')
        record_state = 'already_recorded_original_preserved'
    elif valid_record_time(origin, pd.Timestamp(now)):
        frozen = freeze_predictions(bundle, prices, ledger, now)
        recorded = len(frozen)
        record_state = 'new_predictions_frozen_before_next_open'
    else:
        record_state = 'outside_recording_window_no_backdated_forecast'
    graded_files = 0
    if ledger_dir.exists():
        for path in sorted(ledger_dir.glob('ml_price_forecasts_forward_*.csv')):
            if '_eval_' in path.name:
                continue
            frame = pd.read_csv(path, dtype={'stock_code': str})
            if not {'model_dataset_sha256', 'model_trained_at'}.issubset(frame):
                continue
            matching = frame.model_dataset_sha256.eq(metadata['dataset_sha256']) & frame.model_trained_at.eq(metadata['trained_at'])
            if not matching.any():
                continue
            _, graded = grade_predictions(frame[matching].copy(), prices, cutoff)
            output = path.with_name(path.name.replace('ml_price_forecasts_forward_', 'ml_price_forecasts_forward_eval_', 1))
            temporary = output.with_suffix('.csv.tmp')
            graded.to_csv(temporary, index=False, encoding='utf-8-sig')
            temporary.replace(output)
            graded_files += 1
    payload = build_payload(bundle, prices, [ROOT, Path(data_root)], ledger_dir, now)
    write_payload(payload, public_output)
    summary = dict(generated_at=now.isoformat(), price_date=str(origin.date()), stock_count=payload['stock_count'],
                   recording_state=record_state, new_frozen_predictions=recorded, graded_files=graded_files,
                   forward=payload['forward'], recommendation_enabled=payload['recommendation_enabled'],
                   note='No backdating, original overwrites, model promotion, or orders. Re-run after fresh completed close and before next open.')
    write_payload(summary, report_path)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-root', type=Path, required=True)
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_forecaster_expanded')
    parser.add_argument('--ledger-dir', type=Path, default=ROOT / 'data/predictions')
    parser.add_argument('--output', type=Path, default=ROOT / 'docs/price_model.json')
    parser.add_argument('--report-path', type=Path, default=ROOT / 'reports/daily_review' / (datetime.now(KST).date().isoformat() + '_price_learning_cycle.json'))
    args = parser.parse_args()
    try:
        summary = run_cycle(args.data_root, args.model_dir, args.ledger_dir, args.output, args.report_path)
        print(json_text(summary))
    except (ValueError, FileNotFoundError) as error:
        parser.exit(2, str(error) + '\n')
    except Exception as error:
        parser.exit(2, 'Price learning cycle failed: ' + type(error).__name__ + '\n')


if __name__ == '__main__':
    main()
