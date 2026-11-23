# Evaluation Integrity Audit - 2026-11-23

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1641114**
- Unique evaluation keys: **53191**
- Duplicate rows by candidate key: **1587923**
- Duplicate rate: **96.76%**
- Exact same-day duplicate rows: **677675**
- Same stock_code + signal_date repeated keys: **51979**
- Same candidate re-evaluated across multiple files: **51980**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 036630 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 036630 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 036630 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 091590 |  |  | 2026-07-20 |  | 5bc402d6287954af | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 004990 |  |  | 2026-07-20 |  | 65698458accec52f | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 036630 |  |  | 2026-07-20 |  | 7dac8e5346d51217 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 259 | 131 | 128 | 50.58 | -0.0136 | -0.0151 | -0.0326 |
| v2_conservative_ranker | 25953 | 13129 | 12824 | 50.59 | -0.0027 | -0.0071 | -0.0127 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2657 | 1114 | 1543 | 41.93 | -0.0029 | -0.011 | -0.0191 |
| avoid | 23296 | 12015 | 11281 | 51.58 | -0.0027 | -0.0066 | -0.0119 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 655 | 280 | 375 | 42.75 | -0.0007 | -0.0053 | -0.0047 |
| Top 20 | 1199 | 520 | 679 | 43.37 | -0.001 | -0.0067 | -0.0073 |
| Top 50 | 2114 | 905 | 1209 | 42.81 | -0.002 | -0.0074 | -0.0113 |
| Top 100 | 2700 | 1128 | 1572 | 41.78 | -0.0017 | -0.0052 | -0.0082 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2596 | 1288 | 1308 | 49.61 | 21.29 | -0.0024 | -0.0013 | -0.0012 |
| D2 | 2595 | 1327 | 1268 | 51.14 | 26.53 | -0.0041 | -0.0065 | -0.0139 |
| D3 | 2595 | 1319 | 1276 | 50.83 | 28.79 | -0.0024 | -0.005 | -0.0126 |
| D4 | 2595 | 1316 | 1279 | 50.71 | 30.82 | -0.0023 | -0.0058 | -0.0119 |
| D5 | 2596 | 1352 | 1244 | 52.08 | 32.72 | -0.0029 | -0.0073 | -0.0151 |
| D6 | 2595 | 1379 | 1216 | 53.14 | 34.52 | -0.0033 | -0.0101 | -0.0132 |
| D7 | 2595 | 1372 | 1223 | 52.87 | 36.25 | -0.0035 | -0.0079 | -0.013 |
| D8 | 2595 | 1340 | 1255 | 51.64 | 37.91 | -0.0009 | -0.0054 | -0.0101 |
| D9 | 2595 | 1348 | 1247 | 51.95 | 40.5 | -0.002 | -0.01 | -0.0165 |
| D10 | 2596 | 1088 | 1508 | 41.91 | 65.93 | -0.0031 | -0.011 | -0.0192 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 40.8968 | 41.7086 | 0.8117 |
| volume_confirmation_score | -1.1502 | -0.9653 | 0.1849 |
| liquidity_score | 2.1714 | 2.0965 | -0.0748 |
| overextension_penalty | 0.8887 | 0.8016 | -0.087 |
| reversal_risk_penalty | 0.71 | 0.6732 | -0.0368 |
| news_risk_penalty | 0.091 | 0.1167 | 0.0257 |
| attention_noise_penalty | 0.2148 | 0.2438 | 0.029 |
| market_regime_penalty | 0.0487 | 0.0452 | -0.0035 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **19125**
- Benchmark-adjusted coverage: **35.96%**
- Benchmark-adjusted success rate: **51.5%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261123.csv`
- Latest market index date: **2026-11-23**
- Latest price signal date: **2026-11-20**
- Latest candidate signal date: **2026-11-20**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **8**
- Eligible groups: **12**
- Groups close to activation: **4**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Some learned event rules are active.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Partial**
- Ranking status: **Ranking inverted**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.