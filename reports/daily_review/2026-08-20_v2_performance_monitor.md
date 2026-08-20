# V2 Performance Monitor - 2026-08-20

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **2485**
- V2 success count: **1002**
- V2 failure count: **1483**
- V2 raw success rate: **40.32%**
- V2 benchmark-adjusted evaluated cases: **2485**
- V2 benchmark-adjusted success rate: **51.51%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.63%**
- V2 average excess_t1_return: **-0.48%**
- Selected-pick evaluated cases: **320**
- Selected-pick success rate: **47.50%**
- Non-selected evaluated cases: **2165**
- Non-selected success rate: **39.26%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 177 | 88 | 89 | 49.72% |
| Top 20 | 287 | 136 | 151 | 47.39% |
| Top 50 | 482 | 218 | 264 | 45.23% |
| Top 100 | 785 | 329 | 456 | 41.91% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 545 | 224 | 321 | 41.10% | -0.30% | -0.81% | -0.49% | 545 | 40.18% |
| avoid | 1940 | 778 | 1162 | 40.10% | 0.89% | 2.56% | 4.89% | 1940 | 54.69% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.