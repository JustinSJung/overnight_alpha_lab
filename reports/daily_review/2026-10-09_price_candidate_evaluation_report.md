# 2026-10-09 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261009.csv`

## Summary

- Absolute close T1 evaluated cases: 9547
- Absolute close T1 success rate: 46.73%
- Benchmark-adjusted T1 evaluated cases: 8072
- Benchmark-adjusted T1 success rate: 51.30%
- Pending cases: 12920
- Skipped cases: 0
- T3 return available: 19017
- T5 return available: 18164

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 128940 | 2026-08-21 | 29.96% | 28.04% |
| 351320 | 2026-08-21 | 29.95% | 28.03% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |
| 002720 | 2026-10-06 | 29.91% | 31.89% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | -32.69% |
| 006740 | 2026-10-07 | -20.67% | -18.00% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |
| 065770 | 2026-07-16 | -14.70% | 0.00% |