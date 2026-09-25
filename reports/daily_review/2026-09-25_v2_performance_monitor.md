# V2 Performance Monitor - 2026-09-25

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **7320**
- V2 success count: **3381**
- V2 failure count: **3939**
- V2 raw success rate: **46.19%**
- V2 benchmark-adjusted evaluated cases: **6982**
- V2 benchmark-adjusted success rate: **51.56%**
- V2 benchmark coverage rate: **95.38%**
- V2 average close_t1_return: **0.23%**
- V2 average excess_t1_return: **-0.07%**
- Selected-pick evaluated cases: **660**
- Selected-pick success rate: **45.00%**
- Non-selected evaluated cases: **6660**
- Non-selected success rate: **46.31%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 371 | 171 | 200 | 46.09% |
| Top 20 | 660 | 297 | 363 | 45.00% |
| Top 50 | 1007 | 446 | 561 | 44.29% |
| Top 100 | 1360 | 574 | 786 | 42.21% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1040 | 452 | 588 | 43.46% | -0.03% | -0.52% | -0.88% | 1020 | 44.41% |
| avoid | 6280 | 2929 | 3351 | 46.64% | 0.27% | 1.11% | 1.70% | 5962 | 52.78% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.