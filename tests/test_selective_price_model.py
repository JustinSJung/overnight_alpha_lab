import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from test_market_context_experiment import panel
from src.crawler.market_clock import KST
from src.features.next_open_dataset import build_next_open_dataset
from src.models.selected_price_model import COLUMNS, ROOT, prepare_selected_features
from src.models.selective_price_model import (
    ARMS, GATE_COLUMNS, add_feedback, base_features, evaluate_gate, fit_gate,
    fit_month_base, freeze_selective, gate_predictions, grade_selective, load_gate,
    paired_success, run_experiment, selection_masks, validate_replay,
)


def protocol():
    p = json.loads((ROOT / 'docs/model_experiments/selective_price_protocol_20261023.json').read_text())
    p.update(base_training_sessions=15, base_calibration_sessions=3,
             gate_training_sessions=15, gate_calibration_sessions=3,
             feedback_sessions=4, bootstrap_samples=100)
    return p


class SelectivePriceModelTests(unittest.TestCase):
    def inputs(self):
        return prepare_selected_features(panel(), COLUMNS)

    def test_feedback_uses_only_mature_past_answers_and_keeps_missing_coverage(self):
        days = pd.bdate_range('2026-01-05', periods=12)
        history = pd.DataFrame(dict(stock_code=['000001'] * 6, signal_date=days[:6],
                                    prediction_asof=days[:6] - pd.Timedelta(days=1),
                                    base_latest_label=days[:6] - pd.Timedelta(days=1),
                                    expected_target_date=days[3:9], label_available_date=days[3:9],
                                    target=[1., 0., np.nan, 1., 0., 1.], monthly_base=.6))
        query = pd.DataFrame({name: [0.] for name in GATE_COLUMNS})
        query['signal_date'] = days[6]
        before = add_feedback(query, history, 20)
        self.assertAlmostEqual(before.recent_bias.iloc[0], -.1)
        self.assertAlmostEqual(before.feedback_coverage.iloc[0], 2 / 3)
        changed = history.copy()
        changed.loc[changed.label_available_date.ge(days[6]), 'target'] = 1000
        after = add_feedback(query, changed, 20)
        pd.testing.assert_frame_equal(before, after)
        bad = history.copy()
        bad.loc[0, 'base_latest_label'] = days[11]
        with self.assertRaises(ValueError):
            add_feedback(query, bad, 20)

    def test_equal_budgets_and_unknown_picks_are_not_replaced(self):
        frame = pd.DataFrame(dict(stock_code=[str(i).zfill(6) for i in range(8)],
                                  signal_date=pd.Timestamp('2026-07-01'),
                                  monthly_base=np.arange(8) / 10 + .1,
                                  probability_only=np.arange(8) / 10 + .1,
                                  learned_gate=np.arange(8)[::-1] / 10 + .1,
                                  target=[np.nan, 1, 1, 0, 1, 0, 0, 1],
                                  net_return_proxy=[np.nan, .1, .1, -.1, .1, -.1, -.1, .1],
                                  label_status=['exit_price_unavailable'] + ['resolved'] * 7))
        p = protocol()
        masks = selection_masks(frame, p)
        for arm in ARMS:
            self.assertEqual(masks['top5_' + arm].sum(), 5)
            self.assertEqual(masks['matched_policy_' + arm].sum(), 3)
        changed = frame.copy()
        changed['target'] = 0
        for name, mask in selection_masks(changed, p).items():
            np.testing.assert_array_equal(mask, masks[name])
        metrics = evaluate_gate(frame, p)
        selected = metrics['selections']['top5_learned_gate']
        self.assertEqual(selected['unresolved_cases'], 1)
        self.assertIsNone(selected['all_date_net_return_proxy'])

    def test_gate_fit_cannot_learn_future_answers(self):
        inputs = self.inputs()
        days = sorted(inputs.signal_date.unique())
        cohort, _ = build_next_open_dataset(inputs, days[-1])
        base, _ = fit_month_base(cohort, days[65], protocol())
        replay = base_features(base, cohort[cohort.signal_date.gt(days[65])])
        replay = add_feedback(replay, replay, 4)
        before = fit_gate(replay, days[110], protocol())
        changed = replay.copy()
        future = changed.label_available_date.gt(days[110])
        changed.loc[future, 'target'] = 1 - changed.loc[future, 'target']
        changed.loc[future, 'target_return'] = 999
        after = fit_gate(changed, days[110], protocol())
        query = replay[replay.signal_date.gt(days[110])]
        np.testing.assert_allclose(gate_predictions(before, query)[ARMS], gate_predictions(after, query)[ARMS])

    def test_paired_intervals_do_not_certify_incomplete_period(self):
        dates = pd.bdate_range('2026-01-01', periods=30)
        frame = pd.DataFrame(dict(signal_date=np.repeat(dates, 2), target=np.tile([1., 0.], 30)))
        left, right = np.tile([True, False], 30), np.tile([False, True], 30)
        frame.loc[0, 'target'] = np.nan
        result = paired_success(frame, left, right, protocol())
        self.assertEqual(result['paired_complete_dates'], 29)
        self.assertIsNotNone(result['family_adjusted_lower'])
        self.assertIsNone(result['complete_period_lower'])

    def test_monthly_base_and_gate_are_out_of_time_and_roundtrip(self):
        inputs = self.inputs()
        days = sorted(inputs.signal_date.unique())
        p = protocol()
        p.update(labels_as_of=str(pd.Timestamp(days[-1]).date()), replay_start='2023-04-03',
                 evaluation_start='2023-06-01', periods={'primary_development': ['2023-06-01', str(pd.Timestamp(days[-1]).date())]})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'source').mkdir()
            (root / 'source/history_manifest.json').write_text('{}')
            with patch('src.models.selective_price_model.load_inputs', return_value=(inputs, {})), patch('builtins.print'):
                summary = run_experiment(root / 'source', root / 'model', p, root / 'report.md')
            self.assertFalse(summary['recommendation_gate_passed'])
            bundle = load_gate(root / 'model')
            self.assertFalse(bundle['metadata']['recommendation_enabled'])
            validate_replay(bundle['feedback_history'])
            for row in summary['fits']['base'] + summary['fits']['gate']:
                self.assertLess(pd.Timestamp(row['train']['latest_label']), pd.Timestamp(row['calibration']['start']))
                self.assertLessEqual(pd.Timestamp(row['calibration']['latest_label']), pd.Timestamp(row['as_of']))
            current = bundle['feedback_history'].tail(8)
            before = gate_predictions(bundle['gate'], current)
            changed = current.copy()
            changed[['target', 'target_return']] = 999
            after = gate_predictions(bundle['gate'], changed)
            np.testing.assert_allclose(before[ARMS], after[ARMS])
            with (Path(summary['run_dir']) / 'model.joblib').open('ab') as handle:
                handle.write(b'tamper')
            with self.assertRaises(ValueError):
                load_gate(root / 'model')

    def test_freeze_is_timely_immutable_and_grade_uses_original_controls(self):
        inputs = self.inputs()
        days = sorted(inputs.signal_date.unique())
        origin = pd.Timestamp(days[110])
        now = origin.tz_localize(KST) + pd.Timedelta(hours=17)
        predictions = pd.DataFrame(dict(stock_code=['000001', '000002'], signal_date=origin,
                                       origin_close=100., probability_monthly_base=[.8, .7],
                                       probability_probability_only=[.6, .5],
                                       probability_learned_gate=[.9, .6], probability_above_cost=[.9, .6],
                                       recommendation='ABSTAIN'))
        scoring = predictions.rename(columns={f'probability_{name}': name for name in ARMS})
        for name, mask in selection_masks(scoring, protocol()).items():
            predictions[name] = mask
        metadata = dict(dataset_sha256='b' * 64, trained_at=(now - pd.Timedelta(minutes=10)).isoformat(),
                        baseline_probability=.5)
        with tempfile.TemporaryDirectory() as directory, patch('src.models.selective_price_model.current_predictions', return_value=predictions):
            root = Path(directory)
            (root / 'history_manifest.json').write_text('{}')
            frozen = freeze_selective({'metadata': metadata}, root, root, now)
            path = Path(frozen['ledger'])
            original = path.read_bytes()
            with self.assertRaises(FileExistsError):
                freeze_selective({'metadata': metadata}, root, root, now)
            with self.assertRaises(ValueError):
                freeze_selective({'metadata': metadata}, root, root, now + pd.Timedelta(days=1))
            frame, summary = grade_selective(path, inputs, days[-1], protocol(),
                                             pd.Timestamp(days[-1], tz=KST) + pd.Timedelta(hours=17))
            self.assertEqual(summary['evaluated_cases'], 2)
            self.assertEqual(set(summary['shadow_models']), set(ARMS))
            self.assertEqual(path.read_bytes(), original)
            path.write_bytes(original + b'\n')
            with self.assertRaises(ValueError):
                grade_selective(path, inputs, days[-1], protocol(), now)

    def test_freeze_rechecks_real_clock_after_inference(self):
        origin = pd.Timestamp('2026-10-22')
        first = origin.tz_localize(KST) + pd.Timedelta(hours=17)
        late = first + pd.Timedelta(hours=16)
        predictions = pd.DataFrame({'stock_code': ['005930'], 'signal_date': [origin]})
        with tempfile.TemporaryDirectory() as directory, \
                patch('src.models.selective_price_model.current_predictions', return_value=predictions), \
                patch('src.models.selective_price_model.datetime') as clock:
            clock.now.side_effect = [first, late]
            with self.assertRaises(ValueError):
                freeze_selective({}, '/unused', directory)
            self.assertEqual(list(Path(directory).iterdir()), [])


if __name__ == '__main__':
    unittest.main()
