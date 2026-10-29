# V2 Performance Monitor - 2026-10-20

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **12914**
- V2 success count: **6238**
- V2 failure count: **6676**
- V2 raw success rate: **48.30%**
- V2 benchmark-adjusted evaluated cases: **10864**
- V2 benchmark-adjusted success rate: **46.98%**
- V2 benchmark coverage rate: **84.13%**
- V2 average close_t1_return: **-0.03%**
- V2 average excess_t1_return: **0.53%**
- Selected-pick evaluated cases: **868**
- Selected-pick success rate: **44.47%**
- Non-selected evaluated cases: **12046**
- Non-selected success rate: **48.58%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Weak market-relative signal / 시장 대비 약한 신호**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 476 | 211 | 265 | 44.33% |
| Top 20 | 864 | 386 | 478 | 44.68% |
| Top 50 | 1401 | 613 | 788 | 43.75% |
| Top 100 | 1907 | 801 | 1106 | 42.00% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1727 | 736 | 991 | 42.62% | -0.17% | -1.11% | -2.06% | 1302 | 52.84% |
| avoid | 11187 | 5502 | 5685 | 49.18% | -0.01% | 0.32% | 0.56% | 9562 | 46.18% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.