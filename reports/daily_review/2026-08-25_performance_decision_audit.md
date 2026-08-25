# Performance Decision Audit - 2026-08-25

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **42.36%** (42922 evaluated)
- Benchmark-adjusted success rate: **52.14%** (38634 evaluated)
- Selected raw success rate: **49.94%**
- Non-selected raw success rate: **41.54%**
- Selected benchmark-adjusted success rate: **52.67%**
- Non-selected benchmark-adjusted success rate: **52.08%**
- Benchmark coverage: **90.01%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 42.36% (42922 eval)

## Return Horizons

- Close T+1 success rate: **44.65%**
- Close T+3 success rate: **47.95%**
- Close T+5 success rate: **49.06%**
- Excess T+1 success rate: **47.01%**
- Excess T+3 success rate: **49.2%**
- Excess T+5 success rate: **48.0%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
