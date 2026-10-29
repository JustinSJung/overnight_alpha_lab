# V2 Performance Monitor - 2026-10-15

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **11255**
- V2 success count: **5624**
- V2 failure count: **5631**
- V2 raw success rate: **49.97%**
- V2 benchmark-adjusted evaluated cases: **9460**
- V2 benchmark-adjusted success rate: **47.28%**
- V2 benchmark coverage rate: **84.05%**
- V2 average close_t1_return: **-0.17%**
- V2 average excess_t1_return: **0.52%**
- Selected-pick evaluated cases: **847**
- Selected-pick success rate: **43.92%**
- Non-selected evaluated cases: **10408**
- Non-selected success rate: **50.46%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Weak market-relative signal / 시장 대비 약한 신호**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 465 | 201 | 264 | 43.23% |
| Top 20 | 843 | 372 | 471 | 44.13% |
| Top 50 | 1401 | 607 | 794 | 43.33% |
| Top 100 | 1923 | 800 | 1123 | 41.60% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1733 | 729 | 1004 | 42.07% | -0.24% | -1.18% | -1.85% | 1334 | 53.60% |
| avoid | 9522 | 4895 | 4627 | 51.41% | -0.16% | 0.35% | 1.06% | 8126 | 46.25% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.