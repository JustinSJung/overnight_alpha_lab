# Evaluation Integrity Audit - 2026-08-05

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **26264**
- Unique evaluation keys: **3267**
- Duplicate rows by candidate key: **22997**
- Duplicate rate: **87.56%**
- Exact same-day duplicate rows: **6039**
- Same stock_code + signal_date repeated keys: **2713**
- Same candidate re-evaluated across multiple files: **2830**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 6006 | 3106 | 2900 | 51.71 | -0.0128 | -0.0119 | -0.0359 |
| v2_conservative_ranker | 7521 | 3292 | 4229 | 43.77 | 0.0036 | -0.019 | -0.0511 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 110 | 55 | 55 | 50.0 | 0.0092 | -0.0385 | -0.0701 |
| Top 20 | 220 | 121 | 99 | 55.0 | 0.0098 | -0.0119 | -0.0417 |
| Top 50 | 550 | 252 | 298 | 45.82 | 0.0098 | 0.0065 | -0.0177 |
| Top 100 | 1088 | 479 | 609 | 44.03 | 0.0113 | 0.0053 | -0.0214 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 753 | 351 | 402 | 46.61 | 16.76 | -0.0025 | -0.0185 | -0.0516 |
| D2 | 752 | 365 | 387 | 48.54 | 21.56 | -0.0045 | -0.0292 | -0.0804 |
| D3 | 752 | 281 | 471 | 37.37 | 24.54 | 0.0079 | -0.0095 | -0.0267 |
| D4 | 752 | 299 | 453 | 39.76 | 27.06 | 0.0109 | -0.0132 | -0.0727 |
| D5 | 752 | 311 | 441 | 41.36 | 29.36 | 0.0136 | -0.0131 | -0.0789 |
| D6 | 752 | 343 | 409 | 45.61 | 31.45 | 0.0006 | -0.0163 | -0.055 |
| D7 | 752 | 267 | 485 | 35.51 | 33.82 | 0.0088 | -0.0036 | -0.0369 |
| D8 | 752 | 355 | 397 | 47.21 | 35.8 | -0.0046 | -0.0424 | -0.0569 |
| D9 | 752 | 353 | 399 | 46.94 | 37.9 | -0.0043 | -0.0364 | -0.0475 |
| D10 | 752 | 367 | 385 | 48.8 | 56.21 | 0.0097 | -0.0077 | -0.0056 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.8173 | 39.487 | -2.3302 |
| volume_confirmation_score | -0.6355 | -0.7159 | -0.0805 |
| liquidity_score | 2.2913 | 2.0686 | -0.2227 |
| overextension_penalty | 1.8166 | 0.9119 | -0.9046 |
| reversal_risk_penalty | 2.1833 | 1.565 | -0.6183 |
| news_risk_penalty | 0.1358 | 0.0766 | -0.0592 |
| attention_noise_penalty | 0.2013 | 0.2293 | 0.0279 |
| market_regime_penalty | 0.0705 | 0.0605 | -0.0099 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **7047**
- Benchmark-adjusted coverage: **26.83%**
- Benchmark-adjusted success rate: **51.34%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260805.csv`
- Latest market index date: **2026-08-05**
- Latest price signal date: **2026-08-05**
- Latest candidate signal date: **2026-08-05**
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