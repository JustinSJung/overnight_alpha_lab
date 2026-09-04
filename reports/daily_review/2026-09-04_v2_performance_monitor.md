# V2 Performance Monitor - 2026-09-04

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **3781**
- V2 success count: **1615**
- V2 failure count: **2166**
- V2 raw success rate: **42.71%**
- V2 benchmark-adjusted evaluated cases: **3781**
- V2 benchmark-adjusted success rate: **49.99%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.44%**
- V2 average excess_t1_return: **0.02%**
- Selected-pick evaluated cases: **447**
- Selected-pick success rate: **45.86%**
- Non-selected evaluated cases: **3334**
- Non-selected success rate: **42.29%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 262 | 124 | 138 | 47.33% |
| Top 20 | 447 | 205 | 242 | 45.86% |
| Top 50 | 655 | 285 | 370 | 43.51% |
| Top 100 | 968 | 394 | 574 | 40.70% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 682 | 289 | 393 | 42.38% | -0.09% | -0.51% | -0.95% | 682 | 43.70% |
| avoid | 3099 | 1326 | 1773 | 42.79% | 0.56% | 2.19% | 3.87% | 3099 | 51.37% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.