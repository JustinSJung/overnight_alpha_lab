from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from src.crawler.market_clock import KST
from src.features.next_open_dataset import TARGET_VERSION
from src.models.improvement_families import BASELINE, FAMILIES, family_spec
from src.models.selected_price_model import ROOT
from src.pipeline.model_improvement import (
    PROTOCOL_PATH, choose_family, freeze_trials, load_protocol, permitted_serving_family,
    read_trials, selection,
)


def protocol():
    return dict(schema='model_improvement_protocol_v1', registered_at='2026-01-01T00:00:00+09:00',
                minimum_candidates=100, families=deepcopy(FAMILIES), pairwise_comparison_budget=12,
                paired_outcome_coverage=.99)


def goal():
    value = json.loads((ROOT / 'docs/model_experiments/reliability_goal_20261026.json').read_text())
    value['registered_policy_ids'] += [name for name in FAMILIES if name != BASELINE]
    value['certification_signal_start'] = '2026-01-01'
    return value


def original_fixture():
    day = pd.Timestamp('2026-10-29')
    frame = pd.DataFrame(dict(stock_code=[str(n).zfill(6) for n in range(100)],
                              signal_date=day, origin_close=100.))
    models = {}
    for index, name in enumerate(FAMILIES):
        frame[name + '_probability'] = np.linspace(.9, .1, len(frame))
        frame[name + '_selected'] = selection(frame, frame[name + '_probability'])
        models[name] = dict(dataset_sha256='abcd'[index] * 64, trained_at='2026-10-29T16:20:00+09:00',
                            as_of='2026-10-28', target_version=TARGET_VERSION, baseline_probability=.5,
                            model_family=name, private_path='/never/publish', api_secret='PRIVATE_FIXTURE')
    return frame, models, pd.Timestamp('2026-10-29T17:00:00+09:00')


def graded_fixture(days=150, success=True):
    dates = pd.bdate_range('2026-01-05', periods=days + 5)
    frames = {}
    probabilities = [.65, .9, .85, .75]
    for name, probability in zip(FAMILIES, probabilities):
        records = []
        for number, day in enumerate(dates[:-5]):
            for code in range(5):
                y = 1. if success else float((number + code) % 2)
                records.append(dict(stock_code=str(code).zfill(6), signal_date=day,
                    recorded_at=(day.tz_localize(KST) + pd.Timedelta(hours=17)).isoformat(),
                    model_trained_at=(day.tz_localize(KST) + pd.Timedelta(hours=16)).isoformat(),
                    prediction_id=f'{name}-{number}-{code}', target_version=TARGET_VERSION,
                    horizon_sessions=5, cost_assumption=.003, target=y,
                    net_return_proxy=.02 if y else -.02, fixed_policy_selected=True,
                    probability_above_cost=probability, origin_price_revised=False))
        frames[name] = pd.DataFrame(records)
    benchmark = pd.DataFrame([dict(signal_date=day, entry_date=dates[index + 1],
        exit_date=dates[index + 5], net_return=.001, source=goal()['benchmark_source_id'])
        for index, day in enumerate(dates[:-5])])
    return frames, dates, benchmark, pd.Timestamp('2026-10-29T18:00:00+09:00')


class ModelImprovementTests(unittest.TestCase):
    def test_unknown_family_is_not_added_automatically(self):
        with self.assertRaises(ValueError):
            family_spec('unlimited_new_algorithm')

    def test_no_evidence_preserves_baseline(self):
        result = choose_family({name: pd.DataFrame() for name in FAMILIES}, [], goal(), protocol(), None,
                               pd.Timestamp('2026-10-29T18:00:00+09:00'))
        self.assertEqual(result['active_family'], BASELINE)
        self.assertFalse(result['recommendation_enabled'])
        self.assertTrue(all(not item['goal_passed'] for item in result['candidate_goals'].values()))

    def test_originals_are_portable_immutable_and_common_pool_is_not_reduced(self):
        frame, models, now = original_fixture()
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(freeze_trials(frame, models, protocol(), directory, now), 'new_prospective_batch_recorded')
            before = {path.name: path.read_bytes() for path in Path(directory).iterdir()}
            changed = frame.copy()
            changed[next(iter(FAMILIES)) + '_probability'] = .99
            self.assertEqual(freeze_trials(changed, models, protocol(), directory, now), 'original_batch_preserved')
            self.assertEqual(before, {path.name: path.read_bytes() for path in Path(directory).iterdir()})
            batches, later = read_trials(directory, protocol())
            self.assertEqual(len(batches[0][0]), 100)
            self.assertEqual(later, 0)
            self.assertNotIn('PRIVATE_FIXTURE', str(batches[0][1]))
            self.assertNotIn('/never/publish', str(batches[0][1]))
            from src.pipeline.original_forecast_cache import copy_improvement_originals
            restored = Path(directory) / 'restored'
            self.assertEqual(copy_improvement_originals(directory, restored, protocol()), 2)
            restored_batches, _ = read_trials(restored, protocol())
            pd.testing.assert_frame_equal(batches[0][0], restored_batches[0][0])

    def test_modified_original_or_missing_manifest_blocks_evaluation(self):
        frame, models, now = original_fixture()
        with tempfile.TemporaryDirectory() as directory:
            freeze_trials(frame, models, protocol(), directory, now)
            path = next(Path(directory).glob('*.csv'))
            original = path.read_bytes()
            path.write_bytes(original + b'\n')
            with self.assertRaisesRegex(ValueError, 'checksum'):
                read_trials(directory, protocol())
            path.write_bytes(original)
            path.with_suffix('.manifest.json').unlink()
            with self.assertRaisesRegex(ValueError, 'Incomplete'):
                read_trials(directory, protocol())

    def test_future_model_and_invalid_selection_are_rejected_before_writing(self):
        frame, models, now = original_fixture()
        with tempfile.TemporaryDirectory() as directory:
            models[BASELINE]['trained_at'] = '2026-10-30T17:00:00+09:00'
            with self.assertRaises(ValueError):
                freeze_trials(frame, models, protocol(), directory, now)
            self.assertEqual(list(Path(directory).iterdir()), [])
            models[BASELINE]['trained_at'] = '2026-10-29T16:00:00+09:00'
            frame[BASELINE + '_selected'] = True
            with self.assertRaises(ValueError):
                freeze_trials(frame, models, protocol(), directory, now)
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_backdating_and_reduced_candidate_pool_are_rejected(self):
        frame, models, now = original_fixture()
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                freeze_trials(frame.iloc[:20].copy(), models, protocol(), directory, now)
            frame['signal_date'] -= pd.Timedelta(days=1)
            with self.assertRaisesRegex(ValueError, 'prospective'):
                freeze_trials(frame, models, protocol(), directory, now)

    def test_exactly_60_perfect_dates_do_not_bypass_conservative_small_sample_guard(self):
        frames, calendar, benchmark, now = graded_fixture(days=60)
        result = choose_family(frames, calendar, goal(), protocol(), benchmark, now)
        self.assertEqual(result['active_family'], BASELINE)
        for status in result['candidate_goals'].values():
            self.assertEqual(status['evaluated_cases'], 300)
            self.assertLess(status['success_lower'], .6)

    def test_strong_prospective_evidence_promotes_best_passing_candidate(self):
        frames, calendar, benchmark, now = graded_fixture()
        result = choose_family(frames, calendar, goal(), protocol(), benchmark, now)
        self.assertEqual(result['active_family'], 'auto_linear_504_v1')
        self.assertEqual(result['action'], 'promote')
        self.assertTrue(result['candidate_goals']['auto_linear_504_v1']['goal_passed'])
        self.assertTrue(result['comparisons']['auto_linear_504_v1_vs_baseline']['passed'])
        self.assertFalse(result['recommendation_enabled'])

    def test_good_incumbent_is_not_replaced_by_worse_challengers(self):
        frames, calendar, benchmark, now = graded_fixture()
        result = choose_family(frames, calendar, goal(), protocol(), benchmark, now, 'auto_linear_504_v1')
        self.assertEqual(result['active_family'], 'auto_linear_504_v1')
        self.assertEqual(result['action'], 'retain')
        self.assertFalse(result['comparisons']['auto_hgb_504_v1_vs_incumbent']['passed'])

    def test_bad_recent_performance_rolls_back_and_does_not_weaken_goal(self):
        frames, calendar, benchmark, now = graded_fixture(success=False)
        before = deepcopy(goal())
        result = choose_family(frames, calendar, before, protocol(), benchmark, now, 'auto_linear_504_v1')
        self.assertEqual(result['active_family'], BASELINE)
        self.assertEqual(result['action'], 'rollback')
        self.assertEqual(before, goal())

    def test_unknown_outcomes_and_price_revisions_cannot_be_silently_dropped(self):
        frames, calendar, benchmark, now = graded_fixture()
        for frame in frames.values():
            frame.loc[0, 'target'] = np.nan
        result = choose_family(frames, calendar, goal(), protocol(), benchmark, now)
        self.assertEqual(result['active_family'], BASELINE)
        self.assertIn('mature_selected_outcomes_missing', result['candidate_goals']['auto_linear_504_v1']['reasons'])
        frames, calendar, benchmark, now = graded_fixture()
        for frame in frames.values():
            frame['origin_price_revised'] = True
        self.assertEqual(choose_family(frames, calendar, goal(), protocol(), benchmark, now)['active_family'], BASELINE)

    def test_missing_benchmark_prevents_promotion(self):
        frames, calendar, _, now = graded_fixture()
        result = choose_family(frames, calendar, goal(), protocol(), None, now)
        self.assertEqual(result['active_family'], BASELINE)

    def test_nonbaseline_serving_requires_fresh_passed_audit(self):
        with self.assertRaises(ValueError):
            permitted_serving_family({'active_family': 'auto_linear_504_v1'}, '2026-10-29')
        frames, calendar, benchmark, now = graded_fixture()
        decision = choose_family(frames, calendar, goal(), protocol(), benchmark, now)
        decision['price_date'] = '2026-10-29'
        self.assertEqual(permitted_serving_family(decision, '2026-10-29'), 'auto_linear_504_v1')
        with self.assertRaises(ValueError):
            permitted_serving_family(decision, '2026-10-30')

    def test_live_protocol_is_pinned_and_lowered_threshold_is_rejected(self):
        actual, registered_goal = load_protocol()
        self.assertEqual(len(registered_goal['registered_policy_ids']), 8)
        self.assertEqual(registered_goal['minimum_evaluated_cases'], 300)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'protocol.json'
            actual['threshold'] = .5
            path.write_text(json.dumps(actual))
            with self.assertRaises(ValueError):
                load_protocol(path)

    def test_learning_cycle_cannot_bypass_the_promotion_audit(self):
        from src.pipeline.next_open_learning_cycle import run_cycle
        inputs = pd.DataFrame({'signal_date': [pd.Timestamp('2026-10-28')]})
        with patch('src.pipeline.next_open_learning_cycle.load_inputs', return_value=(inputs, {})):
            with self.assertRaisesRegex(ValueError, 'unvalidated'):
                run_cycle('/unused', '/unused', '/unused', None, '/unused',
                          now=pd.Timestamp('2026-10-29T18:00:00+09:00'), family='auto_linear_504_v1')

    def test_public_status_hides_family_names_and_cannot_claim_success_without_proof(self):
        from src.report_generator.model_improvement_panel import render_model_improvement_card
        frames, calendar, benchmark, now = graded_fixture(days=20)
        result = choose_family(frames, calendar, goal(), protocol(), benchmark, now)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'status.json'
            path.write_text(json.dumps(result))
            html = render_model_improvement_card(path, now.to_pydatetime())
            self.assertIn('학습·비교 검증 중', html)
            self.assertNotIn('auto_linear', html)
            result['status'], result['active_family'] = 'validated_challenger_active', 'auto_linear_504_v1'
            path.write_text(json.dumps(result))
            self.assertIn('점검 필요', render_model_improvement_card(path, now.to_pydatetime()))

    def test_public_recorded_days_are_distinct_from_selected_outcome_days(self):
        from src.report_generator.model_improvement_panel import render_model_improvement_card
        frames = {name: pd.DataFrame() for name in FAMILIES}
        now = pd.Timestamp('2026-10-29T18:00:00+09:00')
        result = choose_family(frames, [], goal(), protocol(), None, now)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'status.json'
            result.update(original_batches=0, recording='new_prospective_batch_recorded')
            path.write_text(json.dumps(result))
            html = render_model_improvement_card(path, now.to_pydatetime())
            self.assertIn('사전 예측 1일', html)
            self.assertIn('선택 후보 평가 0일', html)
            result.update(original_batches=1, recording='original_batch_preserved')
            path.write_text(json.dumps(result))
            self.assertIn('사전 예측 1일', render_model_improvement_card(path, now.to_pydatetime()))


if __name__ == '__main__':
    unittest.main()
