# V2 Performance Monitor - 2026-09-03

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **3595**
- V2 success count: **1590**
- V2 failure count: **2005**
- V2 raw success rate: **44.23%**
- V2 benchmark-adjusted evaluated cases: **3595**
- V2 benchmark-adjusted success rate: **49.65%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.38%**
- V2 average excess_t1_return: **0.01%**
- Selected-pick evaluated cases: **433**
- Selected-pick success rate: **45.27%**
- Non-selected evaluated cases: **3162**
- Non-selected success rate: **44.09%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 255 | 119 | 136 | 46.67% |
| Top 20 | 433 | 196 | 237 | 45.27% |
| Top 50 | 642 | 277 | 365 | 43.15% |
| Top 100 | 967 | 394 | 573 | 40.74% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 668 | 280 | 388 | 41.92% | -0.08% | -0.53% | -0.97% | 668 | 44.31% |
| avoid | 2927 | 1310 | 1617 | 44.76% | 0.48% | 2.27% | 3.74% | 2927 | 50.87% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.