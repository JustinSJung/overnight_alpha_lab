# V2 Performance Monitor - 2026-11-10

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **20437**
- V2 success count: **10405**
- V2 failure count: **10032**
- V2 raw success rate: **50.91%**
- V2 benchmark-adjusted evaluated cases: **15832**
- V2 benchmark-adjusted success rate: **49.68%**
- V2 benchmark coverage rate: **77.47%**
- V2 average close_t1_return: **-0.31%**
- V2 average excess_t1_return: **0.31%**
- Selected-pick evaluated cases: **1072**
- Selected-pick success rate: **43.94%**
- Non-selected evaluated cases: **19365**
- Non-selected success rate: **51.30%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 599 | 264 | 335 | 44.07% |
| Top 20 | 1068 | 471 | 597 | 44.10% |
| Top 50 | 1743 | 751 | 992 | 43.09% |
| Top 100 | 2284 | 955 | 1329 | 41.81% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2089 | 881 | 1208 | 42.17% | -0.22% | -1.14% | -2.03% | 1336 | 55.54% |
| avoid | 18348 | 9524 | 8824 | 51.91% | -0.32% | -0.93% | -1.29% | 14496 | 49.14% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.