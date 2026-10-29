from datetime import datetime
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np

from src.crawler.market_clock import KST
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION, history_features
from src.features.price_learning_dataset import FEATURES
from src.pipeline.price_learning_cycle import run_cycle
from test_completed_price_history import prices
from test_forward_price_forecast import bundle


class PriceLearningCycleTests(unittest.TestCase):
    def run_example(self, root, now, failed=False, wrong_schema=False):
        model = bundle()
        model['metadata'].update(feature_version=HISTORY_FEATURE_VERSION, features=FEATURES)
        raw = history_features(prices())
        raw.attrs = {'feature_version': 'wrong' if wrong_schema else HISTORY_FEATURE_VERSION,
                     'history_provenance': {'failed_stocks': int(failed)}}
        with patch('src.pipeline.price_learning_cycle.load_bundle', return_value=model), patch(
                'src.pipeline.price_learning_cycle.load_model_snapshots', return_value=(raw, {})), patch(
                'src.models.price_forecaster.predict_values', return_value=(np.array([.65]), np.array([.01]))), patch(
                'src.report_generator.supervised_forecast_report.stock_catalog', return_value={'삼성전자': {'005930'}}):
            return run_cycle(root, root, root / 'ledgers', root / 'public.json', root / 'status.json', now)

    def test_timely_original_is_frozen_once_then_only_graded(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            now = datetime(2026, 10, 20, 18, tzinfo=KST)
            first = self.run_example(root, now)
            self.assertEqual(first['new_frozen_predictions'], 1)
            self.assertEqual(first['forward']['pending'], 1)
            originals = [p for p in (root / 'ledgers').glob('*.csv') if '_eval_' not in p.name]
            self.assertEqual(len(originals), 1)
            before = hashlib.sha256(originals[0].read_bytes()).hexdigest()
            again = self.run_example(root, now)
            self.assertEqual(again['new_frozen_predictions'], 0)
            self.assertEqual(again['recording_state'], 'already_recorded_original_preserved')
            self.assertEqual(before, hashlib.sha256(originals[0].read_bytes()).hexdigest())
            self.assertFalse(again['recommendation_enabled'])

    def test_after_open_does_not_create_a_backdated_original(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result = self.run_example(root, datetime(2026, 10, 21, 10, tzinfo=KST))
            self.assertEqual(result['new_frozen_predictions'], 0)
            self.assertEqual(result['recording_state'], 'outside_recording_window_no_backdated_forecast')
            self.assertFalse((root / 'ledgers').exists())
            self.assertTrue((root / 'public.json').exists())

    def test_failed_collection_or_wrong_schema_cannot_replace_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / 'public.json'
            output.write_text('previous')
            for options in [{'failed': True}, {'wrong_schema': True}]:
                with self.assertRaises(ValueError):
                    self.run_example(root, datetime(2026, 10, 20, 18, tzinfo=KST), **options)
                self.assertEqual(output.read_text(), 'previous')
                self.assertFalse((root / 'ledgers').exists())


if __name__ == '__main__':
    unittest.main()
