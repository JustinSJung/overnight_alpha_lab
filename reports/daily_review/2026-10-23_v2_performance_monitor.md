# V2 Performance Monitor - 2026-10-23

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **14605**
- V2 success count: **7246**
- V2 failure count: **7359**
- V2 raw success rate: **49.61%**
- V2 benchmark-adjusted evaluated cases: **12247**
- V2 benchmark-adjusted success rate: **47.33%**
- V2 benchmark coverage rate: **83.85%**
- V2 average close_t1_return: **-0.13%**
- V2 average excess_t1_return: **0.52%**
- Selected-pick evaluated cases: **946**
- Selected-pick success rate: **43.97%**
- Non-selected evaluated cases: **13659**
- Non-selected success rate: **50.00%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Weak market-relative signal / 시장 대비 약한 신호**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 520 | 225 | 295 | 43.27% |
| Top 20 | 942 | 416 | 526 | 44.16% |
| Top 50 | 1507 | 654 | 853 | 43.40% |
| Top 100 | 2026 | 847 | 1179 | 41.81% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1838 | 776 | 1062 | 42.22% | -0.19% | -1.07% | -1.97% | 1370 | 54.09% |
| avoid | 12767 | 6470 | 6297 | 50.68% | -0.12% | -0.08% | 0.22% | 10877 | 46.48% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.