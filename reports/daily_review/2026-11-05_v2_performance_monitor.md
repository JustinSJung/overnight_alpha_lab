# V2 Performance Monitor - 2026-11-05

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **18668**
- V2 success count: **9109**
- V2 failure count: **9559**
- V2 raw success rate: **48.79%**
- V2 benchmark-adjusted evaluated cases: **14866**
- V2 benchmark-adjusted success rate: **51.86%**
- V2 benchmark coverage rate: **79.63%**
- V2 average close_t1_return: **-0.09%**
- V2 average excess_t1_return: **0.03%**
- Selected-pick evaluated cases: **1017**
- Selected-pick success rate: **43.85%**
- Non-selected evaluated cases: **17651**
- Non-selected success rate: **49.08%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 567 | 248 | 319 | 43.74% |
| Top 20 | 1013 | 446 | 567 | 44.03% |
| Top 50 | 1613 | 700 | 913 | 43.40% |
| Top 100 | 2151 | 897 | 1254 | 41.70% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1939 | 820 | 1119 | 42.29% | -0.19% | -1.16% | -2.06% | 1279 | 52.78% |
| avoid | 16729 | 8289 | 8440 | 49.55% | -0.08% | -0.40% | -0.82% | 13587 | 51.78% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.