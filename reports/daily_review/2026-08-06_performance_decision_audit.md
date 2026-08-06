# Performance Decision Audit - 2026-08-06

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **45.18%** (11600 evaluated)
- Benchmark-adjusted success rate: **52.67%** (7312 evaluated)
- Selected raw success rate: **50.16%**
- Non-selected raw success rate: **44.89%**
- Selected benchmark-adjusted success rate: **68.18%**
- Non-selected benchmark-adjusted success rate: **51.62%**
- Benchmark coverage: **63.03%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 45.18% (11600 eval)

## Return Horizons

- Close T+1 success rate: **40.44%**
- Close T+3 success rate: **38.99%**
- Close T+5 success rate: **34.23%**
- Excess T+1 success rate: **51.24%**
- Excess T+3 success rate: **55.14%**
- Excess T+5 success rate: **55.38%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
