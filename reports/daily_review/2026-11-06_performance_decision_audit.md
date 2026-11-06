# Performance Decision Audit - 2026-11-06

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.83%** (19365 evaluated)
- Benchmark-adjusted success rate: **50.9%** (15430 evaluated)
- Selected raw success rate: **44.81%**
- Non-selected raw success rate: **50.11%**
- Selected benchmark-adjusted success rate: **51.33%**
- Non-selected benchmark-adjusted success rate: **50.88%**
- Benchmark coverage: **79.68%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.31% (267 eval); 100-199: 53.57% (644 eval); 200+: 49.72% (18454 eval)

## Return Horizons

- Close T+1 success rate: **39.4%**
- Close T+3 success rate: **36.78%**
- Close T+5 success rate: **35.23%**
- Excess T+1 success rate: **50.56%**
- Excess T+3 success rate: **51.45%**
- Excess T+5 success rate: **50.87%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
