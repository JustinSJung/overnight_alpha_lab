# V2 Performance Monitor - 2026-11-19

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **25070**
- V2 success count: **12526**
- V2 failure count: **12544**
- V2 raw success rate: **49.96%**
- V2 benchmark-adjusted evaluated cases: **18612**
- V2 benchmark-adjusted success rate: **51.35%**
- V2 benchmark coverage rate: **74.24%**
- V2 average close_t1_return: **-0.18%**
- V2 average excess_t1_return: **0.13%**
- Selected-pick evaluated cases: **1219**
- Selected-pick success rate: **43.15%**
- Non-selected evaluated cases: **23851**
- Non-selected success rate: **50.31%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 674 | 287 | 387 | 42.58% |
| Top 20 | 1215 | 526 | 689 | 43.29% |
| Top 50 | 2103 | 899 | 1204 | 42.75% |
| Top 100 | 2843 | 1172 | 1671 | 41.22% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2634 | 1094 | 1540 | 41.53% | -0.28% | -1.15% | -1.92% | 1718 | 53.32% |
| avoid | 22436 | 11432 | 11004 | 50.95% | -0.17% | -0.65% | -1.05% | 16894 | 51.15% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.