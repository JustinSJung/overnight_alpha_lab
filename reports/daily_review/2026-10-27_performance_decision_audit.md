# Performance Decision Audit - 2026-10-27

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.44%** (16308 evaluated)
- Benchmark-adjusted success rate: **50.73%** (13092 evaluated)
- Selected raw success rate: **43.93%**
- Non-selected raw success rate: **49.78%**
- Selected benchmark-adjusted success rate: **50.66%**
- Non-selected benchmark-adjusted success rate: **50.73%**
- Benchmark coverage: **80.28%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.52% (270 eval); 100-199: 54.72% (667 eval); 200+: 49.22% (15371 eval)

## Return Horizons

- Close T+1 success rate: **39.18%**
- Close T+3 success rate: **37.19%**
- Close T+5 success rate: **36.75%**
- Excess T+1 success rate: **50.63%**
- Excess T+3 success rate: **52.96%**
- Excess T+5 success rate: **54.34%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
