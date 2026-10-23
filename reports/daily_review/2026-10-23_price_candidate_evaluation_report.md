# 2026-10-23 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261023.csv`

## Summary

- Absolute close T1 evaluated cases: 14750
- Absolute close T1 success rate: 49.59%
- Benchmark-adjusted T1 evaluated cases: 12247
- Benchmark-adjusted T1 success rate: 47.33%
- Pending cases: 16722
- Skipped cases: 0
- T3 return available: 27701
- T5 return available: 25881

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 011330 | 2026-10-13 | 30.00% | 30.47% |
| 128940 | 2026-08-21 | 29.96% | 0.00% |
| 351320 | 2026-08-21 | 29.95% | 0.00% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 006740 | 2026-10-07 | -20.58% | -17.91% |
| 278470 | 2026-10-12 | -19.60% | -18.49% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |
| 065770 | 2026-07-16 | -14.70% | 0.00% |