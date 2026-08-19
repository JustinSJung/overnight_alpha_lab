# V2 Performance Monitor - 2026-08-19

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **2353**
- V2 success count: **954**
- V2 failure count: **1399**
- V2 raw success rate: **40.54%**
- V2 benchmark-adjusted evaluated cases: **2353**
- V2 benchmark-adjusted success rate: **50.28%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.63%**
- V2 average excess_t1_return: **-0.30%**
- Selected-pick evaluated cases: **302**
- Selected-pick success rate: **46.69%**
- Non-selected evaluated cases: **2051**
- Non-selected success rate: **39.64%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 167 | 82 | 85 | 49.10% |
| Top 20 | 269 | 125 | 144 | 46.47% |
| Top 50 | 464 | 207 | 257 | 44.61% |
| Top 100 | 767 | 318 | 449 | 41.46% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 527 | 213 | 314 | 40.42% | -0.32% | -0.23% | 0.01% | 527 | 41.37% |
| avoid | 1826 | 741 | 1085 | 40.58% | 0.90% | 2.84% | 5.09% | 1826 | 52.85% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.