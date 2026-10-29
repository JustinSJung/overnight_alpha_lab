from datetime import datetime, timedelta
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import joblib
import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.crawler.market_clock import KST
from src.features.price_learning_dataset import build_dataset, temporal_partitions
from src.models.context_model_selection import FEATURE_SETS, run_experiment, select_inputs
from src.models.selected_price_model import (
    COLUMNS, CONTEXT_COLUMNS, ROOT, checked_columns, fit_data_digest,
    prepare_selected_features, query_selected,
)


class ContextSelectionTests(unittest.TestCase):
    def setUp(self):
        self.raw = panel()
        self.days = sorted(self.raw.signal_date.unique())

    def test_combined_inputs_are_causal_and_market_coverage_is_required(self):
        before = prepare_selected_features(self.raw, CONTEXT_COLUMNS, 4)
        changed = self.raw.copy()
        future = changed.signal_date > self.days[80]
        changed.loc[future, ['open', 'high', 'low', 'close', 'volume']] *= 2
        changed.loc[future, ['return_1d', 'return_5d', 'return_20d']] += 1
        changed['target_return'] = np.arange(len(changed))
        after = prepare_selected_features(changed, CONTEXT_COLUMNS, 4)
        columns = ['stock_code', 'signal_date'] + CONTEXT_COLUMNS
        pd.testing.assert_frame_equal(before.loc[before.signal_date.le(self.days[80]), columns],
                                      after.loc[after.signal_date.le(self.days[80]), columns])
        sparse = prepare_selected_features(self.raw, CONTEXT_COLUMNS, 9)
        self.assertTrue(sparse.market_return_1d.isna().all())
        with self.assertRaises(ValueError):
            checked_columns(COLUMNS + ['target_return'])

    def test_feature_and_family_choice_cannot_see_external_outcomes(self):
        prepared = prepare_selected_features(self.raw, CONTEXT_COLUMNS, 4)
        dataset, _ = build_dataset(prepared)
        train, calibration, _ = temporal_partitions(dataset, self.days[100], self.days[120])
        poisoned = dataset.copy()
        poisoned.loc[poisoned.signal_date.ge(self.days[120]), 'target_return'] = -999
        external = poisoned.signal_date.ge(self.days[120])
        poisoned.loc[external, 'target'] = 1 - poisoned.loc[external, 'target']
        safe_train, safe_cal, _ = temporal_partitions(poisoned, self.days[100], self.days[120])
        self.assertEqual(fit_data_digest(train, calibration, CONTEXT_COLUMNS),
                         fit_data_digest(safe_train, safe_cal, CONTEXT_COLUMNS))
        seen = []

        def controlled(frame, progress_path=None, columns=None):
            pd.testing.assert_frame_equal(frame, train)
            seen.append(columns)
            scores = {'linear': .2 if columns == COLUMNS else .21}
            return 'linear', scores, .25, [], pd.DataFrame()

        with patch('src.models.context_model_selection.select_family', side_effect=controlled):
            selected, choices, _ = select_inputs(train)
        self.assertEqual(selected, 'ohlcv_19')
        self.assertEqual(len(choices), 2)
        self.assertEqual(seen, [COLUMNS, CONTEXT_COLUMNS])

    def test_full_run_keeps_test_scores_outside_artifact_and_query_uses_whole_universe(self):
        protocol = json.loads((ROOT / 'docs/model_experiments/context_selection_protocol_20261021.json').read_text())
        protocol.update(labels_as_of=str(pd.Timestamp(self.days[-1]).date()), market_min_stocks=4,
                        calibration_start=str(pd.Timestamp(self.days[100]).date()), test_start=str(pd.Timestamp(self.days[120]).date()),
                        periods={'development_audit': [str(pd.Timestamp(self.days[120]).date()), str(pd.Timestamp(self.days[-6]).date())]})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('src.models.context_model_selection.load_snapshots', return_value=(self.raw, {})), patch('builtins.print'):
                summary = run_experiment('/unused', root / 'models', protocol, root / 'report.md')
            self.assertFalse(summary['recommendation_gate_passed'])
            run = Path(summary['run_dir'])
            expected = min(summary['choices'], key=lambda arm: (
                summary['choices'][arm]['scores'][summary['choices'][arm]['family']], arm, summary['choices'][arm]['family']))
            self.assertEqual(summary['selected_arm'], expected)
            for arm, columns in FEATURE_SETS.items():
                bundle = joblib.load(run / (arm + '_model.joblib'))
                self.assertEqual(bundle['features'], columns)
                self.assertNotIn('results', bundle['metadata'])
                self.assertNotIn('test', bundle['metadata'])
                self.assertEqual(len(bundle['metadata']['dataset_sha256']), 64)
                predictions = pd.read_csv(run / (arm + '_development_audit.csv'))
                self.assertTrue(predictions.recommendation.eq('ABSTAIN').all())
                self.assertEqual(len(predictions), summary['results']['development_audit']['ohlcv_19']['evaluated_rows'])
            # Force only the research pointer to the fitted context arm for a query test.
            joblib.dump(joblib.load(run / 'ohlcv_market_29_model.joblib'), run / 'model.joblib')
            with patch('src.models.selected_price_model.load_snapshots', return_value=(self.raw, {})):
                result = query_selected(root / 'models', root, '000001', now=datetime.now(KST) + timedelta(seconds=1))
            self.assertEqual(result['recommendation'], 'ABSTAIN')
            self.assertTrue(0 <= result['probability_above_cost'] <= 1)
            self.assertLessEqual(result['empirical_return_lower'], result['empirical_return_upper'])


if __name__ == '__main__':
    unittest.main()
