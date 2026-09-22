# Evaluation Integrity Audit - 2026-09-22

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **299560**
- Unique evaluation keys: **16293**
- Duplicate rows by candidate key: **283267**
- Duplicate rate: **94.56%**
- Exact same-day duplicate rows: **86174**
- Same stock_code + signal_date repeated keys: **15536**
- Same candidate re-evaluated across multiple files: **15537**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 263800 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 263800 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 263800 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  | 2026-07-20 |  | 65698458accec52f | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 263800 |  |  | 2026-07-20 |  | dac5f7822d6fdaf1 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 398 | 194 | 204 | 48.74 | -0.0131 | 0.0107 | 0.0061 |
| v2_conservative_ranker | 6806 | 3121 | 3685 | 45.86 | 0.0027 | 0.0095 | 0.0142 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 960 | 420 | 540 | 43.75 | -0.0004 | -0.0054 | -0.0104 |
| avoid | 5846 | 2701 | 3145 | 46.2 | 0.0032 | 0.012 | 0.0185 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 347 | 160 | 187 | 46.11 | 0.0001 | -0.003 | -0.0027 |
| Top 20 | 620 | 279 | 341 | 45.0 | -0.0002 | -0.0047 | -0.0036 |
| Top 50 | 929 | 415 | 514 | 44.67 | -0.0001 | -0.0056 | -0.0102 |
| Top 100 | 1256 | 533 | 723 | 42.44 | 0.003 | 0.002 | -0.0012 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 681 | 304 | 377 | 44.64 | 19.68 | 0.0013 | 0.0149 | 0.0346 |
| D2 | 681 | 314 | 367 | 46.11 | 26.21 | 0.0068 | 0.0214 | 0.035 |
| D3 | 680 | 304 | 376 | 44.71 | 29.45 | 0.0076 | 0.0165 | 0.0198 |
| D4 | 681 | 314 | 367 | 46.11 | 31.77 | -0.0 | 0.007 | 0.0057 |
| D5 | 680 | 323 | 357 | 47.5 | 33.7 | 0.0022 | 0.0057 | 0.0044 |
| D6 | 681 | 321 | 360 | 47.14 | 35.44 | 0.0 | 0.0153 | 0.0247 |
| D7 | 680 | 322 | 358 | 47.35 | 37.08 | 0.005 | 0.011 | 0.017 |
| D8 | 681 | 310 | 371 | 45.52 | 38.55 | 0.0034 | 0.0066 | 0.0096 |
| D9 | 680 | 309 | 371 | 45.44 | 48.62 | 0.0005 | 0.0017 | 0.0003 |
| D10 | 681 | 300 | 381 | 44.05 | 66.62 | 0.0003 | -0.0053 | -0.0097 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.0337 | 44.6864 | -0.3473 |
| volume_confirmation_score | -1.2325 | -1.1167 | 0.1158 |
| liquidity_score | 2.1573 | 2.0098 | -0.1476 |
| overextension_penalty | 1.7367 | 1.3849 | -0.3519 |
| reversal_risk_penalty | 1.2637 | 1.0523 | -0.2113 |
| news_risk_penalty | 0.1753 | 0.2035 | 0.0283 |
| attention_noise_penalty | 0.3563 | 0.3569 | 0.0006 |
| market_regime_penalty | 0.1012 | 0.0841 | -0.0171 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **6577**
- Benchmark-adjusted coverage: **40.37%**
- Benchmark-adjusted success rate: **51.79%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260922.csv`
- Latest market index date: **2026-09-22**
- Latest price signal date: **2026-09-22**
- Latest candidate signal date: **2026-09-22**
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