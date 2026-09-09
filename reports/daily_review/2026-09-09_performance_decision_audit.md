# Performance Decision Audit - 2026-09-09

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **44.13%** (4752 evaluated)
- Benchmark-adjusted success rate: **51.61%** (4493 evaluated)
- Selected raw success rate: **45.74%**
- Non-selected raw success rate: **43.95%**
- Selected benchmark-adjusted success rate: **46.78%**
- Non-selected benchmark-adjusted success rate: **52.19%**
- Benchmark coverage: **94.55%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 47.92% (265 eval); 100-199: 53.46% (651 eval); 200+: 42.28% (3836 eval)

## Return Horizons

- Close T+1 success rate: **41.93%**
- Close T+3 success rate: **44.87%**
- Close T+5 success rate: **45.01%**
- Excess T+1 success rate: **46.64%**
- Excess T+3 success rate: **46.77%**
- Excess T+5 success rate: **45.46%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
