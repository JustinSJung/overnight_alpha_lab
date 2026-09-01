# V2 Performance Monitor - 2026-09-01

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **3136**
- V2 success count: **1327**
- V2 failure count: **1809**
- V2 raw success rate: **42.32%**
- V2 benchmark-adjusted evaluated cases: **3136**
- V2 benchmark-adjusted success rate: **49.17%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.56%**
- V2 average excess_t1_return: **0.04%**
- Selected-pick evaluated cases: **392**
- Selected-pick success rate: **45.92%**
- Non-selected evaluated cases: **2744**
- Non-selected success rate: **41.80%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 230 | 109 | 121 | 47.39% |
| Top 20 | 392 | 180 | 212 | 45.92% |
| Top 50 | 594 | 258 | 336 | 43.43% |
| Top 100 | 890 | 365 | 525 | 41.01% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 620 | 261 | 359 | 42.10% | -0.09% | -0.45% | -1.06% | 620 | 43.71% |
| avoid | 2516 | 1066 | 1450 | 42.37% | 0.73% | 2.55% | 3.82% | 2516 | 50.52% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.