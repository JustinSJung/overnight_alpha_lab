import json
from pathlib import Path
import tempfile
import unittest

from src.report_generator.nature_model_diagnostics import render_nature_diagnostics


class NatureDiagnosticsTests(unittest.TestCase):
    def test_missing_or_bad_reports_do_not_create_zero_metrics(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(render_nature_diagnostics(root), '')
            reports = root / 'reports/daily_review'
            reports.mkdir(parents=True)
            (reports / '2026-10-22_neural_circuit_research.json').write_text('{}')
            self.assertEqual(render_nature_diagnostics(root), '')

    def test_internal_table_is_labeled_research_and_escapes_names(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            reports = root / 'reports/daily_review'
            reports.mkdir(parents=True)
            value = {'results': {'primary_development': {'<script>alert(1)</script>': {
                'input_candidates': 100, 'evaluated_cases': 90, 'mean_daily_auc': .53, 'date_brier': .247,
                'top20': {'conditional_date_success_rate': .44}}}}}
            (reports / '2026-10-22_neural_circuit_research.json').write_text(json.dumps(value))
            html = render_nature_diagnostics(root)
            self.assertIn('RESEARCH ONLY', html)
            self.assertIn('44.00%', html)
            self.assertNotIn('<script>alert', html)
            self.assertIn('&lt;script&gt;', html)


if __name__ == '__main__':
    unittest.main()
