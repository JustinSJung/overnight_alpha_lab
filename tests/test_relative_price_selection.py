import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import joblib
import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.features.price_learning_dataset import FEATURES, temporal_partitions
from src.models.relative_price_selection import (
    ROOT, block_interval, daily_portfolio, fit_models, paired_returns,
    random_portfolios, rank_candidates, relative_dataset, run_experiment, score_inputs,
)


class RelativeSelectionTests(unittest.TestCase):
    def setUp(self):
        self.raw = panel()
        self.calendar = pd.DatetimeIndex(sorted(self.raw.signal_date.unique()))
        self.dataset, self.coverage, _ = relative_dataset(self.raw, self.calendar[-1], minimum_stocks=4)

    def test_targets_share_same_date_universe_but_keep_absolute_definition(self):
        for _, part in self.dataset.groupby('signal_date'):
            np.testing.assert_allclose(part.universe_return, part.target_return.mean())
            np.testing.assert_array_equal(part.relative_target, part.target_return.gt(part.target_return.mean()))
            np.testing.assert_array_equal(part.target, part.target_return.gt(.003))
            self.assertAlmostEqual(part.relative_return.mean(), 0)
        self.assertTrue((self.dataset.label_available_date >= self.dataset.target_date).all())

    def test_unresolved_stock_excludes_whole_date_not_just_stock(self):
        damaged = self.raw.copy()
        signal = self.calendar[100]
        missing = (damaged.stock_code == '000001') & damaged.signal_date.eq(self.calendar[105])
        damaged = damaged[~missing].copy()
        dataset, coverage, _ = relative_dataset(damaged, self.calendar[-1], minimum_stocks=4)
        self.assertEqual(coverage.loc[signal, 'eligible_count'], 8)
        self.assertEqual(coverage.loc[signal, 'resolved_count'], 7)
        self.assertFalse(coverage.loc[signal, 'included'])
        self.assertFalse(dataset.signal_date.eq(signal).any())
        with self.assertRaises(ValueError):
            relative_dataset(pd.concat([self.raw, self.raw.iloc[:1]]), self.calendar[-1], 4)

    def test_relative_label_waits_for_last_reference_outcome(self):
        delayed = self.raw.copy()
        signal, target_day, available = self.calendar[90], self.calendar[95], self.calendar[98]
        delayed.loc[delayed.stock_code.eq('000001') & delayed.signal_date.eq(target_day), 'snapshot_date'] = available
        dataset, _, _ = relative_dataset(delayed, self.calendar[-1], 4)
        part = dataset[dataset.signal_date.eq(signal)]
        self.assertEqual(len(part), 8)
        self.assertTrue(part.label_available_date.eq(available).all())
        before, _, _ = relative_dataset(delayed, self.calendar[96], 4)
        self.assertFalse(before.signal_date.eq(signal).any())

    def test_rank_ignores_future_labels_and_is_stable_under_shuffling(self):
        frame = self.dataset.copy()
        frame['score'] = .5
        original = rank_candidates(frame, 'score', 3)
        poisoned = frame.sample(frac=1, random_state=12)
        poisoned['target_return'] *= -1000
        poisoned['relative_target'] = 1 - poisoned.relative_target
        other = rank_candidates(poisoned, 'score', 3)
        keys = ['stock_code', 'signal_date']
        pd.testing.assert_frame_equal(original[keys].reset_index(drop=True), other[keys].reset_index(drop=True))
        self.assertEqual(set(original.stock_code), {'000001', '000002', '000003'})
        self.assertTrue(original.groupby('signal_date').size().eq(3).all())
        frame.loc[frame.index[0], 'score'] = np.nan
        with self.assertRaises(ValueError):
            rank_candidates(frame, 'score', 3)

    def test_random_is_reproducible_and_uses_all_dates_not_best_seed(self):
        before, dispersion = random_portfolios(self.dataset, [2, 3], 5, 42)
        after, _ = random_portfolios(self.dataset.sample(frac=1, random_state=2), [2, 3], 5, 42)
        for k in [2, 3]:
            pd.testing.assert_frame_equal(before[k], after[k])
            self.assertEqual(len(before[k]), self.dataset.signal_date.nunique())
            self.assertTrue(before[k].selected_count.eq(k).all())
            self.assertEqual(dispersion[str(k)]['replicates'], 5)
        pool = self.dataset.groupby('signal_date').target_return.mean()
        daily = daily_portfolio(self.dataset, pool)
        np.testing.assert_allclose(daily.excess_vs_pool, 0)

    def test_purge_future_outcomes_do_not_change_asof_models(self):
        cal_start, test_start = self.calendar[50], self.calendar[100]
        train, calibration, test = temporal_partitions(self.dataset, cal_start, test_start)
        poisoned = self.dataset.copy()
        future = poisoned.label_available_date >= test_start
        poisoned.loc[future, 'relative_target'] = 1 - poisoned.loc[future, 'relative_target']
        poisoned.loc[future, 'target'] = 1 - poisoned.loc[future, 'target']
        poisoned_train, poisoned_calibration, _ = temporal_partitions(poisoned, cal_start, test_start)
        pd.testing.assert_frame_equal(train, poisoned_train)
        pd.testing.assert_frame_equal(calibration, poisoned_calibration)
        self.assertLess(train.label_available_date.max(), calibration.signal_date.min())
        a = fit_models(train, calibration, self.calendar[99])
        b = fit_models(poisoned_train, poisoned_calibration, self.calendar[99])
        for name, probability in score_inputs(a, test).items():
            np.testing.assert_array_equal(probability, score_inputs(b, test)[name])
        with self.assertRaises(ValueError):
            fit_models(train, calibration, calibration.label_available_date.min())

    def test_blocks_pair_dates_and_do_not_treat_rows_as_independent(self):
        result = block_interval(np.full(30, .01), samples=100, alpha=.05 / 4)
        self.assertAlmostEqual(result['lower'], .01)
        self.assertAlmostEqual(result['upper'], .01)
        self.assertIsNone(block_interval(np.arange(5.)).get('lower'))
        protocol = {'bootstrap_samples': 100, 'bootstrap_block_sessions': 5, 'bootstrap_seed': 42}
        daily = pd.DataFrame({'mean_return': np.arange(30.)}, index=pd.bdate_range('2020-01-01', periods=30))
        self.assertEqual(paired_returns(daily, daily, protocol)['mean'], 0)
        with self.assertRaises(ValueError):
            paired_returns(daily, daily.iloc[::-1], protocol)

    def test_end_to_end_never_promotes_relative_probability_to_buy_confidence(self):
        parts = []
        for offset in [0, 1000, 2000]:
            part = self.raw.copy()
            part.stock_code = part.stock_code.map(lambda code: str(int(code) + offset).zfill(6))
            parts.append(part)
        raw = pd.concat(parts, ignore_index=True)
        raw.attrs = self.raw.attrs.copy()
        protocol = json.loads((ROOT / 'docs/model_experiments/relative_selection_protocol_20261021.json').read_text())
        protocol.update(labels_as_of=str(self.calendar[-1].date()), calibration_start=str(self.calendar[50].date()),
                        evaluation_start=str(self.calendar[100].date()), evaluation_end=str(self.calendar[-6].date()),
                        minimum_stocks_per_date=4, random_replicates=3, bootstrap_samples=100)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('src.models.relative_price_selection.load_snapshots', return_value=(raw, {})), patch('builtins.print'):
                summary = run_experiment('/unused', root / 'models', protocol, root / 'report.md')
            self.assertFalse(summary['recommendation_gate_passed'])
            self.assertFalse(summary['development_screen_passed'])
            self.assertEqual(summary['coverage']['eligible_dates'], summary['coverage']['included_dates'])
            run = Path(summary['run_dir'])
            ledger = pd.read_csv(run / 'historical_predictions.csv')
            self.assertFalse(ledger.duplicated(['stock_code', 'signal_date']).any())
            self.assertTrue(ledger.recommendation.eq('ABSTAIN').all())
            self.assertNotIn('probability_above_cost', ledger.columns)
            bundle = joblib.load(run / 'research_models.joblib')
            self.assertNotIn('test', bundle['metadata'])
            self.assertEqual(set(bundle['metadata']['fit_partitions']), {'train', 'calibration'})
            self.assertEqual(bundle['metadata']['features'], FEATURES)
            self.assertFalse(bundle['metadata']['recommendation_gate_passed'])
            for k in [10, 20]:
                self.assertEqual(summary['portfolios'][f'relative_top{k}']['selected_cases'], k * summary['coverage']['included_dates'])
            self.assertTrue((root / 'report.md').exists())
            self.assertTrue((root / 'report.json').exists())


if __name__ == '__main__':
    unittest.main()
