# V2 Performance Monitor - 2026-08-29

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **2985**
- V2 success count: **1235**
- V2 failure count: **1750**
- V2 raw success rate: **41.37%**
- V2 benchmark-adjusted evaluated cases: **2985**
- V2 benchmark-adjusted success rate: **49.18%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.63%**
- V2 average excess_t1_return: **-0.09%**
- Selected-pick evaluated cases: **357**
- Selected-pick success rate: **47.06%**
- Non-selected evaluated cases: **2628**
- Non-selected success rate: **40.60%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 215 | 102 | 113 | 47.44% |
| Top 20 | 357 | 168 | 189 | 47.06% |
| Top 50 | 530 | 232 | 298 | 43.77% |
| Top 100 | 856 | 349 | 507 | 40.77% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 543 | 229 | 314 | 42.17% | -0.06% | -0.35% | -1.03% | 543 | 41.62% |
| avoid | 2442 | 1006 | 1436 | 41.20% | 0.78% | 2.90% | 4.08% | 2442 | 50.86% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.