# Evaluation Integrity Audit - 2026-10-21

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **742077**
- Unique evaluation keys: **30125**
- Duplicate rows by candidate key: **711952**
- Duplicate rate: **95.94%**
- Exact same-day duplicate rows: **267179**
- Same stock_code + signal_date repeated keys: **29190**
- Same candidate re-evaluated across multiple files: **29191**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 115480 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 001470 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 023440 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 115480 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 001470 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 023440 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 001470 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 023440 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 115480 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 115480 |  |  | 2026-07-20 |  | 99324e77405de44c | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 001470 |  |  | 2026-07-20 |  | dbc380342d6e7c72 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 023440 |  |  | 2026-07-20 |  | b0166524146063a5 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 405 | 201 | 204 | 49.63 | -0.0143 | 0.0072 | 0.0034 |
| v2_conservative_ranker | 13766 | 6601 | 7165 | 47.95 | -0.0003 | 0.0007 | 0.0004 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1798 | 769 | 1029 | 42.77 | -0.0016 | -0.011 | -0.02 |
| avoid | 11968 | 5832 | 6136 | 48.73 | -0.0001 | 0.0026 | 0.004 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 502 | 225 | 277 | 44.82 | 0.0017 | -0.0033 | 0.0 |
| Top 20 | 911 | 411 | 500 | 45.12 | 0.0003 | -0.0045 | -0.0033 |
| Top 50 | 1467 | 649 | 818 | 44.24 | -0.0003 | -0.0062 | -0.0094 |
| Top 100 | 1989 | 844 | 1145 | 42.43 | 0.001 | -0.0039 | -0.0098 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1377 | 619 | 758 | 44.95 | 21.16 | 0.0015 | 0.0128 | 0.03 |
| D2 | 1377 | 644 | 733 | 46.77 | 27.1 | 0.0001 | 0.0033 | 0.0046 |
| D3 | 1376 | 626 | 750 | 45.49 | 29.66 | 0.002 | 0.0058 | 0.006 |
| D4 | 1377 | 668 | 709 | 48.51 | 31.82 | -0.0 | 0.0032 | -0.0006 |
| D5 | 1376 | 687 | 689 | 49.93 | 33.74 | -0.0012 | 0.0001 | -0.0032 |
| D6 | 1377 | 687 | 690 | 49.89 | 35.5 | -0.0025 | 0.0011 | 0.0022 |
| D7 | 1376 | 692 | 684 | 50.29 | 37.14 | 0.001 | 0.0012 | 0.002 |
| D8 | 1377 | 704 | 673 | 51.13 | 38.56 | -0.0012 | -0.0006 | -0.0021 |
| D9 | 1376 | 675 | 701 | 49.06 | 46.74 | -0.0017 | -0.0087 | -0.0106 |
| D10 | 1377 | 599 | 778 | 43.5 | 66.89 | -0.0011 | -0.0098 | -0.0198 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 43.4483 | 43.6226 | 0.1743 |
| volume_confirmation_score | -1.3477 | -1.2064 | 0.1413 |
| liquidity_score | 2.1323 | 2.0124 | -0.1198 |
| overextension_penalty | 1.2628 | 1.0839 | -0.1789 |
| reversal_risk_penalty | 0.8774 | 0.8007 | -0.0766 |
| news_risk_penalty | 0.1265 | 0.1512 | 0.0247 |
| attention_noise_penalty | 0.2568 | 0.2623 | 0.0055 |
| market_regime_penalty | 0.0673 | 0.0572 | -0.01 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **11396**
- Benchmark-adjusted coverage: **37.83%**
- Benchmark-adjusted success rate: **48.52%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261021.csv`
- Latest market index date: **2026-10-21**
- Latest price signal date: **2026-10-21**
- Latest candidate signal date: **2026-10-21**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **7**
- Eligible groups: **11**
- Groups close to activation: **3**
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