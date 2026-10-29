# V2 Performance Monitor - 2026-10-12

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **10164**
- V2 success count: **4798**
- V2 failure count: **5366**
- V2 raw success rate: **47.21%**
- V2 benchmark-adjusted evaluated cases: **8392**
- V2 benchmark-adjusted success rate: **51.13%**
- V2 benchmark coverage rate: **82.57%**
- V2 average close_t1_return: **0.12%**
- V2 average excess_t1_return: **0.10%**
- Selected-pick evaluated cases: **811**
- Selected-pick success rate: **45.13%**
- Non-selected evaluated cases: **9353**
- Non-selected success rate: **47.39%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 445 | 201 | 244 | 45.17% |
| Top 20 | 807 | 365 | 442 | 45.23% |
| Top 50 | 1346 | 595 | 751 | 44.21% |
| Top 100 | 1888 | 800 | 1088 | 42.37% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1678 | 723 | 955 | 43.09% | -0.11% | -0.35% | 0.10% | 1363 | 50.11% |
| avoid | 8486 | 4075 | 4411 | 48.02% | 0.17% | 0.87% | 1.46% | 7029 | 51.33% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.