# 2026-11-27 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261127.csv`

## Summary

- Absolute close T1 evaluated cases: 28806
- Absolute close T1 success rate: 50.57%
- Benchmark-adjusted T1 evaluated cases: 22170
- Benchmark-adjusted T1 success rate: 51.81%
- Pending cases: 28775
- Skipped cases: 0
- T3 return available: 49762
- T5 return available: 47334

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 011330 | 2026-10-13 | 30.00% | 30.47% |
| 042370 | 2026-09-16 | 30.00% | 0.00% |
| 128940 | 2026-08-21 | 29.96% | 0.00% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |
| 220100 | 2026-10-22 | 29.91% | 32.15% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | 0.00% |
| 054220 | 2026-11-16 | -27.61% | -29.69% |
| 096870 | 2026-11-19 | -22.95% | -19.75% |
| 418420 | 2026-11-13 | -21.69% | -19.47% |
| 192410 | 2026-11-03 | -21.02% | -15.04% |