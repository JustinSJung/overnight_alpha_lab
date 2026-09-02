# 2026-09-02 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20260902.csv`

## Summary

- Absolute close T1 evaluated cases: 3410
- Absolute close T1 success rate: 42.64%
- Benchmark-adjusted T1 evaluated cases: 3410
- Benchmark-adjusted T1 success rate: 49.47%
- Pending cases: 4582
- Skipped cases: 0
- T3 return available: 6433
- T5 return available: 5739

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 128940 | 2026-08-21 | 29.96% | 28.04% |
| 351320 | 2026-08-21 | 29.95% | 28.03% |
| 488900 | 2026-08-07 | 29.93% | 21.29% |
| 950220 | 2026-08-19 | 29.88% | 27.17% |
| 044380 | 2026-08-28 | 20.15% | 19.74% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | -32.69% |
| 065770 | 2026-07-16 | -14.70% | -10.20% |
| 263750 | 2026-08-11 | -14.50% | -13.99% |
| 071200 | 2026-08-14 | -13.93% | -12.56% |
| 038530 | 2026-07-16 | -12.53% | -8.03% |