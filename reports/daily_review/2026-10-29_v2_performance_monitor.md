# V2 Performance Monitor - 2026-10-29

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **16564**
- V2 success count: **8130**
- V2 failure count: **8434**
- V2 raw success rate: **49.08%**
- V2 benchmark-adjusted evaluated cases: **13680**
- V2 benchmark-adjusted success rate: **52.13%**
- V2 benchmark coverage rate: **82.59%**
- V2 average close_t1_return: **-0.10%**
- V2 average excess_t1_return: **0.02%**
- Selected-pick evaluated cases: **964**
- Selected-pick success rate: **44.09%**
- Non-selected evaluated cases: **15600**
- Non-selected success rate: **49.39%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 544 | 238 | 306 | 43.75% |
| Top 20 | 960 | 425 | 535 | 44.27% |
| Top 50 | 1521 | 662 | 859 | 43.52% |
| Top 100 | 2043 | 853 | 1190 | 41.75% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1849 | 781 | 1068 | 42.24% | -0.19% | -1.16% | -2.10% | 1276 | 52.98% |
| avoid | 14715 | 7349 | 7366 | 49.94% | -0.09% | -0.33% | -0.51% | 12404 | 52.05% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.