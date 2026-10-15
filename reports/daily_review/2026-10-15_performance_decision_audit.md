# Performance Decision Audit - 2026-10-15

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.95%** (11660 evaluated)
- Benchmark-adjusted success rate: **47.28%** (9460 evaluated)
- Selected raw success rate: **43.9%**
- Non-selected raw success rate: **50.43%**
- Selected benchmark-adjusted success rate: **51.6%**
- Non-selected benchmark-adjusted success rate: **46.98%**
- Benchmark coverage: **81.13%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.33% (269 eval); 100-199: 53.51% (656 eval); 200+: 49.77% (10735 eval)

## Return Horizons

- Close T+1 success rate: **38.97%**
- Close T+3 success rate: **39.65%**
- Close T+5 success rate: **40.76%**
- Excess T+1 success rate: **53.27%**
- Excess T+3 success rate: **51.67%**
- Excess T+5 success rate: **49.53%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
