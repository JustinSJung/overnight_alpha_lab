# 2026-11-11 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261111.csv`

## Summary

- Absolute close T1 evaluated cases: 21365
- Absolute close T1 success rate: 49.94%
- Benchmark-adjusted T1 evaluated cases: 16283
- Benchmark-adjusted T1 success rate: 50.70%
- Pending cases: 21834
- Skipped cases: 0
- T3 return available: 37254
- T5 return available: 35049

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 011330 | 2026-10-13 | 30.00% | 30.47% |
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 128940 | 2026-08-21 | 29.96% | 0.00% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |
| 220100 | 2026-10-22 | 29.91% | 32.15% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | 0.00% |
| 006740 | 2026-10-07 | -22.25% | -19.58% |
| 192410 | 2026-11-03 | -19.80% | -13.82% |
| 278470 | 2026-10-12 | -19.60% | -18.49% |
| 005870 | 2026-11-03 | -16.44% | -10.75% |