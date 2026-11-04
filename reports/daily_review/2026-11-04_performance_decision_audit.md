# Performance Decision Audit - 2026-11-04

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.27%** (18354 evaluated)
- Benchmark-adjusted success rate: **51.86%** (14256 evaluated)
- Selected raw success rate: **44.23%**
- Non-selected raw success rate: **49.56%**
- Selected benchmark-adjusted success rate: **50.53%**
- Non-selected benchmark-adjusted success rate: **51.91%**
- Benchmark coverage: **77.67%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.89% (270 eval); 100-199: 54.42% (678 eval); 200+: 49.08% (17406 eval)

## Return Horizons

- Close T+1 success rate: **39.39%**
- Close T+3 success rate: **37.02%**
- Close T+5 success rate: **35.32%**
- Excess T+1 success rate: **49.68%**
- Excess T+3 success rate: **49.86%**
- Excess T+5 success rate: **50.61%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
