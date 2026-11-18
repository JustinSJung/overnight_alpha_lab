# 2026-11-18 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261118.csv`

## Summary

- Absolute close T1 evaluated cases: 24481
- Absolute close T1 success rate: 50.20%
- Benchmark-adjusted T1 evaluated cases: 18078
- Benchmark-adjusted T1 success rate: 50.71%
- Pending cases: 24573
- Skipped cases: 0
- T3 return available: 42932
- T5 return available: 40623

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 0.00% |
| 011330 | 2026-10-13 | 30.00% | 30.47% |
| 128940 | 2026-08-21 | 29.96% | 0.00% |
| 351320 | 2026-08-21 | 29.95% | 0.00% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | 0.00% |
| 418420 | 2026-11-13 | -21.69% | -19.47% |
| 192410 | 2026-11-03 | -19.80% | -13.82% |
| 278470 | 2026-10-12 | -19.60% | -18.49% |
| 005870 | 2026-11-03 | -16.44% | -10.75% |