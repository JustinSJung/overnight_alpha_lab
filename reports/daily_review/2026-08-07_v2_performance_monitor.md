# V2 Performance Monitor - 2026-08-07

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **10307**
- V2 success count: **4413**
- V2 failure count: **5894**
- V2 raw success rate: **42.82%**
- V2 benchmark-adjusted evaluated cases: **7993**
- V2 benchmark-adjusted success rate: **51.91%**
- V2 benchmark coverage rate: **77.55%**
- V2 average close_t1_return: **0.52%**
- V2 average excess_t1_return: **-0.30%**
- Selected-pick evaluated cases: **701**
- Selected-pick success rate: **51.64%**
- Non-selected evaluated cases: **9606**
- Non-selected success rate: **42.17%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 101 | 49 | 52 | 48.51% |
| Top 20 | 204 | 106 | 98 | 51.96% |
| Top 50 | 453 | 226 | 227 | 49.89% |
| Top 100 | 635 | 323 | 312 | 50.87% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.