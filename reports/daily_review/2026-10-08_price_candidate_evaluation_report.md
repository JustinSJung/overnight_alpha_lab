# 2026-10-08 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261008.csv`

## Summary

- Absolute close T1 evaluated cases: 9667
- Absolute close T1 success rate: 46.65%
- Benchmark-adjusted T1 evaluated cases: 8182
- Benchmark-adjusted T1 success rate: 51.26%
- Pending cases: 12800
- Skipped cases: 0
- T3 return available: 19251
- T5 return available: 18398

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |
| 002720 | 2026-10-06 | 29.91% | 31.89% |
| 950220 | 2026-08-19 | 29.88% | 27.17% |
| 321370 | 2026-09-16 | 20.69% | 20.51% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |
| 065770 | 2026-07-16 | -14.70% | 0.00% |
| 263750 | 2026-08-11 | -14.50% | -13.99% |
| 071200 | 2026-08-14 | -13.93% | -12.56% |