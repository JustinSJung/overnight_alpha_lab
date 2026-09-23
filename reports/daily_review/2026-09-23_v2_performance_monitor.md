# V2 Performance Monitor - 2026-09-23

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **7060**
- V2 success count: **3290**
- V2 failure count: **3770**
- V2 raw success rate: **46.60%**
- V2 benchmark-adjusted evaluated cases: **6749**
- V2 benchmark-adjusted success rate: **51.15%**
- V2 benchmark coverage rate: **95.59%**
- V2 average close_t1_return: **0.21%**
- V2 average excess_t1_return: **-0.01%**
- Selected-pick evaluated cases: **647**
- Selected-pick success rate: **44.98%**
- Non-selected evaluated cases: **6413**
- Non-selected success rate: **46.76%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 364 | 168 | 196 | 46.15% |
| Top 20 | 647 | 291 | 356 | 44.98% |
| Top 50 | 981 | 436 | 545 | 44.44% |
| Top 100 | 1304 | 553 | 751 | 42.41% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1011 | 443 | 568 | 43.82% | -0.05% | -0.56% | -0.97% | 992 | 45.87% |
| avoid | 6049 | 2847 | 3202 | 47.07% | 0.25% | 1.05% | 1.55% | 5757 | 52.06% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.