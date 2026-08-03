# 2026-08-03 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20260803.csv`

## Summary

- Absolute close T1 evaluated cases: 1441
- Absolute close T1 success rate: 45.18%
- Benchmark-adjusted T1 evaluated cases: 1441
- Benchmark-adjusted T1 success rate: 51.28%
- Pending cases: 1113
- Skipped cases: 0
- T3 return available: 1803
- T5 return available: 1435

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 465770 | 2026-07-16 | 29.98% | 37.12% |
| 189330 | 2026-07-07 | 29.97% | 36.64% |
| 465770 | 2026-07-13 | 29.92% | 32.75% |
| 236810 | 2026-07-31 | 12.55% | 9.49% |
| 012160 | 2026-07-13 | 12.10% | 11.27% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 189330 | 2026-07-10 | -18.56% | -14.26% |
| 036630 | 2026-07-10 | -17.25% | -7.48% |
| 017670 | 2026-07-27 | -16.04% | -4.85% |
| 263800 | 2026-07-10 | -16.03% | -11.73% |
| 465770 | 2026-07-15 | -14.84% | -9.51% |