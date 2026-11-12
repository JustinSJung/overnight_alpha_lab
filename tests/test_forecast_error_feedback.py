from pathlib import Path
import json
import tempfile
import unittest

import numpy as np
import pandas as pd

from src.crawler.market_clock import KST
from src.features.next_open_dataset import TARGET_VERSION
from src.models.forecast_error_feedback import PROB, describe_base, fit_feedback, predict_feedback, prepare
from src.pipeline.forecast_feedback_shadow import run


DAY = '2026-11-12'
CLOCK = pd.Timestamp(DAY + ' 18:00', tz=KST)


def pool():
    batches = []
    for date in [*pd.bdate_range('2026-10-12', periods=7), pd.Timestamp(DAY)]:
        code = np.arange(100)
        old = date != pd.Timestamp(DAY)
        issue = date.tz_localize(KST) + pd.Timedelta(hours=17)
        batches.append(pd.DataFrame(dict(
            prediction_id=[date.strftime('%Y%m%d') + str(i) for i in code],
            stock_code=[str(i).zfill(6) for i in code], signal_date=date, recorded_at=issue.isoformat(),
            probability_above_cost=.35 + (code // 5) / 100, validation_base_rate=.4,
            horizon_sessions=5, cost_assumption=.003, target_version=TARGET_VERSION,
            target=(code % 5 == 0).astype(float) if old else np.nan,
            label_available_date=date + pd.offsets.BDay(5) if old else pd.NaT)))
    return pd.concat(batches, ignore_index=True)


class TestForecastFeedback(unittest.TestCase):
    def test_signed_correction_can_reorder_peers_and_lower_overconfidence(self):
        f = prepare(pool(), DAY)
        state = fit_feedback(f, pd.Timestamp(DAY))
        q = f[f.signal_date.eq(DAY)]
        p = predict_feedback(q, state)
        self.assertEqual(state['dates'], 7)
        self.assertLess(state['offset'], 0)
        self.assertGreater(p.iloc[0], p.iloc[1])
        self.assertGreater(p.iloc[0], q[PROB].iloc[0])
        self.assertTrue(p.between(0, 1).all())
        self.assertLess(p.mean(), q[PROB].mean())

    def test_fit_cannot_use_future_labels_or_sparse_days(self):
        f = prepare(pool(), DAY)
        origin = pd.Timestamp('2026-10-21')
        state = fit_feedback(f, origin)
        altered = f.copy()
        late = altered.label_available_date.gt(origin)
        altered.loc[late, 'target'] = 1 - altered.loc[late, 'target']
        self.assertEqual(state, fit_feedback(altered, origin))
        self.assertFalse(state['ready'])
        self.assertTrue(predict_feedback(f, state).equals(f[PROB]))
        f.loc[f.stock_code.lt('000006'), 'target'] = np.nan
        self.assertEqual(fit_feedback(f, pd.Timestamp(DAY))['dates'], 0)

    def test_ranks_use_all_originals_before_outcome_filtering(self):
        rows = pool()
        rows.loc[rows.stock_code.ge('000080'), 'target'] = np.nan
        by_day = describe_base(prepare(rows, DAY))['rank_by_date'][0]
        self.assertEqual(by_day['top']['issued'], 20)
        self.assertEqual(by_day['top']['resolved'], 0)
        self.assertIsNone(by_day['top_minus_bottom'])

    def test_duplicates_wrong_target_and_unavailable_label_rejected(self):
        rows = pool()
        for broken in [pd.concat([rows, rows.iloc[:1]]), rows.assign(target_version='other'),
                       rows.assign(label_available_date=pd.Timestamp('2030-01-01'))]:
            with self.assertRaises(ValueError):
                prepare(broken, DAY)

    def test_freeze_once_and_only_score_same_future_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            rows = pool()
            launch = run(rows, DAY, tmp, CLOCK)
            self.assertEqual(launch['recording'], 'new_prospective_shadow')
            self.assertEqual(launch['prospective']['resolved'], 0)
            path = Path(tmp) / (DAY + '.json')
            original = path.read_bytes()
            self.assertEqual(run(rows.sample(frac=1), DAY, tmp, CLOCK)['recording'], 'first_batch_preserved')
            self.assertEqual(original, path.read_bytes())
            near = rows.signal_date.eq(DAY) & rows.stock_code.ne('000099')
            rows.loc[near, 'target'] = 1.
            rows.loc[near, 'label_available_date'] = pd.Timestamp('2026-11-19')
            later = run(rows, '2026-11-19', tmp, CLOCK + pd.Timedelta(days=7))
            comparison = later['prospective']
            self.assertEqual((comparison['issued'], comparison['resolved']), (100, 99))
            self.assertEqual(comparison['models'][PROB]['top_5']['resolved'], 4)
            self.assertEqual(comparison['models'][PROB]['at_least_60pct_top_5']['issued'], 0)
            self.assertIsNotNone(comparison['models']['shadow']['date_brier'])
            self.assertEqual(original, path.read_bytes())
            forged = json.loads(original)
            forged['payload']['predictions'][0] = .99
            path.write_text(json.dumps(forged))
            with self.assertRaises(ValueError):
                run(rows, '2026-11-19', tmp, CLOCK + pd.Timedelta(days=7))

    def test_no_late_original_no_backfill(self):
        with tempfile.TemporaryDirectory() as tmp:
            late = CLOCK + pd.Timedelta(days=1)
            self.assertEqual(run(pool(), DAY, tmp, late)['recording'], 'outside_recording_window')
            self.assertEqual(run(pool(), '2026-11-13', tmp, late)['recording'], 'no_timely_primary_original')
            self.assertEqual(list(Path(tmp).iterdir()), [])
