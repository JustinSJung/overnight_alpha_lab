# 2026-10-16 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261016.csv`

## Summary

- Absolute close T1 evaluated cases: 11948
- Absolute close T1 success rate: 48.08%
- Benchmark-adjusted T1 evaluated cases: 10082
- Benchmark-adjusted T1 success rate: 48.09%
- Pending cases: 14904
- Skipped cases: 0
- T3 return available: 22981
- T5 return available: 21214

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 011330 | 2026-10-13 | 30.00% | 30.47% |
| 128940 | 2026-08-21 | 29.96% | 28.04% |
| 351320 | 2026-08-21 | 29.95% | 33.57% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 006740 | 2026-10-07 | -22.25% | -19.58% |
| 278470 | 2026-10-12 | -19.60% | -18.49% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |
| 065770 | 2026-07-16 | -14.70% | 0.00% |