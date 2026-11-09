# Performance Decision Audit - 2026-11-09

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **50.92%** (20194 evaluated)
- Benchmark-adjusted success rate: **49.94%** (15374 evaluated)
- Selected raw success rate: **44.79%**
- Non-selected raw success rate: **51.27%**
- Selected benchmark-adjusted success rate: **54.34%**
- Non-selected benchmark-adjusted success rate: **49.77%**
- Benchmark coverage: **76.13%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.3% (265 eval); 100-199: 54.36% (653 eval); 200+: 50.84% (19276 eval)

## Return Horizons

- Close T+1 success rate: **38.93%**
- Close T+3 success rate: **36.42%**
- Close T+5 success rate: **34.93%**
- Excess T+1 success rate: **52.07%**
- Excess T+3 success rate: **52.28%**
- Excess T+5 success rate: **50.58%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
