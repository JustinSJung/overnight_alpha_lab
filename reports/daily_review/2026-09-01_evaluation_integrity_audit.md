# Evaluation Integrity Audit - 2026-09-01

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **139172**
- Unique evaluation keys: **8044**
- Duplicate rows by candidate key: **131128**
- Duplicate rate: **94.22%**
- Exact same-day duplicate rows: **22178**
- Same stock_code + signal_date repeated keys: **7613**
- Same candidate re-evaluated across multiple files: **7614**
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
| v1/unknown | 384 | 188 | 196 | 48.96 | -0.0123 | 0.0114 | 0.0041 |
| v2_conservative_ranker | 3136 | 1327 | 1809 | 42.32 | 0.0056 | 0.0198 | 0.029 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 620 | 261 | 359 | 42.1 | -0.0009 | -0.0045 | -0.0106 |
| avoid | 2516 | 1066 | 1450 | 42.37 | 0.0073 | 0.0255 | 0.0382 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 230 | 109 | 121 | 47.39 | 0.0026 | 0.0037 | 0.006 |
| Top 20 | 392 | 180 | 212 | 45.92 | 0.0012 | -0.0011 | 0.0012 |
| Top 50 | 594 | 258 | 336 | 43.43 | -0.0004 | -0.0051 | -0.0103 |
| Top 100 | 890 | 365 | 525 | 41.01 | 0.0037 | 0.0022 | -0.0031 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 314 | 135 | 179 | 42.99 | 18.25 | 0.0092 | 0.0378 | 0.058 |
| D2 | 314 | 126 | 188 | 40.13 | 24.63 | 0.0134 | 0.0518 | 0.0792 |
| D3 | 313 | 128 | 185 | 40.89 | 28.24 | 0.0133 | 0.0289 | 0.0413 |
| D4 | 314 | 127 | 187 | 40.45 | 30.9 | 0.0049 | 0.0285 | 0.0319 |
| D5 | 313 | 133 | 180 | 42.49 | 33.28 | 0.0045 | 0.0139 | 0.0139 |
| D6 | 314 | 144 | 170 | 45.86 | 35.3 | 0.0 | 0.0133 | 0.0222 |
| D7 | 313 | 133 | 180 | 42.49 | 37.21 | 0.0075 | 0.0125 | 0.0209 |
| D8 | 314 | 138 | 176 | 43.95 | 39.25 | 0.0049 | 0.0171 | 0.0348 |
| D9 | 313 | 126 | 187 | 40.26 | 61.58 | -0.0027 | -0.0115 | -0.0153 |
| D10 | 314 | 137 | 177 | 43.63 | 69.23 | 0.0015 | 0.0008 | -0.0064 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 48.0218 | 46.2658 | -1.756 |
| volume_confirmation_score | -0.5395 | -0.5103 | 0.0292 |
| liquidity_score | 2.3165 | 2.1039 | -0.2126 |
| overextension_penalty | 2.4397 | 1.5999 | -0.8398 |
| reversal_risk_penalty | 1.9675 | 1.4268 | -0.5408 |
| news_risk_penalty | 0.3188 | 0.3068 | -0.012 |
| attention_noise_penalty | 0.2803 | 0.2489 | -0.0314 |
| market_regime_penalty | 0.0904 | 0.0719 | -0.0186 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3261**
- Benchmark-adjusted coverage: **40.54%**
- Benchmark-adjusted success rate: **49.68%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260901.csv`
- Latest market index date: **2026-09-01**
- Latest price signal date: **2026-09-01**
- Latest candidate signal date: **2026-09-01**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **8**
- Eligible groups: **9**
- Groups close to activation: **2**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Some learned event rules are active.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Partial**
- Ranking status: **Ranking improving**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.