import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd

from src.crawler.market_clock import KST
from src.evaluator.reliability_goal import certify_goal
from src.features.next_open_dataset import TARGET_VERSION
from src.models.selected_price_model import ROOT


class ReliabilityGoalTests(unittest.TestCase):
    def fixture(self, dates=150):
        calendar = pd.bdate_range('2026-10-26', periods=180)
        rows = []
        for day in calendar[:dates]:
            for stock in range(5):
                rows.append(dict(stock_code=str(stock).zfill(6), signal_date=day,
                                 prediction_id=str(len(rows)), selected=True, target=1., net_return_proxy=.02,
                                 target_version=TARGET_VERSION, horizon_sessions=5, cost_assumption=.003,
                                 recorded_at=(day.tz_localize(KST) + pd.Timedelta(hours=17)).isoformat(),
                                 model_trained_at=(day.tz_localize(KST) - pd.Timedelta(hours=1)).isoformat()))
        frame = pd.DataFrame(rows)
        benchmark = pd.DataFrame(dict(signal_date=calendar[:dates], entry_date=calendar[1:dates+1],
                                      exit_date=calendar[5:dates+5], net_return=.005, source='equal_weight_069500_229200'))
        now = calendar[-1].tz_localize(KST) + pd.Timedelta(hours=17)
        return frame, calendar, now, benchmark

    def goal(self):
        return json.loads((ROOT / 'docs/model_experiments/reliability_goal_20261026.json').read_text())

    def evaluate(self, frame, calendar, now, benchmark=None, role='hash_verified_timely_originals'):
        return certify_goal(frame, calendar, 'selected', self.goal(), now, role, 'next_open_current_v1', benchmark)

    def test_perfect_small_history_is_not_a_certified_high_confidence_model(self):
        frame, calendar, now, benchmark = self.fixture(60)
        result = self.evaluate(frame, calendar, now, benchmark)
        self.assertFalse(result['goal_passed'])
        self.assertLess(result['success_lower'], .6)
        self.assertLess(result['success_lower'], result['pooled_success_rate'])

    def test_sufficient_perfect_synthetic_evidence_passes_all_prespecified_checks(self):
        frame, calendar, now, benchmark = self.fixture()
        result = self.evaluate(frame, calendar, now, benchmark)
        self.assertTrue(result['goal_passed'])
        self.assertEqual(result['certification_look'], 600)
        self.assertEqual(result['selected_cases'], 600)
        self.assertGreaterEqual(result['success_lower'], .6)
        self.assertLess(result['success_lower'], 1)
        self.assertGreater(result['benchmark_excess_lower'], 0)

    def test_retrospective_unknown_policy_duplicates_and_bad_timing_are_rejected(self):
        frame, calendar, now, _ = self.fixture()
        with self.assertRaises(ValueError):
            self.evaluate(frame, calendar, now, role='historical_development')
        with self.assertRaises(ValueError):
            certify_goal(frame, calendar, 'selected', self.goal(), now, 'hash_verified_timely_originals', 'new_posthoc_winner')
        with self.assertRaises(ValueError):
            self.evaluate(pd.concat([frame, frame.iloc[:1]]), calendar, now)
        frame.loc[0, 'recorded_at'] = (pd.Timestamp(frame.loc[0, 'recorded_at']) + pd.Timedelta(days=3)).isoformat()
        with self.assertRaises(ValueError):
            self.evaluate(frame, calendar, now)

    def test_missing_mature_answers_and_wrong_benchmark_never_pass(self):
        frame, calendar, now, benchmark = self.fixture()
        frame.loc[0, ['target', 'net_return_proxy']] = np.nan
        result = self.evaluate(frame, calendar, now, benchmark)
        self.assertFalse(result['goal_passed'])
        self.assertIsNone(result['success_lower'])
        self.assertIn('mature_selected_outcomes_missing', result['reasons'])
        frame.loc[0, ['target', 'net_return_proxy']] = [1, .02]
        benchmark.loc[0, 'entry_date'] += pd.Timedelta(days=1)
        result = self.evaluate(frame, calendar, now, benchmark)
        self.assertFalse(result['goal_passed'])
        self.assertIsNone(result['benchmark_excess_lower'])

    def test_only_scheduled_mature_dates_count_not_whichever_answers_arrive(self):
        frame, calendar, now, _ = self.fixture(60)
        now = calendar[4].tz_localize(KST) + pd.Timedelta(hours=17)
        frame = frame[frame.signal_date.le(calendar[4])]
        result = self.evaluate(frame, calendar, now)
        self.assertEqual(result['evaluated_cases'], 0)
        self.assertEqual(result['reasons'], ['no_scheduled_mature_originals'])

    def test_no_repeated_statistical_looks_between_fixed_thresholds_and_health_can_veto(self):
        frame, calendar, now, benchmark = self.fixture()
        first = self.evaluate(frame, calendar, now, benchmark)
        frame.loc[frame.signal_date.gt(calendar[119]), 'target'] = 0
        second = self.evaluate(frame, calendar, now, benchmark)
        self.assertEqual(first['success_lower'], second['success_lower'])
        self.assertFalse(second['goal_passed'])
        self.assertIn('recent_health_not_adequate', second['reasons'])

    def test_no_recommendations_is_not_a_perfect_success_rate(self):
        frame, calendar, now, benchmark = self.fixture()
        frame['selected'] = False
        result = self.evaluate(frame, calendar, now, benchmark)
        self.assertFalse(result['goal_passed'])
        self.assertIsNone(result['pooled_success_rate'])
        self.assertEqual(result['issue_date_coverage'], 0)

    def test_missing_issue_days_count_in_coverage_and_calendar_blocks(self):
        frame, calendar, now, benchmark = self.fixture(150)
        sparse = frame[frame.signal_date.isin(calendar[:150:3])]
        result = self.evaluate(sparse, calendar, now, benchmark)
        self.assertEqual(result['selected_signal_dates'], 50)
        self.assertEqual(result['recorded_mature_issue_dates'], 50)
        self.assertEqual(result['mature_issue_dates'], 175)
        self.assertAlmostEqual(result['issue_date_coverage'], 50 / 175)
        self.assertIn('recommendation_frequency_too_low', result['reasons'])
        self.assertFalse(result['goal_passed'])

    def test_mixed_date_formats_cannot_bypass_duplicate_detection(self):
        frame, calendar, now, benchmark = self.fixture(60)
        frame['signal_date'] = frame.signal_date.astype(str)
        duplicate = frame.iloc[:1].assign(signal_date='2026-10-26 00:00:00', prediction_id='new-id')
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            self.evaluate(pd.concat([frame, duplicate]), calendar, now, benchmark)


if __name__ == '__main__':
    unittest.main()
