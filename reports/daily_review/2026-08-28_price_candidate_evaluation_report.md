# 2026-08-28 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20260828.csv`

## Summary

- Absolute close T1 evaluated cases: 3679
- Absolute close T1 success rate: 42.29%
- Benchmark-adjusted T1 evaluated cases: 3679
- Benchmark-adjusted T1 success rate: 49.82%
- Pending cases: 4107
- Skipped cases: 0
- T3 return available: 7023
- T5 return available: 6392

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 465770 | 2026-07-16 | 29.98% | 37.12% |
| 189330 | 2026-07-07 | 29.97% | 36.64% |
| 128940 | 2026-08-21 | 29.96% | 28.04% |
| 351320 | 2026-08-21 | 29.95% | 28.03% |
| 488900 | 2026-08-07 | 29.93% | 21.29% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | -32.69% |
| 189330 | 2026-07-10 | -18.56% | -14.26% |
| 036630 | 2026-07-10 | -17.25% | -7.48% |
| 017670 | 2026-07-27 | -16.04% | -4.85% |
| 263800 | 2026-07-10 | -16.03% | -11.73% |