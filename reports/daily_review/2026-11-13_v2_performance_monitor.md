# V2 Performance Monitor - 2026-11-13

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **22533**
- V2 success count: **11140**
- V2 failure count: **11393**
- V2 raw success rate: **49.44%**
- V2 benchmark-adjusted evaluated cases: **17739**
- V2 benchmark-adjusted success rate: **51.71%**
- V2 benchmark coverage rate: **78.72%**
- V2 average close_t1_return: **-0.10%**
- V2 average excess_t1_return: **0.09%**
- Selected-pick evaluated cases: **1143**
- Selected-pick success rate: **44.27%**
- Non-selected evaluated cases: **21390**
- Non-selected success rate: **49.71%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 637 | 279 | 358 | 43.80% |
| Top 20 | 1141 | 506 | 635 | 44.35% |
| Top 50 | 1906 | 837 | 1069 | 43.91% |
| Top 100 | 2483 | 1063 | 1420 | 42.81% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2302 | 999 | 1303 | 43.40% | -0.17% | -0.95% | -1.89% | 1506 | 51.53% |
| avoid | 20231 | 10141 | 10090 | 50.13% | -0.09% | -0.42% | -1.23% | 16233 | 51.72% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.