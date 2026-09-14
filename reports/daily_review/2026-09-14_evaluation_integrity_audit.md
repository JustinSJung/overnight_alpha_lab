# Evaluation Integrity Audit - 2026-09-14

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **228127**
- Unique evaluation keys: **12687**
- Duplicate rows by candidate key: **215440**
- Duplicate rate: **94.44%**
- Exact same-day duplicate rows: **57431**
- Same stock_code + signal_date repeated keys: **12023**
- Same candidate re-evaluated across multiple files: **12024**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 002780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 101970 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 002780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 101970 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 101970 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 002780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 002780 |  |  | 2026-07-20 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 020560 |  |  | 2026-07-20 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 101970 |  |  | 2026-07-20 |  | dd1b5a251ebc1581 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 397 | 195 | 202 | 49.12 | -0.0143 | 0.0086 | -0.0004 |
| v2_conservative_ranker | 5132 | 2359 | 2773 | 45.97 | 0.0027 | 0.0121 | 0.0218 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 818 | 347 | 471 | 42.42 | -0.0013 | -0.0041 | -0.0076 |
| avoid | 4314 | 2012 | 2302 | 46.64 | 0.0034 | 0.0153 | 0.028 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 309 | 144 | 165 | 46.6 | 0.0014 | 0.002 | 0.0086 |
| Top 20 | 533 | 239 | 294 | 44.84 | -0.0001 | -0.0017 | 0.0029 |
| Top 50 | 785 | 340 | 445 | 43.31 | -0.001 | -0.0045 | -0.0072 |
| Top 100 | 1114 | 460 | 654 | 41.29 | 0.0022 | 0.0014 | -0.0006 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 514 | 216 | 298 | 42.02 | 19.48 | 0.0038 | 0.0228 | 0.0451 |
| D2 | 513 | 235 | 278 | 45.81 | 25.78 | 0.0063 | 0.0314 | 0.0552 |
| D3 | 513 | 222 | 291 | 43.27 | 29.17 | 0.0105 | 0.022 | 0.0347 |
| D4 | 513 | 243 | 270 | 47.37 | 31.56 | -0.0003 | 0.0114 | 0.0141 |
| D5 | 513 | 258 | 255 | 50.29 | 33.57 | 0.0012 | 0.0088 | 0.0197 |
| D6 | 513 | 237 | 276 | 46.2 | 35.38 | -0.0004 | 0.0102 | 0.0161 |
| D7 | 513 | 255 | 258 | 49.71 | 37.1 | 0.004 | 0.0108 | 0.0214 |
| D8 | 513 | 249 | 264 | 48.54 | 38.72 | 0.0037 | 0.0095 | 0.0214 |
| D9 | 513 | 227 | 286 | 44.25 | 52.82 | -0.001 | -0.0001 | 0.0007 |
| D10 | 514 | 217 | 297 | 42.22 | 67.54 | -0.001 | -0.0054 | -0.0103 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.7206 | 45.3866 | -0.334 |
| volume_confirmation_score | -1.0643 | -0.8913 | 0.1731 |
| liquidity_score | 2.1899 | 2.0263 | -0.1636 |
| overextension_penalty | 1.8179 | 1.4335 | -0.3844 |
| reversal_risk_penalty | 1.3632 | 1.1545 | -0.2087 |
| news_risk_penalty | 0.2306 | 0.2481 | 0.0175 |
| attention_noise_penalty | 0.3353 | 0.3552 | 0.0199 |
| market_regime_penalty | 0.1026 | 0.0786 | -0.024 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **5270**
- Benchmark-adjusted coverage: **41.54%**
- Benchmark-adjusted success rate: **49.03%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260914.csv`
- Latest market index date: **2026-09-14**
- Latest price signal date: **2026-09-14**
- Latest candidate signal date: **2026-09-14**
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