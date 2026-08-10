# Performance Decision Audit - 2026-08-10

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **44.11%** (16448 evaluated)
- Benchmark-adjusted success rate: **52.98%** (12160 evaluated)
- Selected raw success rate: **52.27%**
- Non-selected raw success rate: **43.54%**
- Selected benchmark-adjusted success rate: **66.67%**
- Non-selected benchmark-adjusted success rate: **51.89%**
- Benchmark coverage: **73.93%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 44.11% (16448 eval)

## Return Horizons

- Close T+1 success rate: **42.54%**
- Close T+3 success rate: **43.01%**
- Close T+5 success rate: **40.38%**
- Excess T+1 success rate: **51.09%**
- Excess T+3 success rate: **55.2%**
- Excess T+5 success rate: **54.1%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
