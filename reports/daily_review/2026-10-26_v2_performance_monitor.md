# V2 Performance Monitor - 2026-10-26

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **15178**
- V2 success count: **7612**
- V2 failure count: **7566**
- V2 raw success rate: **50.15%**
- V2 benchmark-adjusted evaluated cases: **12492**
- V2 benchmark-adjusted success rate: **48.05%**
- V2 benchmark coverage rate: **82.30%**
- V2 average close_t1_return: **-0.15%**
- V2 average excess_t1_return: **0.46%**
- Selected-pick evaluated cases: **963**
- Selected-pick success rate: **43.41%**
- Non-selected evaluated cases: **14215**
- Non-selected success rate: **50.61%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 531 | 226 | 305 | 42.56% |
| Top 20 | 959 | 418 | 541 | 43.59% |
| Top 50 | 1525 | 655 | 870 | 42.95% |
| Top 100 | 2054 | 853 | 1201 | 41.53% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1856 | 778 | 1078 | 41.92% | -0.21% | -1.16% | -1.98% | 1349 | 54.04% |
| avoid | 13322 | 6834 | 6488 | 51.30% | -0.14% | -0.23% | -0.08% | 11143 | 47.32% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.