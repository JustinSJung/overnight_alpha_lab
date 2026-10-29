# V2 Performance Monitor - 2026-10-09

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **9399**
- V2 success count: **4389**
- V2 failure count: **5010**
- V2 raw success rate: **46.70%**
- V2 benchmark-adjusted evaluated cases: **8072**
- V2 benchmark-adjusted success rate: **51.30%**
- V2 benchmark coverage rate: **85.88%**
- V2 average close_t1_return: **0.19%**
- V2 average excess_t1_return: **0.02%**
- Selected-pick evaluated cases: **756**
- Selected-pick success rate: **45.37%**
- Non-selected evaluated cases: **8643**
- Non-selected success rate: **46.81%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 412 | 188 | 224 | 45.63% |
| Top 20 | 755 | 343 | 412 | 45.43% |
| Top 50 | 1260 | 563 | 697 | 44.68% |
| Top 100 | 1748 | 749 | 999 | 42.85% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1537 | 669 | 868 | 43.53% | -0.04% | 0.04% | 0.14% | 1396 | 46.06% |
| avoid | 7862 | 3720 | 4142 | 47.32% | 0.24% | 0.93% | 1.36% | 6676 | 52.40% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.