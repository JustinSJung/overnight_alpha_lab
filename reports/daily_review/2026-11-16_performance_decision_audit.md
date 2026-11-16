# Performance Decision Audit - 2026-11-16

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.46%** (23811 evaluated)
- Benchmark-adjusted success rate: **51.49%** (17458 evaluated)
- Selected raw success rate: **43.66%**
- Non-selected raw success rate: **49.75%**
- Selected benchmark-adjusted success rate: **50.35%**
- Non-selected benchmark-adjusted success rate: **51.53%**
- Benchmark coverage: **73.32%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.31% (267 eval); 100-199: 53.75% (653 eval); 200+: 49.35% (22891 eval)

## Return Horizons

- Close T+1 success rate: **40.38%**
- Close T+3 success rate: **38.18%**
- Close T+5 success rate: **35.48%**
- Excess T+1 success rate: **49.99%**
- Excess T+3 success rate: **51.69%**
- Excess T+5 success rate: **53.98%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
