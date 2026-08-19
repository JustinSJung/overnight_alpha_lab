# Performance Decision Audit - 2026-08-19

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **42.6%** (31518 evaluated)
- Benchmark-adjusted success rate: **52.38%** (27230 evaluated)
- Selected raw success rate: **51.58%**
- Non-selected raw success rate: **41.73%**
- Selected benchmark-adjusted success rate: **56.29%**
- Non-selected benchmark-adjusted success rate: **51.96%**
- Benchmark coverage: **86.4%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 42.6% (31518 eval)

## Return Horizons

- Close T+1 success rate: **45.03%**
- Close T+3 success rate: **48.8%**
- Close T+5 success rate: **49.34%**
- Excess T+1 success rate: **48.07%**
- Excess T+3 success rate: **51.02%**
- Excess T+5 success rate: **50.46%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
