import importlib.util
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
from src.models.pairwise_price_model import (
    ARMS, CONTEXT, PRIMARY, RANK_COLUMNS, calibrated_probability, cross_section_inputs,
    evaluate_rank, fit_models, fit_monotone_calibration, freeze, grade_original, load_model,
    predict_models, save_run, selection_masks, training_pairs,
)
from src.models.selected_price_model import COLUMNS, ROOT, prepare_selected_features


def protocol():
    p = json.loads((ROOT / 'docs/model_experiments/pairwise_price_protocol_20261026.json').read_text())
    p.update(training_sessions=15, calibration_sessions=3, iterations=4, depth=2,
             pairs_per_date=12, bootstrap_samples=100)
    return p


class PairwiseInputsTests(unittest.TestCase):
    def inputs(self):
        inputs = prepare_selected_features(panel(), COLUMNS)
        return build_next_open_dataset(inputs, inputs.signal_date.max())[0]

    def test_cross_section_ranks_do_not_depend_on_future_answers(self):
        frame = self.inputs()
        before = cross_section_inputs(frame)
        altered = frame.copy()
        altered[['target', 'target_return']] = 999
        after = cross_section_inputs(altered)
        pd.testing.assert_frame_equal(before[['stock_code', 'signal_date'] + RANK_COLUMNS + CONTEXT],
                                      after[['stock_code', 'signal_date'] + RANK_COLUMNS + CONTEXT])
        self.assertEqual(len(before), len(frame))
        self.assertTrue(before[RANK_COLUMNS].ge(-1).all(axis=None))
        self.assertTrue(before[RANK_COLUMNS].le(1).all(axis=None))
        with self.assertRaises(ValueError):
            cross_section_inputs(pd.concat([frame, frame.iloc[:1]]))

    def test_training_pairs_are_same_day_reproducible_and_date_equal(self):
        frame = pd.DataFrame(dict(signal_date=np.repeat(pd.to_datetime(['2026-01-02', '2026-01-05']), [6, 4]),
                                  stock_code=[str(i).zfill(6) for i in range(10)], target=[1, 1, 1, 0, 0, 0, 1, 0, 0, 0]))
        ordered, pairs, weights, dates = training_pairs(frame, 5, 42)
        self.assertEqual(dates, 2)
        self.assertTrue((ordered.iloc[pairs[:, 0]].signal_date.to_numpy() == ordered.iloc[pairs[:, 1]].signal_date.to_numpy()).all())
        self.assertTrue(ordered.iloc[pairs[:, 0]].target.eq(1).all())
        self.assertTrue(ordered.iloc[pairs[:, 1]].target.eq(0).all())
        self.assertEqual(len(np.unique(pairs, axis=0)), len(pairs))
        mass = pd.Series(weights).groupby(ordered.iloc[pairs[:, 0]].signal_date.to_numpy()).sum()
        self.assertAlmostEqual(mass.iloc[0], mass.iloc[1])
        _, other, other_weights, _ = training_pairs(frame.sample(frac=1, random_state=4), 5, 42)
        np.testing.assert_array_equal(pairs, other)
        np.testing.assert_allclose(weights, other_weights)

    def test_probability_calibration_is_monotone_and_uses_no_future_labels(self):
        n = 80
        score = np.linspace(-2, 2, n)
        frame = pd.DataFrame({name: np.zeros(n) for name in CONTEXT})
        frame['signal_date'] = pd.Timestamp('2026-01-02')
        frame['label_available_date'] = pd.Timestamp('2026-01-09')
        frame['target'] = (score < 0).astype(int)
        cal = fit_monotone_calibration(score, frame, .05)
        self.assertGreaterEqual(cal['own_score_slope'], 0)
        query = frame.assign(signal_date=pd.Timestamp('2026-01-12'))
        probability = calibrated_probability(cal, score, query)
        self.assertTrue((np.diff(probability) >= -1e-12).all())
        with self.assertRaises(ValueError):
            calibrated_probability(cal, score, frame)
        changed = query.assign(target=999)
        np.testing.assert_allclose(probability, calibrated_probability(cal, score, changed))

    def test_equal_selection_budgets_do_not_remove_unknown_outcomes(self):
        frame = pd.DataFrame(dict(stock_code=[str(i).zfill(6) for i in range(8)],
                                  signal_date=pd.Timestamp('2026-07-01'),
                                  target=[np.nan, 1, 0, 1, 0, 1, 0, 0],
                                  net_return_proxy=[np.nan, .1, -.1, .1, -.1, .1, -.1, -.1],
                                  label_status=['exit_price_unavailable'] + ['resolved'] * 7))
        for name in ARMS:
            frame['score_' + name] = np.arange(8)[::-1]
            frame['probability_' + name] = np.arange(8)[::-1] / 10 + .1
        masks = selection_masks(frame, protocol())
        for name in ARMS:
            self.assertEqual(masks['top5_' + name].sum(), 5)
            self.assertEqual(masks['matched_policy_' + name].sum(), 3)
        changed = frame.assign(target=0)
        for name, mask in selection_masks(changed, protocol()).items():
            np.testing.assert_array_equal(mask, masks[name])
        metrics = evaluate_rank(frame, protocol())
        self.assertEqual(metrics['selections']['top5_' + PRIMARY]['unresolved_cases'], 1)
        self.assertIsNone(metrics['selections']['top5_' + PRIMARY]['all_date_net_return_proxy'])

    def test_original_is_timely_immutable_and_all_controls_grade(self):
        inputs = prepare_selected_features(panel(), COLUMNS)
        days = sorted(inputs.signal_date.unique())
        origin = pd.Timestamp(days[110])
        now = origin.tz_localize(KST) + pd.Timedelta(hours=17)
        frame = pd.DataFrame(dict(stock_code=['000001', '000002'], signal_date=origin, origin_close=100.))
        for name in ARMS:
            frame['score_' + name] = [1., 0.]
            frame['probability_' + name] = [.7, .5]
        for name, mask in selection_masks(frame, protocol()).items():
            frame[name] = mask
        frame['probability_above_cost'] = frame['probability_' + PRIMARY]
        metadata = dict(dataset_sha256='a' * 64, trained_at=(now - pd.Timedelta(minutes=1)).isoformat(), baseline_probability=.5)
        with tempfile.TemporaryDirectory() as directory, patch('src.models.pairwise_price_model.current_predictions', return_value=frame):
            root = Path(directory)
            (root / 'history_manifest.json').write_text('{}')
            saved = freeze({'metadata': metadata}, root, root, now)
            path = Path(saved['ledger'])
            original = path.read_bytes()
            with self.assertRaises(FileExistsError):
                freeze({'metadata': metadata}, root, root, now)
            with self.assertRaises(ValueError):
                freeze({'metadata': metadata}, root, root, now + pd.Timedelta(days=1))
            _, summary = grade_original(path, inputs, days[-1], protocol(), pd.Timestamp(days[-1], tz=KST) + pd.Timedelta(hours=17))
            self.assertEqual(summary['evaluated_cases'], 2)
            self.assertEqual(set(summary['shadow_models']), set(ARMS))
            self.assertEqual(path.read_bytes(), original)
            path.write_bytes(original + b'\n')
            with self.assertRaises(ValueError):
                grade_original(path, inputs, days[-1], protocol(), now)

    def test_live_clock_is_rechecked_after_prediction(self):
        origin = pd.Timestamp('2026-10-22')
        first = origin.tz_localize(KST) + pd.Timedelta(hours=17)
        late = first + pd.Timedelta(hours=16)
        frame = pd.DataFrame({'stock_code': ['005930'], 'signal_date': [origin]})
        with tempfile.TemporaryDirectory() as directory, patch('src.models.pairwise_price_model.current_predictions', return_value=frame), \
                patch('src.models.pairwise_price_model.datetime') as clock:
            clock.now.side_effect = [first, late]
            with self.assertRaises(ValueError):
                freeze({}, '/unused', directory)
            self.assertEqual(list(Path(directory).iterdir()), [])

    @unittest.skipUnless(importlib.util.find_spec('catboost'), 'optional isolated CatBoost runtime')
    def test_real_engine_roundtrip_purge_and_future_answer_invariance(self):
        frame = cross_section_inputs(self.inputs())
        days = sorted(frame.signal_date.unique())
        as_of = pd.Timestamp(days[60])
        bundle, audit = fit_models(frame, as_of, protocol())
        self.assertLess(pd.Timestamp(audit['train']['latest_label']), pd.Timestamp(audit['calibration']['start']))
        self.assertLessEqual(pd.Timestamp(audit['calibration']['latest_label']), as_of)
        query = frame[frame.signal_date.gt(as_of)].copy()
        before = predict_models(bundle, query)
        altered = frame.copy()
        future = altered.label_available_date.gt(as_of)
        altered.loc[future, 'target'] = 1 - altered.loc[future, 'target']
        other, _ = fit_models(altered, as_of, protocol())
        after = predict_models(other, query)
        cols = ['score_' + name for name in ARMS] + ['probability_' + name for name in ARMS]
        np.testing.assert_allclose(before[cols], after[cols], rtol=0, atol=1e-12)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'history_manifest.json').write_text('{}')
            saved = save_run(bundle, root, frame, as_of, protocol(), root / 'model', audit)
            loaded = load_model(root / 'model')
            np.testing.assert_allclose(before[cols], predict_models(loaded, query)[cols])
            with (Path(saved['run_dir']) / 'model.joblib').open('ab') as handle:
                handle.write(b'tampered')
            with self.assertRaises(ValueError):
                load_model(root / 'model')


if __name__ == '__main__':
    unittest.main()
