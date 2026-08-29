# V2 Performance Monitor - 2026-08-29

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **2913**
- V2 success count: **1199**
- V2 failure count: **1714**
- V2 raw success rate: **41.16%**
- V2 benchmark-adjusted evaluated cases: **2913**
- V2 benchmark-adjusted success rate: **49.47%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.68%**
- V2 average excess_t1_return: **-0.13%**
- Selected-pick evaluated cases: **353**
- Selected-pick success rate: **47.31%**
- Non-selected evaluated cases: **2560**
- Non-selected success rate: **40.31%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 211 | 101 | 110 | 47.87% |
| Top 20 | 353 | 167 | 186 | 47.31% |
| Top 50 | 523 | 230 | 293 | 43.98% |
| Top 100 | 825 | 335 | 490 | 40.61% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 539 | 228 | 311 | 42.30% | -0.05% | -0.35% | -1.05% | 539 | 41.56% |
| avoid | 2374 | 971 | 1403 | 40.90% | 0.85% | 2.89% | 4.31% | 2374 | 51.26% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.