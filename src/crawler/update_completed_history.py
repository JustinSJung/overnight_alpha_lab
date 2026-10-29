"""Create a new completed-history snapshot; retain the original research snapshot."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.crawler.kis_client import KISClient, KISCredentialsMissing
from src.crawler.market_clock import completed_price_cutoff
from src.crawler.price_learning_history import PacedHistoryClient, fetch_history, file_digest, reusable_entry, save_manifest


def merge_completed_series(client, code, old, start, end):
    old = old.copy()
    old['date'] = pd.to_datetime(old.date).dt.normalize()
    overlap_start = max(pd.Timestamp(start), old.date.max() - pd.Timedelta(days=60))
    fresh = client.get_daily_ohlcv(code, overlap_start.strftime('%Y%m%d'), pd.Timestamp(end).strftime('%Y%m%d'))
    if fresh.empty:
        raise ValueError('No update returned; cached observations are not silently treated as current.')
    fresh = fresh.copy()
    fresh['date'] = pd.to_datetime(fresh.date, errors='coerce').dt.normalize()
    if fresh.date.isna().any() or fresh.date.duplicated().any() or not fresh.date.between(overlap_start, pd.Timestamp(end)).all():
        raise ValueError('Invalid or out-of-range update dates.')
    shared = old.merge(fresh, on='date', suffixes=('_old', '_new'), validate='one_to_one')
    revised = pd.Series(False, index=shared.index)
    for column in ['open', 'high', 'low', 'close']:
        if not shared.empty:
            a, b = pd.to_numeric(shared[column + '_old']), pd.to_numeric(shared[column + '_new'])
            revised |= ~np.isclose(a, b, rtol=1e-7, atol=1e-4)
    terminal = old.date.max()
    older = shared.date.lt(terminal)
    terminal_only = (bool(revised.any()) and shared.loc[revised, 'date'].eq(terminal).all()
                     and older.sum() >= 5 and not revised[older].any())
    if shared.empty or (revised.any() and not terminal_only):
        # Mixing pre/post corporate-action scales can manufacture momentum and labels.
        result = fetch_history(client, code, start, end, pause=0)
        method = 'full_refresh_after_overlap_revision'
    else:
        result = pd.concat([old, fresh], ignore_index=True).drop_duplicates('date', keep='last').sort_values('date')
        method = 'verified_older_overlap_terminal_revision' if terminal_only else 'verified_overlap_update'
    if result.empty or result.date.max() < old.date.max():
        raise ValueError('Updated history regressed or is empty.')
    if result.date.duplicated().any() or not result.date.between(pd.Timestamp(start), pd.Timestamp(end)).all():
        raise ValueError('Invalid completed history range.')
    if not old.date.isin(result.date).all():
        raise ValueError('Full refresh dropped previously verified historical dates.')
    numeric = result[['open', 'high', 'low', 'close', 'volume']].apply(pd.to_numeric, errors='coerce')
    active = numeric.volume.gt(0)
    valid_active = (numeric.open.gt(0) & numeric.low.gt(0) & numeric.high.ge(numeric[['open', 'close']].max(axis=1))
                    & numeric.low.le(numeric[['open', 'close']].min(axis=1)))
    if (not np.isfinite(numeric).all(axis=None) or not numeric.close.gt(0).all()
            or not numeric[['open', 'high', 'low', 'volume']].ge(0).all(axis=None)
            or (active & ~valid_active).any()):
        raise ValueError('Invalid OHLCV observations.')
    result['stock_code'] = code
    if revised.any():
        result.attrs['overlap_revision'] = dict(
            changed_price_dates=[str(value.date()) for value in shared.loc[revised, 'date']],
            previous_terminal_date=str(terminal.date()), older_verified_dates=int(older.sum()),
            terminal_only=bool(terminal_only),
            note='Provider revision observed; not proof of error, finalization time or corporate-action cause')
    return result, method


def update_history(client, parent_dir, output_dir, end, workers=8):
    parent_dir, output_dir = Path(parent_dir).resolve(), Path(output_dir).resolve()
    if parent_dir == output_dir or parent_dir in output_dir.parents or output_dir in parent_dir.parents:
        raise ValueError('Update output must be separate from the preserved parent snapshot.')
    if not 1 <= workers <= 16 or pd.Timestamp(end).date() > completed_price_cutoff():
        raise ValueError('Use 1-16 workers and a completed-bar end date.')
    parent_path = parent_dir / 'history_manifest.json'
    parent = json.loads(parent_path.read_text())
    if (not parent.get('completed_bars_only') or not parent.get('collection_complete')
            or parent.get('source') != 'kis_adjusted_daily' or pd.Timestamp(end) < pd.Timestamp(parent['end'])):
        raise ValueError('A complete compatible parent snapshot is required.')
    codes = parent['requested_codes']
    parents = {entry['stock_code']: entry for entry in parent['stocks']}
    if len(set(codes)) != len(codes) or set(parents) != set(codes):
        raise ValueError('Parent universe is incomplete or duplicated.')
    for code in codes:
        if not reusable_entry(parents[code], parent_dir / 'raw'):
            raise ValueError('Parent series did not pass checksum verification.')
    raw = output_dir / 'raw'
    raw.mkdir(parents=True, exist_ok=True)
    path = output_dir / 'history_manifest.json'
    manifest = dict(source=parent['source'], completed_bars_only=True, collection_complete=False,
                    start=parent['start'], end=end, scope=parent['scope'], requested_codes=codes,
                    retrieved_at=datetime.now(timezone.utc).isoformat(), stocks=[],
                    historical_limitations=parent['historical_limitations'],
                    parent_manifest_sha256=file_digest(parent_path), parent_end=parent['end'])
    entries = {}
    if path.exists():
        previous = json.loads(path.read_text())
        for key in ['parent_manifest_sha256', 'end', 'requested_codes']:
            if manifest[key] != previous.get(key):
                raise ValueError('Existing update has a different protocol: ' + key)
        manifest['retrieved_at'] = previous['retrieved_at']
        entries = {entry['stock_code']: entry for entry in previous['stocks'] if reusable_entry(entry, raw)}

    def fetch(code):
        try:
            old = pd.read_csv(parent_dir / 'raw' / (code + '.csv'), dtype={'stock_code': str})
            result, method = merge_completed_series(client, code, old, parent['start'], end)
            target = raw / (code + '.csv')
            temporary = target.with_suffix('.csv.tmp')
            result.to_csv(temporary, index=False, encoding='utf-8-sig')
            temporary.replace(target)
            return dict(stock_code=code, status='success', rows=len(result), update_method=method,
                        overlap_revision=result.attrs.get('overlap_revision'),
                        first_date=str(result.date.min().date()), last_date=str(result.date.max().date()),
                        sha256=file_digest(target), retrieved_at=datetime.now(timezone.utc).isoformat())
        except Exception as error:
            return dict(stock_code=code, status='failed', error_type=type(error).__name__)

    manifest['stocks'] = list(entries.values())
    save_manifest(path, manifest)
    pending = [code for code in codes if code not in entries]
    print(f'Universe {len(codes)}; verified resumed {len(entries)}; updates {len(pending)}', flush=True)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        tasks = [executor.submit(fetch, code) for code in pending]
        for task in as_completed(tasks):
            entry = task.result()
            entries[entry['stock_code']] = entry
            manifest['stocks'] = [entries[code] for code in codes if code in entries]
            save_manifest(path, manifest)
            if len(entries) % 50 == 0 or entry['status'] != 'success':
                print(f"Updated {len(entries)}/{len(codes)}; latest status {entry['status']}", flush=True)
    manifest['collection_complete'] = True
    manifest['updated_at'] = datetime.now(timezone.utc).isoformat()
    save_manifest(path, manifest)
    return manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--parent-dir', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--end', default=completed_price_cutoff().isoformat())
    parser.add_argument('--workers', type=int, default=8)
    args = parser.parse_args()
    try:
        client = KISClient()
        client.get_access_token()
    except KISCredentialsMissing:
        print('KIS credentials missing: update skipped.')
        return
    except Exception as error:
        parser.exit(2, 'KIS authentication unavailable: ' + type(error).__name__ + '\n')
    interval = .55 if client.base_url.endswith(':29443') else .15
    manifest = update_history(PacedHistoryClient(client, interval), args.parent_dir, args.output_dir, args.end, args.workers)
    failed = sum(row['status'] != 'success' for row in manifest['stocks'])
    print(json.dumps({'stocks': len(manifest['stocks']), 'failed': failed, 'end': manifest['end']}))
    if failed:
        parser.exit(2, 'Some stock updates failed; rerun to retry. Do not publish this incomplete universe.\n')


if __name__ == '__main__':
    main()
