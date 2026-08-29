# Evaluation Integrity Audit - 2026-08-29

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **124572**
- Unique evaluation keys: **7241**
- Duplicate rows by candidate key: **117331**
- Duplicate rate: **94.19%**
- Exact same-day duplicate rows: **16210**
- Same stock_code + signal_date repeated keys: **7191**
- Same candidate re-evaluated across multiple files: **7192**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 003070 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 322780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 003070 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 322780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003070 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 322780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003070 |  |  | 2026-07-20 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 322780 |  |  | 2026-07-20 |  | 588b4708dca67cf1 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 388 | 194 | 194 | 50.0 | -0.0151 | 0.0043 | -0.0 |
| v2_conservative_ranker | 2913 | 1199 | 1714 | 41.16 | 0.0068 | 0.0229 | 0.0325 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 539 | 228 | 311 | 42.3 | -0.0005 | -0.0035 | -0.0105 |
| avoid | 2374 | 971 | 1403 | 40.9 | 0.0085 | 0.0289 | 0.0431 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 211 | 101 | 110 | 47.87 | 0.0039 | 0.0064 | 0.0105 |
| Top 20 | 353 | 167 | 186 | 47.31 | 0.0025 | 0.0007 | 0.0026 |
| Top 50 | 523 | 230 | 293 | 43.98 | -0.0002 | -0.0041 | -0.0099 |
| Top 100 | 825 | 335 | 490 | 40.61 | 0.005 | 0.0086 | 0.0055 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 292 | 123 | 169 | 42.12 | 18.14 | 0.0078 | 0.0368 | 0.0585 |
| D2 | 291 | 113 | 178 | 38.83 | 24.29 | 0.0136 | 0.051 | 0.0681 |
| D3 | 291 | 105 | 186 | 36.08 | 27.77 | 0.0206 | 0.0347 | 0.0517 |
| D4 | 291 | 117 | 174 | 40.21 | 30.51 | 0.0057 | 0.0363 | 0.0473 |
| D5 | 292 | 129 | 163 | 44.18 | 32.88 | 0.0019 | 0.0138 | 0.0121 |
| D6 | 291 | 125 | 166 | 42.96 | 34.91 | 0.0045 | 0.0253 | 0.046 |
| D7 | 291 | 119 | 172 | 40.89 | 36.84 | 0.0062 | 0.0134 | 0.0225 |
| D8 | 291 | 121 | 170 | 41.58 | 38.81 | 0.0088 | 0.0248 | 0.0422 |
| D9 | 291 | 119 | 172 | 40.89 | 58.79 | -0.0031 | -0.0104 | -0.0127 |
| D10 | 292 | 128 | 164 | 43.84 | 69.15 | 0.0022 | 0.0025 | -0.0057 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.7079 | 45.3911 | -2.3168 |
| volume_confirmation_score | -0.4962 | -0.4758 | 0.0203 |
| liquidity_score | 2.3286 | 2.1085 | -0.2201 |
| overextension_penalty | 2.4903 | 1.4892 | -1.0011 |
| reversal_risk_penalty | 2.0176 | 1.4369 | -0.5807 |
| news_risk_penalty | 0.3219 | 0.2765 | -0.0454 |
| attention_noise_penalty | 0.2003 | 0.1838 | -0.0166 |
| market_regime_penalty | 0.0684 | 0.0548 | -0.0135 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3042**
- Benchmark-adjusted coverage: **42.01%**
- Benchmark-adjusted success rate: **50.2%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260829.csv`
- Latest market index date: **2026-08-28**
- Latest price signal date: **2026-08-28**
- Latest candidate signal date: **2026-08-28**
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