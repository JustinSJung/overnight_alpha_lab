# V2 Performance Monitor - 2026-09-08

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **4062**
- V2 success count: **1749**
- V2 failure count: **2313**
- V2 raw success rate: **43.06%**
- V2 benchmark-adjusted evaluated cases: **4062**
- V2 benchmark-adjusted success rate: **50.57%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.48%**
- V2 average excess_t1_return: **-0.01%**
- Selected-pick evaluated cases: **457**
- Selected-pick success rate: **45.08%**
- Non-selected evaluated cases: **3605**
- Non-selected success rate: **42.80%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 268 | 127 | 141 | 47.39% |
| Top 20 | 457 | 206 | 251 | 45.08% |
| Top 50 | 672 | 290 | 382 | 43.15% |
| Top 100 | 994 | 399 | 595 | 40.14% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 707 | 298 | 409 | 42.15% | -0.12% | -0.55% | -1.02% | 707 | 42.86% |
| avoid | 3355 | 1451 | 1904 | 43.25% | 0.60% | 2.17% | 3.22% | 3355 | 52.19% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.