# 2026-10-05 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261005.csv`

## Summary

- Absolute close T1 evaluated cases: 8678
- Absolute close T1 success rate: 46.60%
- Benchmark-adjusted T1 evaluated cases: 7303
- Benchmark-adjusted T1 success rate: 52.66%
- Pending cases: 11151
- Skipped cases: 0
- T3 return available: 17634
- T5 return available: 16038

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 128940 | 2026-08-21 | 29.96% | 28.04% |
| 351320 | 2026-08-21 | 29.95% | 28.03% |
| 488900 | 2026-08-07 | 29.93% | 21.29% |
| 950220 | 2026-08-19 | 29.88% | 27.17% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | -32.69% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |
| 065770 | 2026-07-16 | -14.70% | 0.00% |
| 263750 | 2026-08-11 | -14.50% | -13.99% |