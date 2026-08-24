# V2 Performance Monitor - 2026-08-24

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **2787**
- V2 success count: **1168**
- V2 failure count: **1619**
- V2 raw success rate: **41.91%**
- V2 benchmark-adjusted evaluated cases: **2787**
- V2 benchmark-adjusted success rate: **51.27%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.46%**
- V2 average excess_t1_return: **-0.36%**
- Selected-pick evaluated cases: **360**
- Selected-pick success rate: **46.67%**
- Non-selected evaluated cases: **2427**
- Non-selected success rate: **41.20%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 197 | 96 | 101 | 48.73% |
| Top 20 | 327 | 152 | 175 | 46.48% |
| Top 50 | 522 | 233 | 289 | 44.64% |
| Top 100 | 816 | 339 | 477 | 41.54% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 586 | 240 | 346 | 40.96% | -0.25% | -0.75% | -1.72% | 586 | 40.78% |
| avoid | 2201 | 928 | 1273 | 42.16% | 0.65% | 2.15% | 4.28% | 2201 | 54.07% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.