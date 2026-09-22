# Performance Decision Audit - 2026-09-22

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.02%** (7204 evaluated)
- Benchmark-adjusted success rate: **51.79%** (6577 evaluated)
- Selected raw success rate: **44.96%**
- Non-selected raw success rate: **46.12%**
- Selected benchmark-adjusted success rate: **46.62%**
- Non-selected benchmark-adjusted success rate: **52.31%**
- Benchmark coverage: **91.3%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.33% (269 eval); 100-199: 54.1% (647 eval); 200+: 45.09% (6288 eval)

## Return Horizons

- Close T+1 success rate: **41.43%**
- Close T+3 success rate: **42.78%**
- Close T+5 success rate: **42.08%**
- Excess T+1 success rate: **46.65%**
- Excess T+3 success rate: **44.38%**
- Excess T+5 success rate: **44.95%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
