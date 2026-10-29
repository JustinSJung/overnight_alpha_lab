import unittest

import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.features.next_open_dataset import build_next_open_dataset
from src.models.selected_price_model import COLUMNS, prepare_selected_features


class NextOpenDatasetTests(unittest.TestCase):
    def prepared(self):
        return prepare_selected_features(panel(), COLUMNS)

    def test_target_uses_next_open_not_signal_close_and_strict_cost(self):
        inputs = self.prepared()
        result, _ = build_next_open_dataset(inputs, inputs.signal_date.max())
        row = result[result.target.notna()].iloc[30]
        stock = inputs[inputs.stock_code.eq(row.stock_code)].sort_values('signal_date')
        position = list(stock.signal_date).index(row.signal_date)
        self.assertEqual(row.entry_date, stock.iloc[position + 1].signal_date)
        self.assertEqual(row.target_date, stock.iloc[position + 5].signal_date)
        self.assertAlmostEqual(row.target_return, stock.iloc[position + 5].close / stock.iloc[position + 1].open - 1)
        self.assertEqual(row.target, float(row.target_return > .003))
        self.assertTrue(result.loc[result.signal_date.eq(inputs.signal_date.max()), 'target'].isna().all())

    def test_missing_session_is_not_a_longer_horizon_or_a_failure(self):
        inputs = self.prepared()
        days = sorted(inputs.signal_date.unique())
        inputs = inputs[~(inputs.stock_code.eq('000001') & inputs.signal_date.eq(days[62]))]
        result, _ = build_next_open_dataset(inputs, days[-1])
        row = result[result.stock_code.eq('000001') & result.signal_date.eq(days[60])].iloc[0]
        self.assertEqual(row.label_status, 'missing_session_prices')
        self.assertTrue(pd.isna(row.target))
        self.assertEqual(row.expected_target_date, days[65])

    def test_unavailable_entry_exit_and_exceptional_moves_remain_in_pool(self):
        inputs = self.prepared()
        days = sorted(inputs.signal_date.unique())
        before, _ = build_next_open_dataset(inputs, days[-1])
        bad = inputs.stock_code.eq('000001') & inputs.signal_date.eq(days[61])
        inputs.loc[bad, 'volume'] = 0
        after, _ = build_next_open_dataset(inputs, days[-1])
        origin = after[after.stock_code.eq('000001') & after.signal_date.eq(days[60])].iloc[0]
        self.assertEqual(origin.label_status, 'entry_price_unavailable')
        self.assertTrue(pd.isna(origin.target))
        keys = ['stock_code', 'signal_date']
        pd.testing.assert_frame_equal(before.loc[before.signal_date.le(days[60]), keys].reset_index(drop=True),
                                      after.loc[after.signal_date.le(days[60]), keys].reset_index(drop=True))
        inputs = self.prepared()
        inputs.loc[bad, ['open', 'high', 'low', 'close']] *= 10
        after, _ = build_next_open_dataset(inputs, days[-1])
        origin = after[after.stock_code.eq('000001') & after.signal_date.eq(days[59])].iloc[0]
        self.assertEqual(origin.label_status, 'price_discontinuity_requires_review')
        self.assertTrue(pd.isna(origin.target))

    def test_features_and_candidate_membership_do_not_depend_on_future(self):
        inputs = self.prepared()
        days = sorted(inputs.signal_date.unique())
        before, _ = build_next_open_dataset(inputs, days[-1])
        inputs.loc[inputs.signal_date.gt(days[80]), ['open', 'close', 'volume']] *= 10
        after, _ = build_next_open_dataset(inputs, days[-1])
        cols = ['stock_code', 'signal_date'] + COLUMNS
        pd.testing.assert_frame_equal(before.loc[before.signal_date.le(days[80]), cols].reset_index(drop=True),
                                      after.loc[after.signal_date.le(days[80]), cols].reset_index(drop=True))
        with self.assertRaises(ValueError):
            build_next_open_dataset(pd.concat([inputs, inputs.iloc[:1]]), days[-1])
        with self.assertRaises(ValueError):
            build_next_open_dataset(inputs, days[-1], horizon=0)


if __name__ == '__main__':
    unittest.main()
