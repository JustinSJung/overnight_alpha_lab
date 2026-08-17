# V2 Performance Monitor - 2026-08-17

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **2037**
- V2 success count: **818**
- V2 failure count: **1219**
- V2 raw success rate: **40.16%**
- V2 benchmark-adjusted evaluated cases: **2037**
- V2 benchmark-adjusted success rate: **51.64%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **1.00%**
- V2 average excess_t1_return: **-0.51%**
- Selected-pick evaluated cases: **242**
- Selected-pick success rate: **52.07%**
- Non-selected evaluated cases: **1795**
- Non-selected success rate: **38.55%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 147 | 77 | 70 | 52.38% |
| Top 20 | 229 | 117 | 112 | 51.09% |
| Top 50 | 390 | 189 | 201 | 48.46% |
| Top 100 | 643 | 293 | 350 | 45.57% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 395 | 188 | 207 | 47.59% | 0.37% | 0.55% | 2.14% | 395 | 41.52% |
| avoid | 1642 | 630 | 1012 | 38.37% | 1.15% | 2.98% | 5.34% | 1642 | 54.08% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.