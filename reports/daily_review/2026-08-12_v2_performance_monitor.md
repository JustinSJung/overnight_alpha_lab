# V2 Performance Monitor - 2026-08-12

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **1834**
- V2 success count: **740**
- V2 failure count: **1094**
- V2 raw success rate: **40.35%**
- V2 benchmark-adjusted evaluated cases: **1834**
- V2 benchmark-adjusted success rate: **52.07%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **1.05%**
- V2 average excess_t1_return: **-0.39%**
- Selected-pick evaluated cases: **202**
- Selected-pick success rate: **54.95%**
- Non-selected evaluated cases: **1632**
- Non-selected success rate: **38.54%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 127 | 72 | 55 | 56.69% |
| Top 20 | 189 | 102 | 87 | 53.97% |
| Top 50 | 301 | 153 | 148 | 50.83% |
| Top 100 | 551 | 256 | 295 | 46.46% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 303 | 151 | 152 | 49.83% | 0.49% | 1.48% | 2.24% | 303 | 48.51% |
| avoid | 1531 | 589 | 942 | 38.47% | 1.16% | 2.90% | 4.94% | 1531 | 52.78% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.