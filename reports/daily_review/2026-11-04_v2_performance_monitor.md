# V2 Performance Monitor - 2026-11-04

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **17948**
- V2 success count: **8842**
- V2 failure count: **9106**
- V2 raw success rate: **49.26%**
- V2 benchmark-adjusted evaluated cases: **14256**
- V2 benchmark-adjusted success rate: **51.86%**
- V2 benchmark coverage rate: **79.43%**
- V2 average close_t1_return: **-0.12%**
- V2 average excess_t1_return: **0.04%**
- Selected-pick evaluated cases: **1008**
- Selected-pick success rate: **44.25%**
- Non-selected evaluated cases: **16940**
- Non-selected success rate: **49.56%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 562 | 246 | 316 | 43.77% |
| Top 20 | 1004 | 446 | 558 | 44.42% |
| Top 50 | 1569 | 678 | 891 | 43.21% |
| Top 100 | 2099 | 877 | 1222 | 41.78% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1896 | 799 | 1097 | 42.14% | -0.24% | -1.15% | -2.01% | 1231 | 53.37% |
| avoid | 16052 | 8043 | 8009 | 50.11% | -0.11% | -0.37% | -0.75% | 13025 | 51.72% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.