# 2026-08-17 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20260817.csv`

## Summary

- Absolute close T1 evaluated cases: 2415
- Absolute close T1 success rate: 41.90%
- Benchmark-adjusted T1 evaluated cases: 2415
- Benchmark-adjusted T1 success rate: 51.22%
- Pending cases: 2902
- Skipped cases: 0
- T3 return available: 4110
- T5 return available: 3601

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 465770 | 2026-07-16 | 29.98% | 37.12% |
| 189330 | 2026-07-07 | 29.97% | 36.64% |
| 488900 | 2026-08-07 | 29.93% | 21.29% |
| 465770 | 2026-07-13 | 29.92% | 32.75% |
| 019570 | 2026-08-07 | 17.95% | 17.77% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 189330 | 2026-07-10 | -18.56% | -14.26% |
| 036630 | 2026-07-10 | -17.25% | -7.48% |
| 017670 | 2026-07-27 | -16.04% | -4.85% |
| 263800 | 2026-07-10 | -16.03% | -11.73% |
| 348370 | 2026-07-16 | -15.22% | -8.08% |