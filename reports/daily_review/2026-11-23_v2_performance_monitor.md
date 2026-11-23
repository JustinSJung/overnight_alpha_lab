# V2 Performance Monitor - 2026-11-23

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **25953**
- V2 success count: **13129**
- V2 failure count: **12824**
- V2 raw success rate: **50.59%**
- V2 benchmark-adjusted evaluated cases: **19125**
- V2 benchmark-adjusted success rate: **51.50%**
- V2 benchmark coverage rate: **73.69%**
- V2 average close_t1_return: **-0.27%**
- V2 average excess_t1_return: **0.13%**
- Selected-pick evaluated cases: **1202**
- Selected-pick success rate: **43.26%**
- Non-selected evaluated cases: **24751**
- Non-selected success rate: **50.94%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 655 | 280 | 375 | 42.75% |
| Top 20 | 1199 | 520 | 679 | 43.37% |
| Top 50 | 2114 | 905 | 1209 | 42.81% |
| Top 100 | 2700 | 1128 | 1572 | 41.78% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2657 | 1114 | 1543 | 41.93% | -0.29% | -1.10% | -1.91% | 1679 | 54.02% |
| avoid | 23296 | 12015 | 11281 | 51.58% | -0.27% | -0.66% | -1.19% | 17446 | 51.26% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.