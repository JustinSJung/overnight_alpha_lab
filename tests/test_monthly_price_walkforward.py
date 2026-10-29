from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.features.price_learning_dataset import FEATURES, build_dataset
from src.models.market_context_experiment import date_metrics
from src.models.monthly_price_walkforward import (
    fit_asof, month_plan, monthly_split, paired_interval, run_experiment,
)
from src.models.price_forecaster import forecast_row, load_bundle, predict_values, save_artifacts


class MonthlyWalkForwardTests(unittest.TestCase):
    def setUp(self):
        self.raw = panel()
        self.dataset, self.metadata = build_dataset(self.raw, as_of=self.raw.signal_date.max())
        self.calendar = pd.DatetimeIndex(sorted(self.raw.signal_date.unique()))
        self.start = self.calendar[100]
        self.end = self.calendar[-6]
        self.plan = month_plan(self.dataset, self.calendar, self.start, self.end)

    def test_first_partial_month_still_uses_previous_calendar_month(self):
        month, as_of, test = self.plan[0]
        self.assertGreater(test.signal_date.min().day, 1)
        self.assertLess(as_of, pd.Period(month).start_time)
        self.assertEqual(as_of, self.calendar[self.calendar < pd.Period(month).start_time][-1])

    def test_maturity_purge_and_window_sizes(self):
        _, as_of, _ = self.plan[0]
        train, calibration = monthly_split(self.dataset, as_of, 40, 10)
        self.assertEqual(train.signal_date.nunique(), 40)
        self.assertEqual(calibration.signal_date.nunique(), 10)
        self.assertLess(train.label_available_date.max(), calibration.signal_date.min())
        self.assertLessEqual(calibration.label_available_date.max(), as_of)
        self.assertTrue((pd.concat([train, calibration]).target_date <= as_of).all())
        with self.assertRaises(ValueError):
            monthly_split(self.dataset, as_of, 500, 10)

    def test_prior_test_labels_enter_only_after_becoming_known(self):
        _, first_asof, first_test = self.plan[0]
        _, next_asof, _ = self.plan[1]
        train, calibration = monthly_split(self.dataset, next_asof, 40, 10)
        known = pd.concat([train, calibration])
        mature_prior_dates = first_test.loc[first_test.label_available_date <= next_asof, 'signal_date']
        self.assertTrue(known.signal_date.isin(mature_prior_dates).any())
        late = self.dataset[(self.dataset.signal_date <= next_asof) & (self.dataset.label_available_date > next_asof)]
        keys = set(zip(known.stock_code, known.signal_date))
        self.assertTrue(set(zip(late.stock_code, late.signal_date)).isdisjoint(keys))
        self.assertGreater(next_asof, first_asof)

    def test_future_outcome_poisoning_cannot_change_asof_model(self):
        _, as_of, test = self.plan[0]
        altered = self.dataset.copy()
        future = altered.label_available_date > as_of
        altered.loc[future, 'target'] = 1 - altered.loc[future, 'target']
        altered.loc[future, 'target_return'] *= -100
        original_split = monthly_split(self.dataset, as_of, 40, 10)
        poisoned_split = monthly_split(altered, as_of, 40, 10)
        pd.testing.assert_frame_equal(original_split[0], poisoned_split[0])
        pd.testing.assert_frame_equal(original_split[1], poisoned_split[1])
        with tempfile.TemporaryDirectory() as directory:
            a, run = fit_asof(*original_split, as_of, 40, self.metadata, Path(directory) / 'original')
            b, _ = fit_asof(*poisoned_split, as_of, 40, self.metadata, Path(directory) / 'poisoned')
            np.testing.assert_array_equal(predict_values(a, test[FEATURES])[0], predict_values(b, test[FEATURES])[0])
            self.assertEqual(a['metadata']['dataset_sha256'], b['metadata']['dataset_sha256'])
            self.assertIsNone(a['metadata']['test']['roc_auc'])
            self.assertEqual(set(a['metadata']['partitions']), {'train', 'calibration'})
            self.assertFalse((run / 'holdout_predictions.csv').exists())
            self.assertTrue((run / 'calibration_predictions.csv').exists())

    def test_baseline_vectors_align_and_paired_zero_difference(self):
        data = self.dataset[self.dataset.signal_date.between(self.start, self.end)].copy()
        data['probability_above_cost'] = .45
        data['predicted_close_return'] = .01
        data['selected_by_fixed_policy'] = False
        priors = np.where(data.signal_date.dt.month % 2, .4, .5)
        metrics = date_metrics(data, priors)
        self.assertTrue(np.isfinite(metrics['common_date_baseline_brier']))
        with self.assertRaises(ValueError):
            date_metrics(data, priors[:-1])
        interval = paired_interval(data, data, samples=100)
        self.assertEqual(interval['date_brier_delta'], 0)
        self.assertEqual(interval['lower_95'], 0)
        self.assertEqual(interval['upper_95'], 0)

    def test_artifact_filename_cannot_escape_run_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                save_artifacts({}, pd.DataFrame(), directory, predictions_name='../outside.csv')

    def test_complete_replay_matches_controls_and_keeps_forecasts_disabled(self):
        protocol = {'training_windows': [20, 40], 'calibration_sessions': 10,
                    'classifier': 'hist_gradient_boosting', 'features': FEATURES,
                    'horizon_sessions': 5, 'cost_assumption': .003, 'probability_threshold': .6,
                    'labels_as_of': str(self.calendar[-1].date()),
                    'evaluation_start': str(self.start.date()), 'evaluation_end': str(self.end.date())}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('src.models.monthly_price_walkforward.load_snapshots', return_value=(self.raw, {})), patch('builtins.print'):
                summary = run_experiment('/unused', root / 'models', protocol, root / 'report.md')
            self.assertEqual(len(summary['fits']), len(self.plan) * 2)
            reference = None
            for window in protocol['training_windows']:
                frozen = pd.read_csv(root / f'models/frozen_{window}/historical_predictions.csv')
                monthly = pd.read_csv(root / f'models/monthly_{window}/historical_predictions.csv')
                self.assertEqual(frozen.model_run.nunique(), 1)
                self.assertEqual(monthly.model_run.nunique(), len(self.plan))
                self.assertTrue((pd.to_datetime(monthly.model_asof) < pd.to_datetime(monthly.signal_date)).all())
                first_month = monthly.signal_date.str[:7].eq(self.plan[0][0])
                np.testing.assert_array_equal(frozen.loc[first_month, 'probability_above_cost'], monthly.loc[first_month, 'probability_above_cost'])
                for frame in [frozen, monthly]:
                    if reference is None:
                        reference = frame[['stock_code', 'signal_date', 'target']]
                    self.assertTrue(reference.equals(frame[['stock_code', 'signal_date', 'target']]))
                    self.assertFalse(frame.duplicated(['stock_code', 'signal_date']).any())
                    self.assertTrue(frame.recommendation.eq('ABSTAIN').all())
                    self.assertTrue(frame.origin.eq('retrospective_replay_not_prospective_forecast').all())
                model_dir = root / f'models/window_{window}' / self.plan[-1][0]
                bundle = load_bundle(model_dir)
                row = self.raw.iloc[-1]
                result = forecast_row(bundle, row, row.signal_date)
                self.assertEqual(result['recommendation'], 'ABSTAIN')
                self.assertIsNone(result['validation_auc'])
            self.assertTrue((root / 'report.md').exists())
            self.assertTrue((root / 'report.json').exists())


if __name__ == '__main__':
    unittest.main()
