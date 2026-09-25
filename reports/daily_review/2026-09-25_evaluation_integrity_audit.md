# Evaluation Integrity Audit - 2026-09-25

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **349203**
- Unique evaluation keys: **17081**
- Duplicate rows by candidate key: **332122**
- Duplicate rate: **95.11%**
- Exact same-day duplicate rows: **106835**
- Same stock_code + signal_date repeated keys: **17080**
- Same candidate re-evaluated across multiple files: **17081**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 0126Z0 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 0126Z0 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 0126Z0 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  | 2026-07-20 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 142760 |  |  | 2026-07-20 |  | c16f76d404f3524f | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 415 | 205 | 210 | 49.4 | -0.014 | 0.0089 | 0.0031 |
| v2_conservative_ranker | 7320 | 3381 | 3939 | 46.19 | 0.0023 | 0.0087 | 0.0132 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1040 | 452 | 588 | 43.46 | -0.0003 | -0.0052 | -0.0088 |
| avoid | 6280 | 2929 | 3351 | 46.64 | 0.0027 | 0.0111 | 0.017 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 371 | 171 | 200 | 46.09 | 0.0014 | -0.0012 | 0.0016 |
| Top 20 | 660 | 297 | 363 | 45.0 | -0.0 | -0.0046 | -0.0025 |
| Top 50 | 1007 | 446 | 561 | 44.29 | -0.0001 | -0.0054 | -0.0084 |
| Top 100 | 1360 | 574 | 786 | 42.21 | 0.0029 | 0.0019 | -0.0011 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 732 | 328 | 404 | 44.81 | 19.64 | 0.0007 | 0.0143 | 0.0299 |
| D2 | 732 | 339 | 393 | 46.31 | 26.18 | 0.0062 | 0.0214 | 0.0349 |
| D3 | 732 | 324 | 408 | 44.26 | 29.45 | 0.0076 | 0.0164 | 0.0226 |
| D4 | 732 | 350 | 382 | 47.81 | 31.78 | -0.0004 | 0.007 | 0.0079 |
| D5 | 732 | 347 | 385 | 47.4 | 33.71 | 0.0017 | 0.0059 | 0.0043 |
| D6 | 732 | 349 | 383 | 47.68 | 35.47 | -0.0013 | 0.0091 | 0.0132 |
| D7 | 732 | 350 | 382 | 47.81 | 37.13 | 0.0047 | 0.0097 | 0.0151 |
| D8 | 732 | 341 | 391 | 46.58 | 38.58 | 0.003 | 0.0069 | 0.0105 |
| D9 | 732 | 329 | 403 | 44.95 | 48.83 | 0.0001 | 0.0008 | 0.0007 |
| D10 | 732 | 324 | 408 | 44.26 | 66.65 | 0.0006 | -0.005 | -0.0085 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 44.9981 | 44.702 | -0.2961 |
| volume_confirmation_score | -1.2346 | -1.099 | 0.1356 |
| liquidity_score | 2.1568 | 2.0048 | -0.1519 |
| overextension_penalty | 1.7237 | 1.3519 | -0.3719 |
| reversal_risk_penalty | 1.2506 | 1.0534 | -0.1972 |
| news_risk_penalty | 0.1733 | 0.2016 | 0.0283 |
| attention_noise_penalty | 0.3533 | 0.349 | -0.0043 |
| market_regime_penalty | 0.1035 | 0.0823 | -0.0213 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **6982**
- Benchmark-adjusted coverage: **40.88%**
- Benchmark-adjusted success rate: **51.56%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260925.csv`
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