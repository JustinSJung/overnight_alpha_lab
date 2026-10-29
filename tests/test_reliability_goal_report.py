import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
import pandas as pd

from src.crawler.price_learning_history import file_digest
from src.report_generator.reliability_goal_report import exact_benchmark, shadow_originals


class ReliabilityGoalReportTests(unittest.TestCase):
    def benchmark_fixture(self, root):
        calendar = pd.bdate_range('2026-10-01', periods=12)
        (root / 'raw').mkdir()
        stocks = []
        for code, offset in [('069500', 0), ('229200', 10)]:
            frame = pd.DataFrame(dict(date=calendar, open=100. + offset + np.arange(12),
                                      close=101. + offset + np.arange(12), high=120. + offset,
                                      low=90. + offset, volume=1000.))
            path = root / 'raw' / (code + '.csv')
            frame.to_csv(path, index=False)
            stocks.append(dict(stock_code=code, status='success', sha256=file_digest(path)))
        (root / 'history_manifest.json').write_text(json.dumps(dict(collection_complete=True,
            completed_bars_only=True, requested_codes=['069500', '229200'], stocks=stocks)))
        return calendar

    def test_benchmark_uses_exact_next_open_and_fifth_close_with_same_cost(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            calendar = self.benchmark_fixture(root)
            result = exact_benchmark(root, calendar, 'etf-test')
            self.assertEqual(len(result), 7)
            self.assertEqual(result.iloc[0].entry_date, calendar[1])
            self.assertEqual(result.iloc[0].exit_date, calendar[5])
            expected = ((106 / 101 - 1) + (116 / 111 - 1)) / 2 - .003
            self.assertAlmostEqual(result.iloc[0].net_return, expected)
            self.assertTrue(result.source.eq('etf-test').all())

    def test_changed_benchmark_file_fails_and_missing_exact_session_is_not_shifted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            calendar = self.benchmark_fixture(root)
            path = root / 'raw/069500.csv'
            frame = pd.read_csv(path).drop(index=5)
            frame.to_csv(path, index=False)
            with self.assertRaisesRegex(ValueError, 'checksum'):
                exact_benchmark(root, calendar, 'etf-test')
            manifest_path = root / 'history_manifest.json'
            manifest = json.loads(manifest_path.read_text())
            manifest['stocks'][0]['sha256'] = file_digest(path)
            manifest_path.write_text(json.dumps(manifest))
            result = exact_benchmark(root, calendar, 'etf-test')
            self.assertNotIn(calendar[0], result.signal_date.tolist())
            self.assertNotIn(calendar[4], result.signal_date.tolist())
            self.assertIn(calendar[1], result.signal_date.tolist())

    def test_first_shadow_batch_is_chosen_before_answers_and_hash_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            model = root / 'models/runs/example'
            model.mkdir(parents=True)
            identity = dict(dataset_sha256='a' * 64, trained_at='2026-10-26T15:00:00+09:00')
            (model / 'model_metadata.json').write_text(json.dumps(identity))
            for key, signal, hour in [('a', '2026-10-26', 17), ('b', '2026-10-26 00:00:00', 18)]:
                path = root / ('ml_test_20261026_' + key * 16 + '.csv')
                pd.DataFrame([dict(signal_date=signal, recorded_at=f'2026-10-26T{hour}:00:00+09:00',
                    model_dataset_sha256=identity['dataset_sha256'], model_trained_at=identity['trained_at'])]).to_csv(path, index=False)
                path.with_suffix('.manifest.json').write_text(json.dumps(dict(sha256=file_digest(path))))
            paths, excluded = shadow_originals(root, 'ml_test_', root / 'models')
            self.assertEqual(paths[0].name, 'ml_test_20261026_' + 'a' * 16 + '.csv')
            self.assertEqual(excluded, 1)
            paths[0].write_text(paths[0].read_text() + '\n')
            with self.assertRaisesRegex(ValueError, 'changed'):
                shadow_originals(root, 'ml_test_', root / 'models')


if __name__ == '__main__':
    unittest.main()
