# Evaluation Integrity Audit - 2026-09-29

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **384689**
- Unique evaluation keys: **18675**
- Duplicate rows by candidate key: **366014**
- Duplicate rate: **95.15%**
- Exact same-day duplicate rows: **121685**
- Same stock_code + signal_date repeated keys: **17868**
- Same candidate re-evaluated across multiple files: **17869**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 010140 |  |  | 2026-07-20 |  | 7a97bf307b3df2b2 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 064400 |  |  | 2026-07-20 |  | 2e327c9a00465eab | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 401 | 198 | 203 | 49.38 | -0.0138 | 0.0083 | 0.0044 |
| v2_conservative_ranker | 7692 | 3624 | 4068 | 47.11 | 0.0017 | 0.0072 | 0.012 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1115 | 483 | 632 | 43.32 | -0.0001 | -0.0042 | -0.0072 |
| avoid | 6577 | 3141 | 3436 | 47.76 | 0.002 | 0.0091 | 0.0152 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 380 | 176 | 204 | 46.32 | 0.0018 | -0.0012 | 0.0027 |
| Top 20 | 677 | 306 | 371 | 45.2 | 0.0008 | -0.0031 | -0.0009 |
| Top 50 | 1047 | 459 | 588 | 43.84 | 0.0001 | -0.0042 | -0.0066 |
| Top 100 | 1413 | 595 | 818 | 42.11 | 0.0028 | 0.0028 | 0.0008 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 770 | 354 | 416 | 45.97 | 20.0 | -0.0003 | 0.0147 | 0.0284 |
| D2 | 769 | 364 | 405 | 47.33 | 26.58 | 0.006 | 0.0156 | 0.0303 |
| D3 | 769 | 343 | 426 | 44.6 | 29.84 | 0.0049 | 0.0121 | 0.0149 |
| D4 | 769 | 380 | 389 | 49.41 | 32.16 | -0.0009 | 0.0051 | 0.005 |
| D5 | 769 | 381 | 388 | 49.54 | 34.06 | 0.0011 | 0.0076 | 0.0113 |
| D6 | 769 | 378 | 391 | 49.15 | 35.78 | -0.0025 | 0.0049 | 0.0083 |
| D7 | 769 | 370 | 399 | 48.11 | 37.37 | 0.0043 | 0.0076 | 0.0132 |
| D8 | 769 | 381 | 388 | 49.54 | 38.76 | 0.0032 | 0.0078 | 0.0126 |
| D9 | 769 | 333 | 436 | 43.3 | 49.85 | 0.0003 | -0.0014 | -0.0007 |
| D10 | 770 | 340 | 430 | 44.16 | 66.66 | 0.001 | -0.0037 | -0.0072 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 44.8967 | 45.0122 | 0.1154 |
| volume_confirmation_score | -1.2642 | -1.1025 | 0.1617 |
| liquidity_score | 2.149 | 2.0175 | -0.1316 |
| overextension_penalty | 1.6432 | 1.3985 | -0.2447 |
| reversal_risk_penalty | 1.1656 | 1.0014 | -0.1642 |
| news_risk_penalty | 0.165 | 0.2026 | 0.0375 |
| attention_noise_penalty | 0.3327 | 0.3409 | 0.0082 |
| market_regime_penalty | 0.1004 | 0.0855 | -0.0149 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **6953**
- Benchmark-adjusted coverage: **37.23%**
- Benchmark-adjusted success rate: **51.04%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260929.csv`
- Latest market index date: **2026-09-29**
- Latest price signal date: **2026-09-29**
- Latest candidate signal date: **2026-09-29**
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