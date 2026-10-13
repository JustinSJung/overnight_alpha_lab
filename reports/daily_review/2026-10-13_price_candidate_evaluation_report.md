# 2026-10-13 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261013.csv`

## Summary

- Absolute close T1 evaluated cases: 10378
- Absolute close T1 success rate: 48.81%
- Benchmark-adjusted T1 evaluated cases: 8517
- Benchmark-adjusted T1 success rate: 49.98%
- Pending cases: 13852
- Skipped cases: 0
- T3 return available: 20800
- T5 return available: 19055

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 128940 | 2026-08-21 | 29.96% | 28.04% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |
| 002720 | 2026-10-06 | 29.91% | 31.89% |
| 950220 | 2026-08-19 | 29.88% | 27.17% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 288980 | 2026-08-19 | -29.98% | -32.69% |
| 006740 | 2026-10-07 | -22.25% | -19.58% |
| 278470 | 2026-10-12 | -19.46% | -15.18% |
| 067080 | 2026-10-08 | -18.91% | -15.08% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |