import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import pandas as pd

from src.crawler.price_learning_history import file_digest
from src.crawler.update_completed_history import merge_completed_series, update_history


def series():
    days = pd.bdate_range('2026-10-01', periods=12)
    return pd.DataFrame({'stock_code': '005930', 'date': days, 'open': 100., 'high': 102.,
                         'low': 98., 'close': 101., 'volume': 1000., 'trading_value': 101000., 'price_source': 'kis'})


class CompletedUpdateTests(unittest.TestCase):
    def test_overlap_update_preserves_older_prices_and_adds_only_completed_days(self):
        full = series()
        old, fresh = full.iloc[:10].copy(), full.iloc[7:].copy()
        client = Mock()
        client.get_daily_ohlcv.return_value = fresh
        result, method = merge_completed_series(client, '005930', old, '2026-10-01', '2026-10-16')
        self.assertEqual(method, 'verified_overlap_update')
        self.assertEqual(len(result), 12)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), full)

    def test_overlap_price_revision_forces_full_coherent_refresh(self):
        full = series()
        old = full.iloc[:10].copy()
        adjusted = full.copy()
        adjusted[['open', 'high', 'low', 'close']] /= 2
        client = Mock()
        client.get_daily_ohlcv.return_value = adjusted.iloc[7:].copy()
        with patch('src.crawler.update_completed_history.fetch_history', return_value=adjusted) as fetch:
            result, method = merge_completed_series(client, '005930', old, '2026-10-01', '2026-10-16')
        fetch.assert_called_once()
        self.assertEqual(method, 'full_refresh_after_overlap_revision')
        self.assertTrue(result.close.eq(50.5).all())

    def test_terminal_bar_revision_merges_only_after_older_overlap_is_verified(self):
        full = series()
        old = full.iloc[:10].copy()
        corrected = full.copy()
        corrected.loc[9, 'close'] = 101.5
        corrected.loc[9, 'volume'] = 2000.
        client = Mock()
        client.get_daily_ohlcv.return_value = corrected.iloc[2:].copy()
        with patch('src.crawler.update_completed_history.fetch_history') as fetch:
            result, method = merge_completed_series(client, '005930', old, '2026-10-01', '2026-10-16')
        fetch.assert_not_called()
        self.assertEqual(method, 'verified_older_overlap_terminal_revision')
        self.assertTrue(result.attrs['overlap_revision']['terminal_only'])
        self.assertEqual(result.attrs['overlap_revision']['older_verified_dates'], 7)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), corrected)
        self.assertEqual(old.loc[9, 'close'], 101.)

    def test_terminal_revision_with_too_little_overlap_still_requires_full_refresh(self):
        full = series()
        changed = full.copy()
        changed.loc[9, 'close'] = 101.5
        client = Mock()
        client.get_daily_ohlcv.return_value = changed.iloc[8:].copy()
        with patch('src.crawler.update_completed_history.fetch_history', return_value=changed) as fetch:
            _, method = merge_completed_series(client, '005930', full.iloc[:10], '2026-10-01', '2026-10-16')
        fetch.assert_called_once()
        self.assertEqual(method, 'full_refresh_after_overlap_revision')

    def test_bad_or_future_updates_are_not_silently_cached(self):
        old = series().iloc[:10].copy()
        client = Mock()
        for bad in [pd.DataFrame(), series().assign(date=pd.Timestamp('2026-10-22')),
                    series().assign(close=-1), series().assign(volume=-1)]:
            client.get_daily_ohlcv.return_value = bad
            with self.assertRaises(ValueError):
                merge_completed_series(client, '005930', old, '2026-10-01', '2026-10-16')

    def test_full_refresh_cannot_silently_drop_old_history(self):
        full = series()
        adjusted = full.copy()
        adjusted[['open', 'high', 'low', 'close']] /= 2
        client = Mock()
        client.get_daily_ohlcv.return_value = adjusted.iloc[7:].copy()
        with patch('src.crawler.update_completed_history.fetch_history', return_value=adjusted.iloc[1:].copy()):
            with self.assertRaisesRegex(ValueError, 'dropped previously verified'):
                merge_completed_series(client, '005930', full.iloc[:10], '2026-10-01', '2026-10-16')

    def test_parent_is_immutable_update_is_resumable_and_failed_stock_is_not_hidden(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent, output = root / 'parent', root / 'updated'
            (parent / 'raw').mkdir(parents=True)
            entries = []
            for code in ['005930', '000001']:
                path = parent / 'raw' / (code + '.csv')
                series().iloc[:10].assign(stock_code=code).to_csv(path, index=False)
                entries.append({'stock_code': code, 'status': 'success', 'sha256': file_digest(path)})
            manifest = dict(source='kis_adjusted_daily', completed_bars_only=True, collection_complete=True,
                            start='2026-10-01', end='2026-10-14', scope='expanded_current_universe_research',
                            historical_limitations='test', requested_codes=['005930', '000001'], stocks=entries)
            path = parent / 'history_manifest.json'
            path.write_text(json.dumps(manifest))
            digest = file_digest(path)
            client = Mock()
            client.get_daily_ohlcv.side_effect = lambda code, *args: series().iloc[7:].assign(stock_code=code) if code == '005930' else (_ for _ in ()).throw(RuntimeError())
            with patch('builtins.print'):
                result = update_history(client, parent, output, '2026-10-16', workers=1)
            self.assertEqual(len(result['stocks']), 2)
            self.assertEqual(sum(row['status'] == 'failed' for row in result['stocks']), 1)
            self.assertEqual(file_digest(path), digest)
            client.get_daily_ohlcv.side_effect = lambda code, *args: series().iloc[7:].assign(stock_code=code)
            client.get_daily_ohlcv.reset_mock()
            with patch('builtins.print'):
                result = update_history(client, parent, output, '2026-10-16', workers=1)
            self.assertTrue(all(row['status'] == 'success' for row in result['stocks']))
            self.assertEqual(client.get_daily_ohlcv.call_count, 1)
            self.assertEqual(file_digest(path), digest)
            with self.assertRaises(ValueError):
                update_history(client, parent, parent, '2026-10-16')


if __name__ == '__main__':
    unittest.main()
