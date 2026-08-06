# Performance Decision Audit - 2026-08-06

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **45.24%** (11599 evaluated)
- Benchmark-adjusted success rate: **52.7%** (7311 evaluated)
- Selected raw success rate: **50.31%**
- Non-selected raw success rate: **44.94%**
- Selected benchmark-adjusted success rate: **69.05%**
- Non-selected benchmark-adjusted success rate: **51.6%**
- Benchmark coverage: **63.03%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 45.24% (11599 eval)

## Return Horizons

- Close T+1 success rate: **40.28%**
- Close T+3 success rate: **39.0%**
- Close T+5 success rate: **34.21%**
- Excess T+1 success rate: **51.51%**
- Excess T+3 success rate: **55.22%**
- Excess T+5 success rate: **55.38%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
