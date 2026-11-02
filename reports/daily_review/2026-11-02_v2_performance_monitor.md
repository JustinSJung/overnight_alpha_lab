# V2 Performance Monitor - 2026-11-02

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **15936**
- V2 success count: **7787**
- V2 failure count: **8149**
- V2 raw success rate: **48.86%**
- V2 benchmark-adjusted evaluated cases: **12857**
- V2 benchmark-adjusted success rate: **52.14%**
- V2 benchmark coverage rate: **80.68%**
- V2 average close_t1_return: **-0.10%**
- V2 average excess_t1_return: **0.02%**
- Selected-pick evaluated cases: **905**
- Selected-pick success rate: **43.76%**
- Non-selected evaluated cases: **15031**
- Non-selected success rate: **49.17%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 505 | 222 | 283 | 43.96% |
| Top 20 | 901 | 396 | 505 | 43.95% |
| Top 50 | 1425 | 612 | 813 | 42.95% |
| Top 100 | 1904 | 786 | 1118 | 41.28% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1744 | 729 | 1015 | 41.80% | -0.26% | -1.26% | -2.21% | 1169 | 52.61% |
| avoid | 14192 | 7058 | 7134 | 49.73% | -0.09% | -0.47% | -0.77% | 11688 | 52.09% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.