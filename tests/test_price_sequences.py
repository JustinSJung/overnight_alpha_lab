import unittest

import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.features.price_sequences import PriceSequences, sample_input_candidates
from src.models.selected_price_model import COLUMNS, prepare_selected_features


class PriceSequenceTests(unittest.TestCase):
    def test_windows_are_same_stock_past_only_and_future_changes_cannot_change_them(self):
        inputs = prepare_selected_features(panel(), COLUMNS)
        store = PriceSequences(inputs, 10)
        day = sorted(inputs.signal_date.unique())[90]
        selected = inputs[inputs.signal_date.eq(day)]
        rows = store.attach(selected)
        before = store.windows(rows.sequence_end, np.zeros(len(COLUMNS)), np.ones(len(COLUMNS)), 1e9)
        changed = inputs.copy()
        changed.loc[changed.signal_date.gt(day), COLUMNS] = 10000
        later = PriceSequences(changed, 10)
        after = later.windows(later.attach(selected).sequence_end, np.zeros(len(COLUMNS)), np.ones(len(COLUMNS)), 1e9)
        np.testing.assert_array_equal(before, after)
        for i, row in enumerate(rows.itertuples()):
            part = store.frame.iloc[row.sequence_end - 9:row.sequence_end + 1]
            self.assertEqual(part.stock_code.nunique(), 1)
            self.assertEqual(part.stock_code.iloc[0], row.stock_code)
            self.assertLessEqual(part.signal_date.max(), day)
            np.testing.assert_allclose(before[i], part[COLUMNS].to_numpy(dtype=np.float32))

    def test_missing_or_nonfinite_history_is_not_filled_or_replaced_by_another_stock(self):
        inputs = prepare_selected_features(panel(), COLUMNS)
        days = sorted(inputs.signal_date.unique())
        missing = inputs.stock_code.eq('000001') & inputs.signal_date.eq(days[85])
        reduced = inputs[~missing]
        store = PriceSequences(reduced, 10)
        rows = store.attach(reduced[reduced.signal_date.eq(days[90])])
        unavailable = rows[rows.stock_code.eq('000001')]
        self.assertFalse(unavailable.sequence_available.any())
        with self.assertRaises(ValueError):
            store.windows(unavailable.sequence_end, np.zeros(len(COLUMNS)), np.ones(len(COLUMNS)))
        inputs.loc[missing, COLUMNS[0]] = np.nan
        store = PriceSequences(inputs, 10)
        rows = store.attach(inputs[inputs.signal_date.eq(days[90])])
        self.assertFalse(rows.loc[rows.stock_code.eq('000001'), 'sequence_available'].any())
        with self.assertRaises(ValueError):
            PriceSequences(pd.concat([inputs, inputs.iloc[:1]]), 10)

    def test_training_sampler_is_input_only_and_not_a_prediction_pool_limit(self):
        inputs = panel()
        sample = sample_input_candidates(inputs, 3, 42)
        changed = inputs.assign(target=np.arange(len(inputs)) % 2, target_return=999.)
        after = sample_input_candidates(changed.sample(frac=1, random_state=1), 3, 42)
        keys = ['stock_code', 'signal_date']
        pd.testing.assert_frame_equal(sample[keys], after[keys])
        self.assertTrue(sample.groupby('signal_date').size().eq(3).all())
        self.assertEqual(inputs.groupby('signal_date').size().min(), 8)


if __name__ == '__main__':
    unittest.main()
