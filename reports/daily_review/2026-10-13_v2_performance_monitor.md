# V2 Performance Monitor - 2026-10-13

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **10233**
- V2 success count: **4996**
- V2 failure count: **5237**
- V2 raw success rate: **48.82%**
- V2 benchmark-adjusted evaluated cases: **8517**
- V2 benchmark-adjusted success rate: **49.98%**
- V2 benchmark coverage rate: **83.23%**
- V2 average close_t1_return: **-0.08%**
- V2 average excess_t1_return: **0.22%**
- Selected-pick evaluated cases: **810**
- Selected-pick success rate: **44.44%**
- Non-selected evaluated cases: **9423**
- Non-selected success rate: **49.20%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 447 | 200 | 247 | 44.74% |
| Top 20 | 806 | 360 | 446 | 44.67% |
| Top 50 | 1352 | 587 | 765 | 43.42% |
| Top 100 | 1875 | 785 | 1090 | 41.87% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1685 | 708 | 977 | 42.02% | -0.28% | -1.13% | -0.73% | 1336 | 51.57% |
| avoid | 8548 | 4288 | 4260 | 50.16% | -0.04% | 0.63% | 1.15% | 7181 | 49.69% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.