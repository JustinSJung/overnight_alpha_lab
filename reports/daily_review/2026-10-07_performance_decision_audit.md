# Performance Decision Audit - 2026-10-07

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.47%** (9512 evaluated)
- Benchmark-adjusted success rate: **51.53%** (7832 evaluated)
- Selected raw success rate: **45.76%**
- Non-selected raw success rate: **46.53%**
- Selected benchmark-adjusted success rate: **42.05%**
- Non-selected benchmark-adjusted success rate: **52.35%**
- Benchmark coverage: **82.34%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.67% (263 eval); 100-199: 52.34% (640 eval); 200+: 45.96% (8609 eval)

## Return Horizons

- Close T+1 success rate: **42.07%**
- Close T+3 success rate: **44.05%**
- Close T+5 success rate: **43.9%**
- Excess T+1 success rate: **46.45%**
- Excess T+3 success rate: **42.96%**
- Excess T+5 success rate: **42.09%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
