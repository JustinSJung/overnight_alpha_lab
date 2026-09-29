# V2 Performance Monitor - 2026-09-29

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **7692**
- V2 success count: **3624**
- V2 failure count: **4068**
- V2 raw success rate: **47.11%**
- V2 benchmark-adjusted evaluated cases: **6953**
- V2 benchmark-adjusted success rate: **51.04%**
- V2 benchmark coverage rate: **90.39%**
- V2 average close_t1_return: **0.17%**
- V2 average excess_t1_return: **0.14%**
- Selected-pick evaluated cases: **677**
- Selected-pick success rate: **45.20%**
- Non-selected evaluated cases: **7015**
- Non-selected success rate: **47.30%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 380 | 176 | 204 | 46.32% |
| Top 20 | 677 | 306 | 371 | 45.20% |
| Top 50 | 1047 | 459 | 588 | 43.84% |
| Top 100 | 1413 | 595 | 818 | 42.11% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1115 | 483 | 632 | 43.32% | -0.01% | -0.42% | -0.72% | 1069 | 44.71% |
| avoid | 6577 | 3141 | 3436 | 47.76% | 0.20% | 0.91% | 1.52% | 5884 | 52.19% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.