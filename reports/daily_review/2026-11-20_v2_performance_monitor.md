# V2 Performance Monitor - 2026-11-20

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **25499**
- V2 success count: **12658**
- V2 failure count: **12841**
- V2 raw success rate: **49.64%**
- V2 benchmark-adjusted evaluated cases: **19273**
- V2 benchmark-adjusted success rate: **52.07%**
- V2 benchmark coverage rate: **75.58%**
- V2 average close_t1_return: **-0.15%**
- V2 average excess_t1_return: **0.06%**
- Selected-pick evaluated cases: **1232**
- Selected-pick success rate: **44.16%**
- Non-selected evaluated cases: **24267**
- Non-selected success rate: **49.92%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 678 | 295 | 383 | 43.51% |
| Top 20 | 1228 | 544 | 684 | 44.30% |
| Top 50 | 2125 | 935 | 1190 | 44.00% |
| Top 100 | 2807 | 1188 | 1619 | 42.32% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2670 | 1137 | 1533 | 42.58% | -0.23% | -1.08% | -1.81% | 1771 | 52.85% |
| avoid | 22829 | 11521 | 11308 | 50.47% | -0.14% | -0.68% | -1.15% | 17502 | 51.99% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.