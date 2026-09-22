# 2026-09-22 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20260922.csv`

## Summary

- Absolute close T1 evaluated cases: 6945
- Absolute close T1 success rate: 45.85%
- Benchmark-adjusted T1 evaluated cases: 6577
- Benchmark-adjusted T1 success rate: 51.79%
- Pending cases: 8819
- Skipped cases: 0
- T3 return available: 13786
- T5 return available: 12360

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 128940 | 2026-08-21 | 29.96% | 28.04% |
| 488900 | 2026-08-07 | 29.93% | 21.29% |
| 950220 | 2026-08-19 | 29.88% | 27.17% |
| 321370 | 2026-09-16 | 20.69% | 20.51% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 017670 | 2026-07-27 | -16.04% | -4.85% |
| 065770 | 2026-07-16 | -14.70% | 0.00% |
| 263750 | 2026-08-11 | -14.50% | -13.99% |
| 071200 | 2026-08-14 | -13.93% | -12.56% |
| 440110 | 2026-09-10 | -13.62% | -9.97% |