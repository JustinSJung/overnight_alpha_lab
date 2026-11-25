# 2026-11-25 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261125.csv`

## Summary

- Absolute close T1 evaluated cases: 27593
- Absolute close T1 success rate: 50.37%
- Benchmark-adjusted T1 evaluated cases: 20685
- Benchmark-adjusted T1 success rate: 52.41%
- Pending cases: 27515
- Skipped cases: 0
- T3 return available: 47963
- T5 return available: 45571

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 011330 | 2026-10-13 | 30.00% | 30.47% |
| 042370 | 2026-09-16 | 30.00% | 0.00% |
| 128940 | 2026-08-21 | 29.96% | 0.00% |
| 351320 | 2026-08-21 | 29.95% | 0.00% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | 0.00% |
| 054220 | 2026-11-16 | -28.63% | -30.71% |
| 096870 | 2026-11-19 | -22.95% | -19.75% |
| 006740 | 2026-10-07 | -22.25% | -19.58% |
| 418420 | 2026-11-13 | -21.69% | -19.47% |