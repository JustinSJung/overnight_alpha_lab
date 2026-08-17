# Performance Decision Audit - 2026-08-17

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **42.93%** (26665 evaluated)
- Benchmark-adjusted success rate: **52.72%** (22377 evaluated)
- Selected raw success rate: **52.87%**
- Non-selected raw success rate: **42.04%**
- Selected benchmark-adjusted success rate: **58.8%**
- Non-selected benchmark-adjusted success rate: **52.12%**
- Benchmark coverage: **83.92%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 42.93% (26665 eval)

## Return Horizons

- Close T+1 success rate: **45.15%**
- Close T+3 success rate: **48.17%**
- Close T+5 success rate: **47.99%**
- Excess T+1 success rate: **48.64%**
- Excess T+3 success rate: **52.09%**
- Excess T+5 success rate: **51.83%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
