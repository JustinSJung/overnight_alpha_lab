# Performance Decision Audit - 2026-09-04

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **43.31%** (4168 evaluated)
- Benchmark-adjusted success rate: **50.5%** (3909 evaluated)
- Selected raw success rate: **45.8%**
- Non-selected raw success rate: **43.0%**
- Selected benchmark-adjusted success rate: **47.79%**
- Non-selected benchmark-adjusted success rate: **50.85%**
- Benchmark coverage: **93.79%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.12% (266 eval); 100-199: 54.04% (644 eval); 200+: 40.79% (3258 eval)

## Return Horizons

- Close T+1 success rate: **42.46%**
- Close T+3 success rate: **44.0%**
- Close T+5 success rate: **46.03%**
- Excess T+1 success rate: **47.86%**
- Excess T+3 success rate: **51.16%**
- Excess T+5 success rate: **48.43%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
