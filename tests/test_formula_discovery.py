from datetime import datetime, timedelta
from importlib.util import find_spec
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import joblib
import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.crawler.market_clock import KST
from src.evaluator.forward_price_forecast import grade_predictions
from src.models.distributional_selector import four_partitions
from src.models.formula_discovery import (
    BASE, RANKS, ROOT, choose_policy, discovery_dataset, discovery_sample, fit_fingerprint,
    crossfit_residuals, freeze, load_research, nonlinear_fractions, policy_mask, prefix_and_survival, query, rank_inputs, run_training,
)


def market_panel():
    raw = panel()
    parts = []
    for offset in [0, 8, 16]:
        part = raw.copy()
        part['stock_code'] = part.stock_code.map(lambda code: str(int(code)+offset).zfill(6))
        parts.append(part)
    result = pd.concat(parts, ignore_index=True)
    result.attrs = raw.attrs.copy()
    return result


def fixture_protocol(raw):
    protocol = json.loads((ROOT/'docs/model_experiments/formula_residual_discovery_protocol_20261021.json').read_text())
    days = sorted(raw.signal_date.unique())
    protocol.update(labels_as_of=str(pd.Timestamp(days[-1]).date()), formula_validation_start=str(pd.Timestamp(days[60]).date()),
                    probability_calibration_start=str(pd.Timestamp(days[80]).date()), policy_calibration_start=str(pd.Timestamp(days[100]).date()),
                    evaluation_start=str(pd.Timestamp(days[120]).date()), minimum_stocks_per_date=20,
                    formula_population=16, formula_generations=2, formula_hall_of_fame=6, formula_candidates=4,
                    formula_sample_per_date=12, formula_min_ic_dates_per_block=2, residual_min_train_dates=3,
                    periods={'development_audit': [str(pd.Timestamp(days[120]).date()), str(pd.Timestamp(days[-6]).date())],
                             'short_recent_tail': ['2030-01-01', '2030-01-31']})
    return protocol


class DiscoverySafetyTests(unittest.TestCase):
    def setUp(self):
        self.raw = market_panel()
        self.protocol = fixture_protocol(self.raw)
        self.days = sorted(self.raw.signal_date.unique())

    def test_rank_inputs_are_causal_and_ignore_outcomes(self):
        before = rank_inputs(self.raw, self.days[-1])
        changed = self.raw.copy()
        future = changed.signal_date > self.days[80]
        changed.loc[future, ['open', 'high', 'low', 'close']] *= 2
        changed.loc[future, ['return_1d', 'return_5d', 'return_20d']] += 1
        changed['target_return'] = np.arange(len(changed))
        after = rank_inputs(changed, self.days[-1])
        columns = ['stock_code', 'signal_date'] + BASE
        pd.testing.assert_frame_equal(before.loc[before.signal_date.le(self.days[80]), columns],
                                      after.loc[after.signal_date.le(self.days[80]), columns])
        self.assertTrue((before[RANKS] >= -1).all(axis=None))
        self.assertTrue((before[RANKS] <= 1).all(axis=None))

    def test_prefix_sample_keys_do_not_depend_on_outcomes_or_input_order(self):
        frame = rank_inputs(self.raw, self.days[-1]).assign(target_return=.01)
        before = discovery_sample(frame, 4, 42)
        after = discovery_sample(frame.sample(frac=1, random_state=9).assign(target_return=-999), 4, 42)
        pd.testing.assert_frame_equal(before[['stock_code', 'signal_date']], after[['stock_code', 'signal_date']])
        self.assertTrue(before.groupby('signal_date').size().eq(4).all())
        self.assertGreater(frame.stock_code.nunique(), 4)

    def test_all_selection_stages_exclude_external_outcomes_and_fingerprint_includes_ranks(self):
        dataset, _ = discovery_dataset(self.raw, self.protocol)
        train, cal, policy, test = four_partitions(dataset, self.protocol)
        prefix, survival = prefix_and_survival(train, self.protocol['formula_validation_start'])
        self.assertLess(prefix.label_available_date.max(), survival.signal_date.min())
        self.assertLess(train.label_available_date.max(), cal.signal_date.min())
        self.assertLess(cal.label_available_date.max(), policy.signal_date.min())
        self.assertLess(policy.label_available_date.max(), test.signal_date.min())
        poisoned = dataset.copy()
        external = poisoned.signal_date.ge(pd.Timestamp(self.protocol['evaluation_start']))
        poisoned.loc[external, 'target_return'] = -999
        poisoned.loc[external, 'target'] = 1 - poisoned.loc[external, 'target']
        safe = four_partitions(poisoned, self.protocol)
        self.assertEqual(fit_fingerprint(train, cal, policy), fit_fingerprint(*safe[:3]))
        changed = cal.copy()
        changed.loc[changed.index[0], RANKS[0]] += .1
        self.assertNotEqual(fit_fingerprint(train, cal, policy), fit_fingerprint(train, changed, policy))

    def test_unqualified_policy_is_not_replaced_with_best_looking_failed_trial(self):
        days = pd.bdate_range('2024-01-02', periods=32)
        frame = pd.DataFrame([{'stock_code': str(code).zfill(6), 'signal_date': day, 'formula_augmented': .9,
                               'target': 0, 'net_return_proxy': -.02} for day in days for code in range(8)])
        selected, trials = choose_policy(frame, self.protocol)
        self.assertIsNone(selected)
        self.assertEqual(len(trials), 4)
        self.assertFalse(any(row['passed'] for row in trials))
        self.assertFalse(policy_mask(frame, None, self.protocol).any())
        passing, _ = choose_policy(frame.assign(target=1, net_return_proxy=.02), self.protocol)
        self.assertEqual(passing, .7)
        self.assertTrue(frame[policy_mask(frame, passing, self.protocol)].groupby('signal_date').size().eq(5).all())

    def test_linear_sums_are_not_mislabeled_as_new_nonlinear_information(self):
        rng = np.random.default_rng(42)
        inputs = rng.uniform(-1, 1, (500, 3))
        generated = np.column_stack([inputs[:, 0]+inputs[:, 1], inputs[:, 0]*inputs[:, 1]])
        fractions = nonlinear_fractions(inputs, generated)
        self.assertLess(fractions[0], 1e-10)
        self.assertGreater(fractions[1], .9)

    def test_residual_generation_is_purged_out_of_fold(self):
        dataset, _ = discovery_dataset(self.raw, self.protocol)
        train = four_partitions(dataset, self.protocol)[0]
        prefix, _ = prefix_and_survival(train, self.protocol['formula_validation_start'])
        residuals, reference, folds = crossfit_residuals(prefix, self.protocol)
        self.assertEqual(len(folds), 3)
        self.assertFalse(residuals.duplicated(['stock_code', 'signal_date']).any())
        self.assertTrue(np.isfinite(residuals.gp_target).all())
        for fold in folds:
            self.assertLess(fold['train']['latest_label'], fold['out_of_fold']['start'])
        self.assertTrue(np.isfinite(reference.predict(prefix[BASE])).all())


@unittest.skipUnless(find_spec('gplearn') is not None, 'Run integration in the isolated .venv-discovery runtime.')
class DiscoveryIntegrationTests(unittest.TestCase):
    def test_actual_genetic_training_query_and_forward_ledger_are_research_only(self):
        raw = market_panel()
        protocol = fixture_protocol(raw)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('src.models.formula_discovery.load_snapshots', return_value=(raw, {})), patch('builtins.print'):
                summary = run_training('/unused', root/'models', protocol, root/'report.md')
            run = Path(summary['run_dir'])
            bundle = joblib.load(run/'model.joblib')
            self.assertFalse(summary['recommendation_gate_passed'])
            self.assertNotIn('results', bundle['metadata'])
            self.assertNotIn('evaluation', bundle['metadata']['partitions'])
            self.assertEqual(len(bundle['metadata']['dataset_sha256']), 64)
            self.assertEqual(summary['results']['short_recent_tail']['status'], 'unavailable_no_complete_outcome_dates')
            self.assertLess(bundle['discovery']['prefix']['latest_label'], bundle['discovery']['survival']['start'])
            for row in summary['formula_audit']:
                self.assertIn('rank__', row['expression'])
                self.assertNotIn('target', row['expression'])
            predictions = pd.read_csv(run/'development_audit.csv')
            self.assertTrue(predictions.recommendation.eq('ABSTAIN').all())
            if summary['retained_formulas'] == 0:
                np.testing.assert_allclose(predictions.formula_augmented, predictions.rank_control, atol=1e-12)
            now = datetime.now(KST)+timedelta(seconds=1)
            with patch('src.models.formula_discovery.load_snapshots', return_value=(raw, {})):
                result = query(root/'models', root, '000001', now=now)
            self.assertEqual(result['recommendation'], 'ABSTAIN')
            self.assertEqual(result['status'], 'STALE_DATA')
            self.assertTrue(0 <= result['probability_above_cost'] <= 1)
            origin = pd.Timestamp(sorted(raw.signal_date.unique())[-6])
            issued = origin.tz_localize(KST)+pd.Timedelta(hours=18)
            with self.assertRaises(ValueError):
                load_research(root/'models', issued)
            bundle['metadata']['trained_at'] = (issued-pd.Timedelta(hours=1)).isoformat()
            with patch('src.models.formula_discovery.load_research', return_value=bundle), \
                    patch('src.models.formula_discovery.load_snapshots', return_value=(raw, {})):
                saved = freeze(root/'models', root, root/'ledgers', issued)
                path = Path(saved['ledger'])
                original = path.read_bytes()
                with self.assertRaises(FileExistsError):
                    freeze(root/'models', root, root/'ledgers', issued)
                self.assertEqual(original, path.read_bytes())
                ledger = pd.read_csv(path, dtype={'stock_code': str})
                self.assertTrue(ledger.recommendation.eq('ABSTAIN').all())
                pending, _ = grade_predictions(ledger, raw, origin+pd.offsets.BDay(4))
                resolved, _ = grade_predictions(ledger, raw, origin+pd.offsets.BDay(5))
                self.assertEqual(pending['resolved'], 0)
                self.assertEqual(resolved['resolved'], 24)
                stale = raw[raw.signal_date.le(origin)].copy()
                with patch('src.models.formula_discovery.load_snapshots', return_value=(stale, {})):
                    skipped = freeze(root/'models', root, root/'late', issued+pd.offsets.BDay(1))
                self.assertEqual(skipped['frozen_predictions'], 0)
                self.assertFalse((root/'late').exists())


if __name__ == '__main__':
    unittest.main()
