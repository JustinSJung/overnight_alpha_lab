from datetime import datetime, timedelta, timezone
from pathlib import Path
import tempfile
import json
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from src.crawler.market_clock import completed_price_cutoff
from src.crawler.kis_price_collector import collect_for_stock, date_range
from src.crawler.price_learning_history import collect_history, fetch_history, PacedHistoryClient
from src.features.completed_price_dataset import history_features, load_completed_history
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.price_learning_dataset import make_features
from src.models.price_forecaster import refreshed_signal
from src.features.daily_price_signals import calculate_signal


def prices():
    close = np.arange(100.0, 140.0)
    return pd.DataFrame({'stock_code': '005930', 'date': pd.bdate_range(end='2026-10-20', periods=40),
                         'open': close, 'high': close + 1, 'low': close - 1,
                         'close': close, 'volume': np.full(40, 1000)})


class CompletedHistoryTests(unittest.TestCase):
    def test_history_model_refresh_matches_training_feature_precision(self):
        raw = prices()
        raw['close'] *= 1.00123456
        with patch('src.crawler.kis_client.KISClient') as factory:
            factory.return_value.get_daily_ohlcv.return_value = raw
            with patch('src.crawler.market_clock.completed_price_cutoff', return_value=datetime(2026, 10, 20).date()):
                row = refreshed_signal('005930', '2026-10-20', HISTORY_FEATURE_VERSION)
        expected = make_features(history_features(raw).tail(1)).reset_index(drop=True)
        actual = make_features(pd.DataFrame([row])).reset_index(drop=True)
        pd.testing.assert_frame_equal(expected, actual)

    def test_refresh_with_no_prices_abstains_cleanly(self):
        with patch('src.crawler.kis_client.KISClient') as factory:
            factory.return_value.get_daily_ohlcv.return_value = pd.DataFrame()
            with self.assertRaises(ValueError):
                refreshed_signal('005930', '2026-10-20', HISTORY_FEATURE_VERSION)

    def test_resume_skips_verified_files_and_refetches_tampered_files(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch('src.crawler.price_learning_history.fetch_history', return_value=prices()) as fetch:
                collect_history(None, ['005930'], directory, '2023-01-01', '2026-10-20')
                collect_history(None, ['005930'], directory, '2023-01-01', '2026-10-20')
                self.assertEqual(fetch.call_count, 1)
                (Path(directory) / 'raw/005930.csv').write_text('damaged')
                collect_history(None, ['005930'], directory, '2023-01-01', '2026-10-20')
                self.assertEqual(fetch.call_count, 2)
                with self.assertRaises(ValueError):
                    collect_history(None, ['005930'], directory, '2023-01-01', '2026-10-19')

    def test_stock_failure_does_not_stop_other_stocks_and_is_retried(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch('src.crawler.price_learning_history.fetch_history', side_effect=[RuntimeError('private'), prices()]):
                manifest = collect_history(None, ['000001', '000002'], directory, '2023-01-01', '2026-10-20')
            self.assertEqual([row['status'] for row in manifest['stocks']], ['failed', 'success'])
            self.assertNotIn('private', str(manifest))
            with patch('src.crawler.price_learning_history.fetch_history', return_value=prices()) as fetch:
                manifest = collect_history(None, ['000001', '000002'], directory, '2023-01-01', '2026-10-20')
                self.assertEqual(fetch.call_count, 1)
                self.assertTrue(all(row['status'] == 'success' for row in manifest['stocks']))

    def test_transient_request_is_retried_without_exposing_payload(self):
        client = unittest.mock.Mock()
        client.get_daily_ohlcv.side_effect = [RuntimeError('private'), prices()]
        with patch('src.crawler.price_learning_history.time.sleep'):
            result = PacedHistoryClient(client).get_daily_ohlcv('005930', '20230101', '20261020')
        self.assertEqual(len(result), 40)
        self.assertEqual(client.get_daily_ohlcv.call_count, 2)

    def test_loader_rejects_in_progress_collection_and_checks_digests(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch('src.crawler.price_learning_history.fetch_history', return_value=prices()):
                manifest = collect_history(None, ['005930'], directory, '2023-01-01', '2026-10-20')
            frame, _ = load_completed_history(directory)
            self.assertEqual(frame.attrs['history_provenance']['requested_stocks'], 1)
            path = Path(directory) / 'history_manifest.json'
            manifest['collection_complete'] = False
            path.write_text(json.dumps(manifest))
            with self.assertRaises(ValueError):
                load_completed_history(directory)
            manifest['collection_complete'] = True
            path.write_text(json.dumps(manifest))
            (Path(directory) / 'raw/005930.csv').write_text('damaged')
            with self.assertRaises(ValueError):
                load_completed_history(directory)

    def test_cutoff_is_korean_time_with_close_buffer(self):
        utc = timezone.utc
        self.assertEqual(str(completed_price_cutoff(datetime(2026, 10, 20, 0, tzinfo=utc))), '2026-10-19')
        self.assertEqual(str(completed_price_cutoff(datetime(2026, 10, 20, 7, tzinfo=utc))), '2026-10-20')
        self.assertEqual(date_range(now=datetime(2026, 10, 20, 10))[1], '20261019')

    def test_unfinished_bar_cannot_change_daily_signal(self):
        original = prices()
        changed = original.copy()
        changed.loc[39, 'close'] = 100000
        expected = calculate_signal(original.iloc[:-1], Path('test'), cutoff='2026-10-19')
        actual = calculate_signal(changed, Path('test'), cutoff='2026-10-19')
        self.assertEqual(expected, actual)
        self.assertEqual(actual['signal_date'], '2026-10-19')

    def test_collector_filters_provider_rows_beyond_requested_end(self):
        client = unittest.mock.Mock()
        client.get_daily_ohlcv.return_value = prices().tail(2)
        client.get_current_quote.return_value = {}
        result, _ = collect_for_stock('005930', '20260901', '20261019', client)
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result.iloc[0]['date'].date()), '2026-10-19')

    def test_ohlcv_features_are_consistent_and_causal(self):
        raw = prices()
        features = history_features(raw)
        self.assertAlmostEqual(features.iloc[30]['return_1d'], raw.iloc[30]['close']/raw.iloc[29]['close']-1)
        self.assertAlmostEqual(features.iloc[30]['return_20d'], raw.iloc[30]['close']/raw.iloc[10]['close']-1)
        raw.loc[raw.index > 30, 'close'] *= 10
        changed = history_features(raw)
        pd.testing.assert_frame_equal(features.iloc[:31], changed.iloc[:31])

    def test_pagination_moves_backward_and_stops_when_no_older_bars(self):
        class Client:
            def __init__(self):
                self.ends = []
            def get_daily_ohlcv(self, code, start, end):
                self.ends.append(end)
                return [pd.DataFrame({'date': ['2026-10-19', '2026-10-20'], 'close': [100, 101]}),
                        pd.DataFrame({'date': ['2026-10-16'], 'close': [99]}),
                        pd.DataFrame()][len(self.ends)-1]
        client = Client()
        frame = fetch_history(client, '005930', '20260101', '20261020', pause=0)
        self.assertEqual(client.ends, ['20261020', '20261018', '20261015'])
        self.assertEqual(len(frame), 3)

    def test_repeated_provider_page_fails_instead_of_looping(self):
        client = unittest.mock.Mock()
        client.get_daily_ohlcv.return_value = pd.DataFrame({'date': ['2026-10-20'], 'close': [100]})
        with self.assertRaises(ValueError):
            fetch_history(client, '005930', '20260101', '20261020', pause=0)


if __name__ == '__main__':
    unittest.main()
