# V2 Performance Monitor - 2026-10-27

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **15903**
- V2 success count: **7861**
- V2 failure count: **8042**
- V2 raw success rate: **49.43%**
- V2 benchmark-adjusted evaluated cases: **13092**
- V2 benchmark-adjusted success rate: **50.73%**
- V2 benchmark coverage rate: **82.32%**
- V2 average close_t1_return: **-0.11%**
- V2 average excess_t1_return: **0.24%**
- Selected-pick evaluated cases: **951**
- Selected-pick success rate: **43.95%**
- Non-selected evaluated cases: **14952**
- Non-selected success rate: **49.78%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 531 | 226 | 305 | 42.56% |
| Top 20 | 947 | 418 | 529 | 44.14% |
| Top 50 | 1503 | 650 | 853 | 43.25% |
| Top 100 | 2022 | 847 | 1175 | 41.89% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1831 | 770 | 1061 | 42.05% | -0.24% | -1.21% | -2.09% | 1317 | 53.53% |
| avoid | 14072 | 7091 | 6981 | 50.39% | -0.09% | -0.33% | -0.24% | 11775 | 50.41% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.