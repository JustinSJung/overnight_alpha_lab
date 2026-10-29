"""Immutable news metadata and as-of features for a separate research model."""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import hashlib
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
import uuid

import numpy as np
import pandas as pd

from src.crawler.market_clock import KST

SCHEMA = 'point_in_time_news_v1'
NEWS_COLUMNS = [
    'news_collection_observed', 'news_company_query_observed', 'news_count_24h',
    'news_source_count_24h', 'news_positive_terms_24h', 'news_negative_terms_24h',
    'news_risk_terms_24h', 'disclosure_count_24h', 'global_news_count_24h',
    'global_risk_terms_24h',
]
POSITIVE = ['수주', '흑자', '실적개선', '승인', '공급계약', 'earnings beat', 'profit growth', 'approval']
NEGATIVE = ['적자', '감소', '소송', '유상증자', 'earnings miss', 'loss', 'lawsuit', 'downgrade']
RISK = ['거래정지', '상장폐지', '압수수색', '전쟁', '제재', 'default', 'sanction', 'war', 'fraud']


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def clean_text(value):
    parser = PlainText()
    parser.feed(str(value or ''))
    return ' '.join(unicodedata.normalize('NFKC', unescape(' '.join(parser.parts))).split())


def aware_time(value):
    try:
        result = pd.Timestamp(value)
    except (ValueError, TypeError):
        result = pd.Timestamp(parsedate_to_datetime(str(value)))
    if pd.isna(result) or result.tzinfo is None:
        raise ValueError('An explicit timezone is required; never guess historical availability.')
    return result.tz_convert('UTC')


def canonical_url(value):
    parsed = urlsplit(str(value))
    if parsed.scheme not in {'http', 'https'} or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError('A public article URL is required.')
    # Query parameters can carry access tokens. Store only a public path, not credentials.
    query = ''
    if parsed.hostname == 'dart.fss.or.kr':
        query = urlencode([(key, value) for key, value in parse_qsl(parsed.query)
                           if key == 'rcpNo' and re.fullmatch(r'[0-9]{14}', value)])
    return urlunsplit((parsed.scheme, parsed.netloc.lower(), parsed.path, query, ''))


def title_key(value):
    # Exact normalized headline dedup only; semantic/translated duplicates are not inferred.
    return ' '.join(re.findall(r'\w+', clean_text(value).rsplit(' - ', 1)[0].casefold()))


def entity_patterns(catalog):
    patterns = []
    for code, names in catalog.groupby('stock_code', sort=True):
        for name in sorted(set(names.stock_name.dropna().astype(str))):
            name = clean_text(name)
            if len(name) < 2:
                continue
            patterns.append((str(code), re.compile(r'(?<!\w)' + re.escape(name) + r'(?!\w)', re.I)))
        patterns.append((str(code), re.compile(r'(?<![A-Za-z0-9])' + re.escape(str(code)) + r'(?![A-Za-z0-9])')))
    return patterns


def term_count(text, terms):
    count = 0
    for term in terms:
        pattern = re.escape(term.casefold())
        if term.isascii():
            pattern = r'(?<!\w)' + pattern + r'(?!\w)'
        count += bool(re.search(pattern, text))
    return count


def archive_batch(items, requests, catalog, root, now=None):
    """Record observed NOW, never from a legacy filename or unverified collected_at."""
    observed = aware_time(now or datetime.now(timezone.utc))
    patterns = entity_patterns(catalog)
    codes = set(catalog.stock_code.astype(str))
    rows, rejected, seen = [], Counter(), set()
    for item in items:
        try:
            if item.get('source_provider') == 'gdelt' and item.get('timestamp_kind') != 'publication':
                raise ValueError('GDELT index time is not a verified publication timestamp.')
            published = aware_time(item.get('published_at'))
            title = clean_text(item.get('title'))[:500]
            if not title:
                raise ValueError('Headline is missing.')
            url = canonical_url(item.get('link'))
            publisher = item.get('publisher_url') or url
            domain = urlsplit(canonical_url(publisher)).hostname
            query = clean_text(item.get('query'))[:180]
            provider = str(item.get('source_provider', 'unknown'))[:40]
            identifier = hashlib.sha256((provider + '|' + url + '|' + title).encode()).hexdigest()
            if identifier in seen:
                continue
            seen.add(identifier)
            explicit = str(item.get('verified_stock_code', ''))
            linked = sorted({code for code, pattern in patterns if pattern.search(title)} |
                            ({explicit} if provider == 'dart' and explicit in codes else set()))
            story = hashlib.sha256((published.strftime('%Y-%m-%d') + '|' + title_key(title)).encode()).hexdigest()
            text = title.casefold()
            rows.append(dict(schema=SCHEMA, article_id=identifier, story_id=story, title=title,
                link=url, source_domain=domain, source_provider=provider, query=query,
                published_at=published.isoformat(), first_seen_at=observed.isoformat(),
                available_at=max(observed, published).isoformat(), stock_codes=linked,
                topic=str(item.get('topic', 'company'))[:40],
                positive_terms=term_count(text, POSITIVE),
                negative_terms=term_count(text, NEGATIVE),
                risk_terms=term_count(text, RISK)))
        except (ValueError, TypeError, OverflowError):
            rejected['invalid_publication_or_metadata'] += 1
    safe_requests = []
    for request in requests:
        safe_requests.append(dict(source_provider=str(request['source_provider'])[:40],
            query=clean_text(request['query'])[:180], status=str(request['status'])[:50],
            stock_codes=sorted(set(request.get('stock_codes', [])) & codes),
            topic=str(request.get('topic', 'company'))[:40], observed_at=observed.isoformat()))
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    name = observed.strftime('%Y%m%dT%H%M%S') + '_' + uuid.uuid4().hex[:12]
    payload = ''.join(json.dumps(row, ensure_ascii=False, sort_keys=True) + '\n' for row in rows).encode()
    if len(payload) > 2_000_000:
        raise ValueError('News metadata batch exceeds the publication size budget.')
    manifest = dict(schema=SCHEMA, observed_at=observed.isoformat(), rows=len(rows),
        sha256=hashlib.sha256(payload).hexdigest(), requests=safe_requests, rejected=dict(rejected),
        catalog_sha256=hashlib.sha256(catalog.sort_values(['stock_code', 'stock_name']).to_csv(index=False).encode()).hexdigest(),
        social_media_collected=False, scope='Public headline metadata only; no full article bodies or private posts')
    # Exclusive creation prevents a rerun from rewriting any existing observation batch.
    with (root / (name + '.jsonl')).open('xb') as target:
        target.write(payload)
    with (root / (name + '.manifest.json')).open('x', encoding='utf-8') as target:
        json.dump(manifest, target, ensure_ascii=False, indent=2)
        target.write('\n')
    return manifest


def read_archive(root):
    articles, requests, manifests = [], [], []
    root = Path(root)
    files = sorted(root.glob('*.jsonl'))
    if set(p.stem for p in files) != set(p.name.removesuffix('.manifest.json') for p in root.glob('*.manifest.json')):
        raise ValueError('An incomplete news batch cannot be used for learning.')
    for path in files:
        if path.stat().st_size > 2_000_000:
            raise ValueError('Oversized news batch.')
        payload = path.read_bytes()
        manifest = json.loads(path.with_suffix('.manifest.json').read_text())
        rows = [json.loads(line) for line in payload.splitlines()]
        if (manifest['schema'] != SCHEMA or manifest['rows'] != len(rows)
                or manifest['sha256'] != hashlib.sha256(payload).hexdigest()):
            raise ValueError('News batch checksum/schema mismatch.')
        observed = aware_time(manifest['observed_at'])
        for row in rows:
            published, first_seen = aware_time(row['published_at']), aware_time(row['first_seen_at'])
            if (row['schema'] != SCHEMA or first_seen != observed
                    or aware_time(row['available_at']) != max(published, first_seen)):
                raise ValueError('News observation availability was changed.')
        for request in manifest['requests']:
            if aware_time(request['observed_at']) != observed:
                raise ValueError('News collection status was backdated.')
        articles.extend(rows)
        requests.extend(manifest['requests'])
        manifests.append(manifest)
    return articles, requests, manifests


def add_news_features(cohort, articles, requests):
    """Fixed 16:30 KST decision time; no future articles, revisions or statuses."""
    if cohort.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Unique price candidate keys are required.')
    result = cohort.copy()
    for column in NEWS_COLUMNS:
        result[column] = 0.
    articles = [{**row, '_available': aware_time(row['available_at']),
                 '_published': aware_time(row['published_at']),
                 'positive_terms': term_count(row['title'].casefold(), POSITIVE),
                 'negative_terms': term_count(row['title'].casefold(), NEGATIVE),
                 'risk_terms': term_count(row['title'].casefold(), RISK)} for row in articles]
    requests = [{**row, '_observed': aware_time(row['observed_at'])} for row in requests]
    for day, indices in result.groupby('signal_date').groups.items():
        decision = pd.Timestamp(day).normalize().tz_localize(KST) + pd.Timedelta(hours=16, minutes=30)
        lower = decision - pd.Timedelta(hours=24)
        usable = [r for r in articles if r['_available'] <= decision and lower < r['_published'] <= decision]
        statuses = [r for r in requests if lower < r['_observed'] <= decision and r['status'] == 'success']
        result.loc[indices, 'news_collection_observed'] = float(bool(statuses))
        queried = {code for r in statuses for code in r['stock_codes']}
        global_rows = {r['story_id']: r for r in sorted(usable, key=lambda r: r['_available'], reverse=True)
                       if r['topic'] != 'company'}
        result.loc[indices, 'global_news_count_24h'] = len(global_rows)
        result.loc[indices, 'global_risk_terms_24h'] = sum(r['risk_terms'] for r in global_rows.values())
        by_code, sources_by_code = {}, {}
        for row in sorted(usable, key=lambda r: r['_available'], reverse=True):
            for code in row['stock_codes']:
                by_code.setdefault(code, {})[row['story_id']] = row
                sources_by_code.setdefault(code, set()).add(row['source_domain'])
        for index in indices:
            code = str(result.at[index, 'stock_code'])
            rows = list(by_code.get(code, {}).values())
            result.at[index, 'news_company_query_observed'] = float(code in queried)
            result.at[index, 'news_count_24h'] = len(rows)
            result.at[index, 'news_source_count_24h'] = len(sources_by_code.get(code, set()))
            for name in ['positive', 'negative', 'risk']:
                result.at[index, 'news_' + name + '_terms_24h'] = sum(r[name + '_terms'] for r in rows)
            result.at[index, 'disclosure_count_24h'] = sum(r['source_provider'] == 'dart' for r in rows)
    if not np.isfinite(result[NEWS_COLUMNS]).all(axis=None):
        raise ValueError('Nonfinite news feature values.')
    return result
