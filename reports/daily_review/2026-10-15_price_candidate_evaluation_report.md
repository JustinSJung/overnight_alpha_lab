# 2026-10-15 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261015.csv`

## Summary

- Absolute close T1 evaluated cases: 11401
- Absolute close T1 success rate: 49.93%
- Benchmark-adjusted T1 evaluated cases: 9460
- Benchmark-adjusted T1 success rate: 47.28%
- Pending cases: 14577
- Skipped cases: 0
- T3 return available: 22518
- T5 return available: 20710

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 011330 | 2026-10-13 | 30.00% | 30.47% |
| 128940 | 2026-08-21 | 29.96% | 28.04% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |
| 002720 | 2026-10-06 | 29.91% | 31.89% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | -32.69% |
| 006740 | 2026-10-07 | -20.58% | -17.91% |
| 278470 | 2026-10-12 | -19.60% | -18.49% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |