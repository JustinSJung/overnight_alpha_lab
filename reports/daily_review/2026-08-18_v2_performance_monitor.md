# V2 Performance Monitor - 2026-08-18

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **2250**
- V2 success count: **898**
- V2 failure count: **1352**
- V2 raw success rate: **39.91%**
- V2 benchmark-adjusted evaluated cases: **2250**
- V2 benchmark-adjusted success rate: **50.36%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.70%**
- V2 average excess_t1_return: **-0.39%**
- Selected-pick evaluated cases: **282**
- Selected-pick success rate: **47.16%**
- Non-selected evaluated cases: **1968**
- Non-selected success rate: **38.87%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 157 | 77 | 80 | 49.04% |
| Top 20 | 249 | 117 | 132 | 46.99% |
| Top 50 | 440 | 198 | 242 | 45.00% |
| Top 100 | 743 | 309 | 434 | 41.59% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 503 | 204 | 299 | 40.56% | -0.31% | 0.11% | 0.98% | 503 | 40.36% |
| avoid | 1747 | 694 | 1053 | 39.73% | 0.99% | 2.92% | 5.27% | 1747 | 53.23% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.