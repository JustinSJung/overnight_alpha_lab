import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

from test_market_context_experiment import panel
from src.crawler.market_clock import KST
from src.features.next_open_dataset import TARGET_VERSION, build_next_open_dataset
from src.models.selected_price_model import COLUMNS, fit_data_digest, prepare_selected_features
from src.pipeline.next_open_learning_cycle import collect_originals, implementation_digest, run_cycle
from src.report_generator.next_open_forecast_report import build_payload, observed_performance
from src.report_generator.price_model_panel import load_public_forecast, render_model_panel


class NextOpenLearningCycleTests(unittest.TestCase):
    def test_no_new_fit_rows_preserves_model_and_new_labels_trigger_one_fit(self):
        inputs = prepare_selected_features(panel(), COLUMNS)
        days = sorted(inputs.signal_date.unique())
        cohort, _ = build_next_open_dataset(inputs, days[-1])
        known = cohort[cohort.target.notna()]
        train = known[known.label_available_date.lt(days[70])]
        calibration = known[known.signal_date.ge(days[70]) & known.label_available_date.lt(days[100])]
        digest = fit_data_digest(train, calibration, COLUMNS)
        now = pd.Timestamp(days[-1], tz=KST) + pd.offsets.BDay(1) + pd.Timedelta(hours=10)
        metadata = dict(as_of=str(pd.Timestamp(days[-1]).date()), dataset_sha256=digest,
                        trained_at=(now - pd.Timedelta(days=1)).isoformat(), implementation_sha256=implementation_digest())
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            models = root / 'models'
            models.mkdir()
            (models / 'latest.json').write_text('{}')
            common = [patch('src.pipeline.next_open_learning_cycle.load_inputs', return_value=(inputs, {})),
                      patch('src.pipeline.next_open_learning_cycle.monthly_split', return_value=(train, calibration))]
            with common[0], common[1], patch('src.pipeline.next_open_learning_cycle.load_model', return_value={'metadata': metadata}), \
                    patch('src.pipeline.next_open_learning_cycle.fit_current') as fit:
                report = run_cycle('/unused', models, root, None, root / 'report.json', now)
                self.assertEqual(report['learning_state'], 'no_new_fit_rows_model_preserved')
                self.assertEqual(report['new_mature_labels'], 0)
                self.assertEqual(report['new_frozen_predictions'], 0)
                fit.assert_not_called()
            old = metadata | {'as_of': str(pd.Timestamp(days[100]).date()), 'dataset_sha256': 'old'}
            with patch('src.pipeline.next_open_learning_cycle.load_inputs', return_value=(inputs, {})), \
                    patch('src.pipeline.next_open_learning_cycle.monthly_split', return_value=(train, calibration)), \
                    patch('src.pipeline.next_open_learning_cycle.load_model', side_effect=[{'metadata': old}, {'metadata': metadata}]), \
                    patch('src.pipeline.next_open_learning_cycle.fit_current') as fit:
                report = run_cycle('/unused', models, root, None, root / 'report.json', now)
                self.assertEqual(report['learning_state'], 'new_mature_labels_learned')
                self.assertGreater(report['new_mature_labels'], 0)
                fit.assert_called_once()
                self.assertFalse(report['recommendation_enabled'])

    def original_fixture(self, root):
        metadata = dict(dataset_sha256='a' * 64, trained_at='2026-10-21T15:00:00+09:00',
                        as_of='2026-10-20', target_version=TARGET_VERSION, baseline_probability=.5)
        run = root / 'models/runs/example'
        run.mkdir(parents=True)
        (run / 'model_metadata.json').write_text(json.dumps(metadata))
        frame = pd.DataFrame([dict(model_dataset_sha256='a' * 64, model_trained_at=metadata['trained_at'],
                                   recorded_at='2026-10-21T17:00:00+09:00', signal_date='2026-10-21',
                                   stock_code='005930', prediction_id='original', validation_base_rate=.5,
                                   target_version=TARGET_VERSION)])
        path = root / 'ml_next_open_forward_20261021_aaaaaaaaaaaaaaaa.csv'
        frame.to_csv(path, index=False)
        return path, frame

    def test_sunday_metadata_is_repaired_without_claiming_new_labels(self):
        inputs = prepare_selected_features(panel(), COLUMNS)
        days = sorted(inputs.signal_date.unique())
        cohort, _ = build_next_open_dataset(inputs, days[-1])
        known = cohort[cohort.target.notna()]
        train = known[known.label_available_date.lt(days[100])]
        calibration = known[known.signal_date.ge(days[100])]
        digest = fit_data_digest(train, calibration, COLUMNS)
        now = pd.Timestamp(days[-1], tz=KST) + pd.offsets.BDay(1) + pd.Timedelta(hours=10)
        old = dict(as_of=str((pd.Timestamp(days[-1]) + pd.Timedelta(days=2)).date()), dataset_sha256=digest,
                   trained_at=(now - pd.Timedelta(minutes=1)).isoformat(),
                   implementation_sha256=implementation_digest(),
                   partitions={'calibration': {'latest_label': str(pd.Timestamp(days[-1]).date())}})
        fixed = old | {'as_of': str(pd.Timestamp(days[-1]).date())}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            models = root / 'models'
            models.mkdir()
            (models / 'latest.json').write_text('{}')
            with patch('src.pipeline.next_open_learning_cycle.load_inputs', return_value=(inputs, {})), \
                    patch('src.pipeline.next_open_learning_cycle.monthly_split', return_value=(train, calibration)), \
                    patch('src.pipeline.next_open_learning_cycle.load_model', side_effect=[{'metadata': old}, {'metadata': fixed}]), \
                    patch('src.pipeline.next_open_learning_cycle.fit_current') as fit:
                report = run_cycle('/unused', models, root, None, root / 'report.json', now)
            fit.assert_called_once()
            self.assertEqual(report['learning_state'], 'fit_cutoff_metadata_repaired')
            self.assertEqual(report['new_mature_labels'], 0)

    def test_original_changes_are_detected_and_later_batches_cannot_replace_first(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path, frame = self.original_fixture(root)
            original, registry, excluded = collect_originals(root, root / 'models', {})
            self.assertEqual(len(original), 1)
            self.assertEqual(excluded, 0)
            self.assertEqual(registry[path.name], hashlib.sha256(path.read_bytes()).hexdigest())
            later = frame.assign(recorded_at='2026-10-21T18:00:00+09:00', prediction_id='later')
            later.to_csv(root / 'ml_next_open_forward_20261021_bbbbbbbbbbbbbbbb.csv', index=False)
            chosen, _, excluded = collect_originals(root, root / 'models', registry)
            self.assertEqual(chosen.prediction_id.tolist(), ['original'])
            self.assertEqual(excluded, 1)
            frame.assign(validation_base_rate=.9).to_csv(path, index=False)
            with self.assertRaisesRegex(ValueError, 'changed'):
                collect_originals(root, root / 'models', registry)

    def test_invalid_original_cannot_be_registered(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path, frame = self.original_fixture(root)
            frame.assign(recorded_at='2026-10-22T10:00:00+09:00').to_csv(path, index=False)
            with self.assertRaises(ValueError):
                collect_originals(root, root / 'models', {})

    def test_public_output_has_no_invented_return_or_model_files_and_cannot_enable_recommendations(self):
        now = pd.Timestamp.now(tz=KST)
        day = now.normalize() - pd.Timedelta(days=1)
        forecasts = pd.DataFrame({'stock_code': ['005930'], 'signal_date': [day.tz_localize(None)],
                                  'probability_above_cost': [.63], 'recommendation': ['ABSTAIN']})
        bundle = {'metadata': {'target_version': TARGET_VERSION, 'as_of': str(day.date()),
                               'secret_local_path': '/not/public'}}
        evidence = dict(recorded_candidates=1, evaluated_cases=0, unresolved_cases=1,
                        states={'awaiting_future_sessions': 1})
        prior_record = forecasts.assign(signal_date=day.tz_localize(None) - pd.Timedelta(days=1), target=float('nan'))
        with patch('src.report_generator.next_open_forecast_report.current_predictions', return_value=forecasts), \
                patch('src.report_generator.next_open_forecast_report.stock_catalog', return_value={'Samsung': {'005930'}}):
            payload = build_payload(bundle, '/unused', evidence, prior_record, now)
        self.assertFalse(payload['recommendation_enabled'])
        self.assertIsNone(payload['stocks'][0]['predicted_return'])
        self.assertEqual(payload['forward']['pending'], 1)
        self.assertNotIn('/not/public', json.dumps(payload))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'public.json'
            path.write_text(json.dumps(payload))
            loaded = load_public_forecast(path)
            self.assertIsNotNone(loaded)
            html, script = render_model_panel(loaded)
            self.assertIn('다음 거래일 시가', html)
            self.assertIn('학습 시스템의 실제 미래 평가', html)
            self.assertIn('미제공', script)
            payload.update(model_state='validated', recommendation_enabled=True)
            payload['forward'].update(recorded=1000, resolved=1000, pending=0, signal_dates=100, passed=True)
            payload['stocks'][0]['recommended'] = True
            path.write_text(json.dumps(payload))
            self.assertIsNone(load_public_forecast(path))
            payload['observed_performance'].update(evaluated_cases=1000, success_count=600,
                                                    failure_count=400, success_rate=.6, signal_dates=100)
            path.write_text(json.dumps(payload))
            loaded = load_public_forecast(path)
            self.assertFalse(loaded['recommendation_enabled'])
            self.assertEqual(loaded['recommendations'], [])
            payload['stocks'][0]['predicted_return'] = .1
            path.write_text(json.dumps(payload))
            self.assertIsNone(load_public_forecast(path))

    def test_publication_keeps_frozen_probability_and_separates_unavailable(self):
        now = pd.Timestamp.now(tz=KST)
        day = (now.normalize() - pd.Timedelta(days=1)).tz_localize(None)
        forecasts = pd.DataFrame({'stock_code': ['005930'], 'signal_date': [day],
                                  'probability_above_cost': [.95], 'recommendation': ['ABSTAIN']})
        frozen = pd.concat([forecasts.assign(signal_date=day - pd.Timedelta(days=i), probability_above_cost=.4,
                                             target=float('nan')) for i in range(10)], ignore_index=True)
        bundle = {'metadata': {'target_version': TARGET_VERSION, 'as_of': str(day.date())}}
        evidence = dict(recorded_candidates=10, evaluated_cases=0, unresolved_cases=10,
                        states={'awaiting_future_sessions': 8, 'exit_price_unavailable': 2})
        with patch('src.report_generator.next_open_forecast_report.current_predictions', return_value=forecasts), \
                patch('src.report_generator.next_open_forecast_report.stock_catalog', return_value={}):
            payload = build_payload(bundle, '/unused', evidence, frozen, now)
        self.assertEqual(payload['prediction_origin'], 'frozen_original')
        self.assertEqual(payload['stocks'][0]['probability'], .4)
        self.assertEqual(payload['forward']['pending'], 8)
        self.assertEqual(payload['forward']['unavailable'], 2)

    def test_public_observed_rates_use_original_outcomes_not_current_probabilities(self):
        frame = pd.DataFrame(dict(stock_code=['000001', '000002', '000003', '000004'],
                                  signal_date=['2026-10-21'] * 4,
                                  target=[1., 0., float('nan'), 1.],
                                  probability_above_cost=[.7, .8, .9, .4],
                                  fixed_policy_selected=[True, True, True, False]))
        m = observed_performance(frame)
        self.assertEqual(m['evaluated_cases'], 3)
        self.assertEqual(m['success_count'], 2)
        self.assertAlmostEqual(m['success_rate'], 2 / 3)
        self.assertEqual(m['selected_success_rate'], .5)
        self.assertEqual(m['selected_pending_or_unavailable'], 1)
        self.assertIsNone(observed_performance(frame.assign(target=float('nan')))['success_rate'])


if __name__ == '__main__':
    unittest.main()
