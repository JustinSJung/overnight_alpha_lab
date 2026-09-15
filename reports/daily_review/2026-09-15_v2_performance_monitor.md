# V2 Performance Monitor - 2026-09-15

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **5533**
- V2 success count: **2492**
- V2 failure count: **3041**
- V2 raw success rate: **45.04%**
- V2 benchmark-adjusted evaluated cases: **5533**
- V2 benchmark-adjusted success rate: **48.71%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.29%**
- V2 average excess_t1_return: **0.11%**
- Selected-pick evaluated cases: **551**
- Selected-pick success rate: **43.01%**
- Non-selected evaluated cases: **4982**
- Non-selected success rate: **45.26%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 314 | 140 | 174 | 44.59% |
| Top 20 | 551 | 237 | 314 | 43.01% |
| Top 50 | 804 | 339 | 465 | 42.16% |
| Top 100 | 1136 | 456 | 680 | 40.14% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 838 | 346 | 492 | 41.29% | -0.25% | -0.65% | -0.89% | 838 | 45.47% |
| avoid | 4695 | 2146 | 2549 | 45.71% | 0.38% | 1.46% | 2.66% | 4695 | 49.29% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.