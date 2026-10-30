import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from src.features.next_open_dataset import COLUMNS
from src.research.evaluation import development_folds, metrics
from src.research.memory import append_event, locked_memory, read_memory
from src.research.programs import canonical, program_id, propose, transform, validate_program
from src.research.runner import context, execute_trial, load_policy, run_research
from src.report_generator.algorithm_research_panel import render_algorithm_research_card


def program():
    return dict(schema='numerical_research_program_v1', learner='linear',
                nodes=[{'op': 'safe_divide', 'inputs': ['return_5d', 'volatility_20d']},
                       {'op': 'tanh', 'inputs': [0]}], outputs=[0, 1])


def completed():
    return dict(status='completed', metrics={'development_brier_improvement': .001,
                'research_screen_passed': False, 'screen_reasons': ['too_few_selected_development_cases']},
                evidence='reused_historical_development_only', future_validation_required=True,
                production_promotion=False, recommendation_enabled=False)


class ProgramTests(unittest.TestCase):
    def setUp(self):
        self.frame = pd.DataFrame(np.arange(8 * len(COLUMNS)).reshape(8, -1) / 100, columns=COLUMNS)

    def test_pointwise_program_is_independent_of_labels_and_row_order(self):
        original = transform(program(), self.frame)
        augmented = self.frame.assign(target=1, future_close=100000, stock_code='005930')
        np.testing.assert_array_equal(original, transform(program(), augmented))
        np.testing.assert_array_equal(original[::-1], transform(program(), augmented.iloc[::-1]))
        np.testing.assert_array_equal(original[:, :len(COLUMNS)], self.frame)

    def test_zero_division_and_extreme_inputs_are_finite(self):
        self.frame['volatility_20d'] = 0
        self.frame['return_5d'] = 1e300
        result = transform(program(), self.frame)
        self.assertTrue(np.isfinite(result).all())
        self.assertTrue((np.abs(result[:, len(COLUMNS):]) <= 20).all())

    def test_targets_imports_future_nodes_and_boolean_references_rejected(self):
        for reference in ['target', 'label_available_date', 'future_close', '__import__', 0, True, -1]:
            bad = program()
            bad['nodes'][0]['inputs'][0] = reference
            with self.subTest(reference=reference), self.assertRaises(ValueError):
                validate_program(bad)

    def test_arbitrary_code_and_oversized_program_rejected(self):
        for change in ['code', 'many', 'unknown_op', 'nonfinite_input']:
            bad = program()
            if change == 'code': bad['code'] = 'import os'
            elif change == 'many': bad['nodes'] *= 9
            elif change == 'unknown_op': bad['nodes'][0]['op'] = 'exec'
            else: bad['outputs'] = [np.nan]
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_program(bad)

    def test_nonfinite_feature_rejected(self):
        self.frame.loc[0, COLUMNS[0]] = np.nan
        with self.assertRaises(ValueError): transform(program(), self.frame)

    def test_proposer_remembers_failures_and_uses_completed_parent(self):
        first, _ = propose([], 42)
        trial = dict(program=first, program_id=program_id(first), **completed())
        memory = [{'kind': 'trial', 'payload': trial}]
        children = [propose(memory, seed) for seed in range(10)]
        self.assertTrue(all(program_id(child) != trial['program_id'] for child, _ in children))
        self.assertTrue(any(parent == trial['program_id'] for _, parent in children))
        reserved, _ = propose([], 50)
        memory.append({'kind': 'proposal', 'payload': dict(program_id=program_id(reserved))})
        self.assertNotEqual(program_id(propose(memory, 50)[0]), program_id(reserved))


class MemoryTests(unittest.TestCase):
    def test_roundtrip_hash_chain_and_truncated_tail_detection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with locked_memory(root) as events:
                append_event(root, events, 'test', {'n': 1})
                append_event(root, events, 'test', {'n': 2})
            self.assertEqual(len(read_memory(root)), 2)
            (root / 'event_000001.json').unlink()
            with self.assertRaises(ValueError): read_memory(root)

    def test_corrupt_event_missing_anchor_and_symlinks_rejected(self):
        for mode in ['corrupt', 'anchor', 'link']:
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                with locked_memory(root) as events:
                    append_event(root, events, 'test', {'n': 1})
                path = root / 'event_000000.json'
                if mode == 'corrupt': path.write_text(path.read_text().replace('"n":1', '"n":2'))
                elif mode == 'anchor': (root / 'head.json').unlink()
                else:
                    path.rename(root / 'other.json')
                    path.symlink_to(root / 'other.json')
                with self.assertRaises(ValueError): read_memory(root)

    def test_event_size_budget(self):
        with tempfile.TemporaryDirectory() as directory, locked_memory(directory) as events:
            with self.assertRaises(ValueError): append_event(directory, events, 'test', {'text': 'x' * 50000})
            self.assertEqual(events, [])


class ReplayTests(unittest.TestCase):
    def test_purged_dates_and_unresolved_validation_candidates(self):
        dates = pd.bdate_range('2024-01-01', periods=430)
        frame = pd.DataFrame({'signal_date': dates, 'target_date': dates + pd.offsets.BDay(5),
                              'expected_target_date': dates + pd.offsets.BDay(5),
                              'label_available_date': dates + pd.offsets.BDay(5), 'target': np.arange(430) % 2})
        frame.loc[400, 'target'] = np.nan
        folds = development_folds(frame, load_policy())
        self.assertEqual(len(folds), 3)
        for train, calibration, validation in folds:
            self.assertLess(train.label_available_date.max(), calibration.signal_date.min())
            self.assertLess(calibration.label_available_date.max(), validation.signal_date.min())
        self.assertEqual(sum(val.target.isna().sum() for _, _, val in folds), 1)

    def test_selection_retains_unknowns_and_all_input_candidates(self):
        frame = pd.DataFrame({'stock_code': ['000001', '000002', '000003'],
                              'signal_date': pd.to_datetime(['2026-10-01'] * 3),
                              'target': [1, np.nan, 0], 'net_return_proxy': [.1, np.nan, -.1]})
        result = metrics(frame, np.array([.8, .9, .2]))
        self.assertEqual(result['input_candidates'], 3)
        self.assertEqual(result['selected_cases'], 2)
        self.assertEqual(result['selected_missing_outcomes'], 1)
        self.assertEqual(result['selected_evaluated_cases'], 1)


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = self.root / 'prices'
        self.data.mkdir()
        self.manifest = self.data / 'history_manifest.json'
        self.manifest.write_text(json.dumps(dict(end='2026-10-28', collection_complete=True,
                                                completed_bars_only=True, source='kis_adjusted_daily')))
        self.state, self.output, self.report = [self.root / name for name in ['memory', 'status.json', 'report.md']]

    def run_cycle(self, **kwargs):
        return run_research(self.data, self.state, self.output, self.report, **kwargs)

    @patch('src.research.runner.execute_trial', return_value=completed())
    def test_two_trials_once_per_snapshot_and_memory_guides_next_day(self, execute):
        result = self.run_cycle()
        self.assertEqual(result['trials_completed'], 2)
        self.assertFalse(result['production_promotion'])
        self.assertFalse(result['llm_enabled'])
        original = {p.name: p.read_bytes() for p in self.state.glob('*.json')}
        repeated = self.run_cycle()
        self.assertEqual(repeated['status'], 'snapshot_already_researched')
        self.assertEqual(execute.call_count, 2)
        self.assertEqual(original, {p.name: p.read_bytes() for p in self.state.glob('*.json')})
        manifest = json.loads(self.manifest.read_text())
        manifest['end'] = '2026-10-29'
        self.manifest.write_text(json.dumps(manifest))
        self.assertEqual(self.run_cycle()['trials_completed'], 4)
        self.assertEqual(context(read_memory(self.state))['trials_reserved'], 4)

    @patch('src.research.runner.execute_trial', return_value=dict(status='failed', failure_type='timeout'))
    def test_failure_consumes_budget_is_remembered_and_not_retried(self, execute):
        first = self.run_cycle()
        self.assertEqual(first['trials_failed'], 2)
        self.run_cycle()
        self.assertEqual(execute.call_count, 2)
        trials = [e for e in read_memory(self.state) if e['kind'] == 'trial']
        self.assertTrue(all(row['payload']['failure_type'] == 'timeout' for row in trials))

    @patch('src.research.runner.execute_trial', return_value=completed())
    def test_source_revisions_and_implementation_changes_do_not_reset_history(self, execute):
        self.run_cycle()
        count = len(read_memory(self.state))
        with patch('src.research.runner.implementation_fingerprint', return_value={'changed': 'hash'}):
            with self.assertRaises(ValueError): self.run_cycle()
        self.manifest.write_text(self.manifest.read_text() + '\n')
        with self.assertRaises(ValueError): self.run_cycle()
        self.assertEqual(len(read_memory(self.state)), count)

    def test_future_input_and_missing_history_fail_closed(self):
        data = json.loads(self.manifest.read_text())
        data['end'] = '2099-01-01'
        self.manifest.write_text(json.dumps(data))
        with self.assertRaises(ValueError): self.run_cycle()
        status = run_research(None, self.state, self.output, self.report)
        self.assertEqual(status['status'], 'waiting_for_price_history')
        self.assertEqual(status['trials_reserved'], 0)

    @patch('src.research.runner.execute_trial', return_value=completed())
    def test_dashboard_has_plain_progress_not_model_ids_or_confidence_claims(self, execute):
        self.run_cycle()
        html = render_algorithm_research_card(self.output)
        self.assertIn('실험 평가 2개', html)
        self.assertIn('과거 비교 기준 통과 0개', html)
        self.assertIn('LLM 미연결', html)
        self.assertIn('운영 모델 미반영', html)
        self.assertNotIn('linear', html)
        self.assertNotIn('hgb_shallow', html)
        data = json.loads(self.output.read_text())
        data['production_promotion'] = True
        self.output.write_text(json.dumps(data))
        self.assertIn('연구 상태 점검 필요', render_algorithm_research_card(self.output))

    def test_interrupted_reservation_never_restarts_or_disappears(self):
        with patch('src.research.runner.execute_trial', side_effect=RuntimeError('interrupted')):
            with self.assertRaises(RuntimeError): self.run_cycle()
        with patch('src.research.runner.execute_trial') as execute:
            status = self.run_cycle()
            self.assertEqual(status['status'], 'interrupted_research_requires_review')
            self.assertEqual(status['trials_incomplete'], 1)
            execute.assert_not_called()

    @patch('src.research.runner.execute_trial', return_value=completed())
    def test_imported_numerical_program_is_validated_and_only_one_trial(self, execute):
        self.assertEqual(self.run_cycle(proposal=program())['trials_reserved'], 1)
        self.assertEqual(execute.call_count, 1)

    def test_worker_time_budget_and_secrets_not_in_child_environment(self):
        with patch.dict('os.environ', {'KIS_APP_SECRET': 'test-secret', 'GH_TOKEN': 'test-token'}):
            with patch('src.research.runner.subprocess.run', side_effect=subprocess.TimeoutExpired('worker', 1)) as execute:
                result = execute_trial(self.data, '2026-10-28', program(), 'hash', 1)
        self.assertEqual(result['failure_type'], 'worker_time_budget_exceeded')
        environment = execute.call_args.kwargs['env']
        self.assertNotIn('KIS_APP_SECRET', environment)
        self.assertNotIn('GH_TOKEN', environment)
        self.assertNotIn('OPENAI_API_KEY', environment)
        self.assertEqual(execute.call_args.kwargs['timeout'], 1)

    def test_global_trial_budget_stops_new_experiments(self):
        with patch('src.research.runner.execute_trial', return_value=completed()):
            self.run_cycle()
        with locked_memory(self.state) as events:
            for number in range(118):
                append_event(self.state, events, 'proposal', {'program_id': str(number)})
        data = json.loads(self.manifest.read_text())
        data['end'] = '2026-10-29'
        self.manifest.write_text(json.dumps(data))
        with patch('src.research.runner.execute_trial') as execute:
            self.assertEqual(self.run_cycle()['status'], 'research_budget_requires_review')
            execute.assert_not_called()


if __name__ == '__main__':
    unittest.main()
