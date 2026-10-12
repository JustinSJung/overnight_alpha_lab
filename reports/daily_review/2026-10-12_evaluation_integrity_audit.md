# Evaluation Integrity Audit - 2026-10-12

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **553900**
- Unique evaluation keys: **23905**
- Duplicate rows by candidate key: **529995**
- Duplicate rate: **95.68%**
- Exact same-day duplicate rows: **190419**
- Same stock_code + signal_date repeated keys: **22995**
- Same candidate re-evaluated across multiple files: **22996**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 380540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 013720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 380540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 380540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 380540 |  |  | 2026-07-20 |  | b75cf7aaab02ac1a | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 013720 |  |  | 2026-07-20 |  | 9fea8ac7ec222eec | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 416 | 206 | 210 | 49.52 | -0.0141 | 0.0088 | 0.0032 |
| v2_conservative_ranker | 10164 | 4798 | 5366 | 47.21 | 0.0012 | 0.0068 | 0.0126 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1678 | 723 | 955 | 43.09 | -0.0011 | -0.0035 | 0.001 |
| avoid | 8486 | 4075 | 4411 | 48.02 | 0.0017 | 0.0087 | 0.0146 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 445 | 201 | 244 | 45.17 | 0.0014 | -0.0011 | 0.0054 |
| Top 20 | 807 | 365 | 442 | 45.23 | 0.0004 | -0.0023 | 0.0022 |
| Top 50 | 1346 | 595 | 751 | 44.21 | -0.0001 | -0.0025 | 0.0 |
| Top 100 | 1888 | 800 | 1088 | 42.37 | 0.0016 | 0.0018 | 0.0049 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1017 | 461 | 556 | 45.33 | 20.38 | 0.001 | 0.0156 | 0.0307 |
| D2 | 1016 | 478 | 538 | 47.05 | 27.06 | 0.0051 | 0.0141 | 0.0231 |
| D3 | 1016 | 464 | 552 | 45.67 | 30.28 | 0.0026 | 0.0114 | 0.0137 |
| D4 | 1017 | 492 | 525 | 48.38 | 32.56 | 0.0014 | 0.0072 | 0.0039 |
| D5 | 1016 | 508 | 508 | 50.0 | 34.49 | -0.0011 | 0.0029 | 0.0103 |
| D6 | 1016 | 487 | 529 | 47.93 | 36.22 | 0.0007 | 0.0074 | 0.0115 |
| D7 | 1017 | 481 | 536 | 47.3 | 37.77 | 0.0027 | 0.0067 | 0.0126 |
| D8 | 1016 | 521 | 495 | 51.28 | 39.15 | 0.0015 | 0.0063 | 0.0123 |
| D9 | 1016 | 475 | 541 | 46.75 | 54.64 | -0.0005 | -0.0017 | 0.0057 |
| D10 | 1017 | 431 | 586 | 42.38 | 68.18 | -0.0009 | -0.0037 | -0.0029 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.3132 | 45.5204 | 0.2072 |
| volume_confirmation_score | -1.1577 | -1.0418 | 0.1159 |
| liquidity_score | 2.1722 | 2.0321 | -0.1401 |
| overextension_penalty | 1.6101 | 1.3471 | -0.2629 |
| reversal_risk_penalty | 1.0959 | 0.9486 | -0.1473 |
| news_risk_penalty | 0.1615 | 0.186 | 0.0245 |
| attention_noise_penalty | 0.2848 | 0.2995 | 0.0147 |
| market_regime_penalty | 0.0909 | 0.0753 | -0.0156 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **8392**
- Benchmark-adjusted coverage: **35.11%**
- Benchmark-adjusted success rate: **51.13%**
- Benchmark rows available: **76**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261012.csv`
- Latest market index date: **2026-10-12**
- Latest price signal date: **2026-10-12**
- Latest candidate signal date: **2026-10-12**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **7**
- Eligible groups: **11**
- Groups close to activation: **2**
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