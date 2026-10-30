from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import numpy as np
import pandas as pd

from src.features.next_open_dataset import COLUMNS
from src.pipeline.stock_lookup_release import current_features, fetch_lookup_history, refresh_lookup
from src.report_generator.price_model_panel import render_model_panel
from src.report_generator.stock_lookup_data import build_catalog, load_lookup


def prices(rows=65):
    dates = pd.bdate_range(end='2026-10-29', periods=rows)
    close = 100 + np.arange(rows) * .1
    return pd.DataFrame(dict(date=dates, open=close - .1, high=close + 1, low=close - 1,
                             close=close, volume=1000 + np.arange(rows)))


def primary():
    return dict(schema='public_price_forecast_v1', prediction_target='next_open_to_fifth_close_v1',
                prediction_origin='frozen_original', generated_at=datetime.now(timezone.utc).isoformat(),
                price_date='2026-10-29', learned_labels_through='2026-10-28', model_state='research',
                recommendation_enabled=False, horizon_sessions=5, cost_assumption=.003,
                recommendations=[], watchlist=['005930'], stock_count=1,
                forward=dict(recorded=1, resolved=0, pending=1, unavailable=0, signal_dates=0,
                             integrity_issues=0, scope='learning_system', passed=False),
                stocks=[dict(stock_code='005930', stock_name='삼성전자', aliases=['삼성전자'],
                             probability=.5, predicted_return=None, signal_date='2026-10-29',
                             stale=False, recommended=False)])


class StockLookupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'data/processed').mkdir(parents=True)
        (self.root / 'docs/model_experiments').mkdir(parents=True)
        self.catalog = self.root / 'data/processed/ml_stock_catalog.csv'
        self.catalog.write_text('stock_code,stock_name\n005930,삼성전자\n000660,SK하이닉스\n')
        self.universe = self.root / 'docs/model_experiments/ml_beta_universe.json'
        self.universe.write_text(json.dumps({'stock_codes': ['005930', '000001']}))
        self.primary = self.root / 'docs/price_model.json'
        self.primary.write_text(json.dumps(primary()))
        self.output = self.root / 'docs/stock_lookup.json'
        self.now = datetime.now(timezone.utc)

    def auxiliary(self):
        data = dict(schema='stock_lookup_v1', scope='lookup_only_not_evaluation',
                    generated_at=self.now.isoformat(), price_date='2026-10-29',
                    primary_sha256=hashlib.sha256(self.primary.read_bytes()).hexdigest(),
                    recommendation_enabled=False, states={'000660': 'available'},
                    forecasts=[dict(stock_code='000660', signal_date='2026-10-29', probability=.55,
                                    predicted_return=None, stale=False, recommended=False, lookup_only=True)])
        self.output.write_text(json.dumps(data))
        return data

    def test_missing_regular_prediction_still_has_catalog_identity(self):
        catalog = build_catalog(self.root, primary())
        self.assertEqual({r['stock_code'] for r in catalog}, {'005930', '000660', '000001'})
        self.assertEqual(next(r for r in catalog if r['stock_code'] == '000660')['stock_name'], 'SK하이닉스')
        loaded = load_lookup(self.output, primary(), self.root)
        self.assertEqual(loaded['forecasts'], [])
        self.assertEqual(len(loaded['catalog']), 3)

    def test_auxiliary_forecast_is_separate_and_never_replaces_primary(self):
        self.auxiliary()
        data = primary()
        before = deepcopy(data)
        loaded = load_lookup(self.output, data, self.root)
        self.assertEqual(loaded['forecasts'][0]['stock_code'], '000660')
        self.assertFalse(loaded['forecasts'][0]['recommended'])
        self.assertEqual(data, before)

    def test_stale_mismatched_or_forged_auxiliary_data_is_ignored(self):
        mutations = [lambda d: d.update(primary_sha256='wrong'),
                     lambda d: d.update(generated_at='2000-01-01T00:00:00Z'),
                     lambda d: d.update(price_date='2026-10-28'),
                     lambda d: d.update(recommendation_enabled=True),
                     lambda d: d['forecasts'][0].update(stock_code='005930'),
                     lambda d: d['forecasts'][0].update(probability=True),
                     lambda d: d['forecasts'][0].update(probability=1.1),
                     lambda d: d['forecasts'][0].update(recommended=True),
                     lambda d: d['forecasts'][0].update(lookup_only=False),
                     lambda d: d['forecasts'][0].update(predicted_return=.5)]
        for mutate in mutations:
            data = self.auxiliary()
            mutate(data)
            self.output.write_text(json.dumps(data))
            with self.subTest(mutate=mutate):
                loaded = load_lookup(self.output, primary(), self.root)
                self.assertEqual(loaded['forecasts'], [])
                self.assertEqual(len(loaded['catalog']), 3)

    def test_auxiliary_public_fields_exclude_private_metadata(self):
        data = self.auxiliary()
        data['forecasts'][0]['secret'] = 'DO_NOT_EXPORT'
        self.output.write_text(json.dumps(data))
        lookup = load_lookup(self.output, primary(), self.root)
        html, script = render_model_panel(primary(), lookup)
        self.assertNotIn('DO_NOT_EXPORT', html)
        self.assertIn('SK하이닉스', html)
        self.assertIn('lookup_only', html)
        self.assertIn('!row.lookup_only', script)
        self.assertNotIn('innerHTML', script)

    def test_features_match_existing_19_schema_and_use_completed_prices(self):
        frame, state = current_features(prices(), '000660', '2026-10-29')
        self.assertEqual(state, 'available')
        self.assertEqual(len(frame), 1)
        self.assertTrue(np.isfinite(frame[COLUMNS]).all(axis=None))
        self.assertTrue(frame.stock_code.eq('000660').all())
        for mutate in [lambda p: pd.concat([p, p.tail(1)]),
                       lambda p: p.assign(close=-1),
                       lambda p: p.assign(volume=np.nan),
                       lambda p: p.assign(high=p.low - 1)]:
            with self.assertRaises(ValueError): current_features(mutate(prices()), '000660', '2026-10-29')

    def test_unavailable_states_do_not_invent_probabilities(self):
        self.assertEqual(current_features(prices(10), '000660', '2026-10-29'), (None, 'insufficient_history'))
        self.assertEqual(current_features(prices().iloc[:-1], '000660', '2026-10-29'), (None, 'not_current'))
        self.assertEqual(current_features(prices().assign(volume=0), '000660', '2026-10-29'), (None, 'inactive'))

    @patch('src.pipeline.stock_lookup_release.load_model')
    @patch('src.pipeline.stock_lookup_release.fetch_lookup_history', return_value=prices())
    @patch('src.pipeline.stock_lookup_release.predict_probability', return_value=np.array([.55]))
    def test_refresh_never_retrains_or_changes_regular_pool_or_originals(self, predict, fetch, model):
        model.return_value = {'metadata': {'trained_at': '2026-10-28T00:00:00Z', 'as_of': '2026-10-28'}}
        original = self.primary.read_bytes(), self.universe.read_bytes()
        result = refresh_lookup(self.primary, self.root / 'model', self.root / 'cache', self.output,
                                self.root, client=Mock(), now=self.now)
        self.assertEqual(result['extra_requested'], 1)
        self.assertEqual(result['extra_forecasts'], 1)
        self.assertEqual(fetch.call_args.args[1], '000660')
        self.assertEqual(original, (self.primary.read_bytes(), self.universe.read_bytes()))
        self.assertEqual(len(load_lookup(self.output, primary(), self.root)['forecasts']), 1)

    @patch('src.pipeline.stock_lookup_release.load_model')
    @patch('src.pipeline.stock_lookup_release.predict_probability', return_value=np.array([.55]))
    def test_one_stock_failure_does_not_stop_other_lookup_forecasts(self, predict, model):
        self.catalog.write_text(self.catalog.read_text() + '001111,Test Failure\n')
        model.return_value = {'metadata': {'trained_at': '2026-10-28T00:00:00Z', 'as_of': '2026-10-28'}}
        def fetch(client, code, *args):
            if code == '001111': raise RuntimeError('Private provider payload is not published')
            return prices()
        with patch('src.pipeline.stock_lookup_release.fetch_lookup_history', side_effect=fetch):
            result = refresh_lookup(self.primary, self.root / 'model', self.root / 'cache', self.output,
                                    self.root, client=Mock(), now=self.now)
        self.assertEqual(result['extra_forecasts'], 1)
        self.assertNotIn('Private provider payload', self.output.read_text())
        self.assertEqual(json.loads(self.output.read_text())['states']['001111'], 'price_unavailable')

    def test_quote_cache_is_checksum_checked_before_reuse(self):
        client = Mock()
        p = prices()
        client.get_daily_ohlcv.side_effect = lambda code, start, end: p[p.date.between(pd.Timestamp(start), pd.Timestamp(end))]
        first = fetch_lookup_history(client, '000660', self.root / 'cache', '2026-05-02', '2026-10-29')
        calls = client.get_daily_ohlcv.call_count
        second = fetch_lookup_history(client, '000660', self.root / 'cache', '2026-05-02', '2026-10-29')
        self.assertEqual(len(first), len(second))
        self.assertEqual(client.get_daily_ohlcv.call_count, calls)
        path = self.root / 'cache/snapshot_20261029/000660.csv'
        path.write_text('changed')
        fetch_lookup_history(client, '000660', self.root / 'cache', '2026-05-02', '2026-10-29')
        self.assertGreater(client.get_daily_ohlcv.call_count, calls)


if __name__ == '__main__':
    unittest.main()
