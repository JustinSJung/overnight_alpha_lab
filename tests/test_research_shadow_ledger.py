from pathlib import Path
import tempfile
import unittest

import pandas as pd

from test_market_context_experiment import panel
from src.crawler.market_clock import KST
from src.evaluator.research_shadow_ledger import grade_shadow, seal_ledger
from src.features.next_open_dataset import TARGET_VERSION
from src.models.selected_price_model import COLUMNS, prepare_selected_features


class ResearchShadowLedgerTests(unittest.TestCase):
    def test_all_controls_are_frozen_and_graded_without_replacing_original(self):
        inputs = prepare_selected_features(panel(), COLUMNS)
        days = sorted(inputs.signal_date.unique())
        origin = pd.Timestamp(days[120])
        trained = (origin.tz_localize(KST) + pd.Timedelta(hours=16)).isoformat()
        recorded = (origin.tz_localize(KST) + pd.Timedelta(hours=17)).isoformat()
        metadata = dict(dataset_sha256='a' * 64, trained_at=trained)
        row = dict(stock_code='000001', signal_date=origin, prediction_id='original',
                   recorded_at=recorded, model_trained_at=trained, model_dataset_sha256='a' * 64,
                   target_version=TARGET_VERSION, horizon_sessions=5, cost_assumption=.003,
                   validation_base_rate=.5, probability_above_cost=.6, probability_ncp=.6,
                   probability_control=.4)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'original.csv'
            pd.DataFrame([row]).to_csv(path, index=False)
            seal_ledger(path, 'test', metadata, 'ncp', ['ncp', 'control'])
            before = path.read_bytes()
            now = pd.Timestamp(days[-1], tz=KST) + pd.Timedelta(hours=17)
            graded, summary = grade_shadow(path, inputs, days[-1], 'test', now)
            self.assertEqual(summary['evaluated_cases'], 1)
            self.assertEqual(set(summary['shadow_models']), {'ncp', 'control'})
            self.assertEqual(path.read_bytes(), before)
            self.assertNotEqual(summary['shadow_models']['ncp']['date_brier'], summary['shadow_models']['control']['date_brier'])
            with self.assertRaises(FileExistsError):
                seal_ledger(path, 'test', metadata, 'ncp', ['ncp', 'control'])
            with path.open('ab') as handle:
                handle.write(b'\n')
            with self.assertRaises(ValueError):
                grade_shadow(path, inputs, days[-1], 'test', now)


if __name__ == '__main__':
    unittest.main()
