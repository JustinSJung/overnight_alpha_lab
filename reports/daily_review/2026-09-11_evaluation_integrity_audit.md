# Evaluation Integrity Audit - 2026-09-11

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **215969**
- Unique evaluation keys: **12024**
- Duplicate rows by candidate key: **203945**
- Duplicate rate: **94.43%**
- Exact same-day duplicate rows: **52627**
- Same stock_code + signal_date repeated keys: **11379**
- Same candidate re-evaluated across multiple files: **11380**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 216080 |  |  | 2026-07-20 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 004990 |  |  | 2026-07-20 |  | 65698458accec52f | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 395 | 198 | 197 | 50.13 | -0.0139 | 0.01 | 0.0025 |
| v2_conservative_ranker | 4912 | 2213 | 2699 | 45.05 | 0.0034 | 0.0146 | 0.025 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 792 | 340 | 452 | 42.93 | -0.001 | -0.0042 | -0.0078 |
| avoid | 4120 | 1873 | 2247 | 45.46 | 0.0043 | 0.0183 | 0.0321 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 298 | 141 | 157 | 47.32 | 0.0019 | 0.0029 | 0.0091 |
| Top 20 | 515 | 235 | 280 | 45.63 | 0.0004 | -0.0014 | 0.0034 |
| Top 50 | 759 | 334 | 425 | 44.01 | -0.0006 | -0.0043 | -0.007 |
| Top 100 | 1083 | 454 | 629 | 41.92 | 0.0029 | 0.0033 | 0.0009 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 492 | 212 | 280 | 43.09 | 19.14 | 0.0053 | 0.0294 | 0.0554 |
| D2 | 491 | 215 | 276 | 43.79 | 25.52 | 0.0091 | 0.0326 | 0.0545 |
| D3 | 491 | 210 | 281 | 42.77 | 28.98 | 0.0097 | 0.0223 | 0.0379 |
| D4 | 491 | 223 | 268 | 45.42 | 31.42 | -0.0004 | 0.0162 | 0.0236 |
| D5 | 491 | 233 | 258 | 47.45 | 33.46 | 0.0021 | 0.0136 | 0.0176 |
| D6 | 491 | 229 | 262 | 46.64 | 35.31 | -0.0004 | 0.0124 | 0.0172 |
| D7 | 491 | 233 | 258 | 47.45 | 37.07 | 0.0056 | 0.0134 | 0.0217 |
| D8 | 491 | 235 | 256 | 47.86 | 38.72 | 0.005 | 0.0111 | 0.0281 |
| D9 | 491 | 215 | 276 | 43.79 | 53.27 | -0.0004 | -0.0006 | 0.0023 |
| D10 | 492 | 208 | 284 | 42.28 | 67.7 | -0.0012 | -0.0054 | -0.0113 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 46.2448 | 45.3542 | -0.8906 |
| volume_confirmation_score | -0.9719 | -0.8626 | 0.1093 |
| liquidity_score | 2.2133 | 2.0471 | -0.1662 |
| overextension_penalty | 2.0149 | 1.4646 | -0.5503 |
| reversal_risk_penalty | 1.5419 | 1.2006 | -0.3413 |
| news_risk_penalty | 0.2431 | 0.2501 | 0.007 |
| attention_noise_penalty | 0.3288 | 0.3497 | 0.0209 |
| market_regime_penalty | 0.0976 | 0.0756 | -0.022 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **5048**
- Benchmark-adjusted coverage: **41.98%**
- Benchmark-adjusted success rate: **49.96%**
- Benchmark rows available: **86**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260911.csv`
- Latest market index date: **2026-09-11**
- Latest price signal date: **2026-09-11**
- Latest candidate signal date: **2026-09-11**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **10**
- Eligible groups: **11**
- Groups close to activation: **1**
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