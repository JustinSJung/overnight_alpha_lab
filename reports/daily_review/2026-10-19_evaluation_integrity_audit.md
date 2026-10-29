# Evaluation Integrity Audit - 2026-10-19

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **683819**
- Unique evaluation keys: **28290**
- Duplicate rows by candidate key: **655529**
- Duplicate rate: **95.86%**
- Exact same-day duplicate rows: **242666**
- Same stock_code + signal_date repeated keys: **27380**
- Same candidate re-evaluated across multiple files: **27381**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 088790 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 088790 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 088790 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  | 2026-07-20 |  | 65698458accec52f | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 088790 |  |  | 2026-07-20 |  | 995995047c138c16 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 403 | 202 | 201 | 50.12 | -0.0148 | 0.0046 | 0.0011 |
| v2_conservative_ranker | 12657 | 6097 | 6560 | 48.17 | -0.0002 | -0.0009 | 0.0023 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1762 | 744 | 1018 | 42.22 | -0.0017 | -0.0112 | -0.0206 |
| avoid | 10895 | 5353 | 5542 | 49.13 | 0.0001 | 0.001 | 0.0068 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 478 | 212 | 266 | 44.35 | 0.0011 | -0.004 | -0.001 |
| Top 20 | 874 | 387 | 487 | 44.28 | 0.0004 | -0.0042 | -0.0033 |
| Top 50 | 1431 | 621 | 810 | 43.4 | -0.0005 | -0.0062 | -0.0097 |
| Top 100 | 1959 | 819 | 1140 | 41.81 | 0.0011 | -0.0034 | -0.0095 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1266 | 572 | 694 | 45.18 | 21.34 | 0.0021 | 0.0121 | 0.0321 |
| D2 | 1266 | 627 | 639 | 49.53 | 27.25 | 0.0015 | 0.0016 | 0.0132 |
| D3 | 1265 | 590 | 675 | 46.64 | 29.86 | 0.0015 | 0.0021 | 0.0094 |
| D4 | 1266 | 630 | 636 | 49.76 | 32.04 | -0.0005 | 0.0012 | 0.0021 |
| D5 | 1266 | 630 | 636 | 49.76 | 33.96 | -0.0005 | -0.0001 | 0.0022 |
| D6 | 1265 | 625 | 640 | 49.41 | 35.7 | -0.0032 | -0.0021 | 0.0008 |
| D7 | 1266 | 628 | 638 | 49.61 | 37.3 | 0.0011 | -0.001 | 0.0015 |
| D8 | 1265 | 654 | 611 | 51.7 | 38.71 | -0.0003 | -0.0008 | 0.0014 |
| D9 | 1266 | 604 | 662 | 47.71 | 48.72 | -0.0022 | -0.0101 | -0.0112 |
| D10 | 1266 | 537 | 729 | 42.42 | 67.27 | -0.0011 | -0.0098 | -0.0206 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 43.6689 | 44.2072 | 0.5383 |
| volume_confirmation_score | -1.3078 | -1.1473 | 0.1605 |
| liquidity_score | 2.1402 | 2.0287 | -0.1116 |
| overextension_penalty | 1.3273 | 1.1741 | -0.1533 |
| reversal_risk_penalty | 0.8806 | 0.8108 | -0.0698 |
| news_risk_penalty | 0.1345 | 0.1575 | 0.023 |
| attention_noise_penalty | 0.2529 | 0.2634 | 0.0104 |
| market_regime_penalty | 0.0686 | 0.0607 | -0.0079 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **10604**
- Benchmark-adjusted coverage: **37.48%**
- Benchmark-adjusted success rate: **46.47%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261019.csv`
- Latest market index date: **2026-10-19**
- Latest price signal date: **2026-10-19**
- Latest candidate signal date: **2026-10-19**
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