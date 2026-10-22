# Performance Decision Audit - 2026-10-22

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **48.2%** (14562 evaluated)
- Benchmark-adjusted success rate: **47.97%** (11825 evaluated)
- Selected raw success rate: **43.81%**
- Non-selected raw success rate: **48.5%**
- Selected benchmark-adjusted success rate: **50.55%**
- Non-selected benchmark-adjusted success rate: **47.82%**
- Benchmark coverage: **81.2%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.16% (272 eval); 100-199: 53.86% (661 eval); 200+: 47.93% (13629 eval)

## Return Horizons

- Close T+1 success rate: **40.13%**
- Close T+3 success rate: **39.58%**
- Close T+5 success rate: **39.62%**
- Excess T+1 success rate: **52.73%**
- Excess T+3 success rate: **54.05%**
- Excess T+5 success rate: **54.95%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
