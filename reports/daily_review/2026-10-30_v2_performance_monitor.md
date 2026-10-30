# V2 Performance Monitor - 2026-10-30

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **16560**
- V2 success count: **8145**
- V2 failure count: **8415**
- V2 raw success rate: **49.18%**
- V2 benchmark-adjusted evaluated cases: **13631**
- V2 benchmark-adjusted success rate: **52.25%**
- V2 benchmark coverage rate: **82.31%**
- V2 average close_t1_return: **-0.09%**
- V2 average excess_t1_return: **0.02%**
- Selected-pick evaluated cases: **960**
- Selected-pick success rate: **44.27%**
- Non-selected evaluated cases: **15600**
- Non-selected success rate: **49.49%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 545 | 236 | 309 | 43.30% |
| Top 20 | 956 | 424 | 532 | 44.35% |
| Top 50 | 1509 | 653 | 856 | 43.27% |
| Top 100 | 2015 | 837 | 1178 | 41.54% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1835 | 772 | 1063 | 42.07% | -0.23% | -1.18% | -2.17% | 1258 | 53.10% |
| avoid | 14725 | 7373 | 7352 | 50.07% | -0.08% | -0.28% | -0.46% | 12373 | 52.16% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.