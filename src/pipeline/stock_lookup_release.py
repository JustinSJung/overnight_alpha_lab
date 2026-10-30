"""Extra lookup-only forecasts; never alter training, originals or learning metrics."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

import numpy as np
import pandas as pd

from src.crawler.kis_client import KISClient, KISCredentialsMissing
from src.crawler.market_clock import completed_price_cutoff
from src.crawler.price_learning_history import PacedHistoryClient, fetch_history, file_digest
from src.features.completed_price_dataset import history_features
from src.features.next_open_dataset import COLUMNS, valid_candle
from src.models.next_open_price_model import load_model, predict_probability
from src.models.selected_price_model import prepare_selected_features, write_json
from src.report_generator.price_model_panel import load_public_forecast
from src.report_generator.stock_lookup_data import build_catalog

ROOT = Path(__file__).resolve().parents[2]


def current_features(prices, code, price_date):
    frame = prices.copy()
    frame['date'] = pd.to_datetime(frame.date, errors='coerce').dt.normalize()
    values = frame[['open', 'high', 'low', 'close', 'volume']].apply(pd.to_numeric, errors='coerce')
    if (frame.empty or frame.date.isna().any() or frame.date.duplicated().any()
            or frame.date.dt.dayofweek.ge(5).any() or frame.date.gt(pd.Timestamp(price_date)).any()
            or not np.isfinite(values).all(axis=None) or values.close.le(0).any()
            or values[['open', 'high', 'low', 'volume']].lt(0).any(axis=None)
            or (values.volume.gt(0) & ~valid_candle(values)).any()):
        raise ValueError('Invalid lookup OHLCV history.')
    frame = frame.assign(**{name: values[name] for name in values})
    if frame.date.max() != pd.Timestamp(price_date):
        return None, 'not_current'
    if len(frame) < 21:
        return None, 'insufficient_history'
    frame['stock_code'] = code
    enriched = prepare_selected_features(history_features(frame), COLUMNS)
    latest = enriched[enriched.signal_date.eq(pd.Timestamp(price_date))].copy()
    if latest.volume.le(0).any():
        return None, 'inactive'
    if not np.isfinite(latest[COLUMNS]).all(axis=None):
        return None, 'insufficient_history'
    return latest, 'available'


def fetch_lookup_history(client, code, cache, start, end):
    folder = Path(cache) / ('snapshot_' + end.replace('-', ''))
    folder.mkdir(parents=True, exist_ok=True)
    path, metadata = folder / (code + '.csv'), folder / (code + '.json')
    if path.exists() and metadata.exists():
        record = json.loads(metadata.read_text())
        if record == dict(stock_code=code, start=start, end=end, sha256=file_digest(path)):
            return pd.read_csv(path)
    prices = fetch_history(client, code, start, end, pause=0, max_pages=4)
    if prices.empty:
        raise ValueError('No quote history returned.')
    current_features(prices, code, end)
    prices.to_csv(path, index=False)
    write_json(dict(stock_code=code, start=start, end=end, sha256=file_digest(path)), metadata)
    return prices


def refresh_lookup(primary_path, model_dir, cache, output, root=ROOT, client=None, now=None):
    now = now or datetime.now(timezone.utc)
    primary_path = Path(primary_path)
    primary = load_public_forecast(primary_path)
    if primary is None or primary.get('prediction_target') != 'next_open_to_fifth_close_v1':
        raise ValueError('Valid primary next-open publication required.')
    price_date = primary['price_date']
    if pd.Timestamp(price_date).date() > completed_price_cutoff() or primary['model_state'] == 'stale':
        raise ValueError('Current completed-price publication required.')
    source_hash = file_digest(primary_path)
    api = KISClient(timeout=15) if client is None else None
    bundle = load_model(model_dir)
    metadata = bundle['metadata']
    if (pd.Timestamp(metadata['trained_at']) > pd.Timestamp(now)
            or pd.Timestamp(metadata['as_of']) > pd.Timestamp(price_date)):
        raise ValueError('Lookup model uses data unavailable at its price date.')
    catalog = build_catalog(root, primary)
    regular = {row['stock_code'] for row in primary['stocks']}
    universe = set(json.loads((Path(root) / 'docs/model_experiments/ml_beta_universe.json').read_text())['stock_codes'])
    extras = [row['stock_code'] for row in catalog if row['stock_code'] not in universe
              and row['stock_code'] not in regular and re.fullmatch(r'[0-9]{6}', row['stock_code'])]
    if client is None:
        api.get_access_token()
        client = PacedHistoryClient(api, .55 if api.base_url.endswith(':29443') else .15)
    start = str((pd.Timestamp(price_date) - pd.Timedelta(days=180)).date())
    Path(cache).mkdir(parents=True, exist_ok=True)
    states, forecasts = {}, []

    def predict(code):
        try:
            prices = fetch_lookup_history(client, code, cache, start, price_date)
            latest, state = current_features(prices, code, price_date)
            if latest is None:
                return code, state, None
            probability = float(predict_probability(bundle, latest)[0])
            return code, state, dict(stock_code=code, signal_date=price_date, probability=probability,
                                     predicted_return=None, stale=False, recommended=False, lookup_only=True)
        except Exception:
            return code, 'price_unavailable', None

    with ThreadPoolExecutor(max_workers=4) as executor:
        for code, state, row in executor.map(predict, extras):
            states[code] = state
            if row is not None:
                forecasts.append(row)
    if file_digest(primary_path) != source_hash:
        raise ValueError('Primary publication changed while lookup data was prepared.')
    payload = dict(schema='stock_lookup_v1', scope='lookup_only_not_evaluation',
                   generated_at=now.isoformat(), price_date=price_date, primary_sha256=source_hash,
                   recommendation_enabled=False, states=states,
                   forecasts=sorted(forecasts, key=lambda row: row['stock_code']))
    write_json(payload, output)
    from src.pipeline.ml_beta_release import compact_snapshots
    compact_snapshots(cache, Path(cache) / ('snapshot_' + price_date.replace('-', '')))
    return dict(extra_requested=len(extras), extra_forecasts=len(forecasts),
                unavailable=len(extras) - len(forecasts), price_date=price_date)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primary', type=Path, default=ROOT / 'docs/price_model.json')
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/ml_beta_state/current_model')
    parser.add_argument('--cache', type=Path, default=ROOT / 'data/ml_beta_state/stock_lookup')
    parser.add_argument('--output', type=Path, default=ROOT / 'docs/stock_lookup.json')
    args = parser.parse_args()
    try:
        print(json.dumps(refresh_lookup(args.primary, args.model_dir, args.cache, args.output)))
    except KISCredentialsMissing:
        print('KIS credentials missing: additional lookup collection skipped.')
    except Exception as error:
        parser.exit(1, 'Additional lookup refresh stopped safely: ' + type(error).__name__ + '\n')


if __name__ == '__main__':
    main()
