# Evaluation Integrity Audit - 2026-08-11

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **44835**
- Unique evaluation keys: **4482**
- Duplicate rows by candidate key: **40353**
- Duplicate rate: **90.0%**
- Exact same-day duplicate rows: **8154**
- Same stock_code + signal_date repeated keys: **3655**
- Same candidate re-evaluated across multiple files: **4007**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 141080 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 86c5d271d855238c | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 141080 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 86c5d271d855238c | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 141080 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 86c5d271d855238c | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 374 | 192 | 182 | 51.34 | -0.0113 | -0.004 | -0.0261 |
| v2_conservative_ranker | 1722 | 707 | 1015 | 41.06 | 0.0104 | 0.0243 | 0.0461 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 241 | 130 | 111 | 53.94 | 0.0073 | 0.0125 | 0.0202 |
| avoid | 1481 | 577 | 904 | 38.96 | 0.0109 | 0.0255 | 0.048 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 117 | 68 | 49 | 58.12 | 0.008 | 0.0117 | 0.0195 |
| Top 20 | 169 | 95 | 74 | 56.21 | 0.0083 | 0.0114 | 0.0202 |
| Top 50 | 251 | 136 | 115 | 54.18 | 0.0069 | 0.0112 | 0.0118 |
| Top 100 | 489 | 235 | 254 | 48.06 | 0.0097 | 0.0221 | 0.014 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 173 | 67 | 106 | 38.73 | 17.28 | 0.0118 | 0.0517 | 0.0873 |
| D2 | 172 | 70 | 102 | 40.7 | 22.66 | 0.0072 | 0.0137 | 0.0288 |
| D3 | 172 | 61 | 111 | 35.47 | 25.91 | 0.0176 | 0.034 | 0.0636 |
| D4 | 172 | 62 | 110 | 36.05 | 28.66 | 0.0183 | 0.0412 | 0.0634 |
| D5 | 172 | 63 | 109 | 36.63 | 30.94 | 0.0088 | 0.0329 | 0.0448 |
| D6 | 172 | 69 | 103 | 40.12 | 33.38 | 0.0074 | 0.0156 | 0.0235 |
| D7 | 172 | 76 | 96 | 44.19 | 35.63 | 0.0045 | 0.0061 | 0.024 |
| D8 | 172 | 69 | 103 | 40.12 | 37.7 | 0.0132 | 0.0087 | 0.0379 |
| D9 | 172 | 76 | 96 | 44.19 | 47.96 | 0.0084 | 0.0177 | 0.0487 |
| D10 | 173 | 94 | 79 | 54.34 | 67.98 | 0.0071 | 0.0115 | 0.0108 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.0537 | 42.3893 | -4.6645 |
| volume_confirmation_score | -0.3556 | -0.5576 | -0.202 |
| liquidity_score | 2.3465 | 2.0985 | -0.248 |
| overextension_penalty | 2.6512 | 1.4932 | -1.1581 |
| reversal_risk_penalty | 2.2317 | 1.5918 | -0.64 |
| news_risk_penalty | 0.2716 | 0.1409 | -0.1307 |
| attention_noise_penalty | 0.225 | 0.1969 | -0.0281 |
| market_regime_penalty | 0.0679 | 0.0473 | -0.0206 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **2096**
- Benchmark-adjusted coverage: **46.76%**
- Benchmark-adjusted success rate: **52.48%**
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