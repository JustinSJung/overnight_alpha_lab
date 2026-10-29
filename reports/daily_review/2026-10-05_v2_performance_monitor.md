# V2 Performance Monitor - 2026-10-05

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **8529**
- V2 success count: **3974**
- V2 failure count: **4555**
- V2 raw success rate: **46.59%**
- V2 benchmark-adjusted evaluated cases: **7303**
- V2 benchmark-adjusted success rate: **52.66%**
- V2 benchmark coverage rate: **85.63%**
- V2 average close_t1_return: **0.21%**
- V2 average excess_t1_return: **-0.16%**
- Selected-pick evaluated cases: **721**
- Selected-pick success rate: **45.21%**
- Non-selected evaluated cases: **7808**
- Non-selected success rate: **46.72%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 401 | 187 | 214 | 46.63% |
| Top 20 | 721 | 326 | 395 | 45.21% |
| Top 50 | 1142 | 519 | 623 | 45.45% |
| Top 100 | 1513 | 659 | 854 | 43.56% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1213 | 546 | 667 | 45.01% | 0.09% | -0.12% | -0.39% | 1107 | 43.00% |
| avoid | 7316 | 3428 | 3888 | 46.86% | 0.23% | 0.89% | 1.36% | 6196 | 54.39% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.