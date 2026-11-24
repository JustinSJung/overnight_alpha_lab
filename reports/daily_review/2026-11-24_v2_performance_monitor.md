# V2 Performance Monitor - 2026-11-24

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **26461**
- V2 success count: **13561**
- V2 failure count: **12900**
- V2 raw success rate: **51.25%**
- V2 benchmark-adjusted evaluated cases: **19751**
- V2 benchmark-adjusted success rate: **51.73%**
- V2 benchmark coverage rate: **74.64%**
- V2 average close_t1_return: **-0.32%**
- V2 average excess_t1_return: **0.10%**
- Selected-pick evaluated cases: **1233**
- Selected-pick success rate: **43.07%**
- Non-selected evaluated cases: **25228**
- Non-selected success rate: **51.65%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 664 | 279 | 385 | 42.02% |
| Top 20 | 1229 | 531 | 698 | 43.21% |
| Top 50 | 2171 | 918 | 1253 | 42.28% |
| Top 100 | 2782 | 1140 | 1642 | 40.98% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2738 | 1127 | 1611 | 41.16% | -0.36% | -1.14% | -2.01% | 1755 | 54.36% |
| avoid | 23723 | 12434 | 11289 | 52.41% | -0.32% | -0.79% | -1.24% | 17996 | 51.47% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.