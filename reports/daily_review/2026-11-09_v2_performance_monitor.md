# V2 Performance Monitor - 2026-11-09

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **19799**
- V2 success count: **10087**
- V2 failure count: **9712**
- V2 raw success rate: **50.95%**
- V2 benchmark-adjusted evaluated cases: **15374**
- V2 benchmark-adjusted success rate: **49.94%**
- V2 benchmark coverage rate: **77.65%**
- V2 average close_t1_return: **-0.32%**
- V2 average excess_t1_return: **0.30%**
- Selected-pick evaluated cases: **1069**
- Selected-pick success rate: **44.81%**
- Non-selected evaluated cases: **18730**
- Non-selected success rate: **51.30%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 598 | 266 | 332 | 44.48% |
| Top 20 | 1065 | 479 | 586 | 44.98% |
| Top 50 | 1702 | 745 | 957 | 43.77% |
| Top 100 | 2215 | 939 | 1276 | 42.39% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2026 | 868 | 1158 | 42.84% | -0.18% | -1.09% | -1.99% | 1295 | 56.45% |
| avoid | 17773 | 9219 | 8554 | 51.87% | -0.34% | -0.69% | -1.03% | 14079 | 49.34% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.