# Evaluation Integrity Audit - 2026-11-20

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1588452**
- Unique evaluation keys: **51980**
- Duplicate rows by candidate key: **1536472**
- Duplicate rate: **96.73%**
- Exact same-day duplicate rows: **653425**
- Same stock_code + signal_date repeated keys: **50777**
- Same candidate re-evaluated across multiple files: **50778**
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
| v2_conservative_ranker | 25499 | 12658 | 12841 | 49.64 | -0.0015 | -0.0072 | -0.0122 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2670 | 1137 | 1533 | 42.58 | -0.0023 | -0.0108 | -0.0181 |
| avoid | 22829 | 11521 | 11308 | 50.47 | -0.0014 | -0.0068 | -0.0115 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 678 | 295 | 383 | 43.51 | 0.0004 | -0.0063 | -0.0055 |
| Top 20 | 1228 | 544 | 684 | 44.3 | -0.0005 | -0.007 | -0.0077 |
| Top 50 | 2125 | 935 | 1190 | 44.0 | -0.0012 | -0.0077 | -0.0108 |
| Top 100 | 2807 | 1188 | 1619 | 42.32 | -0.0007 | -0.0065 | -0.0103 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2550 | 1233 | 1317 | 48.35 | 21.31 | -0.0001 | -0.0027 | -0.0033 |
| D2 | 2550 | 1271 | 1279 | 49.84 | 26.57 | -0.0024 | -0.0068 | -0.0136 |
| D3 | 2550 | 1243 | 1307 | 48.75 | 28.87 | -0.0004 | -0.0045 | -0.0115 |
| D4 | 2550 | 1251 | 1299 | 49.06 | 30.92 | -0.0012 | -0.0068 | -0.0117 |
| D5 | 2550 | 1303 | 1247 | 51.1 | 32.82 | -0.0017 | -0.0078 | -0.0141 |
| D6 | 2549 | 1328 | 1221 | 52.1 | 34.6 | -0.0023 | -0.0094 | -0.0127 |
| D7 | 2550 | 1328 | 1222 | 52.08 | 36.32 | -0.0024 | -0.0072 | -0.0108 |
| D8 | 2550 | 1309 | 1241 | 51.33 | 37.96 | -0.0005 | -0.006 | -0.01 |
| D9 | 2550 | 1302 | 1248 | 51.06 | 41.02 | -0.0018 | -0.0101 | -0.016 |
| D10 | 2550 | 1090 | 1460 | 42.75 | 66.03 | -0.0023 | -0.0108 | -0.0182 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.2312 | 41.6789 | 0.4477 |
| volume_confirmation_score | -1.1627 | -0.9794 | 0.1833 |
| liquidity_score | 2.1701 | 2.097 | -0.0731 |
| overextension_penalty | 0.9239 | 0.798 | -0.1258 |
| reversal_risk_penalty | 0.7306 | 0.6658 | -0.0647 |
| news_risk_penalty | 0.097 | 0.1153 | 0.0183 |
| attention_noise_penalty | 0.2168 | 0.2403 | 0.0236 |
| market_regime_penalty | 0.0485 | 0.0435 | -0.0051 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **19273**
- Benchmark-adjusted coverage: **37.08%**
- Benchmark-adjusted success rate: **52.07%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261120.csv`
- Latest market index date: **2026-11-20**
- Latest price signal date: **2026-11-19**
- Latest candidate signal date: **2026-11-19**
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