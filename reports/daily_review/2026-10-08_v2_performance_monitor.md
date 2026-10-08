# V2 Performance Monitor - 2026-10-08

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **9525**
- V2 success count: **4444**
- V2 failure count: **5081**
- V2 raw success rate: **46.66%**
- V2 benchmark-adjusted evaluated cases: **8182**
- V2 benchmark-adjusted success rate: **51.26%**
- V2 benchmark coverage rate: **85.90%**
- V2 average close_t1_return: **0.20%**
- V2 average excess_t1_return: **0.00%**
- Selected-pick evaluated cases: **775**
- Selected-pick success rate: **44.77%**
- Non-selected evaluated cases: **8750**
- Non-selected success rate: **46.82%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 425 | 192 | 233 | 45.18% |
| Top 20 | 774 | 347 | 427 | 44.83% |
| Top 50 | 1284 | 575 | 709 | 44.78% |
| Top 100 | 1795 | 768 | 1027 | 42.79% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1565 | 691 | 874 | 44.15% | -0.01% | -0.03% | -0.01% | 1427 | 46.53% |
| avoid | 7960 | 3753 | 4207 | 47.15% | 0.24% | 0.91% | 1.35% | 6755 | 52.26% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.