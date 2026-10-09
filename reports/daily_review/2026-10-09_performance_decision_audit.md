# Performance Decision Audit - 2026-10-09

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.83%** (9806 evaluated)
- Benchmark-adjusted success rate: **51.3%** (8072 evaluated)
- Selected raw success rate: **45.34%**
- Non-selected raw success rate: **46.95%**
- Selected benchmark-adjusted success rate: **43.92%**
- Non-selected benchmark-adjusted success rate: **51.93%**
- Benchmark coverage: **82.32%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.53% (272 eval); 100-199: 54.5% (666 eval); 200+: 46.2% (8868 eval)

## Return Horizons

- Close T+1 success rate: **41.52%**
- Close T+3 success rate: **43.79%**
- Close T+5 success rate: **44.11%**
- Excess T+1 success rate: **47.53%**
- Excess T+3 success rate: **44.1%**
- Excess T+5 success rate: **42.79%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
