# V2 Performance Monitor - 2026-08-23

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **2628**
- V2 success count: **1101**
- V2 failure count: **1527**
- V2 raw success rate: **41.89%**
- V2 benchmark-adjusted evaluated cases: **2628**
- V2 benchmark-adjusted success rate: **51.79%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.47%**
- V2 average excess_t1_return: **-0.45%**
- Selected-pick evaluated cases: **340**
- Selected-pick success rate: **46.47%**
- Non-selected evaluated cases: **2288**
- Non-selected success rate: **41.22%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 187 | 91 | 96 | 48.66% |
| Top 20 | 307 | 142 | 165 | 46.25% |
| Top 50 | 502 | 224 | 278 | 44.62% |
| Top 100 | 805 | 335 | 470 | 41.61% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 565 | 230 | 335 | 40.71% | -0.32% | -0.79% | -0.87% | 565 | 40.53% |
| avoid | 2063 | 871 | 1192 | 42.22% | 0.69% | 2.28% | 4.64% | 2063 | 54.87% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.