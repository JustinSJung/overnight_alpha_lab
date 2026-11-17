# V2 Performance Monitor - 2026-11-17

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **23934**
- V2 success count: **11994**
- V2 failure count: **11940**
- V2 raw success rate: **50.11%**
- V2 benchmark-adjusted evaluated cases: **17626**
- V2 benchmark-adjusted success rate: **50.81%**
- V2 benchmark coverage rate: **73.64%**
- V2 average close_t1_return: **-0.18%**
- V2 average excess_t1_return: **0.19%**
- Selected-pick evaluated cases: **1155**
- Selected-pick success rate: **43.98%**
- Non-selected evaluated cases: **22779**
- Non-selected success rate: **50.42%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 642 | 276 | 366 | 42.99% |
| Top 20 | 1151 | 508 | 643 | 44.14% |
| Top 50 | 1955 | 852 | 1103 | 43.58% |
| Top 100 | 2596 | 1102 | 1494 | 42.45% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2402 | 1026 | 1376 | 42.71% | -0.23% | -1.03% | -1.86% | 1510 | 54.50% |
| avoid | 21532 | 10968 | 10564 | 50.94% | -0.17% | -0.47% | -0.90% | 16116 | 50.47% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.