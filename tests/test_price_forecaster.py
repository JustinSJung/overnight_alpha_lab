from __future__ import annotations

import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

import numpy as np
import pandas as pd

from src.features.price_learning_dataset import FEATURES, build_dataset, make_features, temporal_partitions
from src.models.price_forecaster import forecast_row, load_bundle, train_model, resolve_stock


def synthetic_snapshots(days=100, stocks=12):
    rng = np.random.default_rng(12)
    dates = pd.bdate_range('2025-01-01', periods=days)
    rows = []
    for stock in range(stocks):
        close = 100.0
        for date in dates:
            change = rng.normal(0.001, 0.018)
            close *= 1 + change
            rows.append({
                'stock_code': str(stock + 1).zfill(6), 'signal_date': date,
                'snapshot_date': date, 'snapshot_file': 'test', 'close': close,
                'return_1d': change, 'return_5d': change * 2, 'return_20d': change * 3,
                'volume_ratio_20d': 1 + rng.random(), 'volatility_20d': 0.02,
                'breakout_score': int(change > 0), 'ma5': close / (1 + change),
                'ma20': close / (1 + change * 2),
            })
    return pd.DataFrame(rows)


class PriceForecasterTests(unittest.TestCase):
    def test_future_changes_do_not_change_features(self):
        snapshots = synthetic_snapshots(days=50, stocks=1)
        before = make_features(snapshots).iloc[:30]
        changed = snapshots.copy()
        changed.loc[changed.index >= 30, 'close'] *= 3
        pd.testing.assert_frame_equal(before, make_features(changed).iloc[:30])
        dataset, _ = build_dataset(snapshots)
        self.assertEqual(dataset.iloc[0]['target_date'], snapshots.iloc[5]['signal_date'])
        self.assertAlmostEqual(dataset.iloc[0]['target_return'], snapshots.iloc[5]['close'] / snapshots.iloc[0]['close'] - 1)
        self.assertNotIn('future_close', FEATURES)

    def test_late_features_and_unavailable_labels_are_excluded(self):
        snapshots = synthetic_snapshots(days=60, stocks=1)
        snapshots.loc[0, 'snapshot_date'] += pd.Timedelta(days=1)
        dataset, _ = build_dataset(snapshots, as_of=snapshots.iloc[40]['signal_date'])
        self.assertNotIn(snapshots.iloc[0]['signal_date'], dataset['signal_date'].tolist())
        self.assertTrue((dataset['label_available_date'] <= snapshots.iloc[40]['signal_date']).all())

    def test_missing_quote_does_not_stretch_horizon(self):
        snapshots = synthetic_snapshots(days=50, stocks=2)
        missing = (snapshots['stock_code'] == '000001') & (snapshots['signal_date'] == snapshots.iloc[3]['signal_date'])
        dataset, _ = build_dataset(snapshots[~missing])
        earliest = snapshots.iloc[0]['signal_date']
        self.assertFalse(((dataset['stock_code'] == '000001') & (dataset['signal_date'] == earliest)).any())

    def test_label_windows_are_purged_at_both_boundaries(self):
        dataset, _ = build_dataset(synthetic_snapshots())
        train, calibration, test = temporal_partitions(dataset)
        self.assertLess(train['label_available_date'].max(), calibration['signal_date'].min())
        self.assertLess(calibration['label_available_date'].max(), test['signal_date'].min())
        self.assertTrue(set(train['signal_date']).isdisjoint(set(test['signal_date'])))

    def test_fixed_date_boundaries_do_not_move_when_universe_expands(self):
        dataset, _ = build_dataset(synthetic_snapshots())
        days = sorted(dataset['signal_date'].unique())
        calibration_start, test_start = str(pd.Timestamp(days[57]).date()), str(pd.Timestamp(days[76]).date())
        train, calibration, test = temporal_partitions(dataset, calibration_start, test_start)
        self.assertLess(train['label_available_date'].max(), pd.Timestamp(calibration_start))
        self.assertLess(calibration['label_available_date'].max(), pd.Timestamp(test_start))
        self.assertEqual(test['signal_date'].min(), pd.Timestamp(test_start))
        with self.assertRaises(ValueError):
            temporal_partitions(dataset, calibration_start)
        with self.assertRaises(ValueError):
            temporal_partitions(dataset, test_start, calibration_start)

    def test_training_serialization_prediction_and_abstention(self):
        snapshots = synthetic_snapshots()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            processed = root / 'data/processed'
            processed.mkdir(parents=True)
            for day, frame in snapshots.groupby('signal_date'):
                frame.to_csv(processed / ('daily_price_signals_' + day.strftime('%Y%m%d') + '.csv'), index=False)
            metadata, run_dir = train_model(root, root / 'models', str(snapshots['signal_date'].max().date()))
            self.assertTrue((run_dir / 'holdout_predictions.csv').exists())
            self.assertIn(metadata['classifier'], ['logistic_regression', 'hist_gradient_boosting'])
            model = load_bundle(root / 'models')
            model['metadata']['test']['recommendation_gate_passed'] = False
            row = snapshots.iloc[-1]
            result = forecast_row(model, row, row['signal_date'])
            self.assertTrue(0 <= result['probability_above_cost'] <= 1)
            self.assertEqual(result['recommendation'], 'ABSTAIN')
            self.assertEqual(result['status'], 'RESEARCH_ONLY')
            with patch('src.models.price_forecaster.predict_values', return_value=(np.array([0.99]), np.array([0.10]))):
                high_probability = forecast_row(model, row, row['signal_date'])
            self.assertEqual(high_probability['recommendation'], 'ABSTAIN')
            stale = forecast_row(model, row, row['signal_date'] + pd.Timedelta(days=10))
            self.assertEqual(stale['status'], 'STALE_DATA')
            with self.assertRaises(ValueError):
                forecast_row(model, row, row['signal_date'] - pd.Timedelta(days=1))

    def test_name_lookup_does_not_guess_unknown_names(self):
        with tempfile.TemporaryDirectory() as directory:
            raw = Path(directory) / 'data/raw'
            raw.mkdir(parents=True)
            pd.DataFrame([{'stock_code': '005930', 'corp_name': '삼성전자'}]).to_csv(raw / 'stock_market_lookup_20251001.csv', index=False)
            self.assertEqual(resolve_stock('삼성전자', [directory]), '005930')
            self.assertEqual(resolve_stock('005930', [directory]), '005930')
            with self.assertRaises(ValueError):
                resolve_stock('없는종목', [directory])

    def test_expanded_history_never_auto_promotes_from_backtest(self):
        snapshots = synthetic_snapshots()
        snapshots.attrs['history_provenance'] = {'scope': 'expanded_current_universe_research'}
        with tempfile.TemporaryDirectory() as directory:
            with patch('src.models.price_forecaster.load_snapshots', return_value=(snapshots, {})):
                metadata, _ = train_model(directory, Path(directory) / 'models', str(snapshots['signal_date'].max().date()))
        self.assertFalse(metadata['test']['recommendation_gate_passed'])
        self.assertIn('reconstructed_history_requires_forward_validation', metadata['test']['gate_reasons'])


if __name__ == '__main__':
    unittest.main()
