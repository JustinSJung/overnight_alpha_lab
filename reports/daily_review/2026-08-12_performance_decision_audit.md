# Performance Decision Audit - 2026-08-12

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **43.58%** (20261 evaluated)
- Benchmark-adjusted success rate: **52.96%** (15973 evaluated)
- Selected raw success rate: **53.23%**
- Non-selected raw success rate: **42.82%**
- Selected benchmark-adjusted success rate: **63.75%**
- Non-selected benchmark-adjusted success rate: **52.01%**
- Benchmark coverage: **78.84%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 43.58% (20261 eval)

## Return Horizons

- Close T+1 success rate: **43.99%**
- Close T+3 success rate: **45.54%**
- Close T+5 success rate: **43.86%**
- Excess T+1 success rate: **50.37%**
- Excess T+3 success rate: **54.34%**
- Excess T+5 success rate: **53.92%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
