# V2 Performance Monitor - 2026-09-16

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **5779**
- V2 success count: **2711**
- V2 failure count: **3068**
- V2 raw success rate: **46.91%**
- V2 benchmark-adjusted evaluated cases: **5779**
- V2 benchmark-adjusted success rate: **49.06%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.20%**
- V2 average excess_t1_return: **0.13%**
- Selected-pick evaluated cases: **567**
- Selected-pick success rate: **44.44%**
- Non-selected evaluated cases: **5212**
- Non-selected success rate: **47.18%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 323 | 149 | 174 | 46.13% |
| Top 20 | 567 | 252 | 315 | 44.44% |
| Top 50 | 825 | 355 | 470 | 43.03% |
| Top 100 | 1155 | 475 | 680 | 41.13% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 856 | 362 | 494 | 42.29% | -0.19% | -0.62% | -0.85% | 856 | 46.96% |
| avoid | 4923 | 2349 | 2574 | 47.71% | 0.27% | 1.18% | 2.13% | 4923 | 49.42% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.