import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.features.foundation_price_features import FOUNDATION_COLUMNS, FoundationWindows, shuffled_foundation
from src.features.next_open_dataset import build_next_open_dataset
from src.models.foundation_price_transfer import ARMS, load_model, predict_heads, train
from src.models.pairwise_price_model import cross_section_inputs
from src.models.selected_price_model import COLUMNS, ROOT, prepare_selected_features


class DummyForecaster:
    def predict_quantiles(self, context, prediction_length, quantile_levels):
        values = np.asarray(context)
        levels = np.asarray(quantile_levels)
        center = values[:, -1, None, None] * (1 + np.arange(1, prediction_length + 1)[None, :, None] * .001)
        quantiles = center * (1 + (levels[None, None, :] - .5) * .02)
        return quantiles, quantiles[:, :, 1]


class FoundationPriceTests(unittest.TestCase):
    def inputs(self):
        frame = prepare_selected_features(panel(), COLUMNS)
        old = sorted(frame.signal_date.unique())
        dates = pd.bdate_range('2025-01-02', periods=len(old))
        mapping = dict(zip(old, dates))
        frame['signal_date'] = frame.signal_date.map(mapping)
        frame['snapshot_date'] = frame.signal_date
        return frame

    def test_shuffled_control_preserves_date_and_availability(self):
        f = pd.DataFrame(dict(stock_code=[str(i).zfill(6) for i in range(12)],
                              signal_date=np.repeat(pd.to_datetime(['2026-01-02', '2026-01-05']), 6),
                              foundation_available=[1, 1, 1, 1, 1, 0] * 2))
        for name in FOUNDATION_COLUMNS:
            f[name] = np.arange(12.) * f.foundation_available
        shuffled = shuffled_foundation(f)
        np.testing.assert_array_equal(shuffled.foundation_available, f.foundation_available)
        for day in f.signal_date.unique():
            before = f[f.signal_date.eq(day)]
            after = shuffled[shuffled.signal_date.eq(day)]
            for name in FOUNDATION_COLUMNS:
                np.testing.assert_array_equal(np.sort(before[name]), np.sort(after[name]))
        self.assertTrue(shuffled.loc[shuffled.foundation_available.eq(0), FOUNDATION_COLUMNS].eq(0).all(axis=None))

    @unittest.skipUnless(importlib.util.find_spec('torch'), 'optional frozen model runtime')
    def test_windows_are_causal_same_stock_and_never_clip_raw_prices_to_eight(self):
        inputs = self.inputs()
        day = sorted(inputs.signal_date.unique())[100]
        cohort, _ = build_next_open_dataset(inputs, inputs.signal_date.max())
        query = cohort[cohort.signal_date.eq(day)]
        before = FoundationWindows(inputs, 8).features(query, DummyForecaster(), 4)
        self.assertEqual(len(before), len(query))
        self.assertTrue(before.foundation_available.eq(1).all())
        self.assertTrue(before.foundation_exit_spread.gt(.01).all())
        altered = inputs.copy()
        altered.loc[altered.signal_date.gt(day), ['open', 'close']] *= 100
        after = FoundationWindows(altered, 8).features(query, DummyForecaster(), 4)
        pd.testing.assert_frame_equal(before, after)
        bad = inputs.copy()
        bad.loc[bad.stock_code.eq('000001') & bad.signal_date.eq(day - pd.offsets.BDay(1)), 'volume'] = 0
        unavailable = FoundationWindows(bad, 8).features(query, DummyForecaster(), 4)
        first = unavailable[unavailable.stock_code.eq('000001')]
        self.assertEqual(first.foundation_available.iloc[0], 0)
        self.assertTrue(first[FOUNDATION_COLUMNS].eq(0).all(axis=None))

    @unittest.skipUnless(importlib.util.find_spec('torch'), 'optional frozen model runtime')
    def test_controlled_supervised_training_full_pool_and_tamper_guard(self):
        inputs = self.inputs()
        days = sorted(inputs.signal_date.unique())
        p = json.loads((ROOT / 'docs/model_experiments/foundation_transfer_protocol_20261026.json').read_text())
        p.update(training_sessions=15, calibration_sessions=3, training_samples_per_date=4,
                 sequence_sessions=8, batch_size=16, labels_as_of=str(pd.Timestamp(days[-1]).date()),
                 fit_as_of=str(pd.Timestamp(days[100]).date()), bootstrap_samples=100,
                 periods={'primary_development': [str(pd.Timestamp(days[110]).date()), str(pd.Timestamp(days[-1]).date())]})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'source').mkdir()
            (root / 'source/history_manifest.json').write_text('{}')
            with patch('src.models.foundation_price_transfer.load_inputs', return_value=(inputs, {})), \
                    patch('src.models.foundation_price_transfer.load_frozen_pipeline', return_value=DummyForecaster()), patch('builtins.print'):
                summary = train(root / 'source', root / 'model', p, root / 'report.md')
            self.assertFalse(summary['recommendation_gate_passed'])
            bundle = load_model(root / 'model')
            cohort, _ = build_next_open_dataset(inputs, days[-1])
            query = cross_section_inputs(cohort[cohort.signal_date.ge(days[110])])
            features = FoundationWindows(inputs, 8).features(query, DummyForecaster(), 16)
            query = query.merge(features, on=['stock_code', 'signal_date'], validate='1:1')
            before = predict_heads(bundle, query)
            self.assertEqual(summary['results']['primary_development']['input_candidates'], len(query))
            altered = query.assign(target=999, target_return=-999)
            after = predict_heads(bundle, altered)
            np.testing.assert_allclose(before[['probability_' + name for name in ARMS]], after[['probability_' + name for name in ARMS]])
            self.assertTrue(before.recommendation.eq('ABSTAIN').all())
            with (Path(summary['run_dir']) / 'model.joblib').open('ab') as handle:
                handle.write(b'tampered')
            with self.assertRaises(ValueError):
                load_model(root / 'model')


if __name__ == '__main__':
    unittest.main()
