# Performance Decision Audit - 2026-08-11

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **43.87%** (18296 evaluated)
- Benchmark-adjusted success rate: **53.06%** (14008 evaluated)
- Selected raw success rate: **52.93%**
- Non-selected raw success rate: **43.2%**
- Selected benchmark-adjusted success rate: **65.31%**
- Non-selected benchmark-adjusted success rate: **52.03%**
- Benchmark coverage: **76.56%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 43.87% (18296 eval)

## Return Horizons

- Close T+1 success rate: **43.28%**
- Close T+3 success rate: **44.19%**
- Close T+5 success rate: **42.2%**
- Excess T+1 success rate: **50.8%**
- Excess T+3 success rate: **55.02%**
- Excess T+5 success rate: **54.01%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
