# V2 Performance Monitor - 2026-10-14

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **10752**
- V2 success count: **5163**
- V2 failure count: **5589**
- V2 raw success rate: **48.02%**
- V2 benchmark-adjusted evaluated cases: **8970**
- V2 benchmark-adjusted success rate: **50.01%**
- V2 benchmark coverage rate: **83.43%**
- V2 average close_t1_return: **0.02%**
- V2 average excess_t1_return: **0.28%**
- Selected-pick evaluated cases: **814**
- Selected-pick success rate: **44.96%**
- Non-selected evaluated cases: **9938**
- Non-selected success rate: **48.27%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 447 | 205 | 242 | 45.86% |
| Top 20 | 810 | 366 | 444 | 45.19% |
| Top 50 | 1351 | 596 | 755 | 44.12% |
| Top 100 | 1862 | 790 | 1072 | 42.43% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1680 | 719 | 961 | 42.80% | -0.18% | -1.07% | -0.94% | 1304 | 51.99% |
| avoid | 9072 | 4444 | 4628 | 48.99% | 0.06% | 0.56% | 1.14% | 7666 | 49.67% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.