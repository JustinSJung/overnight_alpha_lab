# Performance Decision Audit - 2026-09-14

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.19%** (5529 evaluated)
- Benchmark-adjusted success rate: **49.03%** (5270 evaluated)
- Selected raw success rate: **44.8%**
- Non-selected raw success rate: **46.34%**
- Selected benchmark-adjusted success rate: **49.44%**
- Non-selected benchmark-adjusted success rate: **48.99%**
- Benchmark coverage: **95.32%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.52% (270 eval); 100-199: 53.13% (655 eval); 200+: 45.07% (4604 eval)

## Return Horizons

- Close T+1 success rate: **40.39%**
- Close T+3 success rate: **44.0%**
- Close T+5 success rate: **45.03%**
- Excess T+1 success rate: **51.01%**
- Excess T+3 success rate: **48.33%**
- Excess T+5 success rate: **45.62%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
