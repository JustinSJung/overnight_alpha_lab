# Performance Decision Audit - 2026-08-07

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **44.74%** (13158 evaluated)
- Benchmark-adjusted success rate: **52.69%** (8870 evaluated)
- Selected raw success rate: **50.52%**
- Non-selected raw success rate: **44.38%**
- Selected benchmark-adjusted success rate: **68.12%**
- Non-selected benchmark-adjusted success rate: **51.58%**
- Benchmark coverage: **67.41%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 44.74% (13158 eval)

## Return Horizons

- Close T+1 success rate: **41.01%**
- Close T+3 success rate: **40.57%**
- Close T+5 success rate: **36.73%**
- Excess T+1 success rate: **51.47%**
- Excess T+3 success rate: **55.25%**
- Excess T+5 success rate: **54.78%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
