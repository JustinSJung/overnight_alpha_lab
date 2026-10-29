from copy import deepcopy
from datetime import datetime
import json
from pathlib import Path
import tempfile
import subprocess
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from src.crawler.market_clock import KST
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION, history_features
from src.features.price_learning_dataset import FEATURES
from src.report_generator.price_model_panel import load_public_forecast, model_status, render_model_panel
from src.report_generator.supervised_forecast_report import build_payload, forward_evidence, write_payload
from src.report_generator.supervised_forecast_report import ROOT
from test_completed_price_history import prices
from test_forward_price_forecast import bundle


class PublicPriceForecastTests(unittest.TestCase):
    def setUp(self):
        self.model = bundle()
        self.model['metadata'].update(feature_version=HISTORY_FEATURE_VERSION, features=FEATURES)
        self.raw = history_features(prices())
        self.raw.attrs['feature_version'] = HISTORY_FEATURE_VERSION
        self.now = datetime(2026, 10, 21, 8, tzinfo=KST)

    def payload(self, ledger_dir, model=None, snapshots=None):
        with patch('src.models.price_forecaster.predict_values', return_value=(np.array([.99]), np.array([.1]))), patch(
                'src.report_generator.supervised_forecast_report.stock_catalog', return_value={'삼성전자': {'005930'}}):
            return build_payload(model or self.model, snapshots if snapshots is not None else self.raw,
                                 [], ledger_dir, now=self.now)

    def test_high_probability_is_not_a_recommendation_without_forward_validation(self):
        model = deepcopy(self.model)
        model['metadata']['test']['recommendation_gate_passed'] = True
        with tempfile.TemporaryDirectory() as directory:
            payload = self.payload(directory, model)
        self.assertEqual(payload['stocks'][0]['probability'], .99)
        self.assertFalse(payload['recommendation_enabled'])
        self.assertEqual(payload['recommendations'], [])
        self.assertEqual(payload['watchlist'], ['005930'])
        self.assertEqual(payload['forward']['resolved'], 0)
        self.assertEqual(payload['stocks'][0]['stock_name'], '삼성전자')

    def test_future_rows_and_different_price_schema_are_rejected(self):
        raw = self.raw.copy()
        raw.loc[raw.index[-1], 'signal_date'] = pd.Timestamp('2026-10-21')
        raw.loc[raw.index[-1], 'snapshot_date'] = pd.Timestamp('2026-10-21')
        with tempfile.TemporaryDirectory() as directory:
            payload = self.payload(directory, snapshots=raw)
            self.assertEqual(payload['price_date'], '2026-10-19')
            wrong = deepcopy(self.model)
            wrong['metadata']['feature_version'] = 'price_snapshot_v1'
            with self.assertRaises(ValueError):
                self.payload(directory, wrong)
            future = deepcopy(self.model)
            future['metadata']['trained_at'] = '2026-10-22T00:00:00+00:00'
            with self.assertRaises(ValueError):
                self.payload(directory, future)

    def test_only_current_model_original_ledgers_count_and_duplicates_block_readiness(self):
        base = {'model_dataset_sha256': self.model['metadata']['dataset_sha256'],
                'model_trained_at': self.model['metadata']['trained_at'],
                'recorded_at': '2026-10-21T08:00:00+09:00', 'prediction_id': 'first',
                'signal_date': '2026-10-20', 'stock_code': '005930', 'horizon_sessions': 5,
                'cost_assumption': .003, 'probability_above_cost': .7, 'predicted_close_return': .01,
                'validation_base_rate': .45, 'origin_close': 139}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pd.DataFrame([base]).to_csv(root / 'ml_price_forecasts_forward_20261021.csv', index=False)
            pd.DataFrame([base]).to_csv(root / 'ml_price_forecasts_forward_eval_20261021.csv', index=False)
            other = dict(base, model_dataset_sha256='other', prediction_id='other')
            pd.DataFrame([other]).to_csv(root / 'ml_price_forecasts_forward_20261022.csv', index=False)
            report = forward_evidence(self.model['metadata'], self.raw, root, '2026-10-21', self.now)
            self.assertEqual(report['recorded'], 1)
            self.assertEqual(report['pending'], 1)
            self.assertEqual(report['integrity_issues'], 0)
            self.assertFalse(report['passed'])
            pd.DataFrame([base]).to_csv(root / 'ml_price_forecasts_forward_20261023.csv', index=False)
            duplicate = forward_evidence(self.model['metadata'], self.raw, root, '2026-10-21', self.now)
            self.assertEqual(duplicate['integrity_issues'], 2)
            self.assertFalse(duplicate['passed'])

    def test_public_export_is_atomic_and_contains_no_private_metadata(self):
        self.model['metadata']['private_secret'] = 'DO_NOT_EXPORT'
        with tempfile.TemporaryDirectory() as directory:
            payload = self.payload(directory)
            target = Path(directory) / 'public.json'
            write_payload(payload, target)
            text = target.read_text()
            self.assertNotIn('DO_NOT_EXPORT', text)
            self.assertNotIn('dataset_sha256', text)
            self.assertNotIn('gate_reasons', text)
            self.assertEqual(json.loads(text)['schema'], 'public_price_forecast_v1')
            self.assertEqual(list(Path(directory).iterdir()), [target])

    def test_failed_serialization_preserves_previous_output_and_cleans_temporary_file(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'public.json'
            write_payload({'previous': True}, target)
            with self.assertRaises(ValueError):
                write_payload({'bad': float('nan')}, target)
            self.assertEqual(json.loads(target.read_text()), {'previous': True})
            self.assertEqual(list(Path(directory).iterdir()), [target])

    def test_no_eligible_stocks_does_not_publish_an_empty_replacement(self):
        raw = self.raw.copy()
        raw['volume_ratio_20d'] = 0
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, 'No eligible ML forecasts'):
                self.payload(directory, snapshots=raw)

    def test_public_render_escapes_names_and_disables_stale_or_forged_recommendations(self):
        with tempfile.TemporaryDirectory() as directory:
            payload = self.payload(directory)
            payload['stocks'][0]['stock_name'] = '</script><script>alert(1)</script>'
            payload['internal_debug'] = 'DO_NOT_EXPORT'
            html, script = render_model_panel(payload)
            self.assertNotIn('</script><script>', html)
            self.assertNotIn('DO_NOT_EXPORT', html)
            self.assertIn('\\u003c/script', html)
            self.assertIn('textContent', script)
            self.assertNotIn('innerHTML', script)
            target = Path(directory) / 'public.json'
            payload.update(model_state='validated', recommendation_enabled=True)
            payload['stocks'][0]['recommended'] = True
            payload['forward']['passed'] = True
            write_payload(payload, target)
            loaded = load_public_forecast(target)
            self.assertIsNotNone(loaded)
            self.assertFalse(loaded['recommendation_enabled'])
            self.assertNotEqual(model_status(loaded)[0], 'VALIDATED')
            payload.update(price_date='2000-01-01', generated_at='2000-01-01T18:00:00+09:00')
            payload['stocks'][0]['signal_date'] = '2000-01-01'
            target = Path(directory) / 'stale.json'
            write_payload(payload, target)
            loaded = load_public_forecast(target)
            self.assertEqual(loaded['model_state'], 'stale')
            self.assertEqual(loaded['recommendations'], [])
            self.assertTrue(loaded['stocks'][0]['stale'])

    def test_publishing_older_prices_cannot_roll_back_the_dashboard(self):
        with tempfile.TemporaryDirectory() as directory:
            payload = self.payload(directory)
            target = Path(directory) / 'public.json'
            write_payload(payload, target)
            before = target.read_bytes()
            payload['price_date'] = '2026-10-19'
            with self.assertRaisesRegex(ValueError, 'Older price data'):
                write_payload(payload, target)
            self.assertEqual(target.read_bytes(), before)

    def test_missing_or_invalid_public_data_has_explicit_unavailable_state(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'absent.json'
            self.assertIsNone(load_public_forecast(path))
            path.write_text('{"schema": "wrong"}')
            self.assertIsNone(load_public_forecast(path))
        html, script = render_model_panel(None)
        self.assertIn('모델 예측 데이터가 아직 연결되지 않았습니다', html)
        self.assertEqual(script, '')

    def test_shell_help_and_missing_history_work_on_macos_bash(self):
        help_result = subprocess.run(['bash', 'scripts/price_model.sh', '--help'], cwd=ROOT, capture_output=True, text=True, timeout=30)
        self.assertEqual(help_result.returncode, 0, help_result.stderr)
        missing_history = subprocess.run(['bash', 'scripts/price_model.sh', 'train'], cwd=ROOT, capture_output=True, text=True, timeout=30)
        self.assertEqual(missing_history.returncode, 2)
        self.assertIn('verified completed OHLCV history', missing_history.stderr)


if __name__ == '__main__':
    unittest.main()
