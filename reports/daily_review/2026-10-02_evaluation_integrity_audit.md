# Evaluation Integrity Audit - 2026-10-02

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **423498**
- Unique evaluation keys: **20358**
- Duplicate rows by candidate key: **403140**
- Duplicate rate: **95.19%**
- Exact same-day duplicate rows: **137035**
- Same stock_code + signal_date repeated keys: **19508**
- Same candidate re-evaluated across multiple files: **19509**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  | 2026-07-20 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 189330 |  |  | 2026-07-20 |  | 36aaea07ab7c2d86 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 419540 |  |  | 2026-07-20 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 408 | 201 | 207 | 49.26 | -0.0139 | 0.0096 | 0.0039 |
| v2_conservative_ranker | 8483 | 3966 | 4517 | 46.75 | 0.0022 | 0.0073 | 0.011 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1222 | 555 | 667 | 45.42 | 0.0012 | -0.0009 | -0.0036 |
| avoid | 7261 | 3411 | 3850 | 46.98 | 0.0024 | 0.0087 | 0.0135 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 405 | 190 | 215 | 46.91 | 0.0024 | 0.0016 | 0.0057 |
| Top 20 | 726 | 333 | 393 | 45.87 | 0.001 | -0.0014 | 0.0004 |
| Top 50 | 1147 | 527 | 620 | 45.95 | 0.0014 | -0.0018 | -0.004 |
| Top 100 | 1511 | 666 | 845 | 44.08 | 0.0036 | 0.0038 | 0.0013 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 849 | 390 | 459 | 45.94 | 20.0 | -0.0011 | 0.0109 | 0.0263 |
| D2 | 848 | 400 | 448 | 47.17 | 26.59 | 0.0067 | 0.0157 | 0.0278 |
| D3 | 848 | 369 | 479 | 43.51 | 29.88 | 0.0051 | 0.0119 | 0.0154 |
| D4 | 848 | 411 | 437 | 48.47 | 32.17 | 0.0001 | 0.0073 | 0.0044 |
| D5 | 849 | 419 | 430 | 49.35 | 34.07 | 0.0014 | 0.007 | 0.0082 |
| D6 | 848 | 395 | 453 | 46.58 | 35.79 | -0.0007 | 0.0068 | 0.0086 |
| D7 | 848 | 401 | 447 | 47.29 | 37.35 | 0.0034 | 0.0066 | 0.0087 |
| D8 | 848 | 411 | 437 | 48.47 | 38.74 | 0.0032 | 0.0071 | 0.0101 |
| D9 | 848 | 378 | 470 | 44.58 | 49.6 | 0.0016 | 0.0007 | 0.0027 |
| D10 | 849 | 392 | 457 | 46.17 | 66.68 | 0.0022 | -0.0009 | -0.0035 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 44.9482 | 44.6174 | -0.3307 |
| volume_confirmation_score | -1.2816 | -1.1451 | 0.1365 |
| liquidity_score | 2.1483 | 2.0173 | -0.131 |
| overextension_penalty | 1.6001 | 1.3371 | -0.263 |
| reversal_risk_penalty | 1.1486 | 0.9746 | -0.174 |
| news_risk_penalty | 0.1652 | 0.1864 | 0.0213 |
| attention_noise_penalty | 0.3089 | 0.3236 | 0.0147 |
| market_regime_penalty | 0.1029 | 0.0819 | -0.021 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **7592**
- Benchmark-adjusted coverage: **37.29%**
- Benchmark-adjusted success rate: **52.77%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261002.csv`
- Latest market index date: **2026-10-02**
- Latest price signal date: **2026-10-02**
- Latest candidate signal date: **2026-10-02**
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