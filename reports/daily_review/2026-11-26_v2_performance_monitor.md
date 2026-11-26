# V2 Performance Monitor - 2026-11-26

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **28277**
- V2 success count: **14380**
- V2 failure count: **13897**
- V2 raw success rate: **50.85%**
- V2 benchmark-adjusted evaluated cases: **21470**
- V2 benchmark-adjusted success rate: **51.64%**
- V2 benchmark coverage rate: **75.93%**
- V2 average close_t1_return: **-0.25%**
- V2 average excess_t1_return: **0.11%**
- Selected-pick evaluated cases: **1280**
- Selected-pick success rate: **43.83%**
- Non-selected evaluated cases: **26997**
- Non-selected success rate: **51.19%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 688 | 292 | 396 | 42.44% |
| Top 20 | 1276 | 561 | 715 | 43.97% |
| Top 50 | 2288 | 992 | 1296 | 43.36% |
| Top 100 | 2905 | 1219 | 1686 | 41.96% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2864 | 1204 | 1660 | 42.04% | -0.28% | -1.10% | -2.05% | 1855 | 53.64% |
| avoid | 25413 | 13176 | 12237 | 51.85% | -0.25% | -0.85% | -1.32% | 19615 | 51.46% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.