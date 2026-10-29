from datetime import datetime, timezone
import json
from pathlib import Path
import tempfile
import unittest

from src.report_generator.reliability_goal_panel import render_goal_progress
from src.report_generator.extended_model_diagnostics import render_extended_diagnostics


class ReliabilityGoalPanelTests(unittest.TestCase):
    def test_goal_progress_does_not_turn_no_outcomes_into_zero_accuracy_or_approval(self):
        now = datetime(2026, 10, 29, 6, tzinfo=timezone.utc)
        data = dict(schema='public_reliability_goal_v1', recommendation_enabled=False,
                    generated_at=now.isoformat(), price_date='2026-10-28', minimum_cases=300,
                    minimum_dates=60, evaluated_cases=0, selected_signal_dates=0,
                    target_success_rate=.6, target_lower=.6, actual_success_rate=None)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'goal.json'
            path.write_text(json.dumps(data))
            html = render_goal_progress(path, now)
            self.assertIn('적중률 60%', html)
            self.assertIn('0 / 최소 300건', html)
            self.assertIn('미확정', html)
            self.assertIn('추천을 승인하지 않습니다', html)
            data['recommendation_enabled'] = True
            path.write_text(json.dumps(data))
            self.assertEqual(render_goal_progress(path, now), '')

    def test_internal_research_tables_keep_missing_outcomes_and_never_claim_approval(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            folder = root / 'reports/daily_review'
            folder.mkdir(parents=True)
            stats = dict(selected_cases=20, evaluated_cases=0, unresolved_cases=20,
                         conditional_date_success_rate=None)
            mapping = {
                'pairwise_price_research': ('selections', ['top5_' + name for name in [
                    'pointwise_raw', 'pointwise_cross_section', 'pairwise_cross_section']]),
                'foundation_price_transfer': ('top5', ['price_only', 'foundation_shuffled', 'foundation_augmented']),
            }
            for suffix, (key, names) in mapping.items():
                (folder / ('2026-10-26_' + suffix + '.json')).write_text(json.dumps(dict(
                    results={'primary_development': {key: {name: stats for name in names}}})))
            html = render_extended_diagnostics(root)
            self.assertEqual(html.count('<table>'), 2)
            self.assertEqual(html.count('N/A'), 6)
            self.assertIn('RESEARCH ONLY', html)
            self.assertIn('운영 추천으로 승격하지 않았습니다', html)
            self.assertEqual(render_extended_diagnostics(root / 'missing'), '')


if __name__ == '__main__':
    unittest.main()
