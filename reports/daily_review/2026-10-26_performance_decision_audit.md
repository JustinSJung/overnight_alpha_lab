# Performance Decision Audit - 2026-10-26

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **50.12%** (15577 evaluated)
- Benchmark-adjusted success rate: **48.05%** (12492 evaluated)
- Selected raw success rate: **43.33%**
- Non-selected raw success rate: **50.57%**
- Selected benchmark-adjusted success rate: **51.58%**
- Non-selected benchmark-adjusted success rate: **47.86%**
- Benchmark coverage: **80.2%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.13% (268 eval); 100-199: 53.79% (660 eval); 200+: 49.99% (14649 eval)

## Return Horizons

- Close T+1 success rate: **38.62%**
- Close T+3 success rate: **37.75%**
- Close T+5 success rate: **37.54%**
- Excess T+1 success rate: **52.89%**
- Excess T+3 success rate: **54.58%**
- Excess T+5 success rate: **55.76%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
