# Performance Decision Audit - 2026-08-29

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **42.36%** (3388 evaluated)
- Benchmark-adjusted success rate: **49.95%** (3129 evaluated)
- Selected raw success rate: **46.96%**
- Non-selected raw success rate: **41.8%**
- Selected benchmark-adjusted success rate: **47.79%**
- Non-selected benchmark-adjusted success rate: **50.23%**
- Benchmark coverage: **92.36%**
- Diagnosis: **overall_pool_noisy_selected_group_promising**
- Public metric recommendation: **selected_group_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.54% (274 eval); 100-199: 54.12% (704 eval); 200+: 38.22% (2410 eval)

## Return Horizons

- Close T+1 success rate: **43.49%**
- Close T+3 success rate: **47.25%**
- Close T+5 success rate: **47.15%**
- Excess T+1 success rate: **47.43%**
- Excess T+3 success rate: **46.3%**
- Excess T+5 success rate: **45.25%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
