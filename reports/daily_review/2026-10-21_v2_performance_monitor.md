# V2 Performance Monitor - 2026-10-21

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **13766**
- V2 success count: **6601**
- V2 failure count: **7165**
- V2 raw success rate: **47.95%**
- V2 benchmark-adjusted evaluated cases: **11396**
- V2 benchmark-adjusted success rate: **48.52%**
- V2 benchmark coverage rate: **82.78%**
- V2 average close_t1_return: **-0.03%**
- V2 average excess_t1_return: **0.43%**
- Selected-pick evaluated cases: **915**
- Selected-pick success rate: **45.03%**
- Non-selected evaluated cases: **12851**
- Non-selected success rate: **48.16%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 502 | 225 | 277 | 44.82% |
| Top 20 | 911 | 411 | 500 | 45.12% |
| Top 50 | 1467 | 649 | 818 | 44.24% |
| Top 100 | 1989 | 844 | 1145 | 42.43% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1798 | 769 | 1029 | 42.77% | -0.16% | -1.10% | -2.00% | 1329 | 52.52% |
| avoid | 11968 | 5832 | 6136 | 48.73% | -0.01% | 0.26% | 0.40% | 10067 | 47.99% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.