# Performance Decision Audit - 2026-09-08

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **43.63%** (4456 evaluated)
- Benchmark-adjusted success rate: **50.94%** (4197 evaluated)
- Selected raw success rate: **45.02%**
- Non-selected raw success rate: **43.47%**
- Selected benchmark-adjusted success rate: **46.97%**
- Non-selected benchmark-adjusted success rate: **51.43%**
- Benchmark coverage: **94.19%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.5% (266 eval); 100-199: 52.59% (656 eval); 200+: 41.6% (3534 eval)

## Return Horizons

- Close T+1 success rate: **41.72%**
- Close T+3 success rate: **44.86%**
- Close T+5 success rate: **44.59%**
- Excess T+1 success rate: **46.68%**
- Excess T+3 success rate: **46.46%**
- Excess T+5 success rate: **46.2%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
