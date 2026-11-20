# Performance Decision Audit - 2026-11-20

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.65%** (25758 evaluated)
- Benchmark-adjusted success rate: **52.07%** (19273 evaluated)
- Selected raw success rate: **44.16%**
- Non-selected raw success rate: **49.93%**
- Selected benchmark-adjusted success rate: **50.7%**
- Non-selected benchmark-adjusted success rate: **52.12%**
- Benchmark coverage: **74.82%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 50.75% (201 eval); 100-199: 56.4% (594 eval); 200+: 49.48% (24963 eval)

## Return Horizons

- Close T+1 success rate: **40.12%**
- Close T+3 success rate: **36.8%**
- Close T+5 success rate: **35.0%**
- Excess T+1 success rate: **49.73%**
- Excess T+3 success rate: **53.27%**
- Excess T+5 success rate: **54.27%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
