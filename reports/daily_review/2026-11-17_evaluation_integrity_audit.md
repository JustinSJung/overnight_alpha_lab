# Evaluation Integrity Audit - 2026-11-17

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1437698**
- Unique evaluation keys: **48398**
- Duplicate rows by candidate key: **1389300**
- Duplicate rate: **96.63%**
- Exact same-day duplicate rows: **582129**
- Same stock_code + signal_date repeated keys: **47219**
- Same candidate re-evaluated across multiple files: **47220**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 001470 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 001470 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 001470 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 091590 |  |  | 2026-07-20 |  | 5bc402d6287954af | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 001470 |  |  | 2026-07-20 |  | dbc380342d6e7c72 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 328 | 161 | 167 | 49.09 | -0.0104 | 0.0001 | -0.0187 |
| v2_conservative_ranker | 23934 | 11994 | 11940 | 50.11 | -0.0018 | -0.0052 | -0.01 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2402 | 1026 | 1376 | 42.71 | -0.0023 | -0.0103 | -0.0186 |
| avoid | 21532 | 10968 | 10564 | 50.94 | -0.0017 | -0.0047 | -0.009 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 642 | 276 | 366 | 42.99 | -0.0003 | -0.0063 | -0.0063 |
| Top 20 | 1151 | 508 | 643 | 44.14 | -0.0006 | -0.0075 | -0.008 |
| Top 50 | 1955 | 852 | 1103 | 43.58 | -0.0016 | -0.0075 | -0.0111 |
| Top 100 | 2596 | 1102 | 1494 | 42.45 | -0.0002 | -0.0052 | -0.0113 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2394 | 1153 | 1241 | 48.16 | 21.15 | -0.0002 | 0.0034 | 0.0077 |
| D2 | 2393 | 1210 | 1183 | 50.56 | 26.47 | -0.0032 | -0.0058 | -0.0121 |
| D3 | 2393 | 1191 | 1202 | 49.77 | 28.76 | -0.0008 | -0.0029 | -0.0098 |
| D4 | 2394 | 1189 | 1205 | 49.67 | 30.81 | -0.0012 | -0.0043 | -0.009 |
| D5 | 2393 | 1223 | 1170 | 51.11 | 32.74 | -0.0015 | -0.0055 | -0.0129 |
| D6 | 2393 | 1257 | 1136 | 52.53 | 34.53 | -0.0029 | -0.0073 | -0.0094 |
| D7 | 2394 | 1267 | 1127 | 52.92 | 36.24 | -0.0029 | -0.0067 | -0.0105 |
| D8 | 2393 | 1238 | 1155 | 51.73 | 37.9 | -0.0011 | -0.0053 | -0.0092 |
| D9 | 2393 | 1241 | 1152 | 51.86 | 40.17 | -0.0015 | -0.0075 | -0.0142 |
| D10 | 2394 | 1025 | 1369 | 42.82 | 65.72 | -0.0025 | -0.0105 | -0.019 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.1396 | 41.6502 | 0.5106 |
| volume_confirmation_score | -1.2207 | -1.0163 | 0.2044 |
| liquidity_score | 2.1576 | 2.0774 | -0.0802 |
| overextension_penalty | 0.9233 | 0.8179 | -0.1054 |
| reversal_risk_penalty | 0.7266 | 0.6943 | -0.0323 |
| news_risk_penalty | 0.0935 | 0.1193 | 0.0257 |
| attention_noise_penalty | 0.2265 | 0.2448 | 0.0184 |
| market_regime_penalty | 0.0515 | 0.0472 | -0.0043 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **17626**
- Benchmark-adjusted coverage: **36.42%**
- Benchmark-adjusted success rate: **50.81%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261117.csv`
- Latest market index date: **2026-11-17**
- Latest price signal date: **2026-11-16**
- Latest candidate signal date: **2026-11-16**
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