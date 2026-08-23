# Performance Decision Audit - 2026-08-23

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **42.46%** (36883 evaluated)
- Benchmark-adjusted success rate: **52.31%** (32595 evaluated)
- Selected raw success rate: **50.67%**
- Non-selected raw success rate: **41.61%**
- Selected benchmark-adjusted success rate: **54.18%**
- Non-selected benchmark-adjusted success rate: **52.1%**
- Benchmark coverage: **88.37%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 42.46% (36883 eval)

## Return Horizons

- Close T+1 success rate: **44.84%**
- Close T+3 success rate: **48.46%**
- Close T+5 success rate: **49.66%**
- Excess T+1 success rate: **47.4%**
- Excess T+3 success rate: **50.07%**
- Excess T+5 success rate: **49.1%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
