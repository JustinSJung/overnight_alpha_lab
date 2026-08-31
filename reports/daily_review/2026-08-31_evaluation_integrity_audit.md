# Evaluation Integrity Audit - 2026-08-31

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **131657**
- Unique evaluation keys: **7614**
- Duplicate rows by candidate key: **124043**
- Duplicate rate: **94.22%**
- Exact same-day duplicate rows: **19204**
- Same stock_code + signal_date repeated keys: **7240**
- Same candidate re-evaluated across multiple files: **7241**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 003070 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 322780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 003070 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 322780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003070 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 322780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003070 |  |  | 2026-07-20 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 322780 |  |  | 2026-07-20 |  | 588b4708dca67cf1 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 388 | 194 | 194 | 50.0 | -0.0151 | 0.0043 | -0.0 |
| v2_conservative_ranker | 2997 | 1250 | 1747 | 41.71 | 0.006 | 0.0218 | 0.0311 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 593 | 239 | 354 | 40.3 | -0.0011 | -0.0037 | -0.0106 |
| avoid | 2404 | 1011 | 1393 | 42.05 | 0.0077 | 0.0276 | 0.0409 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 218 | 103 | 115 | 47.25 | 0.0033 | 0.006 | 0.0085 |
| Top 20 | 370 | 171 | 199 | 46.22 | 0.0017 | 0.0004 | 0.002 |
| Top 50 | 565 | 240 | 325 | 42.48 | -0.0005 | -0.0044 | -0.01 |
| Top 100 | 870 | 342 | 528 | 39.31 | 0.0042 | 0.0081 | 0.0043 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 300 | 130 | 170 | 43.33 | 18.28 | 0.009 | 0.0338 | 0.0539 |
| D2 | 300 | 118 | 182 | 39.33 | 24.5 | 0.0123 | 0.0526 | 0.0774 |
| D3 | 299 | 117 | 182 | 39.13 | 28.03 | 0.0175 | 0.0279 | 0.0384 |
| D4 | 300 | 125 | 175 | 41.67 | 30.78 | 0.0029 | 0.033 | 0.0439 |
| D5 | 300 | 131 | 169 | 43.67 | 33.17 | 0.0022 | 0.0148 | 0.0125 |
| D6 | 299 | 134 | 165 | 44.82 | 35.17 | 0.0027 | 0.0212 | 0.0395 |
| D7 | 300 | 122 | 178 | 40.67 | 37.11 | 0.0089 | 0.0182 | 0.025 |
| D8 | 299 | 132 | 167 | 44.15 | 39.23 | 0.0063 | 0.0202 | 0.0361 |
| D9 | 300 | 113 | 187 | 37.67 | 61.66 | -0.0031 | -0.0113 | -0.0165 |
| D10 | 300 | 128 | 172 | 42.67 | 69.36 | 0.0016 | 0.0025 | -0.0051 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.847 | 46.197 | -1.65 |
| volume_confirmation_score | -0.5339 | -0.4649 | 0.069 |
| liquidity_score | 2.3224 | 2.1156 | -0.2068 |
| overextension_penalty | 2.4852 | 1.5495 | -0.9357 |
| reversal_risk_penalty | 1.9836 | 1.4192 | -0.5644 |
| news_risk_penalty | 0.3224 | 0.3039 | -0.0185 |
| attention_noise_penalty | 0.229 | 0.2121 | -0.0169 |
| market_regime_penalty | 0.0768 | 0.0595 | -0.0173 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3126**
- Benchmark-adjusted coverage: **41.06%**
- Benchmark-adjusted success rate: **50.29%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260831.csv`
- Latest market index date: **2026-08-31**
- Latest price signal date: **2026-08-31**
- Latest candidate signal date: **2026-08-31**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **5**
- Eligible groups: **6**
- Groups close to activation: **0**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Some learned event rules are active.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Partial**
- Ranking status: **Ranking improving**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.