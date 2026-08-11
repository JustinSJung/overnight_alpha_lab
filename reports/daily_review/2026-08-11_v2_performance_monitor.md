# V2 Performance Monitor - 2026-08-11

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **1722**
- V2 success count: **707**
- V2 failure count: **1015**
- V2 raw success rate: **41.06%**
- V2 benchmark-adjusted evaluated cases: **1722**
- V2 benchmark-adjusted success rate: **53.14%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **1.04%**
- V2 average excess_t1_return: **-0.32%**
- Selected-pick evaluated cases: **182**
- Selected-pick success rate: **57.14%**
- Non-selected evaluated cases: **1540**
- Non-selected success rate: **39.16%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Positive market-relative signal / 시장 대비 긍정 신호**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 117 | 68 | 49 | 58.12% |
| Top 20 | 169 | 95 | 74 | 56.21% |
| Top 50 | 251 | 136 | 115 | 54.18% |
| Top 100 | 489 | 235 | 254 | 48.06% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 241 | 130 | 111 | 53.94% | 0.73% | 1.25% | 2.02% | 241 | 56.43% |
| avoid | 1481 | 577 | 904 | 38.96% | 1.09% | 2.55% | 4.80% | 1481 | 52.60% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.