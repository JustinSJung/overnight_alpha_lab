# Performance Decision Audit - 2026-10-12

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **47.3%** (10580 evaluated)
- Benchmark-adjusted success rate: **51.13%** (8392 evaluated)
- Selected raw success rate: **45.1%**
- Non-selected raw success rate: **47.48%**
- Selected benchmark-adjusted success rate: **46.23%**
- Non-selected benchmark-adjusted success rate: **51.53%**
- Benchmark coverage: **79.32%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.36% (275 eval); 100-199: 54.14% (713 eval); 200+: 46.76% (9592 eval)

## Return Horizons

- Close T+1 success rate: **40.46%**
- Close T+3 success rate: **42.68%**
- Close T+5 success rate: **44.0%**
- Excess T+1 success rate: **49.27%**
- Excess T+3 success rate: **46.62%**
- Excess T+5 success rate: **43.42%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
