from datetime import datetime, timedelta
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import joblib
import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.crawler.market_clock import KST
from src.features.ohlcv_information import add_ohlcv_information
from src.features.price_learning_dataset import build_dataset, temporal_partitions
from src.models.selected_price_model import (
    COLUMNS, NAMES, ROOT, fold_plan, query_selected, raw_probability,
    run_training, select_family, weighted_quantiles,
)


class SelectedModelTests(unittest.TestCase):
    def setUp(self):
        self.raw = panel()
        self.days = sorted(self.raw.signal_date.unique())
        self.dataset, _ = build_dataset(add_ohlcv_information(self.raw))
        self.train, self.calibration, self.test = temporal_partitions(self.dataset, self.days[100], self.days[120])

    def test_all_three_folds_are_purged_and_have_disjoint_validation_dates(self):
        dates = set()
        for train, validation in fold_plan(self.train):
            self.assertLess(train.label_available_date.max(), validation.signal_date.min())
            self.assertTrue(dates.isdisjoint(set(validation.signal_date)))
            dates.update(validation.signal_date)
        self.assertEqual(len(fold_plan(self.train)), 3)

    def test_selection_is_train_only_and_ensemble_is_fixed_mean(self):
        with patch('builtins.print'):
            winner, scores, prior, audits, oof = select_family(self.train)
        self.assertEqual(winner, min(scores, key=lambda name: (scores[name], name)))
        self.assertEqual(set(scores), set(NAMES))
        self.assertEqual(len(audits), 3)
        self.assertTrue(np.isfinite(prior))
        self.assertFalse(oof.duplicated(['stock_code', 'signal_date']).any())
        np.testing.assert_allclose(oof.fixed_mean, oof[['linear', 'hgb_shallow', 'hgb_medium', 'extra_trees']].mean(axis=1))
        models = {}
        for name, value in zip(NAMES[:4], [.1, .3, .6, .8]):
            model = Mock()
            model.predict_proba.return_value = np.array([[1 - value, value]])
            models[name] = model
        np.testing.assert_allclose(raw_probability(models, 'fixed_mean', pd.DataFrame({'x': [0]})), [.45])

    def test_poisoning_external_outcomes_does_not_change_training_or_calibration(self):
        poisoned = self.dataset.copy()
        external = poisoned.signal_date >= self.days[120]
        poisoned.loc[external, 'target'] = 1 - poisoned.loc[external, 'target']
        poisoned.loc[external, 'target_return'] *= -100
        train, calibration, _ = temporal_partitions(poisoned, self.days[100], self.days[120])
        pd.testing.assert_frame_equal(train, self.train)
        pd.testing.assert_frame_equal(calibration, self.calibration)

    def test_weighted_residuals_handle_unequal_date_sizes_without_invalid_values(self):
        np.testing.assert_allclose(weighted_quantiles([.2] * 10, np.ones(10)), [.2, .2])
        self.assertLess(weighted_quantiles([0, 100], [100, 1], [.5])[0], 5)
        with self.assertRaises(ValueError):
            weighted_quantiles([1, 2], [1, 0])
        with self.assertRaises(ValueError):
            weighted_quantiles([np.nan], [1])

    def test_complete_run_artifact_is_queryable_but_cannot_recommend(self):
        protocol = json.loads((ROOT / 'docs/model_experiments/selected_model_protocol_20261021.json').read_text())
        protocol.update(labels_as_of=str(pd.Timestamp(self.days[-1]).date()),
                        calibration_start=str(pd.Timestamp(self.days[100]).date()), test_start=str(pd.Timestamp(self.days[120]).date()),
                        periods={'development_audit': [str(pd.Timestamp(self.days[120]).date()), str(pd.Timestamp(self.days[-6]).date())]})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('src.models.selected_price_model.load_snapshots', return_value=(self.raw, {})), patch('builtins.print'):
                summary = run_training('/unused', root / 'models', protocol, root / 'report.md')
            self.assertFalse(summary['recommendation_gate_passed'])
            self.assertFalse(summary['development_screen_passed'])
            run = Path(summary['run_dir'])
            bundle = joblib.load(run / 'model.joblib')
            self.assertNotIn('results', bundle['metadata'])
            self.assertNotIn('test', bundle['metadata'])
            self.assertEqual(bundle['features'], COLUMNS)
            self.assertEqual(len(bundle['metadata']['dataset_sha256']), 64)
            self.assertLessEqual(bundle['metadata']['partitions']['calibration']['latest_label'], bundle['metadata']['as_of'])
            for role in ['anchor', 'selected']:
                frame = pd.read_csv(run / (role + '_development_audit.csv'))
                self.assertTrue(frame.recommendation.eq('ABSTAIN').all())
                self.assertTrue((frame.empirical_return_lower <= frame.empirical_return_upper).all())
            with patch('src.models.selected_price_model.load_snapshots', return_value=(self.raw, {})):
                result = query_selected(root / 'models', root, '000001', now=datetime.now(KST) + timedelta(seconds=1))
            self.assertEqual(result['recommendation'], 'ABSTAIN')
            self.assertEqual(result['status'], 'STALE_DATA')
            self.assertLessEqual(result['empirical_return_lower'], result['empirical_return_upper'])
            self.assertIn('NOT guaranteed', result['interval_note'])


if __name__ == '__main__':
    unittest.main()
