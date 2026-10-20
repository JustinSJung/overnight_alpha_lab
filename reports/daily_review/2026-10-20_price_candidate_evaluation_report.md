# 2026-10-20 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261020.csv`

## Summary

- Absolute close T1 evaluated cases: 13047
- Absolute close T1 success rate: 48.28%
- Benchmark-adjusted T1 evaluated cases: 10864
- Benchmark-adjusted T1 success rate: 46.98%
- Pending cases: 15615
- Skipped cases: 0
- T3 return available: 24633
- T5 return available: 22878

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 011330 | 2026-10-13 | 30.00% | 30.47% |
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 128940 | 2026-08-21 | 29.96% | 28.04% |
| 351320 | 2026-08-21 | 29.95% | 28.03% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 214330 | 2026-10-19 | -24.61% | -21.00% |
| 006740 | 2026-10-07 | -22.25% | -19.58% |
| 278470 | 2026-10-12 | -19.60% | -18.49% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |