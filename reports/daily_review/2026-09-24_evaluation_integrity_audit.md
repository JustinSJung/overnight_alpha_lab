# Evaluation Integrity Audit - 2026-09-24

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **332651**
- Unique evaluation keys: **17081**
- Duplicate rows by candidate key: **315570**
- Duplicate rate: **94.87%**
- Exact same-day duplicate rows: **99596**
- Same stock_code + signal_date repeated keys: **17067**
- Same candidate re-evaluated across multiple files: **17068**
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
| v1/unknown | 400 | 197 | 203 | 49.25 | -0.0135 | 0.0097 | 0.0053 |
| v2_conservative_ranker | 7131 | 3307 | 3824 | 46.37 | 0.0023 | 0.0084 | 0.0124 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1017 | 448 | 569 | 44.05 | 0.0003 | -0.0041 | -0.0078 |
| avoid | 6114 | 2859 | 3255 | 46.76 | 0.0027 | 0.0105 | 0.0158 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 364 | 169 | 195 | 46.43 | 0.0014 | -0.0011 | 0.0019 |
| Top 20 | 648 | 295 | 353 | 45.52 | 0.0006 | -0.0033 | -0.0013 |
| Top 50 | 985 | 442 | 543 | 44.87 | 0.0005 | -0.0044 | -0.0075 |
| Top 100 | 1317 | 560 | 757 | 42.52 | 0.0035 | 0.0027 | -0.0002 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 714 | 315 | 399 | 44.12 | 19.73 | 0.0019 | 0.0158 | 0.0298 |
| D2 | 713 | 336 | 377 | 47.12 | 26.26 | 0.0055 | 0.0195 | 0.0326 |
| D3 | 713 | 320 | 393 | 44.88 | 29.53 | 0.0071 | 0.016 | 0.0229 |
| D4 | 713 | 337 | 376 | 47.27 | 31.84 | 0.0001 | 0.0061 | 0.0054 |
| D5 | 713 | 340 | 373 | 47.69 | 33.77 | 0.0012 | 0.0022 | 0.0011 |
| D6 | 713 | 345 | 368 | 48.39 | 35.54 | -0.0015 | 0.0104 | 0.0138 |
| D7 | 713 | 340 | 373 | 47.69 | 37.17 | 0.0047 | 0.0086 | 0.0125 |
| D8 | 713 | 330 | 383 | 46.28 | 38.61 | 0.0033 | 0.008 | 0.011 |
| D9 | 713 | 322 | 391 | 45.16 | 48.97 | -0.0002 | 0.0002 | 0.0002 |
| D10 | 713 | 322 | 391 | 45.16 | 66.67 | 0.0014 | -0.0035 | -0.0073 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.0647 | 44.7345 | -0.3302 |
| volume_confirmation_score | -1.2527 | -1.125 | 0.1277 |
| liquidity_score | 2.1533 | 2.0 | -0.1533 |
| overextension_penalty | 1.7183 | 1.3494 | -0.3689 |
| reversal_risk_penalty | 1.2252 | 1.05 | -0.1752 |
| news_risk_penalty | 0.1754 | 0.2024 | 0.027 |
| attention_noise_penalty | 0.3579 | 0.3586 | 0.0007 |
| market_regime_penalty | 0.1058 | 0.0842 | -0.0216 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **6817**
- Benchmark-adjusted coverage: **39.91%**
- Benchmark-adjusted success rate: **51.62%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260924.csv`
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