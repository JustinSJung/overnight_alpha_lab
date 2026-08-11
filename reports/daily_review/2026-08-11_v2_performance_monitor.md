# V2 Performance Monitor - 2026-08-11

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **8875**
- V2 success count: **3838**
- V2 failure count: **5037**
- V2 raw success rate: **43.25%**
- V2 benchmark-adjusted evaluated cases: **6561**
- V2 benchmark-adjusted success rate: **51.87%**
- V2 benchmark coverage rate: **73.93%**
- V2 average close_t1_return: **0.45%**
- V2 average excess_t1_return: **-0.34%**
- Selected-pick evaluated cases: **572**
- Selected-pick success rate: **51.57%**
- Non-selected evaluated cases: **8303**
- Non-selected success rate: **42.67%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 92 | 46 | 46 | 50.00% |
| Top 20 | 186 | 102 | 84 | 54.84% |
| Top 50 | 381 | 198 | 183 | 51.97% |
| Top 100 | 525 | 267 | 258 | 50.86% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 575 | 295 | 280 | 51.30% | 0.25% | -1.71% | -1.93% | 435 | 71.26% |
| avoid | 8300 | 3543 | 4757 | 42.69% | 0.46% | -1.07% | -3.37% | 6126 | 50.49% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.