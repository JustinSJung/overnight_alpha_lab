# V2 Performance Monitor - 2026-08-27

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **3173**
- V2 success count: **1303**
- V2 failure count: **1870**
- V2 raw success rate: **41.07%**
- V2 benchmark-adjusted evaluated cases: **3173**
- V2 benchmark-adjusted success rate: **50.30%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.55%**
- V2 average excess_t1_return: **-0.26%**
- Selected-pick evaluated cases: **394**
- Selected-pick success rate: **46.95%**
- Non-selected evaluated cases: **2779**
- Non-selected success rate: **40.23%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 217 | 104 | 113 | 47.93% |
| Top 20 | 361 | 169 | 192 | 46.81% |
| Top 50 | 558 | 251 | 307 | 44.98% |
| Top 100 | 859 | 361 | 498 | 42.03% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 621 | 257 | 364 | 41.38% | -0.19% | -0.69% | -1.52% | 621 | 40.90% |
| avoid | 2552 | 1046 | 1506 | 40.99% | 0.73% | 2.14% | 3.56% | 2552 | 52.59% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.