# Performance Decision Audit - 2026-10-14

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **48.08%** (11146 evaluated)
- Benchmark-adjusted success rate: **50.01%** (8970 evaluated)
- Selected raw success rate: **44.99%**
- Non-selected raw success rate: **48.32%**
- Selected benchmark-adjusted success rate: **48.43%**
- Non-selected benchmark-adjusted success rate: **50.13%**
- Benchmark coverage: **80.48%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.48% (264 eval); 100-199: 54.45% (641 eval); 200+: 47.67% (10241 eval)

## Return Horizons

- Close T+1 success rate: **39.94%**
- Close T+3 success rate: **40.46%**
- Close T+5 success rate: **41.92%**
- Excess T+1 success rate: **50.88%**
- Excess T+3 success rate: **49.78%**
- Excess T+5 success rate: **47.42%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
