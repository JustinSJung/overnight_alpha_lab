import unittest

import numpy as np
import pandas as pd

from src.features.peer_price_messages import PEER_COLUMNS, add_peer_messages, fit_peer_graph
from src.models.selected_price_model import COLUMNS


def peer_panel():
    rng = np.random.default_rng(719)
    days = pd.bdate_range('2024-01-02', periods=400)
    returns = rng.normal(0, .01, (400, 5))
    returns[1:, 1] = .9 * returns[:-1, 0] + rng.normal(0, .001, 399)
    parts = []
    for i in range(5):
        frame = pd.DataFrame({name: np.zeros(400) for name in COLUMNS})
        frame['return_1d'] = returns[:, i]
        frame['stock_code'] = str(i + 1).zfill(6)
        frame['signal_date'], frame['snapshot_date'] = days, days
        frame['volume'] = 100
        parts.append(frame)
    return pd.concat(parts, ignore_index=True), days


class PeerMessageTests(unittest.TestCase):
    def test_lag_direction_and_future_independence(self):
        inputs, days = peer_panel()
        graph = fit_peer_graph(inputs, days[299], top_k=2, minimum_half_pairs=60, minimum_abs=.2)
        self.assertGreater(graph['weights'][1, 0], 0)
        self.assertTrue(np.diag(graph['weights']).sum() == 0)
        changed = inputs.copy()
        changed.loc[changed.signal_date.gt(days[299]), 'return_1d'] = 1000
        after = fit_peer_graph(changed, days[299], top_k=2, minimum_half_pairs=60, minimum_abs=.2)
        np.testing.assert_array_equal(graph['weights'], after['weights'])
        np.testing.assert_array_equal(graph['shuffled_weights'], after['shuffled_weights'])
        np.testing.assert_array_equal(np.count_nonzero(graph['weights'], axis=1),
                                      np.count_nonzero(graph['shuffled_weights'], axis=1))
        for a, b in zip(graph['weights'], graph['shuffled_weights']):
            np.testing.assert_allclose(np.sort(a[a != 0]), np.sort(b[b != 0]))

    def test_messages_use_only_available_same_date_sources_and_explicit_coverage(self):
        inputs, days = peer_panel()
        weights = np.zeros((5, 5))
        weights[1, 0] = 1
        graph = dict(codes=sorted(inputs.stock_code.unique()), weights=weights, shuffled_weights=weights)
        result = add_peer_messages(inputs, graph)
        source = inputs[inputs.stock_code.eq('000001') & inputs.signal_date.eq(days[100])].iloc[0]
        target = result[result.stock_code.eq('000002') & result.signal_date.eq(days[100])].iloc[0]
        self.assertAlmostEqual(target.peer_return_1d, source.return_1d)
        self.assertEqual(target.peer_coverage, 1)
        changed = inputs.copy()
        changed.loc[changed.signal_date.gt(days[100]), COLUMNS] = 100
        after = add_peer_messages(changed, graph)
        pd.testing.assert_frame_equal(result.loc[result.signal_date.le(days[100]), PEER_COLUMNS].reset_index(drop=True),
                                      after.loc[after.signal_date.le(days[100]), PEER_COLUMNS].reset_index(drop=True))
        changed = inputs.copy()
        mask = changed.stock_code.eq('000001') & changed.signal_date.eq(days[100])
        changed.loc[mask, 'snapshot_date'] += pd.Timedelta(days=1)
        after = add_peer_messages(changed, graph)
        target = after[after.stock_code.eq('000002') & after.signal_date.eq(days[100])].iloc[0]
        self.assertEqual(target.peer_coverage, 0)
        self.assertEqual(target.peer_return_1d, 0)


if __name__ == '__main__':
    unittest.main()
