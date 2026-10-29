from datetime import datetime, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import numpy as np
import pandas as pd

from src.crawler.learning_news_collector import collect_news, disclosure_items, load_catalog, query_plan
from src.features.news_learning import NEWS_COLUMNS, add_news_features, archive_batch, aware_time, read_archive, term_count
from src.models.news_shadow_model import compare_news, split_shadow
from src.models.selected_price_model import COLUMNS


def catalog():
    return pd.DataFrame([['005930', 'Samsung'], ['000660', 'Hynix']], columns=['stock_code', 'stock_name'])


def item(**changes):
    row = dict(source_provider='google_news_rss', title='Samsung profit growth - Publisher',
               published_at='2026-10-29T05:00:00+00:00', link='https://example.com/article?utm_source=test',
               query='Samsung', publisher_url='https://publisher.com', topic='company')
    return {**row, **changes}


def request(**changes):
    return dict(source_provider='google_news_rss', query='Samsung', stock_codes=['005930'],
                status='success', **changes)


def prices(day='2026-10-29'):
    return pd.DataFrame(dict(stock_code=['005930', '000660'], signal_date=[pd.Timestamp(day)] * 2))


class NewsLearningTests(unittest.TestCase):
    def test_utc_and_rfc_dates_are_explicit_and_naive_dates_are_rejected(self):
        self.assertEqual(aware_time('Thu, 29 Oct 2026 14:00:00 +0900'), pd.Timestamp('2026-10-29T05:00Z'))
        with self.assertRaises(ValueError):
            aware_time('2026-10-29 14:00')

    def test_old_file_cannot_backdate_first_seen_and_archive_is_append_only(self):
        with tempfile.TemporaryDirectory() as directory:
            clock = '2026-10-29T08:00:00Z'
            first = archive_batch([item()], [request()], catalog(), directory, clock)
            before = {p.name: p.read_bytes() for p in Path(directory).iterdir()}
            archive_batch([item()], [], catalog(), directory, '2026-10-30T08:00Z')
            self.assertEqual(len(list(Path(directory).glob('*.jsonl'))), 2)
            for name, payload in before.items():
                self.assertEqual((Path(directory) / name).read_bytes(), payload)
            rows, statuses, _ = read_archive(directory)
            features = add_news_features(prices(), rows, statuses)
            self.assertEqual(features.news_count_24h.tolist(), [0, 0])
            self.assertEqual(first['rows'], 1)
            self.assertEqual(aware_time(rows[0]['first_seen_at']), pd.Timestamp(clock))

    def test_query_is_not_proof_of_entity_and_only_public_metadata_is_saved(self):
        with tempfile.TemporaryDirectory() as directory:
            archive_batch([item(title='Unrelated corporation wins contract')], [request()], catalog(), directory,
                          '2026-10-29T06:00Z')
            rows, _, _ = read_archive(directory)
            self.assertEqual(rows[0]['stock_codes'], [])
            self.assertEqual(rows[0]['link'], 'https://example.com/article')
            self.assertNotIn('summary', rows[0])
            self.assertEqual(rows[0]['source_domain'], 'publisher.com')

    def test_future_publication_and_late_revisions_do_not_leak(self):
        with tempfile.TemporaryDirectory() as directory:
            archive_batch([item(), item(title='Samsung future event', published_at='2026-10-29T09:00Z')],
                          [request()], catalog(), directory, '2026-10-29T06:00Z')
            rows, statuses, _ = read_archive(directory)
            before = add_news_features(prices(), rows, statuses)
            archive_batch([item(title='Samsung fraud loss', link='https://example.com/revised')],
                          [], catalog(), directory, '2026-10-29T08:00Z')
            rows, statuses, _ = read_archive(directory)
            after = add_news_features(prices(), rows, statuses)
            pd.testing.assert_frame_equal(before, after)
            self.assertEqual(before.news_count_24h.tolist(), [1, 0])
            self.assertEqual(before.news_risk_terms_24h.tolist(), [0, 0])

    def test_duplicate_stories_do_not_inflate_counts(self):
        with tempfile.TemporaryDirectory() as directory:
            duplicate = item(source_provider='other_feed', title='Samsung profit growth - Other Publisher',
                             link='https://other.example/story')
            archive_batch([item(), duplicate, item()], [request()], catalog(), directory, '2026-10-29T06:00Z')
            archive_batch([item()], [request()], catalog(), directory, '2026-10-29T06:30Z')
            rows, statuses, _ = read_archive(directory)
            features = add_news_features(prices(), rows, statuses)
            self.assertEqual(features.news_count_24h.tolist(), [1, 0])
            self.assertEqual(features.news_company_query_observed.tolist(), [1, 0])

    def test_missing_news_collection_is_not_a_successful_empty_feed(self):
        with tempfile.TemporaryDirectory() as directory:
            archive_batch([], [{**request(), 'status': 'failed'}], catalog(), directory, '2026-10-29T06:00Z')
            rows, statuses, _ = read_archive(directory)
            features = add_news_features(prices(), rows, statuses)
            self.assertEqual(features.news_collection_observed.tolist(), [0, 0])
            self.assertEqual(features.news_count_24h.tolist(), [0, 0])

    def test_global_context_applies_to_every_candidate_without_pool_reduction(self):
        with tempfile.TemporaryDirectory() as directory:
            archive_batch([item(title='Oil war risk', topic='energy')], [request()], catalog(), directory,
                          '2026-10-29T06:00Z')
            rows, statuses, _ = read_archive(directory)
            features = add_news_features(prices(), rows, statuses)
            self.assertEqual(len(features), 2)
            self.assertEqual(features.global_news_count_24h.tolist(), [1, 1])
            self.assertEqual(features.global_risk_terms_24h.tolist(), [1, 1])
            self.assertEqual(features.news_count_24h.tolist(), [0, 0])

    def test_unverified_gdelt_index_time_and_bad_metadata_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            result = archive_batch([item(source_provider='gdelt'), item(published_at='2026-10-29'),
                item(title=''), item(link='https://user:secret@example.com')], [], catalog(), directory,
                '2026-10-29T06:00Z')
            self.assertEqual(result['rows'], 0)
            self.assertEqual(result['rejected']['invalid_publication_or_metadata'], 4)

    def test_checksum_or_incomplete_pair_prevents_learning(self):
        with tempfile.TemporaryDirectory() as directory:
            archive_batch([item()], [], catalog(), directory, '2026-10-29T06:00Z')
            path = next(Path(directory).glob('*.jsonl'))
            original = path.read_bytes()
            path.write_bytes(original + b'\n')
            with self.assertRaises((ValueError, json.JSONDecodeError)):
                read_archive(directory)
            path.write_bytes(original)
            path.with_suffix('.manifest.json').unlink()
            with self.assertRaisesRegex(ValueError, 'incomplete'):
                read_archive(directory)

    def test_rotation_is_broad_and_independent_of_ranking(self):
        full = pd.DataFrame(dict(stock_code=[str(n).zfill(6) for n in range(100)],
                                 stock_name=['Company ' + str(n) for n in range(100)]))
        covered = set()
        for day in range(1, 6):
            plan = query_plan(full, datetime(2026, 10, day, tzinfo=timezone.utc))
            self.assertEqual(len(plan), 24)
            covered |= {code for row in plan for code in row['stock_codes']}
        self.assertEqual(len(covered), 100)

    def test_actual_fetch_failure_does_not_store_exception_secret(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'data/processed').mkdir(parents=True)
            catalog().to_csv(root / 'data/processed/ml_stock_catalog.csv', index=False)
            provider = Mock(provider_name='test_feed')
            provider.fetch.side_effect = RuntimeError('SECRET_DO_NOT_PUBLISH')
            with patch('src.crawler.learning_news_collector.time.sleep'):
                result = collect_news(root, limit=1, provider_factory=lambda language: provider)
            self.assertEqual(result['rows'], 0)
            self.assertNotIn('SECRET_DO_NOT_PUBLISH', str(result))
            self.assertTrue(all(row['status'] == 'failed_RuntimeError' for row in result['requests']))

    def test_date_only_disclosures_are_conservative_and_verified_by_code(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'data/raw').mkdir(parents=True)
            pd.DataFrame([dict(rcept_dt='20261029', rcept_no='20261029000001', corp_name='Unmatched alias',
                               report_nm='Disclosure', stock_code='005930')]).to_csv(
                                   root / 'data/raw/dart_disclosures_20261029.csv', index=False)
            items = disclosure_items(root, now=datetime(2026, 10, 29, tzinfo=timezone.utc))
            self.assertEqual(aware_time(items[0]['published_at']), pd.Timestamp('2026-10-29T14:59:59Z'))
            archive_batch(items, [], catalog(), root / 'ledger', '2026-10-29T06:00Z')
            rows, statuses, _ = read_archive(root / 'ledger')
            self.assertEqual(rows[0]['stock_codes'], ['005930'])
            self.assertEqual(add_news_features(prices(), rows, statuses).news_count_24h.tolist(), [0, 0])

    def test_no_fake_training_when_news_has_not_accumulated(self):
        empty = prices().assign(target=np.nan, news_collection_observed=0.)
        result = compare_news(empty)
        self.assertEqual(result['status'], 'accumulating_point_in_time_news')
        self.assertEqual(result['mature_news_rows'], 0)
        self.assertNotIn('results', result)
        self.assertFalse(result['recommendation_enabled'])

    def test_english_keyword_matches_are_not_substrings(self):
        self.assertEqual(term_count('award winner', ['war']), 0)
        self.assertEqual(term_count('trade war escalates', ['war']), 1)

    def test_empty_archive_never_loads_prices_or_fits_synthetic_news_history(self):
        from src.models.news_shadow_model import run_shadow
        with tempfile.TemporaryDirectory() as directory, patch('src.models.news_shadow_model.load_inputs') as load:
            root = Path(directory)
            result = run_shadow(root / 'not-a-price-snapshot', root / 'archive', root / 'result.json', '2026-10-28')
            load.assert_not_called()
            self.assertEqual(result['mature_news_rows'], 0)

    def test_legacy_provider_error_does_not_expose_credential_in_url(self):
        from src.news_providers.provider_runner import run_provider
        provider = Mock(provider_name='configured_feed')
        provider.is_available.return_value = True
        provider.fetch.side_effect = RuntimeError('https://api.example/?api_key=SECRET_TEST_VALUE')
        with patch('builtins.print') as output:
            rows, status = run_provider(provider, 'Samsung', 5)
        self.assertEqual(rows, [])
        self.assertEqual(status['error_message'], 'RuntimeError')
        self.assertNotIn('SECRET_TEST_VALUE', str(output.call_args_list))

    def test_same_story_can_be_company_news_and_global_context_without_double_count(self):
        with tempfile.TemporaryDirectory() as directory:
            archive_batch([item(), item(topic='semiconductors')], [request()], catalog(), directory,
                          '2026-10-29T06:00Z')
            rows, statuses, _ = read_archive(directory)
            features = add_news_features(prices(), rows, statuses)
            self.assertEqual(features.news_count_24h.tolist(), [1, 0])
            self.assertEqual(features.global_news_count_24h.tolist(), [1, 1])

    def test_public_card_does_not_claim_validation_or_render_raw_research_strings(self):
        from src.report_generator.news_learning_panel import render_news_learning_card
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'status.json'
            now = datetime(2026, 10, 29, tzinfo=timezone.utc)
            data = dict(status='accumulating_point_in_time_news', generated_at=now.isoformat(),
                        mature_news_dates=0, mature_news_rows=0, recommendation_enabled=False,
                        production_model_changed=False, raw_rule='<script>unsafe()</script>')
            path.write_text(json.dumps(data))
            html = render_news_learning_card(path, now)
            self.assertIn('학습용 이력 축적 중', html)
            self.assertIn('아직 적용하지 않습니다', html)
            self.assertNotIn('<script>', html)
            data['recommendation_enabled'] = True
            path.write_text(json.dumps(data))
            self.assertIn('점검 필요', render_news_learning_card(path, now))

    def test_public_card_detects_stale_and_missing_status_without_fabricating_success(self):
        from src.report_generator.news_learning_panel import render_news_learning_card
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'status.json'
            now = datetime(2026, 10, 29, tzinfo=timezone.utc)
            self.assertIn('데이터 연결 대기', render_news_learning_card(path, now))
            path.write_text(json.dumps(dict(status='accumulating_point_in_time_news',
                generated_at='2026-10-01T00:00:00+00:00', recommendation_enabled=False,
                production_model_changed=False)))
            self.assertIn('상태 갱신 필요', render_news_learning_card(path, now))

    def test_matched_models_use_identical_purged_rows_and_do_not_promote(self):
        rng = np.random.default_rng(11)
        days = pd.bdate_range('2025-01-01', periods=60)
        frame = pd.DataFrame([(str(code).zfill(6), day) for day in days for code in range(30)],
                             columns=['stock_code', 'signal_date'])
        for column in COLUMNS + NEWS_COLUMNS:
            frame[column] = rng.normal(size=len(frame))
        frame['news_collection_observed'] = 1.
        frame['label_available_date'] = frame.signal_date + pd.offsets.BDay(5)
        frame['target'] = np.arange(len(frame)) % 2
        frame['net_return_proxy'] = np.where(frame.target.eq(1), .02, -.02)
        train, calibration, test = split_shadow(frame)
        self.assertLess(train.label_available_date.max(), calibration.signal_date.min())
        self.assertLess(calibration.label_available_date.max(), test.signal_date.min())
        result = compare_news(frame)
        self.assertEqual(result['status'], 'matched_development_comparison')
        self.assertEqual(result['results']['price_only']['evaluated_cases'], result['results']['price_plus_news']['evaluated_cases'])
        self.assertFalse(result['production_model_changed'])
        self.assertFalse(result['recommendation_enabled'])


if __name__ == '__main__':
    unittest.main()
