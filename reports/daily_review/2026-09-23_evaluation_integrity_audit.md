# Evaluation Integrity Audit - 2026-09-23

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **316099**
- Unique evaluation keys: **17068**
- Duplicate rows by candidate key: **299031**
- Duplicate rate: **94.6%**
- Exact same-day duplicate rows: **92714**
- Same stock_code + signal_date repeated keys: **16292**
- Same candidate re-evaluated across multiple files: **16293**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 003070 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 003070 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003070 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003070 |  |  | 2026-07-20 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 187870 |  |  | 2026-07-20 |  | d7198ed24f95f4db | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 396 | 196 | 200 | 49.49 | -0.0142 | 0.008 | 0.0005 |
| v2_conservative_ranker | 7060 | 3290 | 3770 | 46.6 | 0.0021 | 0.0082 | 0.0118 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1011 | 443 | 568 | 43.82 | -0.0005 | -0.0056 | -0.0097 |
| avoid | 6049 | 2847 | 3202 | 47.07 | 0.0025 | 0.0105 | 0.0155 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 364 | 168 | 196 | 46.15 | 0.0006 | -0.0028 | -0.0024 |
| Top 20 | 647 | 291 | 356 | 44.98 | -0.0005 | -0.0054 | -0.0045 |
| Top 50 | 981 | 436 | 545 | 44.44 | -0.0003 | -0.0059 | -0.0094 |
| Top 100 | 1304 | 553 | 751 | 42.41 | 0.0027 | 0.0007 | -0.0021 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 706 | 324 | 382 | 45.89 | 19.75 | -0.0004 | 0.0136 | 0.0263 |
| D2 | 706 | 322 | 384 | 45.61 | 26.28 | 0.0064 | 0.0208 | 0.0356 |
| D3 | 706 | 325 | 381 | 46.03 | 29.56 | 0.0058 | 0.0142 | 0.019 |
| D4 | 706 | 344 | 362 | 48.73 | 31.88 | -0.0 | 0.0058 | 0.0047 |
| D5 | 706 | 334 | 372 | 47.31 | 33.79 | 0.0012 | 0.0057 | 0.0041 |
| D6 | 706 | 339 | 367 | 48.02 | 35.55 | -0.0009 | 0.0105 | 0.0131 |
| D7 | 706 | 342 | 364 | 48.44 | 37.19 | 0.0045 | 0.0086 | 0.0137 |
| D8 | 706 | 327 | 379 | 46.32 | 38.62 | 0.0037 | 0.0076 | 0.0111 |
| D9 | 706 | 318 | 388 | 45.04 | 49.09 | -0.0003 | 0.0001 | -0.0004 |
| D10 | 706 | 315 | 391 | 44.62 | 66.68 | 0.0005 | -0.0057 | -0.0101 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 44.9748 | 44.8281 | -0.1467 |
| volume_confirmation_score | -1.2739 | -1.1141 | 0.1598 |
| liquidity_score | 2.1471 | 2.0019 | -0.1453 |
| overextension_penalty | 1.6928 | 1.3431 | -0.3498 |
| reversal_risk_penalty | 1.2081 | 1.0509 | -0.1572 |
| news_risk_penalty | 0.1705 | 0.2077 | 0.0372 |
| attention_noise_penalty | 0.3605 | 0.3533 | -0.0072 |
| market_regime_penalty | 0.1033 | 0.0849 | -0.0185 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **6749**
- Benchmark-adjusted coverage: **39.54%**
- Benchmark-adjusted success rate: **51.15%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260923.csv`
- Latest market index date: **2026-09-23**
- Latest price signal date: **2026-09-23**
- Latest candidate signal date: **2026-09-23**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **7**
- Eligible groups: **11**
- Groups close to activation: **1**
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