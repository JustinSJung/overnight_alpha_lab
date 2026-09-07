# V2 Performance Monitor - 2026-09-07

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **3775**
- V2 success count: **1609**
- V2 failure count: **2166**
- V2 raw success rate: **42.62%**
- V2 benchmark-adjusted evaluated cases: **3775**
- V2 benchmark-adjusted success rate: **49.99%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.50%**
- V2 average excess_t1_return: **0.02%**
- Selected-pick evaluated cases: **449**
- Selected-pick success rate: **45.43%**
- Non-selected evaluated cases: **3326**
- Non-selected success rate: **42.24%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 264 | 125 | 139 | 47.35% |
| Top 20 | 449 | 204 | 245 | 45.43% |
| Top 50 | 656 | 284 | 372 | 43.29% |
| Top 100 | 967 | 393 | 574 | 40.64% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 683 | 288 | 395 | 42.17% | -0.09% | -0.54% | -0.98% | 683 | 43.78% |
| avoid | 3092 | 1321 | 1771 | 42.72% | 0.63% | 2.14% | 3.75% | 3092 | 51.36% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.