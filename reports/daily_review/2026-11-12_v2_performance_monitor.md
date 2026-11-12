# V2 Performance Monitor - 2026-11-12

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **22028**
- V2 success count: **10763**
- V2 failure count: **11265**
- V2 raw success rate: **48.86%**
- V2 benchmark-adjusted evaluated cases: **17093**
- V2 benchmark-adjusted success rate: **51.56%**
- V2 benchmark coverage rate: **77.60%**
- V2 average close_t1_return: **-0.09%**
- V2 average excess_t1_return: **0.08%**
- Selected-pick evaluated cases: **1125**
- Selected-pick success rate: **44.09%**
- Non-selected evaluated cases: **20903**
- Non-selected success rate: **49.12%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 624 | 273 | 351 | 43.75% |
| Top 20 | 1121 | 496 | 625 | 44.25% |
| Top 50 | 1854 | 808 | 1046 | 43.58% |
| Top 100 | 2433 | 1036 | 1397 | 42.58% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2233 | 962 | 1271 | 43.08% | -0.16% | -1.06% | -1.95% | 1433 | 51.36% |
| avoid | 19795 | 9801 | 9994 | 49.51% | -0.08% | -0.62% | -1.30% | 15660 | 51.58% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.