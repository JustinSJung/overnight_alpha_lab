"""Search coverage is separate from the registered forecasting/evaluation cohort."""
from datetime import datetime, timedelta, timezone
import hashlib
import json
import math
from pathlib import Path
import re

import pandas as pd


def build_catalog(root, primary):
    root, entries = Path(root), {}

    def add(code, name):
        if not isinstance(code, str) or not re.fullmatch(r'[0-9A-Z]{6}', code):
            return
        row = entries.setdefault(code, dict(stock_code=code, stock_name=code, aliases=[]))
        if isinstance(name, str) and name.strip() and name != code:
            name = name.strip()
            if name not in row['aliases']:
                row['aliases'].append(name)
            if row['stock_name'] == code:
                row['stock_name'] = name

    path = root / 'data/processed/ml_stock_catalog.csv'
    if path.exists():
        for row in pd.read_csv(path, dtype=str).to_dict('records'):
            add(row['stock_code'], row.get('stock_name'))
    universe = root / 'docs/model_experiments/ml_beta_universe.json'
    if universe.exists():
        for code in json.loads(universe.read_text())['stock_codes']:
            add(code, None)
    for row in primary['stocks']:
        add(row['stock_code'], row['stock_name'])
        for alias in row['aliases']:
            add(row['stock_code'], alias)
    for row in entries.values():
        row['aliases'].sort()
    return sorted(entries.values(), key=lambda row: row['stock_code'])


def load_lookup(path, primary, root, now=None):
    """Invalid/old auxiliary output must never invalidate the primary forecasts."""
    catalog = build_catalog(root, primary)
    fallback = dict(catalog=catalog, forecasts=[], states={})
    try:
        path = Path(path)
        if path.stat().st_size > 2_000_000:
            return fallback
        data = json.loads(path.read_text())
        generated = datetime.fromisoformat(data['generated_at'])
        now = now or datetime.now(timezone.utc)
        primary_path = Path(root) / 'docs/price_model.json'
        if (primary.get('prediction_target') != 'next_open_to_fifth_close_v1'
                or data['schema'] != 'stock_lookup_v1' or data['scope'] != 'lookup_only_not_evaluation'
                or data['recommendation_enabled'] is not False or generated.tzinfo is None
                or generated > now + timedelta(minutes=5) or now - generated > timedelta(days=7)
                or data['price_date'] != primary['price_date']
                or data['primary_sha256'] != hashlib.sha256(primary_path.read_bytes()).hexdigest()):
            return fallback
        codes = {row['stock_code'] for row in catalog}
        regular = {row['stock_code'] for row in primary['stocks']}
        seen, forecasts = set(), []
        for row in data['forecasts']:
            code = row['stock_code']
            if (code not in codes or code in regular or code in seen or row['lookup_only'] is not True
                    or row['recommended'] is not False or row['signal_date'] != primary['price_date']
                    or type(row['stale']) is not bool or row['predicted_return'] is not None
                    or not isinstance(row['probability'], (int, float)) or isinstance(row['probability'], bool)
                    or not math.isfinite(row['probability']) or not 0 <= row['probability'] <= 1):
                return fallback
            seen.add(code)
            forecasts.append({key: row[key] for key in ['stock_code', 'signal_date', 'probability',
                                                        'predicted_return', 'stale', 'recommended', 'lookup_only']})
        states = data['states']
        if not isinstance(states, dict) or any(code not in codes or value not in {
                'price_unavailable', 'insufficient_history', 'not_current', 'inactive', 'available'}
                for code, value in states.items()):
            return fallback
        return dict(catalog=catalog, forecasts=forecasts, states=states)
    except (OSError, ValueError, KeyError, TypeError, OverflowError):
        return fallback
