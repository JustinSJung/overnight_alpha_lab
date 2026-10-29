from datetime import datetime, timedelta
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
from src.models.distributional_selector import (
    ROOT, complete_cohort, four_partitions, freeze, load_research, outcome_bins,
    policy_selection, query, run_training, select_policy, temperature_probability,
)
from src.models.selected_price_model import COLUMNS, fit_data_digest


def protocol():
    return json.loads((ROOT/'docs/model_experiments/distributional_selector_protocol_20261021.json').read_text())


class DistributionSelectorTests(unittest.TestCase):
    def setUp(self):
        raw = panel()
        parts = []
        for offset in [0, 8, 16]:
            part = raw.copy()
            part['stock_code'] = part.stock_code.map(lambda code: str(int(code)+offset).zfill(6))
            parts.append(part)
        self.raw = pd.concat(parts, ignore_index=True)
        self.raw.attrs = raw.attrs.copy()
        self.days = sorted(self.raw.signal_date.unique())
        self.protocol = protocol()
        self.protocol.update(labels_as_of=str(pd.Timestamp(self.days[-1]).date()), minimum_stocks_per_date=20,
                             probability_calibration_start=str(pd.Timestamp(self.days[80]).date()),
                             policy_calibration_start=str(pd.Timestamp(self.days[100]).date()),
                             evaluation_start=str(pd.Timestamp(self.days[120]).date()),
                             periods={'development_audit': [str(pd.Timestamp(self.days[120]).date()), str(pd.Timestamp(self.days[-6]).date())],
                                      'short_recent_tail': ['2030-01-01', '2030-01-31']})

    def test_exact_boundaries_match_existing_strict_success_definition(self):
        values = np.array([-.05, -.03, -.029, .003, .003001, .03, .031])
        np.testing.assert_array_equal(outcome_bins(values), [0, 0, 1, 1, 2, 2, 3])
        np.testing.assert_array_equal(outcome_bins(values) >= 2, values > .003)
        with self.assertRaises(ValueError):
            outcome_bins([np.nan])

    def test_temperature_calibration_preserves_valid_distribution(self):
        raw = np.array([[.1, .2, .3, .4], [.7, .1, .1, .1]])
        np.testing.assert_allclose(temperature_probability(raw, 1), raw)
        scaled = temperature_probability(raw, 2)
        np.testing.assert_allclose(scaled.sum(axis=1), 1)
        self.assertTrue((scaled.max(axis=1) < raw.max(axis=1)).all())
        with self.assertRaises(ValueError):
            temperature_probability(np.array([[.8, .8, .1, .1]]), 1)

    def test_all_three_fit_boundaries_are_purged_and_external_poison_is_excluded(self):
        dataset, _, _ = complete_cohort(self.raw, self.protocol['labels_as_of'], 20)
        train, cal, policy, test = four_partitions(dataset, self.protocol)
        self.assertLess(train.label_available_date.max(), cal.signal_date.min())
        self.assertLess(cal.label_available_date.max(), policy.signal_date.min())
        self.assertLess(policy.label_available_date.max(), test.signal_date.min())
        poison = dataset.copy()
        external = poison.signal_date.ge(pd.Timestamp(self.protocol['evaluation_start']))
        poison.loc[external, 'target_return'] *= -100
        poison.loc[external, 'target'] = 1 - poison.loc[external, 'target']
        safe = four_partitions(poison, self.protocol)
        for left, right in zip([train, cal, policy], safe[:3]):
            pd.testing.assert_frame_equal(left, right)
        self.assertEqual(fit_data_digest(train, pd.concat([cal, policy]), COLUMNS),
                         fit_data_digest(safe[0], pd.concat(safe[1:3]), COLUMNS))

    def test_missing_one_outcome_excludes_whole_date_not_just_losing_stock(self):
        base, _, _ = complete_cohort(self.raw, self.protocol['labels_as_of'], 20)
        lost_day = pd.Timestamp(self.days[90])
        bad = self.raw[~(self.raw.stock_code.eq('000001') & self.raw.signal_date.eq(lost_day))].copy()
        altered, coverage, _ = complete_cohort(bad, self.protocol['labels_as_of'], 20)
        prior = pd.Timestamp(self.days[85])
        self.assertTrue(base.signal_date.eq(prior).any())
        self.assertFalse(coverage.loc[prior, 'included'])
        self.assertFalse(altered.signal_date.eq(prior).any())

    def candidate_fixture(self):
        days = pd.bdate_range('2024-01-02', periods=32)
        return pd.DataFrame([{'stock_code': str(code).zfill(6), 'signal_date': day, 'positive_floor': .8,
                              'downside_ceiling': .05, 'probability_disagreement': .01, 'utility_score': .02,
                              'target': 1, 'net_return_proxy': .02}
                             for day in days for code in range(8)])

    def test_policy_never_forces_picks_and_cap_ties_are_deterministic(self):
        frame = self.candidate_fixture()
        policy, trials = select_policy(frame, self.protocol)
        self.assertEqual(len(trials), 9)
        self.assertEqual(policy, {'probability_floor': .65, 'downside_ceiling': .1})
        selected = policy_selection(frame, policy, self.protocol)
        self.assertTrue(frame[selected].groupby('signal_date').size().eq(5).all())
        shuffled = frame.sample(frac=1, random_state=42)
        self.assertEqual(set(frame[selected].index), set(shuffled[policy_selection(shuffled, policy, self.protocol)].index))
        failed = frame.assign(target=0, net_return_proxy=-.02)
        no_policy, trials = select_policy(failed, self.protocol)
        self.assertIsNone(no_policy)
        self.assertFalse(any(row['passed'] for row in trials))
        self.assertFalse(policy_selection(frame, None, self.protocol).any())

    def test_full_run_query_and_immutable_forward_records(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('src.models.distributional_selector.load_snapshots', return_value=(self.raw, {})), patch('builtins.print'):
                summary = run_training('/unused', root/'models', self.protocol, root/'report.md')
            bundle = joblib.load(Path(summary['run_dir'])/'model.joblib')
            self.assertFalse(summary['recommendation_gate_passed'])
            self.assertEqual(summary['results']['short_recent_tail']['status'], 'unavailable_no_complete_outcome_dates')
            self.assertEqual(summary['coverage']['by_period']['short_recent_tail']['evaluated_rows'], 0)
            self.assertNotIn('results', bundle['metadata'])
            self.assertNotIn('evaluation', bundle['metadata']['partitions'])
            self.assertEqual(len(bundle['metadata']['dataset_sha256']), 64)
            now = datetime.now(KST)+timedelta(seconds=1)
            with patch('src.models.distributional_selector.load_snapshots', return_value=(self.raw, {})):
                result = query(root/'models', root, '000001', now=now)
            self.assertEqual(result['recommendation'], 'ABSTAIN')
            self.assertEqual(result['status'], 'STALE_DATA')
            self.assertTrue(0 <= result['probability_above_cost'] <= 1)
            self.assertLessEqual(result['positive_floor'], result['probability_above_cost'])
            with self.assertRaises(ValueError):
                load_research(root/'models', pd.Timestamp(self.days[-6]).tz_localize(KST))
            origin = pd.Timestamp(self.days[-6])
            issued = origin.tz_localize(KST)+pd.Timedelta(hours=18)
            bundle['metadata']['trained_at'] = (issued-pd.Timedelta(hours=1)).isoformat()
            with patch('src.models.distributional_selector.load_research', return_value=bundle), \
                    patch('src.models.distributional_selector.load_snapshots', return_value=(self.raw, {})):
                saved = freeze(root/'models', root, root/'ledgers', issued)
                path = Path(saved['ledger'])
                original = path.read_bytes()
                with self.assertRaises(FileExistsError):
                    freeze(root/'models', root, root/'ledgers', issued)
                self.assertEqual(original, path.read_bytes())
                ledger = pd.read_csv(path, dtype={'stock_code': str})
                self.assertTrue(ledger.recommendation.eq('ABSTAIN').all())
                self.assertEqual(saved['frozen_predictions'], 24)
                pending, _ = grade_predictions(ledger, self.raw, origin+pd.offsets.BDay(4))
                graded, _ = grade_predictions(ledger, self.raw, origin+pd.offsets.BDay(5))
                self.assertEqual(pending['resolved'], 0)
                self.assertEqual(graded['resolved'], 24)
                stale_raw = self.raw[self.raw.signal_date.le(origin)].copy()
                with patch('src.models.distributional_selector.load_snapshots', return_value=(stale_raw, {})):
                    skipped = freeze(root/'models', root, root/'other', issued+pd.offsets.BDay(1))
                self.assertEqual(skipped['frozen_predictions'], 0)
                self.assertFalse((root/'other').exists())


if __name__ == '__main__':
    unittest.main()
