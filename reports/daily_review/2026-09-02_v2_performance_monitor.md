# V2 Performance Monitor - 2026-09-02

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **3287**
- V2 success count: **1397**
- V2 failure count: **1890**
- V2 raw success rate: **42.50%**
- V2 benchmark-adjusted evaluated cases: **3287**
- V2 benchmark-adjusted success rate: **48.89%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.52%**
- V2 average excess_t1_return: **0.01%**
- Selected-pick evaluated cases: **406**
- Selected-pick success rate: **44.09%**
- Non-selected evaluated cases: **2881**
- Non-selected success rate: **42.28%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 235 | 106 | 129 | 45.11% |
| Top 20 | 406 | 179 | 227 | 44.09% |
| Top 50 | 615 | 259 | 356 | 42.11% |
| Top 100 | 923 | 366 | 557 | 39.65% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 641 | 262 | 379 | 40.87% | -0.11% | -0.40% | -0.93% | 641 | 43.21% |
| avoid | 2646 | 1135 | 1511 | 42.89% | 0.67% | 2.60% | 3.98% | 2646 | 50.26% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.