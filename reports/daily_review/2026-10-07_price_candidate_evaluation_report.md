# 2026-10-07 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261007.csv`

## Summary

- Absolute close T1 evaluated cases: 9253
- Absolute close T1 success rate: 46.35%
- Benchmark-adjusted T1 evaluated cases: 7832
- Benchmark-adjusted T1 success rate: 51.53%
- Pending cases: 12318
- Skipped cases: 0
- T3 return available: 18196
- T5 return available: 17359

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 128940 | 2026-08-21 | 29.96% | 28.04% |
| 351320 | 2026-08-21 | 29.95% | 28.03% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |
| 950220 | 2026-08-19 | 29.88% | 27.17% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |
| 065770 | 2026-07-16 | -14.70% | 0.00% |
| 263750 | 2026-08-11 | -14.50% | -13.99% |
| 071200 | 2026-08-14 | -13.93% | -12.56% |