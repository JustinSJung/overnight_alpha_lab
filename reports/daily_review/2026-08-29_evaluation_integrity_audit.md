# Evaluation Integrity Audit - 2026-08-29

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **124530**
- Unique evaluation keys: **7199**
- Duplicate rows by candidate key: **117331**
- Duplicate rate: **94.22%**
- Exact same-day duplicate rows: **16293**
- Same stock_code + signal_date repeated keys: **7191**
- Same candidate re-evaluated across multiple files: **7192**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 0126Z0 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 0126Z0 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 0126Z0 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 0126Z0 |  |  | 2026-07-20 |  | 2ab2d2b2d8fba094 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 347700 |  |  | 2026-07-20 |  | 88a6b82b07d4d16e | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 403 | 200 | 203 | 49.63 | -0.0152 | 0.0044 | -0.0007 |
| v2_conservative_ranker | 2985 | 1235 | 1750 | 41.37 | 0.0063 | 0.0217 | 0.0309 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 543 | 229 | 314 | 42.17 | -0.0006 | -0.0035 | -0.0103 |
| avoid | 2442 | 1006 | 1436 | 41.2 | 0.0078 | 0.0273 | 0.0408 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 215 | 102 | 113 | 47.44 | 0.0038 | 0.0061 | 0.0107 |
| Top 20 | 357 | 168 | 189 | 47.06 | 0.0024 | 0.0006 | 0.0028 |
| Top 50 | 530 | 232 | 298 | 43.77 | -0.0001 | -0.004 | -0.0101 |
| Top 100 | 856 | 349 | 507 | 40.77 | 0.0048 | 0.008 | 0.004 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 299 | 126 | 173 | 42.14 | 18.11 | 0.0076 | 0.0387 | 0.0607 |
| D2 | 298 | 118 | 180 | 39.6 | 24.21 | 0.011 | 0.0452 | 0.0605 |
| D3 | 299 | 110 | 189 | 36.79 | 27.67 | 0.0208 | 0.0348 | 0.0517 |
| D4 | 298 | 122 | 176 | 40.94 | 30.41 | 0.004 | 0.0323 | 0.0393 |
| D5 | 299 | 131 | 168 | 43.81 | 32.78 | 0.0026 | 0.0118 | 0.0105 |
| D6 | 298 | 124 | 174 | 41.61 | 34.84 | 0.0041 | 0.0204 | 0.0412 |
| D7 | 298 | 125 | 173 | 41.95 | 36.78 | 0.0063 | 0.0158 | 0.0248 |
| D8 | 299 | 127 | 172 | 42.47 | 38.74 | 0.0076 | 0.0237 | 0.0408 |
| D9 | 298 | 123 | 175 | 41.28 | 58.08 | -0.0029 | -0.0088 | -0.0115 |
| D10 | 299 | 129 | 170 | 43.14 | 69.07 | 0.0021 | 0.0022 | -0.0057 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.4526 | 45.2827 | -2.1699 |
| volume_confirmation_score | -0.4804 | -0.4768 | 0.0036 |
| liquidity_score | 2.3304 | 2.1046 | -0.2258 |
| overextension_penalty | 2.4385 | 1.4586 | -0.9799 |
| reversal_risk_penalty | 2.0396 | 1.4427 | -0.5969 |
| news_risk_penalty | 0.3134 | 0.2726 | -0.0408 |
| attention_noise_penalty | 0.2011 | 0.1854 | -0.0157 |
| market_regime_penalty | 0.0696 | 0.056 | -0.0136 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3129**
- Benchmark-adjusted coverage: **43.46%**
- Benchmark-adjusted success rate: **49.95%**
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