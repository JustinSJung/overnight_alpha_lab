# V2 Performance Monitor - 2026-09-11

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **4912**
- V2 success count: **2213**
- V2 failure count: **2699**
- V2 raw success rate: **45.05%**
- V2 benchmark-adjusted evaluated cases: **4912**
- V2 benchmark-adjusted success rate: **49.55%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.34%**
- V2 average excess_t1_return: **0.05%**
- Selected-pick evaluated cases: **515**
- Selected-pick success rate: **45.63%**
- Non-selected evaluated cases: **4397**
- Non-selected success rate: **44.99%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 298 | 141 | 157 | 47.32% |
| Top 20 | 515 | 235 | 280 | 45.63% |
| Top 50 | 759 | 334 | 425 | 44.01% |
| Top 100 | 1083 | 454 | 629 | 41.92% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 792 | 340 | 452 | 42.93% | -0.10% | -0.42% | -0.78% | 792 | 45.45% |
| avoid | 4120 | 1873 | 2247 | 45.46% | 0.43% | 1.83% | 3.21% | 4120 | 50.34% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.