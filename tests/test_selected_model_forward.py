from datetime import datetime
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.crawler.market_clock import KST
from src.evaluator.forward_price_forecast import grade_predictions
from src.evaluator.selected_model_forward import freeze_selected
from src.models.selected_price_model import COLUMNS, CONTEXT_COLUMNS


class SelectedForwardTests(unittest.TestCase):
    def setUp(self):
        self.raw = panel()
        self.origin = pd.Timestamp(sorted(self.raw.signal_date.unique())[-6])
        self.now = self.origin.tz_localize(KST) + pd.Timedelta(hours=18)
        self.bundle = {'metadata': {'dataset_sha256': 'a' * 64, 'horizon_sessions': 5,
                                   'cost_assumption': .003, 'as_of': '2023-01-01',
                                   'trained_at': (self.now - pd.Timedelta(hours=1)).isoformat(),
                                   'data_root': '/unused'},
                       'baseline_probability': .48, 'selected_name': 'extra_trees', 'features': COLUMNS}

    def freeze(self, output, now=None, raw=None):
        def predictions(bundle, features):
            return tuple(np.full(len(features), value) for value in [.52, .01, -.1, .12])
        with patch('src.evaluator.selected_model_forward.load_selected', return_value=self.bundle), \
                patch('src.evaluator.selected_model_forward.load_snapshots', return_value=(self.raw if raw is None else raw, {})), \
                patch('src.evaluator.selected_model_forward.predict_values', side_effect=predictions):
            return freeze_selected('/unused', None, output, now if now is not None else self.now)

    def test_original_records_are_unique_immutable_and_grade_only_after_fifth_session(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.freeze(directory)
            path = Path(result['ledger'])
            original = path.read_bytes()
            ledger = pd.read_csv(path, dtype={'stock_code': str})
            self.assertEqual(result['frozen_predictions'], 8)
            self.assertFalse(ledger.prediction_id.duplicated().any())
            self.assertTrue(ledger.recommendation.eq('ABSTAIN').all())
            with self.assertRaises(FileExistsError):
                self.freeze(directory)
            self.assertEqual(original, path.read_bytes())
            pending, _ = grade_predictions(ledger, self.raw, self.origin + pd.offsets.BDay(4))
            resolved, rows = grade_predictions(ledger, self.raw, self.origin + pd.offsets.BDay(5))
            self.assertEqual(pending['resolved'], 0)
            self.assertEqual(resolved['resolved'], 8)
            self.assertTrue(rows.target.notna().all())
            self.assertEqual(original, path.read_bytes())

    def test_after_open_cannot_reconstruct_a_forward_forecast(self):
        raw = self.raw[self.raw.signal_date.le(self.origin)].copy()
        with tempfile.TemporaryDirectory() as directory:
            late = self.origin.tz_localize(KST) + pd.offsets.BDay(1) + pd.Timedelta(hours=10)
            result = self.freeze(directory, now=late, raw=raw)
            self.assertEqual(result['frozen_predictions'], 0)
            self.assertIn('no_backdated', result['status'])
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_unverified_or_same_fit_date_input_is_rejected(self):
        bad = self.raw.copy()
        bad.attrs['history_provenance'] = {'failed_stocks': 1}
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                self.freeze(directory, raw=bad)
            self.bundle['metadata']['as_of'] = str(self.origin.date())
            with self.assertRaises(ValueError):
                self.freeze(directory)
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_naive_clock_and_missing_fingerprint_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                self.freeze(directory, now=datetime(2023, 7, 1, 18))
            self.bundle['metadata'].pop('dataset_sha256')
            with self.assertRaises(ValueError):
                self.freeze(directory)

    def test_context_bundle_freezes_with_same_schema_and_full_universe(self):
        self.bundle['features'] = CONTEXT_COLUMNS
        self.bundle['metadata']['market_min_stocks'] = 4
        with tempfile.TemporaryDirectory() as directory:
            result = self.freeze(directory)
            self.assertEqual(result['frozen_predictions'], 8)


if __name__ == '__main__':
    unittest.main()
