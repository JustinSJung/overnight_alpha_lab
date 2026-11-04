# 2026-11-04 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261104.csv`

## Summary

- Absolute close T1 evaluated cases: 18095
- Absolute close T1 success rate: 49.25%
- Benchmark-adjusted T1 evaluated cases: 14256
- Benchmark-adjusted T1 success rate: 51.86%
- Pending cases: 19499
- Skipped cases: 0
- T3 return available: 32471
- T5 return available: 32419

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
| 288980 | 2026-08-19 | -29.98% | 0.00% |
| 006740 | 2026-10-07 | -22.25% | -19.58% |
| 278470 | 2026-10-12 | -19.60% | -18.49% |
| 067080 | 2026-10-08 | -18.91% | -15.08% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |