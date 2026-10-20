# Evaluation Integrity Audit - 2026-10-20

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **712481**
- Unique evaluation keys: **29191**
- Duplicate rows by candidate key: **683290**
- Duplicate rate: **95.9%**
- Exact same-day duplicate rows: **254520**
- Same stock_code + signal_date repeated keys: **28289**
- Same candidate re-evaluated across multiple files: **28290**
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
| v1/unknown | 392 | 192 | 200 | 48.98 | -0.0141 | 0.0076 | 0.0047 |
| v2_conservative_ranker | 12914 | 6238 | 6676 | 48.3 | -0.0003 | 0.0011 | 0.0014 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1727 | 736 | 991 | 42.62 | -0.0017 | -0.0111 | -0.0206 |
| avoid | 11187 | 5502 | 5685 | 49.18 | -0.0001 | 0.0032 | 0.0056 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 476 | 211 | 265 | 44.33 | 0.0007 | -0.0042 | -0.0008 |
| Top 20 | 864 | 386 | 478 | 44.68 | 0.0002 | -0.0038 | -0.003 |
| Top 50 | 1401 | 613 | 788 | 43.75 | -0.0003 | -0.0058 | -0.0092 |
| Top 100 | 1907 | 801 | 1106 | 42.0 | 0.0011 | -0.0033 | -0.0098 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1292 | 573 | 719 | 44.35 | 21.31 | 0.0017 | 0.0135 | 0.0302 |
| D2 | 1291 | 605 | 686 | 46.86 | 27.19 | 0.0014 | 0.0066 | 0.0113 |
| D3 | 1291 | 591 | 700 | 45.78 | 29.75 | 0.0019 | 0.0061 | 0.0079 |
| D4 | 1292 | 655 | 637 | 50.7 | 31.93 | -0.001 | 0.0041 | 0.0024 |
| D5 | 1291 | 637 | 654 | 49.34 | 33.86 | -0.0012 | -0.0004 | -0.001 |
| D6 | 1291 | 639 | 652 | 49.5 | 35.6 | -0.0024 | 0.002 | 0.0018 |
| D7 | 1292 | 678 | 614 | 52.48 | 37.2 | 0.0005 | 0.0001 | 0.001 |
| D8 | 1291 | 670 | 621 | 51.9 | 38.62 | -0.001 | -0.0003 | -0.0001 |
| D9 | 1291 | 636 | 655 | 49.26 | 47.49 | -0.0022 | -0.0092 | -0.0115 |
| D10 | 1292 | 554 | 738 | 42.88 | 67.11 | -0.0011 | -0.0097 | -0.02 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 43.5492 | 43.8996 | 0.3504 |
| volume_confirmation_score | -1.3335 | -1.1743 | 0.1593 |
| liquidity_score | 2.1335 | 2.013 | -0.1205 |
| overextension_penalty | 1.2857 | 1.1716 | -0.1141 |
| reversal_risk_penalty | 0.8546 | 0.8087 | -0.0459 |
| news_risk_penalty | 0.1276 | 0.151 | 0.0234 |
| attention_noise_penalty | 0.2601 | 0.2772 | 0.017 |
| market_regime_penalty | 0.0689 | 0.0614 | -0.0075 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **10864**
- Benchmark-adjusted coverage: **37.22%**
- Benchmark-adjusted success rate: **46.98%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261020.csv`
- Latest market index date: **2026-10-20**
- Latest price signal date: **2026-10-20**
- Latest candidate signal date: **2026-10-20**
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
- Ranking status: **Ranking inverted**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.