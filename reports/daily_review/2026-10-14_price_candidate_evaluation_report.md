# 2026-10-14 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261014.csv`

## Summary

- Absolute close T1 evaluated cases: 10887
- Absolute close T1 success rate: 48.02%
- Benchmark-adjusted T1 evaluated cases: 8970
- Benchmark-adjusted T1 success rate: 50.01%
- Pending cases: 14211
- Skipped cases: 0
- T3 return available: 21612
- T5 return available: 19835

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 011330 | 2026-10-13 | 30.00% | 28.73% |
| 128940 | 2026-08-21 | 29.96% | 28.04% |
| 351320 | 2026-08-21 | 29.95% | 33.57% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | -32.69% |
| 006740 | 2026-10-07 | -20.58% | -17.91% |
| 278470 | 2026-10-12 | -19.60% | -18.49% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |