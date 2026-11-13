# Performance Decision Audit - 2026-11-13

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.43%** (22926 evaluated)
- Benchmark-adjusted success rate: **51.71%** (17739 evaluated)
- Selected raw success rate: **44.29%**
- Non-selected raw success rate: **49.7%**
- Selected benchmark-adjusted success rate: **49.28%**
- Non-selected benchmark-adjusted success rate: **51.79%**
- Benchmark coverage: **77.38%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.28% (261 eval); 100-199: 53.5% (615 eval); 200+: 49.33% (22050 eval)

## Return Horizons

- Close T+1 success rate: **40.31%**
- Close T+3 success rate: **37.89%**
- Close T+5 success rate: **34.71%**
- Excess T+1 success rate: **49.15%**
- Excess T+3 success rate: **50.8%**
- Excess T+5 success rate: **52.63%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
