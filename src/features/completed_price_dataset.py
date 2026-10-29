"""Rebuild consistent price features from a single completed adjusted OHLCV series."""
from __future__ import annotations

import json
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd

HISTORY_FEATURE_VERSION = 'price_completed_history_v2'


def history_features(prices):
    frame = prices.copy()
    frame['date'] = pd.to_datetime(frame['date'], errors='coerce').dt.normalize()
    for column in ['open', 'high', 'low', 'close', 'volume']:
        frame[column] = pd.to_numeric(frame[column], errors='coerce')
    frame = frame.dropna(subset=['date', 'close']).sort_values('date').drop_duplicates('date', keep='last')
    frame = frame[frame['close'] > 0].reset_index(drop=True)
    close = frame['close']
    returns = close.pct_change(fill_method=None)
    frame['return_1d'] = returns
    frame['return_5d'] = close.pct_change(5, fill_method=None)
    frame['return_20d'] = close.pct_change(20, fill_method=None)
    frame['ma5'] = close.rolling(5, min_periods=5).mean()
    frame['ma20'] = close.rolling(20, min_periods=20).mean()
    volume_mean = frame['volume'].rolling(20, min_periods=20).mean().replace(0, np.nan)
    frame['volume_ratio_20d'] = frame['volume'] / volume_mean
    frame['volatility_20d'] = returns.rolling(20, min_periods=20).std()
    high20 = frame['high'].rolling(20, min_periods=20).max()
    frame['breakout_score'] = (
        (close >= high20 * 0.98).astype(int) * 2
        + (frame['ma5'] > frame['ma20']).astype(int)
        + (frame['volume_ratio_20d'] >= 1.5).astype(int)
        + (frame['return_5d'] > 0).astype(int)
    )
    frame['signal_date'] = frame['date']
    frame['snapshot_date'] = frame['date']
    return frame


def load_completed_history(root):
    root = Path(root)
    manifest = json.loads((root / 'history_manifest.json').read_text(encoding='utf-8'))
    if not manifest.get('completed_bars_only'):
        raise ValueError('History must explicitly identify completed daily bars.')
    if manifest.get('collection_complete') is False:
        raise ValueError('Historical collection is still in progress; wait before training.')
    frames = []
    skipped = []
    for stock in manifest['stocks']:
        if stock['status'] != 'success':
            continue
        path = root / 'raw' / (stock['stock_code'] + '.csv')
        try:
            if stock.get('sha256') and hashlib.sha256(path.read_bytes()).hexdigest() != stock['sha256']:
                raise ValueError('Historical file checksum mismatch.')
            frame = history_features(pd.read_csv(path, dtype={'stock_code': str}))
            frame = frame[frame['date'] <= pd.Timestamp(manifest['end'])]
            frame['snapshot_file'] = path.name
            frame['stock_code'] = stock['stock_code']
            frames.append(frame)
        except (ValueError, OSError, KeyError) as error:
            skipped.append({'file': path.name, 'error': type(error).__name__})
    if not frames:
        raise ValueError('No complete historical price series available.')
    combined = pd.concat(frames, ignore_index=True)
    combined.attrs['feature_version'] = HISTORY_FEATURE_VERSION
    combined.attrs['history_provenance'] = {
        'source': manifest['source'], 'retrieved_at': manifest['retrieved_at'],
        'scope': manifest.get('scope', 'pilot'),
        'stocks': len(frames), 'historical_limitations': manifest['historical_limitations'],
        'requested_stocks': len(manifest.get('requested_codes', manifest['stocks'])),
        'failed_stocks': sum(stock['status'] != 'success' for stock in manifest['stocks']),
        'unreadable_stocks': len(skipped),
    }
    return combined, {'snapshot_files': len(frames), 'skipped_files': skipped}
