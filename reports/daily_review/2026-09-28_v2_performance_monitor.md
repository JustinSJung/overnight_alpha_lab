# V2 Performance Monitor - 2026-09-28

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **7661**
- V2 success count: **3519**
- V2 failure count: **4142**
- V2 raw success rate: **45.93%**
- V2 benchmark-adjusted evaluated cases: **7006**
- V2 benchmark-adjusted success rate: **51.36%**
- V2 benchmark coverage rate: **91.45%**
- V2 average close_t1_return: **0.29%**
- V2 average excess_t1_return: **-0.06%**
- Selected-pick evaluated cases: **673**
- Selected-pick success rate: **45.62%**
- Non-selected evaluated cases: **6988**
- Non-selected success rate: **45.96%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 379 | 178 | 201 | 46.97% |
| Top 20 | 673 | 307 | 366 | 45.62% |
| Top 50 | 1031 | 460 | 571 | 44.62% |
| Top 100 | 1403 | 602 | 801 | 42.91% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1089 | 483 | 606 | 44.35% | 0.01% | -0.47% | -0.79% | 1048 | 45.04% |
| avoid | 6572 | 3036 | 3536 | 46.20% | 0.33% | 1.09% | 1.68% | 5958 | 52.47% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.