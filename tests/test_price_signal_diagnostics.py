import unittest
from unittest.mock import patch

import pandas as pd

from src.report_generator import price_signal_diagnostics_report as report


class PriceSignalDiagnosticsTests(unittest.TestCase):
    def build(self, evaluations):
        candidates = evaluations.drop_duplicates(['stock_code', 'signal_date'])

        def read_all(directory, pattern):
            if pattern.startswith('price_candidate_evaluation_'):
                return evaluations.copy()
            if pattern.startswith('price_based_candidates_'):
                return candidates.copy()
            return pd.DataFrame()

        with patch.object(report, 'read_all_csv', side_effect=read_all), patch.object(
            report, 'read_csv', return_value=candidates
        ):
            return report.build_diagnostics()

    def test_repeat_snapshots_do_not_inflate_counts_or_daily_top_buckets(self):
        rows = []
        for day in ['2026-10-01', '2026-10-02']:
            for rank in range(1, 13):
                rows.append({
                    'stock_code': str(rank).zfill(6),
                    'signal_date': day,
                    'prediction_date': day,
                    'score_version': 'v2_conservative_ranker',
                    'final_price_signal_score_v2': 100 - rank,
                    'volume_ratio_20d': 1.5,
                    'success_close_t1': 'pending' if rank == 1 else (
                        'success' if rank % 2 == 0 else 'failure'
                    ),
                    'evaluated_at': '2026-10-03',
                    'source_file': 'evaluation_20261003.csv',
                })
        original = pd.DataFrame(rows)
        baseline = self.build(original)
        snapshots = [original]
        for day in ['2026-10-04', '2026-10-05', '2026-10-06']:
            snapshots.append(original.assign(evaluated_at=day, source_file=day))
        repeated = self.build(pd.concat(snapshots, ignore_index=True))
        for field in ['evaluated_count', 'success_count', 'failure_count',
                      'pending_count', 'raw_success_rate', 'wilson_reliability_score']:
            self.assertEqual(baseline['summary'][field], repeated['summary'][field])
        self.assertEqual(repeated['summary']['evaluated_count'], 22)
        self.assertEqual(repeated['summary']['top_10_evaluated_count'], 18)
        self.assertEqual(baseline['rank_rows'], repeated['rank_rows'])

    def test_latest_snapshot_and_shared_result_normalization(self):
        original = pd.DataFrame([{
            'stock_code': '005930', 'signal_date': '2026-10-01',
            'prediction_date': '2026-10-01', 'score_version': 'v2_conservative_ranker',
            'final_price_signal_score_v2': 60, 'volume_ratio_20d': 1,
            'success_close_t1': 'pending', 'evaluated_at': '2026-10-01',
        }])
        resolved = original.assign(success_close_t1=' SUCCESS ', evaluated_at='2026-10-02')
        result = self.build(pd.concat([original, resolved], ignore_index=True))
        self.assertEqual(result['summary']['evaluated_count'], 1)
        self.assertEqual(result['summary']['success_count'], 1)
        self.assertEqual(result['summary']['pending_count'], 0)


if __name__ == '__main__':
    unittest.main()
