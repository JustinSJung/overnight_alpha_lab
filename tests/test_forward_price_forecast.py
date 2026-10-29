from datetime import datetime
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from src.crawler.market_clock import KST
from src.evaluator.forward_price_forecast import freeze_predictions, grade_predictions, valid_record_time
from src.features.completed_price_dataset import history_features
from test_completed_price_history import prices


def bundle():
    return {'metadata': {'as_of': '2026-06-30', 'dataset_sha256': 'a' * 64,
        'trained_at': '2026-10-20T09:00:00+00:00', 'horizon_sessions': 5,
        'cost_assumption': 0.003, 'probability_threshold': 0.6,
        'test': {'recommendation_gate_passed': False, 'base_rate': 0.45,
                 'roc_auc': 0.53, 'gate_reasons': ['pilot_universe_not_production_validated']}}}


class ForwardForecastTests(unittest.TestCase):
    def test_next_morning_before_open_is_valid_but_after_open_is_not(self):
        self.assertTrue(valid_record_time('2026-10-20', pd.Timestamp('2026-10-21T08:00:00+09:00')))
        self.assertFalse(valid_record_time('2026-10-20', pd.Timestamp('2026-10-21T09:01:00+09:00')))

    def freeze(self, output):
        with patch('src.models.price_forecaster.predict_values', return_value=(np.array([0.6]), np.array([0.02]))):
            return freeze_predictions(bundle(), history_features(prices()), output, datetime(2026, 10, 20, 18, tzinfo=KST))

    def test_forward_predictions_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'forward.csv'
            self.freeze(output)
            before = output.read_bytes()
            with self.assertRaises(FileExistsError):
                self.freeze(output)
            self.assertEqual(before, output.read_bytes())

    def test_no_future_outcomes_means_pending_not_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            ledger = self.freeze(Path(directory) / 'forward.csv')
        summary, graded = grade_predictions(ledger, history_features(prices()), '2026-10-20')
        self.assertEqual(summary['resolved'], 0)
        self.assertEqual(summary['states'], {'pending': 1})
        self.assertIsNone(summary['auc'])
        self.assertTrue(graded['target'].isna().all())

    def test_only_fifth_later_session_resolves_and_late_records_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            ledger = self.freeze(Path(directory) / 'forward.csv')
        extra = pd.DataFrame({'stock_code': '005930', 'date': pd.bdate_range('2026-10-21', periods=5),
                              'open': np.arange(140, 145), 'high': np.arange(141, 146),
                              'low': np.arange(139, 144), 'close': np.arange(140, 145), 'volume': 1000})
        future = history_features(pd.concat([prices(), extra], ignore_index=True))
        pending, _ = grade_predictions(ledger, future, '2026-10-26')
        self.assertEqual(pending['resolved'], 0)
        resolved, rows = grade_predictions(ledger, future, '2026-10-27')
        self.assertEqual(resolved['resolved'], 1)
        self.assertEqual(rows.iloc[0]['target_date'], '2026-10-27')
        self.assertAlmostEqual(rows.iloc[0]['observed_return'], 144 / 139 - 1)
        self.assertEqual(rows.iloc[0]['target'], 1)
        late = ledger.assign(recorded_at='2026-10-28T18:00:00+09:00')
        rejected, _ = grade_predictions(late, future, '2026-10-28')
        self.assertEqual(rejected['states'], {'invalid_record_time': 1})


if __name__ == '__main__':
    unittest.main()
