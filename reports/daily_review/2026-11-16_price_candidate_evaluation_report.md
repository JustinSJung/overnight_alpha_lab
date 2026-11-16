# 2026-11-16 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261116.csv`

## Summary

- Absolute close T1 evaluated cases: 23552
- Absolute close T1 success rate: 49.44%
- Benchmark-adjusted T1 evaluated cases: 17458
- Benchmark-adjusted T1 success rate: 51.49%
- Pending cases: 23139
- Skipped cases: 0
- T3 return available: 40749
- T5 return available: 38486

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
| 006740 | 2026-10-07 | -22.25% | -19.58% |
| 192410 | 2026-11-03 | -19.80% | -13.82% |
| 278470 | 2026-10-12 | -19.60% | -18.49% |
| 005870 | 2026-11-03 | -16.44% | -10.75% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |