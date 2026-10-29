from datetime import datetime, timedelta
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.crawler.market_clock import KST
from src.evaluator.forward_price_forecast import grade_predictions
from src.features.price_learning_dataset import build_dataset
from src.models.adaptive_memory import (
    EXPERTS, METHODS, ROOT, case_predictions, choose_policy, complete_predictions, delayed_updates,
    fit_base, freeze, input_sample, load_snapshot, policy_mask, query, replay, router_weights, run_training,
)
from src.models.distributional_selector import four_partitions
from src.models.selected_price_model import COLUMNS, prepare_selected_features


def setup_market():
    raw = panel()
    parts = []
    for offset in [0, 8, 16]:
        frame = raw.copy()
        frame['stock_code'] = frame.stock_code.map(lambda code: str(int(code)+offset).zfill(6))
        parts.append(frame)
    combined = pd.concat(parts, ignore_index=True)
    combined.attrs = raw.attrs.copy()
    return combined


class AdaptiveMemoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = setup_market()
        cls.days = sorted(cls.raw.signal_date.unique())
        cls.protocol = json.loads((ROOT/'docs/model_experiments/adaptive_memory_protocol_20261021.json').read_text())
        cls.protocol.update(labels_as_of=str(pd.Timestamp(cls.days[-1]).date()),
                            probability_calibration_start=str(pd.Timestamp(cls.days[80]).date()),
                            policy_calibration_start=str(pd.Timestamp(cls.days[100]).date()),
                            evaluation_start=str(pd.Timestamp(cls.days[120]).date()), memory_sample_per_date=4,
                            memory_dates=40, memory_neighbors=32, prior_dates=20, min_neighbor_dates=3,
                            max_neighbor_rms_distance=5,
                            periods={'development_audit': [str(pd.Timestamp(cls.days[120]).date()), str(pd.Timestamp(cls.days[-6]).date())],
                                     'short_recent_tail': ['2030-01-01', '2030-01-31']})
        full = prepare_selected_features(cls.raw, COLUMNS)
        cls.inputs = full[np.isfinite(full[COLUMNS]).all(axis=1) & full.volume_ratio_20d.gt(0)].copy()
        cls.labels, _ = build_dataset(full)
        cls.labels = cls.labels[np.isfinite(cls.labels[COLUMNS]).all(axis=1)].copy()
        train, cal, _, _ = four_partitions(cls.labels, cls.protocol)
        cls.base = fit_base(train, cal)

    def test_future_answers_cannot_change_earlier_memory_predictions_or_router_weights(self):
        with patch('builtins.print'):
            original, updates, audits, _ = replay(self.base, self.inputs, self.labels, self.protocol)
            changed = self.labels.copy()
            cutoff = pd.Timestamp(self.days[120])
            future = changed.label_available_date.ge(cutoff)
            changed.loc[future, 'target'] = 1-changed.loc[future, 'target']
            changed.loc[future, 'target_return'] *= -100
            poisoned, _, _, _ = replay(self.base, self.inputs, changed, self.protocol)
        columns = METHODS + ['weight_' + name for name in EXPERTS]
        np.testing.assert_allclose(original.loc[original.signal_date.le(cutoff), columns],
                                   poisoned.loc[poisoned.signal_date.le(cutoff), columns], atol=1e-12, rtol=0)
        later = original.signal_date.gt(cutoff)
        self.assertGreater(float(np.max(np.abs(original.loc[later, 'adaptive']-poisoned.loc[later, 'adaptive']))), 1e-5)
        self.assertTrue(updates)
        self.assertTrue(all(row['latest_label'] < row['update_as_of'] for row in updates))
        self.assertTrue(all(row['memory_latest_label'] is None or row['memory_latest_label'] < row['signal_date'] for row in audits))
        self.assertTrue(original.groupby('signal_date').size().eq(24).all())

    def test_router_uses_only_complete_frozen_batches_once_after_maturity(self):
        issue = pd.Timestamp('2024-01-02')
        batch = pd.DataFrame({'stock_code': ['000001', '000002'], 'signal_date': issue,
                              'fixed_base': [.9, .9], 'case_memory': [.2, .2], 'recent_prior': [.4, .4]})
        lookup = pd.DataFrame({'stock_code': ['000001', '000002'], 'signal_date': issue, 'target': [0, 0],
                              'label_available_date': pd.Timestamp('2024-01-09')}).set_index(['stock_code', 'signal_date'])
        weights = np.zeros(3)
        pending, untouched, audit = delayed_updates([batch], lookup, pd.Timestamp('2024-01-09'), weights.copy(), self.protocol)
        self.assertEqual(len(pending), 1)
        self.assertFalse(audit)
        np.testing.assert_array_equal(untouched, weights)
        pending, after, audit = delayed_updates([batch], lookup, pd.Timestamp('2024-01-10'), weights.copy(), self.protocol)
        self.assertFalse(pending)
        self.assertEqual(len(audit), 1)
        self.assertGreater(router_weights(after, .05)[1], router_weights(after, .05)[0])
        _, again, audit = delayed_updates(pending, lookup, pd.Timestamp('2024-01-11'), after.copy(), self.protocol)
        self.assertFalse(audit)
        np.testing.assert_array_equal(again, after)
        missing = lookup.iloc[:1]
        pending, unchanged, audit = delayed_updates([batch], missing, pd.Timestamp('2024-02-01'), weights.copy(), self.protocol)
        self.assertEqual(len(pending), 1)
        self.assertFalse(audit)
        np.testing.assert_array_equal(unchanged, weights)

    def test_many_correlated_same_date_cases_are_not_many_support_dates(self):
        day = pd.Timestamp(self.days[100])
        memory = self.inputs[self.inputs.signal_date.eq(self.days[90])].copy()
        memory['target'] = 1
        memory['label_available_date'] = pd.Timestamp(self.days[95])
        groups = pd.DataFrame({'signal_date': [self.days[90]], 'label_available_date': [self.days[95]], 'total': [4], 'count': [10]})
        predictions, latest = case_predictions(self.base, self.inputs[self.inputs.signal_date.eq(day)], memory, groups, day, self.protocol)
        self.assertTrue(predictions.neighbor_dates.eq(1).all())
        self.assertFalse(predictions.case_supported.any())
        np.testing.assert_allclose(predictions.case_memory, .4)
        self.assertLess(latest, day)

    def test_memory_sample_uses_input_keys_not_outcome_values_or_file_order(self):
        a = input_sample(self.inputs, 4, 42)
        b = input_sample(self.inputs.sample(frac=1, random_state=2).assign(target=-999), 4, 42)
        pd.testing.assert_frame_equal(a[['stock_code', 'signal_date']], b[['stock_code', 'signal_date']])
        self.assertTrue(a.groupby('signal_date').size().eq(4).all())

    def test_incomplete_outcomes_are_reported_without_reranking_remaining_stocks(self):
        predictions = self.inputs[['stock_code', 'signal_date']]
        day = pd.Timestamp(self.days[110])
        labels = self.labels[~(self.labels.signal_date.eq(day) & self.labels.stock_code.eq('000001'))]
        evaluated, coverage = complete_predictions(predictions, labels)
        self.assertEqual(coverage.loc[day, 'issued'], 24)
        self.assertEqual(coverage.loc[day, 'resolved'], 23)
        self.assertFalse(coverage.loc[day, 'complete'])
        self.assertFalse(evaluated.signal_date.eq(day).any())

    def test_policy_rejects_insufficient_evidence_conflict_or_unsupported_cases(self):
        days = pd.bdate_range('2024-01-02', periods=32)
        frame = pd.DataFrame([{'stock_code': str(code).zfill(6), 'signal_date': day, 'adaptive': .8,
                               'fixed_base': .8, 'case_memory': .8, 'case_supported': True,
                               'target': 1, 'net_return_proxy': .02} for day in days for code in range(8)])
        policy, _ = choose_policy(frame, self.protocol)
        self.assertEqual(policy, .7)
        self.assertTrue(frame[policy_mask(frame, policy, self.protocol)].groupby('signal_date').size().eq(5).all())
        self.assertFalse(policy_mask(frame.assign(case_supported=False), .7, self.protocol).any())
        self.assertFalse(policy_mask(frame.assign(case_memory=.2), .7, self.protocol).any())
        policy, trials = choose_policy(frame.assign(target=0, net_return_proxy=-.02), self.protocol)
        self.assertIsNone(policy)
        self.assertFalse(any(row['passed'] for row in trials))

    def test_full_training_snapshot_query_and_forward_grading_remain_research_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('src.models.adaptive_memory.load_snapshots', return_value=(self.raw, {})), patch('builtins.print'):
                summary = run_training('/unused', root/'models', self.protocol, root/'report.md')
            self.assertFalse(summary['recommendation_gate_passed'])
            self.assertEqual(summary['results']['short_recent_tail']['status'], 'unavailable_no_complete_outcome_dates')
            now = datetime.now(KST)+timedelta(seconds=1)
            metadata, predictions = load_snapshot(root/'models', now)
            self.assertLess(metadata['latest_known_label_date'], metadata['signal_date'])
            result = query(root/'models', '000001', now)
            self.assertEqual(result['recommendation'], 'ABSTAIN')
            self.assertEqual(result['status'], 'STALE_DATA')
            run = Path(summary['run_dir'])
            all_predictions = pd.read_csv(run/'prequential_predictions.csv', dtype={'stock_code': str}, parse_dates=['signal_date'])
            origin = pd.Timestamp(self.days[-6])
            batch = all_predictions[all_predictions.signal_date.eq(origin)].copy()
            issued = origin.tz_localize(KST)+pd.Timedelta(hours=18)
            with self.assertRaises(ValueError):
                load_snapshot(root/'models', issued)
            meta = dict(metadata, trained_at=(issued-pd.Timedelta(hours=1)).isoformat(), signal_date=origin.date().isoformat())
            with patch('src.models.adaptive_memory.load_snapshot', return_value=(meta, batch)):
                result = freeze(root/'models', root/'ledgers', issued)
                path = Path(result['ledger'])
                original = path.read_bytes()
                with self.assertRaises(FileExistsError):
                    freeze(root/'models', root/'ledgers', issued)
                self.assertEqual(original, path.read_bytes())
                ledger = pd.read_csv(path, dtype={'stock_code': str})
                self.assertTrue(ledger.recommendation.eq('ABSTAIN').all())
                pending, _ = grade_predictions(ledger, self.raw, origin+pd.offsets.BDay(4))
                resolved, _ = grade_predictions(ledger, self.raw, origin+pd.offsets.BDay(5))
                self.assertEqual(pending['resolved'], 0)
                self.assertEqual(resolved['resolved'], 24)
                skipped = freeze(root/'models', root/'late', issued+pd.offsets.BDay(1))
                self.assertEqual(skipped['frozen_predictions'], 0)
            snapshot = run/'latest_predictions.csv'
            snapshot.write_text(snapshot.read_text()+'\n', encoding='utf-8')
            with self.assertRaises(ValueError):
                load_snapshot(root/'models', now)


if __name__ == '__main__':
    unittest.main()
