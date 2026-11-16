# V2 Performance Monitor - 2026-11-16

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **23486**
- V2 success count: **11618**
- V2 failure count: **11868**
- V2 raw success rate: **49.47%**
- V2 benchmark-adjusted evaluated cases: **17458**
- V2 benchmark-adjusted success rate: **51.49%**
- V2 benchmark coverage rate: **74.33%**
- V2 average close_t1_return: **-0.10%**
- V2 average excess_t1_return: **0.11%**
- Selected-pick evaluated cases: **1138**
- Selected-pick success rate: **43.67%**
- Non-selected evaluated cases: **22348**
- Non-selected success rate: **49.76%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 621 | 263 | 358 | 42.35% |
| Top 20 | 1134 | 497 | 637 | 43.83% |
| Top 50 | 1935 | 843 | 1092 | 43.57% |
| Top 100 | 2560 | 1088 | 1472 | 42.50% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2367 | 1016 | 1351 | 42.92% | -0.19% | -0.99% | -1.91% | 1495 | 52.84% |
| avoid | 21119 | 10602 | 10517 | 50.20% | -0.09% | -0.31% | -0.92% | 15963 | 51.36% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.