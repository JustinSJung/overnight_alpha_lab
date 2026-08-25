# V2 Performance Monitor - 2026-08-25

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **3005**
- V2 success count: **1234**
- V2 failure count: **1771**
- V2 raw success rate: **41.06%**
- V2 benchmark-adjusted evaluated cases: **3005**
- V2 benchmark-adjusted success rate: **50.65%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.50%**
- V2 average excess_t1_return: **-0.35%**
- Selected-pick evaluated cases: **373**
- Selected-pick success rate: **46.65%**
- Non-selected evaluated cases: **2632**
- Non-selected success rate: **40.27%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 206 | 100 | 106 | 48.54% |
| Top 20 | 340 | 158 | 182 | 46.47% |
| Top 50 | 536 | 240 | 296 | 44.78% |
| Top 100 | 837 | 351 | 486 | 41.94% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 599 | 246 | 353 | 41.07% | -0.24% | -0.80% | -1.58% | 599 | 40.57% |
| avoid | 2406 | 988 | 1418 | 41.06% | 0.68% | 1.85% | 3.79% | 2406 | 53.16% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.