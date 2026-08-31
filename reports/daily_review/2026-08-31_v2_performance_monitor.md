# V2 Performance Monitor - 2026-08-31

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **2997**
- V2 success count: **1250**
- V2 failure count: **1747**
- V2 raw success rate: **41.71%**
- V2 benchmark-adjusted evaluated cases: **2997**
- V2 benchmark-adjusted success rate: **49.58%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.60%**
- V2 average excess_t1_return: **0.12%**
- Selected-pick evaluated cases: **370**
- Selected-pick success rate: **46.22%**
- Non-selected evaluated cases: **2627**
- Non-selected success rate: **41.07%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 218 | 103 | 115 | 47.25% |
| Top 20 | 370 | 171 | 199 | 46.22% |
| Top 50 | 565 | 240 | 325 | 42.48% |
| Top 100 | 870 | 342 | 528 | 39.31% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 593 | 239 | 354 | 40.30% | -0.11% | -0.37% | -1.06% | 593 | 46.54% |
| avoid | 2404 | 1011 | 1393 | 42.05% | 0.77% | 2.76% | 4.09% | 2404 | 50.33% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.