# 2026-11-02 Price Candidate Evaluation

Source CSV: `data/predictions/price_candidate_evaluation_20261102.csv`

## Summary

- Absolute close T1 evaluated cases: 16060
- Absolute close T1 success rate: 48.85%
- Benchmark-adjusted T1 evaluated cases: 12857
- Benchmark-adjusted T1 success rate: 52.14%
- Pending cases: 19428
- Skipped cases: 0
- T3 return available: 30900
- T5 return available: 28986

Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.

## Top Success Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 042370 | 2026-09-16 | 30.00% | 30.08% |
| 011330 | 2026-10-13 | 30.00% | 30.47% |
| 351320 | 2026-08-21 | 29.95% | 0.00% |
| 488900 | 2026-08-07 | 29.93% | 0.00% |
| 220100 | 2026-10-22 | 29.91% | 32.15% |

## Top Failure Examples

| Stock | Candidate Date | T1 Return | Excess T1 |
|---|---|---:|---:|
| 006740 | 2026-10-07 | -22.25% | -19.58% |
| 278470 | 2026-10-12 | -19.60% | -18.49% |
| 017670 | 2026-07-27 | -16.04% | 0.00% |
| 012200 | 2026-09-22 | -15.31% | -16.44% |
| 065770 | 2026-07-16 | -14.70% | 0.00% |