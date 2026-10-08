# Performance Decision Audit - 2026-10-08

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.76%** (9926 evaluated)
- Benchmark-adjusted success rate: **51.26%** (8182 evaluated)
- Selected raw success rate: **44.74%**
- Non-selected raw success rate: **46.93%**
- Selected benchmark-adjusted success rate: **43.51%**
- Non-selected benchmark-adjusted success rate: **51.93%**
- Benchmark coverage: **82.43%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 47.58% (269 eval); 100-199: 52.55% (666 eval); 200+: 46.3% (8991 eval)

## Return Horizons

- Close T+1 success rate: **41.45%**
- Close T+3 success rate: **43.78%**
- Close T+5 success rate: **44.13%**
- Excess T+1 success rate: **47.63%**
- Excess T+3 success rate: **44.28%**
- Excess T+5 success rate: **43.01%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
