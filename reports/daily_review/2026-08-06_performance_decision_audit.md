# Performance Decision Audit - 2026-08-06

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.71%** (8717 evaluated)
- Benchmark-adjusted success rate: **52.56%** (4429 evaluated)
- Selected raw success rate: **48.51%**
- Non-selected raw success rate: **46.62%**
- Selected benchmark-adjusted success rate: **70.43%**
- Non-selected benchmark-adjusted success rate: **51.46%**
- Benchmark coverage: **50.81%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 46.71% (8717 eval)

## Return Horizons

- Close T+1 success rate: **38.22%**
- Close T+3 success rate: **35.26%**
- Close T+5 success rate: **29.75%**
- Excess T+1 success rate: **51.91%**
- Excess T+3 success rate: **56.52%**
- Excess T+5 success rate: **58.67%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
