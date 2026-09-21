# Evaluation Integrity Audit - 2026-09-21

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **283796**
- Unique evaluation keys: **15537**
- Duplicate rows by candidate key: **268259**
- Duplicate rate: **94.53%**
- Exact same-day duplicate rows: **79721**
- Same stock_code + signal_date repeated keys: **14797**
- Same candidate re-evaluated across multiple files: **14798**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 049950 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 049950 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 049950 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 049950 |  |  | 2026-07-20 |  | c9efaf6944e52f9a | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 010140 |  |  | 2026-07-20 |  | 7a97bf307b3df2b2 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 394 | 195 | 199 | 49.49 | -0.0137 | 0.0094 | 0.0026 |
| v2_conservative_ranker | 6523 | 2987 | 3536 | 45.79 | 0.0026 | 0.0084 | 0.0123 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 929 | 401 | 528 | 43.16 | -0.0011 | -0.0062 | -0.0121 |
| avoid | 5594 | 2586 | 3008 | 46.23 | 0.0032 | 0.0109 | 0.0167 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 343 | 157 | 186 | 45.77 | -0.0 | -0.003 | -0.0029 |
| Top 20 | 607 | 270 | 337 | 44.48 | -0.001 | -0.0055 | -0.0052 |
| Top 50 | 899 | 396 | 503 | 44.05 | -0.0008 | -0.0066 | -0.0118 |
| Top 100 | 1232 | 517 | 715 | 41.96 | 0.0024 | 0.0009 | -0.0024 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 653 | 293 | 360 | 44.87 | 19.71 | 0.0005 | 0.0158 | 0.0354 |
| D2 | 652 | 292 | 360 | 44.79 | 26.15 | 0.0074 | 0.0225 | 0.0402 |
| D3 | 652 | 286 | 366 | 43.87 | 29.37 | 0.0077 | 0.0158 | 0.02 |
| D4 | 652 | 311 | 341 | 47.7 | 31.68 | -0.0003 | 0.006 | 0.0018 |
| D5 | 653 | 304 | 349 | 46.55 | 33.63 | 0.0033 | 0.0083 | 0.0053 |
| D6 | 652 | 315 | 337 | 48.31 | 35.38 | -0.0008 | 0.0057 | 0.0069 |
| D7 | 652 | 311 | 341 | 47.7 | 37.03 | 0.0053 | 0.0114 | 0.016 |
| D8 | 652 | 296 | 356 | 45.4 | 38.54 | 0.0036 | 0.0046 | 0.012 |
| D9 | 652 | 294 | 358 | 45.09 | 48.92 | 0.0001 | 0.0004 | -0.0027 |
| D10 | 653 | 285 | 368 | 43.64 | 66.71 | -0.0006 | -0.0062 | -0.0118 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 44.9731 | 44.7245 | -0.2486 |
| volume_confirmation_score | -1.2118 | -1.0592 | 0.1526 |
| liquidity_score | 2.161 | 2.0059 | -0.1551 |
| overextension_penalty | 1.7002 | 1.3812 | -0.319 |
| reversal_risk_penalty | 1.2518 | 1.0601 | -0.1917 |
| news_risk_penalty | 0.1898 | 0.2124 | 0.0226 |
| attention_noise_penalty | 0.3644 | 0.3555 | -0.0088 |
| market_regime_penalty | 0.1011 | 0.086 | -0.0151 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **6374**
- Benchmark-adjusted coverage: **41.02%**
- Benchmark-adjusted success rate: **50.53%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260921.csv`
- Latest market index date: **2026-09-21**
- Latest price signal date: **2026-09-21**
- Latest candidate signal date: **2026-09-21**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **7**
- Eligible groups: **11**
- Groups close to activation: **0**
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