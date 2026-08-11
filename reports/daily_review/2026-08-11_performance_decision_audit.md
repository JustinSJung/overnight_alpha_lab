# Performance Decision Audit - 2026-08-11

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **43.84%** (18299 evaluated)
- Benchmark-adjusted success rate: **53.02%** (14011 evaluated)
- Selected raw success rate: **53.01%**
- Non-selected raw success rate: **43.16%**
- Selected benchmark-adjusted success rate: **65.31%**
- Non-selected benchmark-adjusted success rate: **51.99%**
- Benchmark coverage: **76.57%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 43.84% (18299 eval)

## Return Horizons

- Close T+1 success rate: **43.36%**
- Close T+3 success rate: **44.2%**
- Close T+5 success rate: **42.22%**
- Excess T+1 success rate: **50.78%**
- Excess T+3 success rate: **55.04%**
- Excess T+5 success rate: **54.01%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
