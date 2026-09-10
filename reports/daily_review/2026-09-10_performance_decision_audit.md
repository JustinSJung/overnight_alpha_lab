# Performance Decision Audit - 2026-09-10

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **45.51%** (5012 evaluated)
- Benchmark-adjusted success rate: **50.54%** (4753 evaluated)
- Selected raw success rate: **44.49%**
- Non-selected raw success rate: **45.62%**
- Selected benchmark-adjusted success rate: **47.7%**
- Non-selected benchmark-adjusted success rate: **50.87%**
- Benchmark coverage: **94.83%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.12% (266 eval); 100-199: 53.82% (654 eval); 200+: 44.01% (4092 eval)

## Return Horizons

- Close T+1 success rate: **40.73%**
- Close T+3 success rate: **44.24%**
- Close T+5 success rate: **45.2%**
- Excess T+1 success rate: **48.63%**
- Excess T+3 success rate: **47.24%**
- Excess T+5 success rate: **44.01%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
