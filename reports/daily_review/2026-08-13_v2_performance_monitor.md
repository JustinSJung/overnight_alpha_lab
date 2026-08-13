# V2 Performance Monitor - 2026-08-13

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **1946**
- V2 success count: **785**
- V2 failure count: **1161**
- V2 raw success rate: **40.34%**
- V2 benchmark-adjusted evaluated cases: **1946**
- V2 benchmark-adjusted success rate: **51.85%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **1.02%**
- V2 average excess_t1_return: **-0.48%**
- Selected-pick evaluated cases: **222**
- Selected-pick success rate: **53.15%**
- Non-selected evaluated cases: **1724**
- Non-selected success rate: **38.69%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 137 | 75 | 62 | 54.74% |
| Top 20 | 209 | 109 | 100 | 52.15% |
| Top 50 | 351 | 173 | 178 | 49.29% |
| Top 100 | 604 | 277 | 327 | 45.86% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 356 | 172 | 184 | 48.31% | 0.45% | 0.85% | 1.91% | 356 | 43.54% |
| avoid | 1590 | 613 | 977 | 38.55% | 1.15% | 2.97% | 5.10% | 1590 | 53.71% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.