# Performance Decision Audit - 2026-10-02

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.87%** (8891 evaluated)
- Benchmark-adjusted success rate: **52.77%** (7592 evaluated)
- Selected raw success rate: **45.83%**
- Non-selected raw success rate: **46.96%**
- Selected benchmark-adjusted success rate: **44.51%**
- Non-selected benchmark-adjusted success rate: **53.56%**
- Benchmark coverage: **85.39%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.15% (270 eval); 100-199: 54.03% (657 eval); 200+: 46.23% (7964 eval)

## Return Horizons

- Close T+1 success rate: **41.97%**
- Close T+3 success rate: **42.92%**
- Close T+5 success rate: **42.53%**
- Excess T+1 success rate: **44.84%**
- Excess T+3 success rate: **43.51%**
- Excess T+5 success rate: **42.35%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
