# Evaluation Integrity Audit - 2026-09-15

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **240970**
- Unique evaluation keys: **13372**
- Duplicate rows by candidate key: **227598**
- Duplicate rate: **94.45%**
- Exact same-day duplicate rows: **62531**
- Same stock_code + signal_date repeated keys: **12686**
- Same candidate re-evaluated across multiple files: **12687**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 004380 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004380 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004380 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 004380 |  |  | 2026-07-20 |  | 0c7b363eacd84407 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 010140 |  |  | 2026-07-20 |  | 7a97bf307b3df2b2 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 399 | 199 | 200 | 49.87 | -0.0141 | 0.0091 | 0.0019 |
| v2_conservative_ranker | 5533 | 2492 | 3041 | 45.04 | 0.0029 | 0.0112 | 0.0207 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 838 | 346 | 492 | 41.29 | -0.0025 | -0.0065 | -0.0089 |
| avoid | 4695 | 2146 | 2549 | 45.71 | 0.0038 | 0.0146 | 0.0266 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 314 | 140 | 174 | 44.59 | 0.0 | -0.0016 | 0.0038 |
| Top 20 | 551 | 237 | 314 | 43.01 | -0.0015 | -0.0039 | 0.0 |
| Top 50 | 804 | 339 | 465 | 42.16 | -0.0023 | -0.0069 | -0.0084 |
| Top 100 | 1136 | 456 | 680 | 40.14 | 0.0018 | 0.0012 | -0.0006 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 554 | 241 | 313 | 43.5 | 19.42 | 0.0045 | 0.0228 | 0.0471 |
| D2 | 553 | 243 | 310 | 43.94 | 25.81 | 0.0068 | 0.0295 | 0.0523 |
| D3 | 553 | 239 | 314 | 43.22 | 29.1 | 0.0092 | 0.0214 | 0.0312 |
| D4 | 553 | 260 | 293 | 47.02 | 31.49 | -0.0004 | 0.0115 | 0.018 |
| D5 | 554 | 265 | 289 | 47.83 | 33.51 | 0.0023 | 0.0061 | 0.0122 |
| D6 | 553 | 262 | 291 | 47.38 | 35.32 | -0.0005 | 0.0091 | 0.0176 |
| D7 | 553 | 258 | 295 | 46.65 | 37.02 | 0.0057 | 0.0128 | 0.0192 |
| D8 | 553 | 250 | 303 | 45.21 | 38.6 | 0.0052 | 0.0101 | 0.0206 |
| D9 | 553 | 243 | 310 | 43.94 | 51.0 | -0.0029 | -0.003 | 0.0003 |
| D10 | 554 | 231 | 323 | 41.7 | 67.22 | -0.0015 | -0.0069 | -0.011 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.5413 | 45.1546 | -0.3867 |
| volume_confirmation_score | -1.0898 | -0.9464 | 0.1435 |
| liquidity_score | 2.1858 | 2.0227 | -0.1631 |
| overextension_penalty | 1.9283 | 1.4366 | -0.4917 |
| reversal_risk_penalty | 1.4243 | 1.1395 | -0.2848 |
| news_risk_penalty | 0.2119 | 0.2331 | 0.0213 |
| attention_noise_penalty | 0.3371 | 0.3602 | 0.0231 |
| market_regime_penalty | 0.1003 | 0.0802 | -0.0201 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **5601**
- Benchmark-adjusted coverage: **41.89%**
- Benchmark-adjusted success rate: **49.04%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260915.csv`
- Latest market index date: **2026-09-15**
- Latest price signal date: **2026-09-15**
- Latest candidate signal date: **2026-09-15**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **9**
- Eligible groups: **11**
- Groups close to activation: **0**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Some learned event rules are active.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Partial**
- Ranking status: **Ranking weak**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.