# 2026-10-21 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261021.csv`

## Summary

- Absolute close T1 evaluated cases: 13912
- Absolute close T1 success rate: 47.95%
- Benchmark-adjusted T1 evaluated cases: 11396
- Benchmark-adjusted T1 success rate: 48.52%
- Pending cases: 15684
- Skipped cases: 0
- T3 return available: 26110
- T5 return available: 24348

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 011330 | 2026-10-13 | 30.00% | 30.47% |
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 128940 | 2026-08-21 | 29.96% | 0.00% |
| 351320 | 2026-08-21 | 29.95% | 0.00% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | 0.00% |
| 006740 | 2026-10-07 | -22.25% | -19.58% |
| 278470 | 2026-10-12 | -17.37% | -16.26% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |