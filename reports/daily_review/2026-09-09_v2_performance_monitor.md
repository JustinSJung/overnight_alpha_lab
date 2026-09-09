# V2 Performance Monitor - 2026-09-09

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **4361**
- V2 success count: **1904**
- V2 failure count: **2457**
- V2 raw success rate: **43.66%**
- V2 benchmark-adjusted evaluated cases: **4361**
- V2 benchmark-adjusted success rate: **51.30%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.46%**
- V2 average excess_t1_return: **-0.01%**
- Selected-pick evaluated cases: **476**
- Selected-pick success rate: **45.80%**
- Non-selected evaluated cases: **3885**
- Non-selected success rate: **43.40%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 279 | 134 | 145 | 48.03% |
| Top 20 | 476 | 218 | 258 | 45.80% |
| Top 50 | 702 | 313 | 389 | 44.59% |
| Top 100 | 1035 | 429 | 606 | 41.45% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 736 | 320 | 416 | 43.48% | -0.06% | -0.49% | -0.89% | 736 | 44.16% |
| avoid | 3625 | 1584 | 2041 | 43.70% | 0.56% | 2.14% | 3.21% | 3625 | 52.74% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.