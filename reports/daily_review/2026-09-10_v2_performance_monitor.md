# V2 Performance Monitor - 2026-09-10

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **4618**
- V2 success count: **2087**
- V2 failure count: **2531**
- V2 raw success rate: **45.19%**
- V2 benchmark-adjusted evaluated cases: **4618**
- V2 benchmark-adjusted success rate: **50.15%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.33%**
- V2 average excess_t1_return: **-0.01%**
- Selected-pick evaluated cases: **494**
- Selected-pick success rate: **44.53%**
- Non-selected evaluated cases: **4124**
- Non-selected success rate: **45.27%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 285 | 132 | 153 | 46.32% |
| Top 20 | 494 | 220 | 274 | 44.53% |
| Top 50 | 729 | 316 | 413 | 43.35% |
| Top 100 | 1054 | 434 | 620 | 41.18% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 763 | 324 | 439 | 42.46% | -0.11% | -0.48% | -0.80% | 763 | 45.74% |
| avoid | 3855 | 1763 | 2092 | 45.73% | 0.42% | 1.91% | 3.15% | 3855 | 51.02% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.