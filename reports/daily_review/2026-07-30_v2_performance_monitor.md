# V2 Performance Monitor - 2026-07-30

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **3064**
- V2 success count: **1457**
- V2 failure count: **1607**
- V2 raw success rate: **47.55%**
- V2 benchmark-adjusted evaluated cases: **750**
- V2 benchmark-adjusted success rate: **47.73%**
- V2 benchmark coverage rate: **24.48%**
- V2 average close_t1_return: **-0.27%**
- V2 average excess_t1_return: **0.70%**
- Selected-pick evaluated cases: **187**
- Selected-pick success rate: **49.20%**
- Non-selected evaluated cases: **2877**
- Non-selected success rate: **47.45%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Benchmark coverage still low / 시장 기준 커버리지 낮음**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 48 | 22 | 26 | 45.83% |
| Top 20 | 86 | 39 | 47 | 45.35% |
| Top 50 | 157 | 71 | 86 | 45.22% |
| Top 100 | 187 | 92 | 95 | 49.20% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.