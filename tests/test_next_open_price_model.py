import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.crawler.market_clock import KST
from src.features.next_open_dataset import TARGET_VERSION, build_next_open_dataset
from src.models.next_open_price_model import (
    ROOT, current_predictions, evaluate, fit_classifier, fit_current, freeze, grade, load_model,
    predict_probability, query_stock, run_experiment, selection_summary,
)
from src.models.selected_price_model import COLUMNS, prepare_selected_features


class NextOpenPriceModelTests(unittest.TestCase):
    def prepared(self):
        return prepare_selected_features(panel(), COLUMNS)

    def test_current_fit_records_actual_label_date_not_nontrading_cutoff(self):
        from src.models.monthly_price_walkforward import monthly_split
        inputs = self.prepared()
        friday = pd.Timestamp(inputs.signal_date.max())
        sunday = friday + pd.Timedelta(days=2)
        with tempfile.TemporaryDirectory() as directory, \
                patch('src.models.next_open_price_model.load_inputs', return_value=(inputs, {})), \
                patch('src.models.next_open_price_model.monthly_split', side_effect=lambda known, as_of, **kwargs: monthly_split(known, as_of, 15, 3)):
            fit_current('/unused', directory, sunday)
            m = load_model(directory)['metadata']
            self.assertEqual(m['as_of'], str(friday.date()))
            self.assertEqual(m['requested_as_of'], str(sunday.date()))
            self.assertEqual(m['as_of'], m['partitions']['calibration']['latest_label'])

    def test_ranking_is_frozen_before_unknown_outcomes_and_no_false_zero_return(self):
        frame = pd.DataFrame({'stock_code': ['000001', '000002', '000003'],
                              'signal_date': pd.Timestamp('2026-07-01'),
                              'label_status': ['exit_price_unavailable', 'resolved', 'resolved'],
                              'target': [np.nan, 1., 0.], 'net_return_proxy': [np.nan, .1, -.1]})
        scored, m = evaluate(frame, np.array([.9, .8, .7]), .5, cap=1)
        self.assertEqual(scored.loc[scored.fixed_policy_selected, 'stock_code'].tolist(), ['000001'])
        self.assertEqual(m['fixed_policy']['selected_cases'], 1)
        self.assertEqual(m['fixed_policy']['unresolved_cases'], 1)
        self.assertIsNone(m['fixed_policy']['all_date_net_return_proxy'])
        self.assertIsNone(m['fixed_policy']['conditional_success_rate'])
        self.assertTrue(scored.recommendation.eq('ABSTAIN').all())
        empty = selection_summary(scored, np.zeros(len(scored), dtype=bool))
        self.assertEqual(empty['selected_cases'], 0)
        self.assertEqual(empty['all_date_net_return_proxy'], 0)
        self.assertIsNone(empty['conditional_success_rate'])

    def test_reproducible_model_roundtrip_and_purged_matched_experiment(self):
        inputs = self.prepared()
        days = sorted(inputs.signal_date.unique())
        protocol = json.loads((ROOT / 'docs/model_experiments/next_open_protocol_20261021.json').read_text())
        protocol.update(labels_as_of=str(pd.Timestamp(days[-1]).date()), calibration_start=str(pd.Timestamp(days[60]).date()),
                        evaluation_start=str(pd.Timestamp(days[90]).date()),
                        periods={'historical': [str(pd.Timestamp(days[90]).date()), str(pd.Timestamp(days[-1]).date())]})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('src.models.next_open_price_model.load_inputs', return_value=(inputs, {})), \
                    patch('src.models.next_open_price_model.raw_audit', return_value={}), patch('builtins.print'):
                summary = run_experiment('/unused', root / 'model', protocol, root / 'report.md')
            self.assertFalse(summary['recommendation_gate_passed'])
            bundle = load_model(root / 'model')
            self.assertEqual(bundle['metadata']['target_version'], TARGET_VERSION)
            self.assertFalse(bundle['metadata']['recommendation_enabled'])
            m = summary['results']['historical']['next_open_trained']
            self.assertGreater(m['unresolved_cases'], 0)
            part = bundle['metadata']['partitions']
            self.assertLess(pd.Timestamp(part['train']['latest_label']), pd.Timestamp(part['calibration']['start']))
            self.assertTrue((root / 'report.md').exists())
            run = Path(summary['run_dir'])
            a, b = [pd.read_csv(run / ('historical_' + role + '.csv')) for role in ['same_close_trained_control', 'next_open_trained']]
            pd.testing.assert_frame_equal(a[['stock_code', 'signal_date', 'target']], b[['stock_code', 'signal_date', 'target']])
            with (run / 'model.joblib').open('ab') as handle:
                handle.write(b'tampered')
            with self.assertRaises(ValueError):
                load_model(root / 'model')

    def bundle(self, inputs):
        cohort, _ = build_next_open_dataset(inputs, inputs.signal_date.max())
        days = sorted(inputs.signal_date.unique())
        train = cohort[cohort.target.notna() & cohort.label_available_date.lt(days[70])]
        calibration = cohort[cohort.signal_date.ge(days[70]) & cohort.label_available_date.lt(days[100])]
        bundle = fit_classifier(train, calibration)
        bundle['metadata'] = dict(dataset_sha256='a' * 64, trained_at=pd.Timestamp(days[110], tz=KST).isoformat(),
                                  as_of=str(pd.Timestamp(days[99]).date()), baseline_probability=.5,
                                  target_version=TARGET_VERSION)
        return bundle

    def test_forward_freeze_is_timely_immutable_and_grade_uses_next_open(self):
        inputs = self.prepared()
        days = sorted(inputs.signal_date.unique())
        origin = pd.Timestamp(days[125])
        now = origin.tz_localize(KST) + pd.Timedelta(hours=17)
        bundle = self.bundle(inputs)
        with tempfile.TemporaryDirectory() as directory:
            with patch('src.models.next_open_price_model.load_inputs', return_value=(inputs[inputs.signal_date.le(origin)], {})):
                data_root = Path(directory) / 'history'
                data_root.mkdir()
                (data_root / 'history_manifest.json').write_text('{}')
                frozen = freeze(bundle, data_root, directory, now)
                with self.assertRaises(FileExistsError):
                    freeze(bundle, data_root, directory, now)
                with self.assertRaises(ValueError):
                    freeze(bundle, data_root, directory, now + pd.Timedelta(hours=20))
            path = Path(frozen['ledger'])
            original = path.read_bytes()
            ledger = pd.read_csv(path, dtype={'stock_code': str})
            graded, summary = grade(ledger, inputs, days[-1], pd.Timestamp(days[-1], tz=KST) + pd.Timedelta(hours=17))
            self.assertEqual(summary['recorded_candidates'], len(ledger))
            self.assertEqual(summary['evaluated_cases'], len(ledger))
            first = graded.iloc[0]
            stock = inputs[inputs.stock_code.eq(first.stock_code)].set_index('signal_date')
            self.assertAlmostEqual(first.target_return, stock.loc[days[130], 'close'] / stock.loc[days[126], 'open'] - 1)
            self.assertEqual(path.read_bytes(), original)
            pending, s = grade(ledger, inputs[inputs.signal_date.le(origin)], origin, now)
            self.assertEqual(s['evaluated_cases'], 0)
            self.assertTrue(pending.label_status.eq('awaiting_future_sessions').all())
            ledger.loc[0, 'recorded_at'] = (now + pd.Timedelta(days=1)).isoformat()
            with self.assertRaises(ValueError):
                grade(ledger, inputs, days[-1], pd.Timestamp(days[-1], tz=KST) + pd.Timedelta(hours=17))

    def test_grading_retains_candidate_even_if_origin_is_now_inactive(self):
        inputs = self.prepared()
        days = sorted(inputs.signal_date.unique())
        origin = pd.Timestamp(days[100])
        keys = pd.DataFrame({'stock_code': ['000001'], 'signal_date': [origin]})
        inputs.loc[inputs.stock_code.eq('000001') & inputs.signal_date.eq(origin), 'volume'] = 0
        outcomes, _ = build_next_open_dataset(inputs, days[-1], candidate_keys=keys)
        self.assertEqual(len(outcomes), 1)
        self.assertTrue(outcomes.target.notna().all())

    def test_stock_name_and_code_lookup_use_existing_resolver_contract(self):
        predictions = pd.DataFrame({'stock_code': ['000001'], 'probability_above_cost': [.42],
                                    'recommendation': ['ABSTAIN']})
        with patch('src.models.next_open_price_model.resolve_stock', return_value='000001'), \
                patch('src.models.next_open_price_model.current_predictions', return_value=predictions):
            for query in ['test name', '000001']:
                result = query_stock({}, '/unused', query)
                self.assertEqual(result['stock_code'], '000001')
                self.assertEqual(result['requested_stock'], query)
                self.assertEqual(result['recommendation'], 'ABSTAIN')

    def test_same_close_mature_labels_are_allowed_but_future_labels_are_not(self):
        origin = pd.Timestamp('2026-10-21')
        now = origin.tz_localize(KST) + pd.Timedelta(hours=17)
        frame = pd.DataFrame({'stock_code': ['005930'], 'signal_date': [origin],
                              'probability_above_cost': [.6], 'recommendation': ['ABSTAIN']})
        metadata = dict(dataset_sha256='a' * 64, trained_at=(now - pd.Timedelta(minutes=10)).isoformat(),
                        as_of=str(origin.date()), baseline_probability=.5, target_version=TARGET_VERSION)
        with tempfile.TemporaryDirectory() as directory, \
                patch('src.models.next_open_price_model.current_predictions', return_value=frame):
            result = freeze({'metadata': metadata}, '/unused', directory, now)
            self.assertEqual(result['predictions'], 1)
            metadata['as_of'] = '2026-10-22'
            with self.assertRaises(ValueError):
                freeze({'metadata': metadata}, '/unused', directory, now)


if __name__ == '__main__':
    unittest.main()
