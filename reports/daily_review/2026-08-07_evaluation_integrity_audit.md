# Evaluation Integrity Audit - 2026-08-07

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **32962**
- Unique evaluation keys: **3744**
- Duplicate rows by candidate key: **29218**
- Duplicate rate: **88.64%**
- Exact same-day duplicate rows: **6885**
- Same stock_code + signal_date repeated keys: **3169**
- Same candidate re-evaluated across multiple files: **3279**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 189330 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 36aaea07ab7c2d86 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 115480 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 99324e77405de44c | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 189330 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 36aaea07ab7c2d86 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 115480 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 99324e77405de44c | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 189330 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 36aaea07ab7c2d86 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 115480 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 99324e77405de44c | data/predictions/price_candidate_evaluation_20260713.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 6750 | 3488 | 3262 | 51.67 | -0.0126 | -0.0109 | -0.0345 |
| v2_conservative_ranker | 10307 | 4413 | 5894 | 42.82 | 0.0052 | -0.0051 | -0.0176 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 130 | 66 | 64 | 50.77 | 0.0097 | -0.0212 | -0.0462 |
| Top 20 | 260 | 143 | 117 | 55.0 | 0.01 | -0.0056 | -0.0387 |
| Top 50 | 650 | 324 | 326 | 49.85 | 0.007 | 0.0084 | -0.0102 |
| Top 100 | 1278 | 582 | 696 | 45.54 | 0.0095 | 0.0128 | -0.002 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1031 | 457 | 574 | 44.33 | 16.75 | 0.0013 | 0.0079 | 0.0048 |
| D2 | 1031 | 478 | 553 | 46.36 | 21.61 | -0.0005 | -0.0189 | -0.0465 |
| D3 | 1030 | 379 | 651 | 36.8 | 24.65 | 0.009 | 0.0119 | 0.0056 |
| D4 | 1031 | 405 | 626 | 39.28 | 27.2 | 0.0128 | 0.0049 | -0.0196 |
| D5 | 1031 | 456 | 575 | 44.23 | 29.49 | 0.0093 | -0.0007 | -0.0366 |
| D6 | 1030 | 398 | 632 | 38.64 | 31.62 | 0.0058 | 0.001 | -0.0197 |
| D7 | 1031 | 397 | 634 | 38.51 | 33.99 | 0.0089 | 0.0037 | -0.0168 |
| D8 | 1030 | 462 | 568 | 44.85 | 36.02 | -0.0034 | -0.0398 | -0.0299 |
| D9 | 1031 | 482 | 549 | 46.75 | 38.11 | 0.004 | -0.0136 | -0.012 |
| D10 | 1031 | 499 | 532 | 48.4 | 58.26 | 0.0044 | -0.0073 | -0.0008 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.3624 | 39.7071 | -2.6553 |
| volume_confirmation_score | -0.5678 | -0.6769 | -0.1091 |
| liquidity_score | 2.3034 | 2.0779 | -0.2255 |
| overextension_penalty | 1.9512 | 0.9706 | -0.9806 |
| reversal_risk_penalty | 2.1889 | 1.5584 | -0.6305 |
| news_risk_penalty | 0.1414 | 0.0814 | -0.06 |
| attention_noise_penalty | 0.2143 | 0.2259 | 0.0116 |
| market_regime_penalty | 0.0712 | 0.0573 | -0.0138 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **10577**
- Benchmark-adjusted coverage: **32.09%**
- Benchmark-adjusted success rate: **51.43%**
- Benchmark rows available: **88**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260807.csv`
- Latest market index date: **2026-08-07**
- Latest price signal date: **2026-08-07**
- Latest candidate signal date: **2026-08-07**
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