# V2 Performance Monitor - 2026-11-18

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **24412**
- V2 success count: **12261**
- V2 failure count: **12151**
- V2 raw success rate: **50.23%**
- V2 benchmark-adjusted evaluated cases: **18078**
- V2 benchmark-adjusted success rate: **50.71%**
- V2 benchmark coverage rate: **74.05%**
- V2 average close_t1_return: **-0.19%**
- V2 average excess_t1_return: **0.20%**
- Selected-pick evaluated cases: **1203**
- Selected-pick success rate: **43.47%**
- Non-selected evaluated cases: **23209**
- Non-selected success rate: **50.58%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 668 | 284 | 384 | 42.51% |
| Top 20 | 1200 | 523 | 677 | 43.58% |
| Top 50 | 2057 | 886 | 1171 | 43.07% |
| Top 100 | 2759 | 1144 | 1615 | 41.46% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2558 | 1069 | 1489 | 41.79% | -0.28% | -1.10% | -1.83% | 1644 | 55.23% |
| avoid | 21854 | 11192 | 10662 | 51.21% | -0.18% | -0.60% | -0.99% | 16434 | 50.26% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.