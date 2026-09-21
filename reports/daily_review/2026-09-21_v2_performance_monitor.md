# V2 Performance Monitor - 2026-09-21

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **6523**
- V2 success count: **2987**
- V2 failure count: **3536**
- V2 raw success rate: **45.79%**
- V2 benchmark-adjusted evaluated cases: **6374**
- V2 benchmark-adjusted success rate: **50.53%**
- V2 benchmark coverage rate: **97.72%**
- V2 average close_t1_return: **0.26%**
- V2 average excess_t1_return: **0.01%**
- Selected-pick evaluated cases: **607**
- Selected-pick success rate: **44.48%**
- Non-selected evaluated cases: **5916**
- Non-selected success rate: **45.93%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 343 | 157 | 186 | 45.77% |
| Top 20 | 607 | 270 | 337 | 44.48% |
| Top 50 | 899 | 396 | 503 | 44.05% |
| Top 100 | 1232 | 517 | 715 | 41.96% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 929 | 401 | 528 | 43.16% | -0.11% | -0.62% | -1.21% | 925 | 45.73% |
| avoid | 5594 | 2586 | 3008 | 46.23% | 0.32% | 1.09% | 1.67% | 5449 | 51.35% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.