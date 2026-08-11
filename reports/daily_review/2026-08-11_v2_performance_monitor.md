# V2 Performance Monitor - 2026-08-11

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **1723**
- V2 success count: **702**
- V2 failure count: **1021**
- V2 raw success rate: **40.74%**
- V2 benchmark-adjusted evaluated cases: **1723**
- V2 benchmark-adjusted success rate: **52.93%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **1.09%**
- V2 average excess_t1_return: **-0.31%**
- Selected-pick evaluated cases: **182**
- Selected-pick success rate: **57.69%**
- Non-selected evaluated cases: **1541**
- Non-selected success rate: **38.74%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 117 | 68 | 49 | 58.12% |
| Top 20 | 169 | 96 | 73 | 56.80% |
| Top 50 | 251 | 137 | 114 | 54.58% |
| Top 100 | 489 | 237 | 252 | 48.47% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 241 | 132 | 109 | 54.77% | 0.78% | 1.29% | 2.04% | 241 | 56.02% |
| avoid | 1482 | 570 | 912 | 38.46% | 1.14% | 2.59% | 4.85% | 1482 | 52.43% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.