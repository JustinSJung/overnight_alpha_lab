# Evaluation Integrity Audit - 2026-11-19

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1537001**
- Unique evaluation keys: **50778**
- Duplicate rows by candidate key: **1486223**
- Duplicate rate: **96.7%**
- Exact same-day duplicate rows: **629265**
- Same stock_code + signal_date repeated keys: **49582**
- Same candidate re-evaluated across multiple files: **49583**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 001470 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 001470 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 001470 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  | 2026-07-20 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 013520 |  |  | 2026-07-20 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 001470 |  |  | 2026-07-20 |  | dbc380342d6e7c72 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 259 | 131 | 128 | 50.58 | -0.0136 | -0.0151 | -0.0326 |
| v2_conservative_ranker | 25070 | 12526 | 12544 | 49.96 | -0.0018 | -0.007 | -0.0114 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2634 | 1094 | 1540 | 41.53 | -0.0028 | -0.0115 | -0.0192 |
| avoid | 22436 | 11432 | 11004 | 50.95 | -0.0017 | -0.0065 | -0.0105 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 674 | 287 | 387 | 42.58 | -0.0007 | -0.0068 | -0.0063 |
| Top 20 | 1215 | 526 | 689 | 43.29 | -0.001 | -0.0074 | -0.0082 |
| Top 50 | 2103 | 899 | 1204 | 42.75 | -0.0019 | -0.0083 | -0.012 |
| Top 100 | 2843 | 1172 | 1671 | 41.22 | -0.0007 | -0.0063 | -0.0119 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2507 | 1209 | 1298 | 48.22 | 21.27 | -0.0003 | -0.001 | 0.0007 |
| D2 | 2507 | 1276 | 1231 | 50.9 | 26.58 | -0.0029 | -0.0068 | -0.0132 |
| D3 | 2507 | 1237 | 1270 | 49.34 | 28.89 | -0.0005 | -0.0039 | -0.0103 |
| D4 | 2507 | 1242 | 1265 | 49.54 | 30.96 | -0.0011 | -0.0066 | -0.0108 |
| D5 | 2507 | 1286 | 1221 | 51.3 | 32.87 | -0.0017 | -0.0078 | -0.0143 |
| D6 | 2507 | 1318 | 1189 | 52.57 | 34.65 | -0.0028 | -0.0092 | -0.0112 |
| D7 | 2507 | 1320 | 1187 | 52.65 | 36.34 | -0.0031 | -0.0071 | -0.011 |
| D8 | 2507 | 1305 | 1202 | 52.05 | 37.98 | -0.0009 | -0.0063 | -0.0091 |
| D9 | 2507 | 1287 | 1220 | 51.34 | 41.11 | -0.0017 | -0.0097 | -0.0158 |
| D10 | 2507 | 1046 | 1461 | 41.72 | 66.05 | -0.0029 | -0.0115 | -0.0193 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.2229 | 41.8762 | 0.6533 |
| volume_confirmation_score | -1.1846 | -0.9869 | 0.1977 |
| liquidity_score | 2.1656 | 2.0889 | -0.0767 |
| overextension_penalty | 0.9319 | 0.8093 | -0.1227 |
| reversal_risk_penalty | 0.7336 | 0.6844 | -0.0492 |
| news_risk_penalty | 0.096 | 0.1232 | 0.0272 |
| attention_noise_penalty | 0.2151 | 0.241 | 0.0259 |
| market_regime_penalty | 0.0493 | 0.0458 | -0.0036 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **18612**
- Benchmark-adjusted coverage: **36.65%**
- Benchmark-adjusted success rate: **51.35%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261119.csv`
- Latest market index date: **2026-11-19**
- Latest price signal date: **2026-11-18**
- Latest candidate signal date: **2026-11-18**
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