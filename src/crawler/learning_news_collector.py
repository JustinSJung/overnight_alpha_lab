"""Bounded public-news collection for point-in-time ML inputs, not trade signals."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import time

import pandas as pd

from src.crawler.market_clock import KST
from src.features.news_learning import archive_batch
from src.news_providers.google_news_rss_provider import GoogleNewsRssProvider

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / 'data/news_learning'
GLOBAL_TOPICS = [
    ('rates', 'Federal Reserve interest rates'),
    ('semiconductors', 'semiconductor chip exports'),
    ('energy', 'oil prices Middle East'),
    ('trade', 'China economy tariffs'),
]


def load_catalog(root=ROOT):
    root = Path(root)
    parts = [pd.read_csv(root / 'data/processed/ml_stock_catalog.csv', dtype=str)]
    latest = sorted((root / 'data/processed').glob('price_based_candidates_*.csv'))
    if latest:
        frame = pd.read_csv(latest[-1], dtype={'stock_code': str})
        if {'stock_code', 'stock_name'}.issubset(frame):
            parts.append(frame[['stock_code', 'stock_name']])
    catalog = pd.concat(parts, ignore_index=True).dropna().drop_duplicates()
    catalog = catalog[catalog.stock_code.str.fullmatch(r'[0-9A-Z]{6}') & catalog.stock_name.str.len().ge(2)]
    return catalog.sort_values(['stock_code', 'stock_name']).reset_index(drop=True)


def query_plan(catalog, now, limit=20):
    """Rotate through the broad catalog independently of ranks or future returns."""
    if not 1 <= limit <= 40:
        raise ValueError('Use a bounded rotating collection budget.')
    unique = catalog.drop_duplicates('stock_code').reset_index(drop=True)
    offset = (now.astimezone(KST).date().toordinal() * limit) % len(unique)
    plan = []
    for step in range(min(limit, len(unique))):
        row = unique.iloc[(offset + step) % len(unique)]
        plan.append(dict(query='"' + row.stock_name + '"', stock_codes=[row.stock_code],
                         topic='company', language='ko'))
    for topic, query in GLOBAL_TOPICS:
        plan.append(dict(query=query, stock_codes=[], topic=topic, language='en'))
    return plan


def disclosure_items(root=ROOT, now=None):
    """Legacy date-only receipts become usable no earlier than the day's end."""
    files = sorted((Path(root) / 'data/raw').glob('dart_disclosures_[0-9]*.csv'))
    if not files:
        return []
    frame = pd.read_csv(files[-1], dtype=str).fillna('')
    current = pd.Timestamp(now or datetime.now(KST)).tz_convert(KST).normalize()
    rows = []
    for row in frame.to_dict('records'):
        try:
            day = pd.to_datetime(row['rcept_dt'], format='%Y%m%d').tz_localize(KST)
            if day < current - pd.Timedelta(days=7) or day > current:
                continue
            publication = day + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)
            receipt = row['rcept_no']
            if not receipt.isdigit():
                continue
            rows.append(dict(source_provider='dart', query=row['corp_name'],
                title=row['corp_name'] + ' ' + row['report_nm'],
                published_at=publication.isoformat(),
                link='https://dart.fss.or.kr/dsaf001/main.do?rcpNo=' + receipt,
                verified_stock_code=row.get('stock_code', ''), topic='company'))
        except (ValueError, KeyError):
            continue
    return rows


def collect_news(root=ROOT, archive=None, limit=20, fetch_live=True, provider_factory=None):
    root = Path(root)
    catalog = load_catalog(root)
    items, statuses = disclosure_items(root), []
    if fetch_live:
        providers = {'ko': GoogleNewsRssProvider(),
                     'en': GoogleNewsRssProvider(hl='en-US', gl='US', ceid='US:en')}
        if provider_factory is not None:
            providers = {language: provider_factory(language) for language in providers}
        for plan in query_plan(catalog, datetime.now(timezone.utc), limit):
            provider = providers[plan['language']]
            try:
                rows = provider.fetch(plan['query'], max_items=5)
                items.extend([{**row, 'topic': plan['topic']} for row in rows])
                status = 'success'
            except Exception as error:
                # Exceptions can embed query URLs/credentials; only the type is recorded.
                status = 'failed_' + type(error).__name__
            statuses.append(dict(source_provider=provider.provider_name, **plan, status=status))
            time.sleep(.2)
    else:
        files = sorted((root / 'data/raw').glob('news_provider_items_*.csv'))
        if files:
            items.extend(pd.read_csv(files[-1]).fillna('').to_dict('records'))
    # Stamp after all fetches: slightly later availability is conservative, never backdated.
    return archive_batch(items, statuses, catalog, archive or root / 'data/news_learning')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--local-only', action='store_true')
    parser.add_argument('--limit', type=int, default=20)
    args = parser.parse_args()
    result = collect_news(limit=args.limit, fetch_live=not args.local_only)
    print(json.dumps({key: result[key] for key in ['schema', 'observed_at', 'rows', 'rejected', 'social_media_collected']}))


if __name__ == '__main__':
    main()
