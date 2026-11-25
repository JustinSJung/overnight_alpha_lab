# Performance Decision Audit - 2026-11-25

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **50.37%** (27852 evaluated)
- Benchmark-adjusted success rate: **52.41%** (20685 evaluated)
- Selected raw success rate: **43.06%**
- Non-selected raw success rate: **50.72%**
- Selected benchmark-adjusted success rate: **51.3%**
- Non-selected benchmark-adjusted success rate: **52.44%**
- Benchmark coverage: **74.27%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 50.75% (201 eval); 100-199: 62.54% (355 eval); 200+: 50.21% (27296 eval)

## Return Horizons

- Close T+1 success rate: **39.57%**
- Close T+3 success rate: **35.65%**
- Close T+5 success rate: **34.11%**
- Excess T+1 success rate: **49.44%**
- Excess T+3 success rate: **53.01%**
- Excess T+5 success rate: **54.21%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
