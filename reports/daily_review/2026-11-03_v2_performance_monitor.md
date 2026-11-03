# V2 Performance Monitor - 2026-11-03

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **17271**
- V2 success count: **8328**
- V2 failure count: **8943**
- V2 raw success rate: **48.22%**
- V2 benchmark-adjusted evaluated cases: **13604**
- V2 benchmark-adjusted success rate: **52.63%**
- V2 benchmark coverage rate: **78.77%**
- V2 average close_t1_return: **-0.04%**
- V2 average excess_t1_return: **-0.02%**
- Selected-pick evaluated cases: **975**
- Selected-pick success rate: **44.41%**
- Non-selected evaluated cases: **16296**
- Non-selected success rate: **48.45%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 547 | 241 | 306 | 44.06% |
| Top 20 | 971 | 433 | 538 | 44.59% |
| Top 50 | 1516 | 660 | 856 | 43.54% |
| Top 100 | 2029 | 852 | 1177 | 41.99% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1835 | 776 | 1059 | 42.29% | -0.21% | -1.22% | -2.08% | 1192 | 52.94% |
| avoid | 15436 | 7552 | 7884 | 48.92% | -0.02% | -0.45% | -0.70% | 12412 | 52.60% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.