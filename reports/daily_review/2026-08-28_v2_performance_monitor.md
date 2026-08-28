# V2 Performance Monitor - 2026-08-28

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **3294**
- V2 success count: **1361**
- V2 failure count: **1933**
- V2 raw success rate: **41.32%**
- V2 benchmark-adjusted evaluated cases: **3294**
- V2 benchmark-adjusted success rate: **49.97%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.55%**
- V2 average excess_t1_return: **-0.19%**
- Selected-pick evaluated cases: **414**
- Selected-pick success rate: **47.10%**
- Non-selected evaluated cases: **2880**
- Non-selected success rate: **40.49%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 227 | 110 | 117 | 48.46% |
| Top 20 | 381 | 179 | 202 | 46.98% |
| Top 50 | 580 | 261 | 319 | 45.00% |
| Top 100 | 883 | 372 | 511 | 42.13% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 643 | 267 | 376 | 41.52% | -0.20% | -0.55% | -1.24% | 643 | 41.68% |
| avoid | 2651 | 1094 | 1557 | 41.27% | 0.73% | 2.31% | 3.52% | 2651 | 51.98% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.