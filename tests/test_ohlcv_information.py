import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.features.ohlcv_information import OHLCV_FEATURES, add_ohlcv_information
from src.features.price_learning_dataset import build_dataset
from src.models.ohlcv_information_experiment import ROOT, development_screen, run_experiment


class OHLCVInformationTests(unittest.TestCase):
    def test_features_are_causal_and_only_within_stock(self):
        raw = panel()
        before = add_ohlcv_information(raw)
        boundary = sorted(raw.signal_date.unique())[80]
        changed = raw.copy()
        changed.loc[changed.signal_date > boundary, ['open', 'high', 'low', 'close', 'volume']] *= 10
        after = add_ohlcv_information(changed)
        cols = ['stock_code', 'signal_date'] + OHLCV_FEATURES
        pd.testing.assert_frame_equal(before.loc[before.signal_date <= boundary, cols], after.loc[after.signal_date <= boundary, cols])
        changed = raw.copy()
        changed.loc[changed.stock_code == '000001', 'volume'] *= 50
        after = add_ohlcv_information(changed)
        pd.testing.assert_frame_equal(before.loc[before.stock_code != '000001', cols], after.loc[after.stock_code != '000001', cols])
        self.assertTrue(set(OHLCV_FEATURES).isdisjoint({'target', 'target_return', 'future_close'}))

    def test_invalid_candles_are_not_invented_and_inactive_bars_do_not_make_fake_gaps(self):
        raw = panel()
        idx = raw.index[60]
        raw.loc[idx, ['open', 'high', 'low']] = 0
        result = add_ohlcv_information(raw)
        bad = result.stock_code.eq(raw.loc[idx, 'stock_code']) & result.signal_date.eq(raw.loc[idx, 'signal_date'])
        self.assertTrue(result.loc[bad, 'overnight_gap'].isna().all())
        raw.loc[idx, 'volume'] = 0
        result = add_ohlcv_information(raw)
        self.assertTrue(result.loc[bad, 'overnight_gap'].eq(0).all())
        self.assertFalse(np.isinf(result[OHLCV_FEATURES]).any(axis=None))
        with self.assertRaises(ValueError):
            add_ohlcv_information(pd.concat([raw, raw.iloc[:1]]))

    def test_default_feature_warmup_and_target_definition_are_preserved(self):
        raw = panel()
        base, _ = build_dataset(raw)
        added, _ = build_dataset(add_ohlcv_information(raw))
        self.assertFalse(added[OHLCV_FEATURES].isna().any(axis=None))
        pd.testing.assert_series_equal(base.target, added.target)
        pd.testing.assert_series_equal(base.target_return, added.target_return)

    def test_complete_comparison_has_shared_rows_and_no_future_metadata(self):
        raw = panel()
        days = sorted(raw.signal_date.unique())
        protocol = json.loads((ROOT / 'docs/model_experiments/ohlcv_information_protocol_20261021.json').read_text())
        protocol.update(labels_as_of=str(pd.Timestamp(days[-1]).date()), calibration_start=str(pd.Timestamp(days[50]).date()),
                        test_start=str(pd.Timestamp(days[100]).date()),
                        periods={'earlier_development': [str(pd.Timestamp(days[100]).date()), str(pd.Timestamp(days[109]).date())],
                                 'later_chronological_audit': [str(pd.Timestamp(days[110]).date()), str(pd.Timestamp(days[-6]).date())]})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('src.models.ohlcv_information_experiment.load_snapshots', return_value=(raw, {})), patch('builtins.print'):
                summary = run_experiment('/unused', root / 'models', protocol, root / 'report.md')
            self.assertFalse(summary['recommendation_gate_passed'])
            self.assertEqual(summary['cohort_excluded_rows'], 0)
            run = Path(summary['run_dir'])
            metadata = json.loads((run / 'model_metadata.json').read_text())
            self.assertNotIn('test', metadata)
            self.assertNotIn('results', metadata)
            self.assertLess(pd.Timestamp(metadata['partitions']['train']['latest_label']), pd.Timestamp(metadata['partitions']['calibration']['start']))
            self.assertLessEqual(pd.Timestamp(metadata['partitions']['calibration']['latest_label']), pd.Timestamp(metadata['as_of']))
            for period in protocol['periods']:
                a = pd.read_csv(run / ('baseline_' + period + '.csv'))
                b = pd.read_csv(run / ('enriched_' + period + '.csv'))
                pd.testing.assert_frame_equal(a[['stock_code', 'signal_date', 'target']], b[['stock_code', 'signal_date', 'target']])
                self.assertTrue(b.recommendation.eq('ABSTAIN').all())
                self.assertFalse(b.duplicated(['stock_code', 'signal_date']).any())

    def test_screen_rejects_weak_or_sparse_results(self):
        metrics = dict(date_brier=.2, common_date_baseline_brier=.25, mean_daily_cross_section_auc=.56,
                       selected_count=100, selected_dates=20, all_dates_return_lower_95=.001)
        self.assertEqual(development_screen(metrics, {'upper_95': -.001}), [])
        self.assertIn('paired_probability_improvement_not_established', development_screen(metrics, {'upper_95': .001}))
        self.assertIn('insufficient_fixed_policy_cases_or_dates', development_screen(metrics | {'selected_dates': 5}, {'upper_95': -.001}))


if __name__ == '__main__':
    unittest.main()
