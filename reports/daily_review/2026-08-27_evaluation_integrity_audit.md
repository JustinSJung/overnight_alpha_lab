# Evaluation Integrity Audit - 2026-08-27

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **110074**
- Unique evaluation keys: **7735**
- Duplicate rows by candidate key: **102339**
- Duplicate rate: **92.97%**
- Exact same-day duplicate rows: **12807**
- Same stock_code + signal_date repeated keys: **6546**
- Same candidate re-evaluated across multiple files: **7187**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 002780 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | fa584432815d5855 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 009540 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | a18bd76da90c09d1 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 002780 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | fa584432815d5855 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 009540 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | a18bd76da90c09d1 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 002780 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | fa584432815d5855 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 009540 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | a18bd76da90c09d1 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260713.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 380 | 192 | 188 | 50.53 | -0.0117 | -0.0048 | -0.0264 |
| v2_conservative_ranker | 3173 | 1303 | 1870 | 41.07 | 0.0055 | 0.0157 | 0.0247 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 621 | 257 | 364 | 41.38 | -0.0019 | -0.0069 | -0.0152 |
| avoid | 2552 | 1046 | 1506 | 40.99 | 0.0073 | 0.0214 | 0.0356 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 217 | 104 | 113 | 47.93 | 0.0046 | 0.0032 | 0.0038 |
| Top 20 | 361 | 169 | 192 | 46.81 | 0.0026 | -0.0035 | -0.0035 |
| Top 50 | 558 | 251 | 307 | 44.98 | 0.001 | -0.0047 | -0.011 |
| Top 100 | 859 | 361 | 498 | 42.03 | 0.0024 | 0.0037 | -0.0059 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 318 | 136 | 182 | 42.77 | 18.09 | 0.007 | 0.03 | 0.0568 |
| D2 | 317 | 121 | 196 | 38.17 | 24.21 | 0.0113 | 0.0353 | 0.0572 |
| D3 | 317 | 118 | 199 | 37.22 | 27.66 | 0.0187 | 0.0293 | 0.0483 |
| D4 | 317 | 132 | 185 | 41.64 | 30.41 | 0.0027 | 0.03 | 0.036 |
| D5 | 318 | 138 | 180 | 43.4 | 32.82 | 0.0019 | 0.0054 | -0.0035 |
| D6 | 317 | 133 | 184 | 41.96 | 34.96 | 0.0027 | 0.0171 | 0.0344 |
| D7 | 317 | 130 | 187 | 41.01 | 36.98 | 0.0074 | 0.0079 | 0.0163 |
| D8 | 317 | 133 | 184 | 41.96 | 38.95 | 0.0068 | 0.0169 | 0.0372 |
| D9 | 317 | 126 | 191 | 39.75 | 61.07 | -0.0052 | -0.0122 | -0.0166 |
| D10 | 318 | 136 | 182 | 42.77 | 69.22 | 0.0015 | -0.0018 | -0.013 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.8879 | 45.7059 | -2.1821 |
| volume_confirmation_score | -0.4812 | -0.4861 | -0.005 |
| liquidity_score | 2.3323 | 2.0984 | -0.2339 |
| overextension_penalty | 2.5012 | 1.4175 | -1.0837 |
| reversal_risk_penalty | 2.123 | 1.4501 | -0.6729 |
| news_risk_penalty | 0.307 | 0.2738 | -0.0332 |
| attention_noise_penalty | 0.2221 | 0.2012 | -0.0209 |
| market_regime_penalty | 0.0675 | 0.0535 | -0.0141 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3553**
- Benchmark-adjusted coverage: **45.93%**
- Benchmark-adjusted success rate: **50.13%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260827.csv`
- Latest market index date: **2026-08-27**
- Latest price signal date: **2026-08-27**
- Latest candidate signal date: **2026-08-27**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **0**
- Eligible groups: **0**
- Groups close to activation: **0**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Learned rules are inactive because the updater learns from DART error_notes event_type groups, not price-candidate v2 outcomes, and current eligible groups are in the neutral adjustment band.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Partial**
- Ranking status: **Ranking improving**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.