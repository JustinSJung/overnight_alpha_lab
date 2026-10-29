"""Backfill completed adjusted OHLCV for model research, without altering the candidate pool."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import threading
import time

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.crawler.kis_client import KISClient, KISCredentialsMissing
from src.crawler.market_clock import completed_price_cutoff


def fetch_history(client, code, start, end, pause=0.55, max_pages=60):
    """The chart endpoint is capped per request: walk backward by oldest returned date."""
    cursor = pd.Timestamp(end).normalize()
    start = pd.Timestamp(start).normalize()
    frames = []
    for _ in range(max_pages):
        page = client.get_daily_ohlcv(code, start.strftime('%Y%m%d'), cursor.strftime('%Y%m%d'))
        if page.empty:
            break
        page = page.copy()
        page['date'] = pd.to_datetime(page['date'], errors='coerce')
        page = page[page['date'].between(start, cursor)].dropna(subset=['date'])
        if page.empty:
            raise ValueError('Provider page did not advance inside the requested interval.')
        frames.append(page)
        oldest = page['date'].min()
        if oldest <= start:
            break
        cursor = oldest - pd.Timedelta(days=1)
        time.sleep(pause)
    else:
        raise ValueError('Pagination limit reached before the history was complete.')
    if not frames:
        return pd.DataFrame()
    result = pd.concat(frames, ignore_index=True).sort_values('date')
    result = result.drop_duplicates('date', keep='last')
    result['stock_code'] = code
    return result


def choose_codes(universe_file, limit):
    codes = pd.read_csv(universe_file, dtype={'stock_code': str})['stock_code'].dropna().astype(str).str.zfill(6)
    codes = sorted(set(codes[codes.str.fullmatch(r'\d{6}')]))
    # Reproducible selection based on identifiers, never subsequent outcomes.
    codes.sort(key=lambda code: hashlib.sha256(('history-pilot-v1|' + code).encode()).hexdigest())
    if '005930' in codes:
        codes.remove('005930')
        codes.insert(0, '005930')
    return codes[:limit] if limit else codes


class PacedHistoryClient:
    """Share one request budget across workers; never log provider payloads."""

    def __init__(self, client, interval=0.55):
        self.client = client
        self.interval = interval
        self.lock = threading.Lock()
        self.last_request = 0.0

    def get_daily_ohlcv(self, *args):
        for attempt in range(3):
            with self.lock:
                time.sleep(max(0, self.last_request + self.interval - time.monotonic()))
                self.last_request = time.monotonic()
            try:
                return self.client.get_daily_ohlcv(*args)
            except (requests.RequestException, RuntimeError):
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)


def file_digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_manifest(path, manifest):
    temporary = path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    os.replace(temporary, path)


def reusable_entry(stock, raw_dir):
    path = Path(raw_dir) / (stock['stock_code'] + '.csv')
    try:
        return (stock.get('status') == 'success' and path.is_file()
                and bool(stock.get('sha256')) and stock['sha256'] == file_digest(path))
    except OSError:
        return False


def collect_history(client, codes, output_dir, start, end, workers=1):
    """Resume only matching, checksum-verified series; retry failed stocks on rerun."""
    output_dir = Path(output_dir)
    raw = output_dir / 'raw'
    raw.mkdir(parents=True, exist_ok=True)
    path = output_dir / 'history_manifest.json'
    manifest = {
        'source': 'kis_adjusted_daily', 'completed_bars_only': True,
        'retrieved_at': datetime.now(timezone.utc).isoformat(), 'start': start, 'end': end,
        'scope': 'expanded_current_universe_research', 'requested_codes': codes, 'stocks': [],
        'collection_complete': False,
        'historical_limitations': 'Current observed universe and retrospectively adjusted prices; not a survivorship-free point-in-time universe.',
    }
    entries = {}
    if path.exists():
        previous = json.loads(path.read_text(encoding='utf-8'))
        for key in ['source', 'completed_bars_only', 'start', 'end', 'requested_codes']:
            if previous.get(key) != manifest[key]:
                raise ValueError('Existing manifest has a different collection protocol: ' + key)
        manifest['retrieved_at'] = previous['retrieved_at']
        for stock in previous['stocks']:
            if reusable_entry(stock, raw):
                entries[stock['stock_code']] = stock

    def fetch(code):
        try:
            history = fetch_history(client, code, start, end, pause=0)
            if history.empty:
                raise ValueError('No historical prices returned.')
            target = raw / (code + '.csv')
            temporary = target.with_suffix('.csv.tmp')
            history.to_csv(temporary, index=False, encoding='utf-8-sig')
            os.replace(temporary, target)
            return {'stock_code': code, 'status': 'success', 'rows': len(history),
                    'first_date': str(history.date.min().date()), 'last_date': str(history.date.max().date()),
                    'sha256': file_digest(target), 'retrieved_at': datetime.now(timezone.utc).isoformat()}
        except Exception as error:
            return {'stock_code': code, 'status': 'failed', 'error_type': type(error).__name__}

    pending = [code for code in codes if code not in entries]
    manifest['stocks'] = list(entries.values())
    save_manifest(path, manifest)
    print(f'Universe: {len(codes)}; verified cached: {len(entries)}; to collect: {len(pending)}', flush=True)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        tasks = {executor.submit(fetch, code): code for code in pending}
        for task in as_completed(tasks):
            entry = task.result()
            entries[entry['stock_code']] = entry
            manifest['stocks'] = [entries[code] for code in codes if code in entries]
            manifest['updated_at'] = datetime.now(timezone.utc).isoformat()
            manifest['collection_complete'] = len(entries) == len(codes)
            save_manifest(path, manifest)
            message = str(entry.get('rows', entry.get('error_type', 'unknown')))
            print(f"[{len(entries)}/{len(codes)}] {entry['stock_code']}: {entry['status']} ({message})", flush=True)
    manifest['collection_complete'] = True
    save_manifest(path, manifest)
    return manifest


def main():
    today = datetime.now(timezone(timedelta(hours=9))).date()
    parser = argparse.ArgumentParser()
    parser.add_argument('--universe-file', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--start', default='2023-01-01')
    parser.add_argument('--end', default=(today - timedelta(days=1)).isoformat())
    parser.add_argument('--limit', type=int, default=30, help='Research pilot only; 0 selects the whole existing universe.')
    parser.add_argument('--workers', type=int, default=1)
    parser.add_argument('--request-interval', type=float, default=0.55)
    args = parser.parse_args()
    if pd.Timestamp(args.end).date() > completed_price_cutoff() or pd.Timestamp(args.start) > pd.Timestamp(args.end):
        parser.error('Use a valid range ending at the completed-bar cutoff or earlier.')
    if args.limit < 0:
        parser.error('limit must be non-negative')
    if not 1 <= args.workers <= 16 or not 0.15 <= args.request_interval <= 60:
        parser.error('Use 1-16 workers and a shared request interval of at least 0.15 seconds.')
    try:
        client = KISClient(timeout=15)
    except KISCredentialsMissing:
        print('KIS credentials missing: historical backfill skipped.')
        return
    codes = choose_codes(args.universe_file, args.limit)
    try:
        client.get_access_token()
    except Exception as error:
        print(f'KIS authentication unavailable: collection skipped ({type(error).__name__}).')
        return
    interval = max(args.request_interval, 0.55 if client.base_url.endswith(':29443') else 0.15)
    manifest = collect_history(PacedHistoryClient(client, interval), codes, args.output_dir,
                               args.start, args.end, workers=args.workers)
    print('Successful stocks:', sum(row['status'] == 'success' for row in manifest['stocks']), flush=True)


if __name__ == '__main__':
    main()
