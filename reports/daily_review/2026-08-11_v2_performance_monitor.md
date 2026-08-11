# V2 Performance Monitor - 2026-08-11

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **1606**
- V2 success count: **655**
- V2 failure count: **951**
- V2 raw success rate: **40.78%**
- V2 benchmark-adjusted evaluated cases: **1606**
- V2 benchmark-adjusted success rate: **53.80%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **1.11%**
- V2 average excess_t1_return: **-0.35%**
- Selected-pick evaluated cases: **162**
- Selected-pick success rate: **59.26%**
- Non-selected evaluated cases: **1444**
- Non-selected success rate: **38.71%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Positive market-relative signal / 시장 대비 긍정 신호**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 107 | 64 | 43 | 59.81% |
| Top 20 | 149 | 87 | 62 | 58.39% |
| Top 50 | 201 | 117 | 84 | 58.21% |
| Top 100 | 435 | 214 | 221 | 49.20% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 187 | 109 | 78 | 58.29% | 1.09% | 1.14% | 1.83% | 187 | 62.03% |
| avoid | 1419 | 546 | 873 | 38.48% | 1.11% | 2.48% | 4.74% | 1419 | 52.71% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.