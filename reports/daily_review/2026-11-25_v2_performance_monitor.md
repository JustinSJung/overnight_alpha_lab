# V2 Performance Monitor - 2026-11-25

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **27593**
- V2 success count: **13898**
- V2 failure count: **13695**
- V2 raw success rate: **50.37%**
- V2 benchmark-adjusted evaluated cases: **20685**
- V2 benchmark-adjusted success rate: **52.41%**
- V2 benchmark coverage rate: **74.96%**
- V2 average close_t1_return: **-0.22%**
- V2 average excess_t1_return: **0.01%**
- Selected-pick evaluated cases: **1282**
- Selected-pick success rate: **43.06%**
- Non-selected evaluated cases: **26311**
- Non-selected success rate: **50.72%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 692 | 288 | 404 | 41.62% |
| Top 20 | 1278 | 552 | 726 | 43.19% |
| Top 50 | 2260 | 968 | 1292 | 42.83% |
| Top 100 | 2873 | 1195 | 1678 | 41.59% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2821 | 1176 | 1645 | 41.69% | -0.32% | -1.20% | -2.06% | 1803 | 52.80% |
| avoid | 24772 | 12722 | 12050 | 51.36% | -0.21% | -0.86% | -1.25% | 18882 | 52.37% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.