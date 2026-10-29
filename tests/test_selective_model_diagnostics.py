import json
from pathlib import Path
import tempfile
import unittest

from src.report_generator.selective_model_diagnostics import render_selective_diagnostics


class SelectiveDiagnosticsTests(unittest.TestCase):
    def test_missing_or_invalid_reports_do_not_invent_results(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(render_selective_diagnostics(directory), '')
            report = Path(directory) / 'reports/daily_review/2026-10-23_selective_recommendation.json'
            report.parent.mkdir(parents=True)
            report.write_text('{}')
            self.assertEqual(render_selective_diagnostics(directory), '')

    def test_research_warning_full_counts_and_unknown_rates(self):
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / 'reports/daily_review/2026-10-23_selective_recommendation.json'
            report.parent.mkdir(parents=True)
            m = dict(selected_cases=25, evaluated_cases=0, unresolved_cases=25, conditional_date_success_rate=None)
            report.write_text(json.dumps({'results': {'primary_development': {'input_candidates': 4500,
                'selections': {'top5_' + name: m for name in ['monthly_base', 'probability_only', 'learned_gate']}}}}))
            html = render_selective_diagnostics(directory)
            self.assertIn('id="selective-research"', html)
            self.assertIn('RESEARCH ONLY', html)
            self.assertIn('4500', html)
            self.assertEqual(html.count('N/A'), 3)
            self.assertEqual(html.count('<tr><td>'), 3)


if __name__ == '__main__':
    unittest.main()
