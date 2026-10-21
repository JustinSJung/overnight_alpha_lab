# Performance Decision Audit - 2026-10-21

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **48.0%** (14171 evaluated)
- Benchmark-adjusted success rate: **48.52%** (11396 evaluated)
- Selected raw success rate: **45.05%**
- Non-selected raw success rate: **48.2%**
- Selected benchmark-adjusted success rate: **49.92%**
- Non-selected benchmark-adjusted success rate: **48.44%**
- Benchmark coverage: **80.42%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.89% (270 eval); 100-199: 54.22% (675 eval); 200+: 47.66% (13226 eval)

## Return Horizons

- Close T+1 success rate: **40.3%**
- Close T+3 success rate: **40.09%**
- Close T+5 success rate: **38.78%**
- Excess T+1 success rate: **51.98%**
- Excess T+3 success rate: **54.42%**
- Excess T+5 success rate: **55.73%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
