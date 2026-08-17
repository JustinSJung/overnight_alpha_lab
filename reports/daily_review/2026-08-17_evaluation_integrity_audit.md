# Evaluation Integrity Audit - 2026-08-17

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **64460**
- Unique evaluation keys: **5592**
- Duplicate rows by candidate key: **58868**
- Duplicate rate: **91.32%**
- Exact same-day duplicate rows: **9846**
- Same stock_code + signal_date repeated keys: **4735**
- Same candidate re-evaluated across multiple files: **5091**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 378 | 194 | 184 | 51.32 | -0.0115 | -0.0047 | -0.0266 |
| v2_conservative_ranker | 2037 | 818 | 1219 | 40.16 | 0.01 | 0.0258 | 0.0497 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 395 | 188 | 207 | 47.59 | 0.0037 | 0.0055 | 0.0214 |
| avoid | 1642 | 630 | 1012 | 38.37 | 0.0115 | 0.0298 | 0.0534 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 147 | 77 | 70 | 52.38 | 0.006 | 0.0077 | 0.0181 |
| Top 20 | 229 | 117 | 112 | 51.09 | 0.0058 | 0.0086 | 0.0182 |
| Top 50 | 390 | 189 | 201 | 48.46 | 0.0041 | 0.0055 | 0.0171 |
| Top 100 | 643 | 293 | 350 | 45.57 | 0.0069 | 0.0154 | 0.0159 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 204 | 83 | 121 | 40.69 | 17.54 | 0.0062 | 0.0406 | 0.0789 |
| D2 | 204 | 78 | 126 | 38.24 | 23.28 | 0.0117 | 0.0267 | 0.0426 |
| D3 | 203 | 72 | 131 | 35.47 | 26.69 | 0.0203 | 0.04 | 0.0662 |
| D4 | 204 | 78 | 126 | 38.24 | 29.51 | 0.0151 | 0.0372 | 0.0558 |
| D5 | 204 | 70 | 134 | 34.31 | 31.89 | 0.0117 | 0.0266 | 0.0322 |
| D6 | 203 | 86 | 117 | 42.36 | 34.45 | 0.0029 | 0.0177 | 0.0373 |
| D7 | 204 | 78 | 126 | 38.24 | 36.67 | 0.0132 | 0.0225 | 0.0511 |
| D8 | 203 | 79 | 124 | 38.92 | 38.78 | 0.0119 | 0.0269 | 0.0623 |
| D9 | 204 | 99 | 105 | 48.53 | 60.86 | 0.0025 | 0.0051 | 0.0294 |
| D10 | 204 | 95 | 109 | 46.57 | 69.73 | 0.0042 | 0.0064 | 0.0143 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 48.483 | 44.6177 | -3.8653 |
| volume_confirmation_score | -0.3146 | -0.4728 | -0.1582 |
| liquidity_score | 2.3545 | 2.1091 | -0.2454 |
| overextension_penalty | 2.6527 | 1.5057 | -1.1469 |
| reversal_risk_penalty | 2.1649 | 1.5557 | -0.6092 |
| news_risk_penalty | 0.3337 | 0.1993 | -0.1344 |
| attention_noise_penalty | 0.2101 | 0.1839 | -0.0262 |
| market_regime_penalty | 0.066 | 0.0509 | -0.0152 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **2415**
- Benchmark-adjusted coverage: **43.19%**
- Benchmark-adjusted success rate: **51.22%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260817.csv`
- Latest market index date: **2026-08-14**
- Latest price signal date: **2026-08-14**
- Latest candidate signal date: **2026-08-14**
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