# Performance Decision Audit - 2026-08-09

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **44.41%** (14716 evaluated)
- Benchmark-adjusted success rate: **52.77%** (10428 evaluated)
- Selected raw success rate: **51.1%**
- Non-selected raw success rate: **43.97%**
- Selected benchmark-adjusted success rate: **67.81%**
- Non-selected benchmark-adjusted success rate: **51.64%**
- Benchmark coverage: **70.86%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 44.41% (14716 eval)

## Return Horizons

- Close T+1 success rate: **41.57%**
- Close T+3 success rate: **41.83%**
- Close T+5 success rate: **38.47%**
- Excess T+1 success rate: **51.41%**
- Excess T+3 success rate: **55.21%**
- Excess T+5 success rate: **54.32%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
