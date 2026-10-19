# V2 Performance Monitor - 2026-10-19

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **12657**
- V2 success count: **6097**
- V2 failure count: **6560**
- V2 raw success rate: **48.17%**
- V2 benchmark-adjusted evaluated cases: **10604**
- V2 benchmark-adjusted success rate: **46.47%**
- V2 benchmark coverage rate: **83.78%**
- V2 average close_t1_return: **-0.02%**
- V2 average excess_t1_return: **0.58%**
- Selected-pick evaluated cases: **878**
- Selected-pick success rate: **44.19%**
- Non-selected evaluated cases: **11779**
- Non-selected success rate: **48.47%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Weak market-relative signal / 시장 대비 약한 신호**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 478 | 212 | 266 | 44.35% |
| Top 20 | 874 | 387 | 487 | 44.28% |
| Top 50 | 1431 | 621 | 810 | 43.40% |
| Top 100 | 1959 | 819 | 1140 | 41.81% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1762 | 744 | 1018 | 42.22% | -0.17% | -1.12% | -2.06% | 1340 | 54.18% |
| avoid | 10895 | 5353 | 5542 | 49.13% | 0.01% | 0.10% | 0.68% | 9264 | 45.36% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.