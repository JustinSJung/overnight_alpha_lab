from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION, history_features
from src.features.market_context import MARKET_FEATURES, MARKET_FEATURE_VERSION, add_market_context, model_features
from src.features.price_learning_dataset import FEATURES
from src.models.market_context_experiment import ARMS, date_metrics, fit_variant, prepare_dataset
from src.models.price_forecaster import classifiers, date_weights, fit_estimator, forecast_row, load_bundle, load_model_snapshots, refreshed_signal


def panel():
    rng = np.random.default_rng(23)
    dates = pd.bdate_range('2023-01-02', periods=140)
    frames = []
    market = rng.normal(.0003, .012, len(dates))
    for code in range(8):
        close = 100 * np.cumprod(1 + market + rng.normal(.0002, .018, len(dates)))
        frames.append(history_features(pd.DataFrame({
            'stock_code': str(code + 1).zfill(6), 'date': dates, 'close': close,
            'open': close, 'high': close * 1.01, 'low': close * .99,
            'volume': rng.integers(1000, 10000, len(dates)),
        })))
    result = pd.concat(frames, ignore_index=True)
    result.attrs = {'feature_version': HISTORY_FEATURE_VERSION,
                    'history_provenance': {'scope': 'expanded_current_universe_research'}}
    return result


class MarketContextTests(unittest.TestCase):
    def test_features_are_causal_and_ignore_outcome_columns(self):
        raw = panel()
        before = add_market_context(raw, 4)
        boundary = sorted(raw.signal_date.unique())[80]
        changed = raw.copy()
        changed.loc[changed.signal_date > boundary, ['return_1d', 'return_5d', 'return_20d', 'close']] *= 10
        changed['target'] = np.arange(len(changed))
        after = add_market_context(changed, 4)
        columns = ['stock_code', 'signal_date'] + MARKET_FEATURES
        pd.testing.assert_frame_equal(before.loc[before.signal_date <= boundary, columns],
                                      after.loc[after.signal_date <= boundary, columns])
        self.assertTrue(set(MARKET_FEATURES).isdisjoint({'target', 'target_return', 'future_close'}))

    def test_same_day_proxy_uses_only_available_active_quotes(self):
        raw = panel()
        day = raw.signal_date.max()
        bad = (raw.stock_code == '000001') & raw.signal_date.eq(day)
        raw.loc[bad, 'return_1d'] = 10
        raw.loc[bad, 'snapshot_date'] += pd.Timedelta(days=1)
        active = raw[raw.signal_date.eq(day) & ~bad]
        result = add_market_context(raw, 4)
        self.assertAlmostEqual(result.loc[result.signal_date.eq(day), 'market_return_1d'].iloc[0], active.return_1d.mean())
        self.assertAlmostEqual(result.loc[result.signal_date.eq(day), 'market_up_fraction'].iloc[0], active.return_1d.gt(0).mean())

    def test_insufficient_context_is_not_filled_or_invented(self):
        raw = panel()
        result = add_market_context(raw, 9)
        self.assertTrue(result[MARKET_FEATURES].isna().all(axis=None))
        with self.assertRaises(ValueError):
            add_market_context(pd.concat([raw, raw.iloc[:1]]), 4)
        with self.assertRaises(ValueError):
            refreshed_signal('005930', '2026-10-21', MARKET_FEATURE_VERSION)

    def test_date_weights_and_pipeline_scaling_respect_equal_dates(self):
        frame = pd.DataFrame({'signal_date': ['2023-01-01'] * 2 + ['2023-01-02'] * 8})
        weights = date_weights(frame)
        sums = pd.Series(weights).groupby(frame.signal_date).sum()
        self.assertAlmostEqual(sums.iloc[0], sums.iloc[1])
        self.assertAlmostEqual(weights.mean(), 1)
        features = pd.DataFrame({'x': np.arange(10.), 'y': np.arange(10.) ** 2})
        model = fit_estimator(classifiers()['logistic_regression'], features, np.arange(10) % 2, weights)
        np.testing.assert_allclose(model.named_steps['standardscaler'].mean_, np.average(features, axis=0, weights=weights))
        with self.assertRaises(ValueError):
            date_weights(frame.iloc[:0])

    def test_pooled_success_does_not_replace_date_equal_success(self):
        data = pd.DataFrame({'signal_date': ['2023-01-01'] * 9 + ['2023-01-02'],
                             'target': [1] * 9 + [0], 'probability_above_cost': .7,
                             'target_return': [.1] * 9 + [-.1], 'predicted_close_return': .02,
                             'net_return_proxy': [.097] * 9 + [-.103],
                             'selected_by_fixed_policy': True})
        metrics = date_metrics(data, .5)
        self.assertAlmostEqual(data.target.mean(), .9)
        self.assertAlmostEqual(metrics['selected_date_success_rate'], .5)
        self.assertAlmostEqual(metrics['date_brier'], .29)
        self.assertAlmostEqual(metrics['common_date_baseline_brier'], .25)
        self.assertAlmostEqual(metrics['all_dates_mean_net_return_proxy'], -.003)

    def test_no_selection_dates_are_zero_exposure_not_failed_cases(self):
        data = pd.DataFrame({'signal_date': pd.to_datetime(['2023-01-02', '2023-01-03']),
                             'target': [1, 1], 'target_return': [.1, .1], 'net_return_proxy': [.097, .097],
                             'probability_above_cost': [.7, .5], 'predicted_close_return': .02,
                             'selected_by_fixed_policy': [True, False]})
        metrics = date_metrics(data, .5)
        self.assertAlmostEqual(metrics['all_dates_mean_net_return_proxy'], .0485)
        self.assertAlmostEqual(metrics['selected_date_success_rate'], 1)
        self.assertEqual(data.target.tolist(), [1, 1])

    def test_market_model_cannot_use_legacy_snapshot_root(self):
        frame = panel()
        frame.attrs['feature_version'] = 'price_snapshot_v1'
        with patch('src.models.price_forecaster.load_snapshots', return_value=(frame, {})):
            with self.assertRaises(ValueError):
                load_model_snapshots('/unused', {'feature_version': MARKET_FEATURE_VERSION, 'market_context': {'min_stocks': 4}})

    def test_all_four_variants_share_rows_serialize_and_abstain(self):
        raw = panel()
        dates = sorted(raw.signal_date.unique())
        as_of = str(pd.Timestamp(dates[-1]).date())
        calibration_start, test_start = str(pd.Timestamp(dates[85]).date()), str(pd.Timestamp(dates[110]).date())
        with patch('src.models.market_context_experiment.load_snapshots', return_value=(raw, {})):
            dataset, metadata, source, context = prepare_dataset('/unused', as_of, 4)
        expected_rows = None
        current = add_market_context(raw, 4).iloc[-1]
        with tempfile.TemporaryDirectory() as directory:
            for name, market, balanced in ARMS:
                output = Path(directory) / name
                fitted, predictions, _ = fit_variant(dataset, metadata, source, output, as_of,
                                                      calibration_start, test_start, name, market, balanced, context)
                keys = list(zip(predictions.stock_code, predictions.signal_date))
                if expected_rows is None:
                    expected_rows = keys
                self.assertEqual(keys, expected_rows)
                self.assertFalse(fitted['test']['recommendation_gate_passed'])
                self.assertEqual(fitted['date_balanced_training'], balanced)
                bundle = load_bundle(output)
                result = forecast_row(bundle, current, as_of)
                self.assertEqual(result['recommendation'], 'ABSTAIN')
                if market:
                    self.assertEqual(fitted['features'], FEATURES + MARKET_FEATURES)
                    with self.assertRaises(ValueError):
                        forecast_row(bundle, raw.iloc[-1], as_of)
                    values = model_features(pd.DataFrame([current]), fitted['features'])
                    self.assertFalse(values.isna().any(axis=None))


if __name__ == '__main__':
    unittest.main()
