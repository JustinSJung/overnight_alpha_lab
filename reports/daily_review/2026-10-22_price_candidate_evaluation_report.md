# 2026-10-22 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261022.csv`

## Summary

- Absolute close T1 evaluated cases: 14303
- Absolute close T1 success rate: 48.16%
- Benchmark-adjusted T1 evaluated cases: 11825
- Benchmark-adjusted T1 success rate: 47.97%
- Pending cases: 16220
- Skipped cases: 0
- T3 return available: 26658
- T5 return available: 24866

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 011330 | 2026-10-13 | 30.00% | 30.47% |
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 128940 | 2026-08-21 | 29.96% | 0.00% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |
| 002720 | 2026-10-06 | 29.91% | 31.89% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 006740 | 2026-10-07 | -20.58% | -17.91% |
| 278470 | 2026-10-12 | -19.60% | -13.35% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |
| 065770 | 2026-07-16 | -14.70% | 0.00% |