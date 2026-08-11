# Evaluation Integrity Audit - 2026-08-11

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **44848**
- Unique evaluation keys: **4495**
- Duplicate rows by candidate key: **40353**
- Duplicate rate: **89.98%**
- Exact same-day duplicate rows: **8154**
- Same stock_code + signal_date repeated keys: **3655**
- Same candidate re-evaluated across multiple files: **4007**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 189330 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 36aaea07ab7c2d86 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 236810 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 9902a24996692a3c | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 066430 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 8666e9dd25327f4e | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 091590 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | a547f253cce6dd59 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 001470 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | bd295081d3bc1d5a | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 189330 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 36aaea07ab7c2d86 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 236810 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 9902a24996692a3c | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 066430 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 8666e9dd25327f4e | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 091590 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | a547f253cce6dd59 | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 001470 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | bd295081d3bc1d5a | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 189330 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 36aaea07ab7c2d86 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 236810 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 9902a24996692a3c | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 066430 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 8666e9dd25327f4e | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 091590 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | a547f253cce6dd59 | data/predictions/price_candidate_evaluation_20260713.csv | pending |
| 001470 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | bd295081d3bc1d5a | data/predictions/price_candidate_evaluation_20260713.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 367 | 188 | 179 | 51.23 | -0.0116 | -0.0039 | -0.0243 |
| v2_conservative_ranker | 1723 | 702 | 1021 | 40.74 | 0.0109 | 0.0246 | 0.0465 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 241 | 132 | 109 | 54.77 | 0.0078 | 0.0129 | 0.0204 |
| avoid | 1482 | 570 | 912 | 38.46 | 0.0114 | 0.0259 | 0.0485 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 117 | 68 | 49 | 58.12 | 0.0078 | 0.0118 | 0.0196 |
| Top 20 | 169 | 96 | 73 | 56.8 | 0.0083 | 0.0115 | 0.0204 |
| Top 50 | 251 | 137 | 114 | 54.58 | 0.0073 | 0.0115 | 0.012 |
| Top 100 | 489 | 237 | 252 | 48.47 | 0.0099 | 0.0222 | 0.0141 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 173 | 66 | 107 | 38.15 | 17.28 | 0.0125 | 0.0526 | 0.0873 |
| D2 | 172 | 69 | 103 | 40.12 | 22.66 | 0.0076 | 0.0135 | 0.0298 |
| D3 | 172 | 61 | 111 | 35.47 | 25.91 | 0.0177 | 0.0339 | 0.0635 |
| D4 | 172 | 63 | 109 | 36.63 | 28.65 | 0.0179 | 0.0408 | 0.0638 |
| D5 | 173 | 60 | 113 | 34.68 | 30.93 | 0.0092 | 0.033 | 0.0452 |
| D6 | 172 | 69 | 103 | 40.12 | 33.38 | 0.0078 | 0.0166 | 0.0239 |
| D7 | 172 | 73 | 99 | 42.44 | 35.63 | 0.0048 | 0.007 | 0.0242 |
| D8 | 172 | 68 | 104 | 39.53 | 37.7 | 0.0149 | 0.0093 | 0.0389 |
| D9 | 172 | 78 | 94 | 45.35 | 47.96 | 0.009 | 0.0182 | 0.0497 |
| D10 | 173 | 95 | 78 | 54.91 | 67.98 | 0.0075 | 0.0116 | 0.011 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.0917 | 42.3807 | -4.711 |
| volume_confirmation_score | -0.3387 | -0.566 | -0.2273 |
| liquidity_score | 2.3504 | 2.0979 | -0.2525 |
| overextension_penalty | 2.6275 | 1.5137 | -1.1138 |
| reversal_risk_penalty | 2.1944 | 1.6206 | -0.5739 |
| news_risk_penalty | 0.2735 | 0.1401 | -0.1334 |
| attention_noise_penalty | 0.2266 | 0.1958 | -0.0308 |
| market_regime_penalty | 0.0712 | 0.047 | -0.0242 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **2090**
- Benchmark-adjusted coverage: **46.5%**
- Benchmark-adjusted success rate: **52.15%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260811.csv`
- Latest market index date: **2026-08-11**
- Latest price signal date: **2026-08-11**
- Latest candidate signal date: **2026-08-11**
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