# Performance Decision Audit - 2026-11-19

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.97%** (25329 evaluated)
- Benchmark-adjusted success rate: **51.35%** (18612 evaluated)
- Selected raw success rate: **43.15%**
- Non-selected raw success rate: **50.32%**
- Selected benchmark-adjusted success rate: **51.12%**
- Non-selected benchmark-adjusted success rate: **51.36%**
- Benchmark coverage: **73.48%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 50.75% (201 eval); 100-199: 54.12% (691 eval); 200+: 49.85% (24437 eval)

## Return Horizons

- Close T+1 success rate: **39.49%**
- Close T+3 success rate: **36.69%**
- Close T+5 success rate: **35.14%**
- Excess T+1 success rate: **50.6%**
- Excess T+3 success rate: **54.31%**
- Excess T+5 success rate: **54.26%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
