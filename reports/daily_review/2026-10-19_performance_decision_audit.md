# Performance Decision Audit - 2026-10-19

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **48.23%** (13060 evaluated)
- Benchmark-adjusted success rate: **46.47%** (10604 evaluated)
- Selected raw success rate: **44.17%**
- Non-selected raw success rate: **48.53%**
- Selected benchmark-adjusted success rate: **51.74%**
- Non-selected benchmark-adjusted success rate: **46.14%**
- Benchmark coverage: **81.19%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.7% (269 eval); 100-199: 53.93% (675 eval); 200+: 47.9% (12116 eval)

## Return Horizons

- Close T+1 success rate: **40.01%**
- Close T+3 success rate: **38.9%**
- Close T+5 success rate: **39.14%**
- Excess T+1 success rate: **53.86%**
- Excess T+3 success rate: **55.06%**
- Excess T+5 success rate: **53.48%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
