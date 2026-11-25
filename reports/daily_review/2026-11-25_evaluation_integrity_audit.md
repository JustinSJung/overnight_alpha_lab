# Evaluation Integrity Audit - 2026-11-25

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1750103**
- Unique evaluation keys: **55637**
- Duplicate rows by candidate key: **1694466**
- Duplicate rate: **96.82%**
- Exact same-day duplicate rows: **728318**
- Same stock_code + signal_date repeated keys: **54409**
- Same candidate re-evaluated across multiple files: **54410**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 368970 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 263800 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 368970 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 263800 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 263800 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 368970 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 368970 |  |  | 2026-07-20 |  | cd91621fccff8931 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 288980 |  |  | 2026-07-20 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 263800 |  |  | 2026-07-20 |  | dac5f7822d6fdaf1 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 259 | 131 | 128 | 50.58 | -0.0136 | -0.0151 | -0.0326 |
| v2_conservative_ranker | 27593 | 13898 | 13695 | 50.37 | -0.0022 | -0.0089 | -0.0134 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2821 | 1176 | 1645 | 41.69 | -0.0032 | -0.012 | -0.0206 |
| avoid | 24772 | 12722 | 12050 | 51.36 | -0.0021 | -0.0086 | -0.0125 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 692 | 288 | 404 | 41.62 | -0.0012 | -0.0072 | -0.0067 |
| Top 20 | 1278 | 552 | 726 | 43.19 | -0.0013 | -0.0075 | -0.008 |
| Top 50 | 2260 | 968 | 1292 | 42.83 | -0.0021 | -0.0086 | -0.0124 |
| Top 100 | 2873 | 1195 | 1678 | 41.59 | -0.002 | -0.0061 | -0.0102 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2760 | 1342 | 1418 | 48.62 | 21.27 | -0.0001 | -0.0035 | -0.001 |
| D2 | 2759 | 1395 | 1364 | 50.56 | 26.44 | -0.003 | -0.011 | -0.0151 |
| D3 | 2759 | 1384 | 1375 | 50.16 | 28.7 | -0.0015 | -0.0076 | -0.0114 |
| D4 | 2759 | 1393 | 1366 | 50.49 | 30.71 | -0.0019 | -0.0073 | -0.0117 |
| D5 | 2760 | 1410 | 1350 | 51.09 | 32.6 | -0.0018 | -0.0103 | -0.014 |
| D6 | 2759 | 1466 | 1293 | 53.14 | 34.41 | -0.0026 | -0.0097 | -0.0133 |
| D7 | 2759 | 1476 | 1283 | 53.5 | 36.16 | -0.0041 | -0.0101 | -0.0163 |
| D8 | 2759 | 1429 | 1330 | 51.79 | 37.85 | -0.001 | -0.0066 | -0.0114 |
| D9 | 2759 | 1452 | 1307 | 52.63 | 40.4 | -0.0026 | -0.011 | -0.018 |
| D10 | 2760 | 1151 | 1609 | 41.7 | 65.98 | -0.0034 | -0.0121 | -0.0206 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 40.8022 | 41.5186 | 0.7164 |
| volume_confirmation_score | -1.1404 | -0.9446 | 0.1959 |
| liquidity_score | 2.174 | 2.1044 | -0.0696 |
| overextension_penalty | 0.8589 | 0.7544 | -0.1046 |
| reversal_risk_penalty | 0.7017 | 0.6723 | -0.0293 |
| news_risk_penalty | 0.0909 | 0.1185 | 0.0276 |
| attention_noise_penalty | 0.2127 | 0.238 | 0.0253 |
| market_regime_penalty | 0.0496 | 0.0437 | -0.006 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **20685**
- Benchmark-adjusted coverage: **37.18%**
- Benchmark-adjusted success rate: **52.41%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261125.csv`
- Latest market index date: **2026-11-25**
- Latest price signal date: **2026-11-24**
- Latest candidate signal date: **2026-11-24**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **8**
- Eligible groups: **12**
- Groups close to activation: **5**
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