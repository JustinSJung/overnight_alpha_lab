# V2 Performance Monitor - 2026-10-16

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **11816**
- V2 success count: **5684**
- V2 failure count: **6132**
- V2 raw success rate: **48.10%**
- V2 benchmark-adjusted evaluated cases: **10082**
- V2 benchmark-adjusted success rate: **48.09%**
- V2 benchmark coverage rate: **85.32%**
- V2 average close_t1_return: **-0.09%**
- V2 average excess_t1_return: **0.47%**
- Selected-pick evaluated cases: **816**
- Selected-pick success rate: **44.98%**
- Non-selected evaluated cases: **11000**
- Non-selected success rate: **48.34%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 451 | 202 | 249 | 44.79% |
| Top 20 | 812 | 367 | 445 | 45.20% |
| Top 50 | 1347 | 586 | 761 | 43.50% |
| Top 100 | 1847 | 778 | 1069 | 42.12% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1675 | 707 | 968 | 42.21% | -0.19% | -1.15% | -2.12% | 1313 | 52.48% |
| avoid | 10141 | 4977 | 5164 | 49.08% | -0.07% | 0.06% | 0.66% | 8769 | 47.43% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.