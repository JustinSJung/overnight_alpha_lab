# V2 Performance Monitor - 2026-11-11

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **21227**
- V2 success count: **10605**
- V2 failure count: **10622**
- V2 raw success rate: **49.96%**
- V2 benchmark-adjusted evaluated cases: **16283**
- V2 benchmark-adjusted success rate: **50.70%**
- V2 benchmark coverage rate: **76.71%**
- V2 average close_t1_return: **-0.20%**
- V2 average excess_t1_return: **0.21%**
- Selected-pick evaluated cases: **1088**
- Selected-pick success rate: **44.39%**
- Non-selected evaluated cases: **20139**
- Non-selected success rate: **50.26%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 603 | 266 | 337 | 44.11% |
| Top 20 | 1084 | 483 | 601 | 44.56% |
| Top 50 | 1790 | 782 | 1008 | 43.69% |
| Top 100 | 2347 | 999 | 1348 | 42.56% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2149 | 920 | 1229 | 42.81% | -0.20% | -1.15% | -2.03% | 1361 | 52.98% |
| avoid | 19078 | 9685 | 9393 | 50.77% | -0.20% | -0.94% | -1.36% | 14922 | 50.49% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.