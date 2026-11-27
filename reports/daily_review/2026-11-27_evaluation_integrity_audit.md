# Evaluation Integrity Audit - 2026-11-27

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1864026**
- Unique evaluation keys: **58110**
- Duplicate rows by candidate key: **1805916**
- Duplicate rate: **96.88%**
- Exact same-day duplicate rows: **782254**
- Same stock_code + signal_date repeated keys: **56870**
- Same candidate re-evaluated across multiple files: **56871**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003490 |  |  | 2026-07-20 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 288980 |  |  | 2026-07-20 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 020560 |  |  | 2026-07-20 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260720.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 259 | 131 | 128 | 50.58 | -0.0136 | -0.0151 | -0.0326 |
| v2_conservative_ranker | 28806 | 14568 | 14238 | 50.57 | -0.0021 | -0.0082 | -0.0159 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2894 | 1224 | 1670 | 42.29 | -0.0027 | -0.0108 | -0.0217 |
| avoid | 25912 | 13344 | 12568 | 51.5 | -0.0021 | -0.0079 | -0.0153 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 682 | 294 | 388 | 43.11 | -0.0006 | -0.0068 | -0.0099 |
| Top 20 | 1278 | 564 | 714 | 44.13 | -0.0008 | -0.007 | -0.0101 |
| Top 50 | 2311 | 1009 | 1302 | 43.66 | -0.0016 | -0.0074 | -0.0135 |
| Top 100 | 2916 | 1218 | 1698 | 41.77 | -0.0013 | -0.0055 | -0.0125 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2881 | 1413 | 1468 | 49.05 | 21.26 | -0.0004 | -0.0035 | -0.0071 |
| D2 | 2881 | 1473 | 1408 | 51.13 | 26.42 | -0.0032 | -0.0099 | -0.0194 |
| D3 | 2880 | 1473 | 1407 | 51.15 | 28.66 | -0.0024 | -0.0069 | -0.0156 |
| D4 | 2881 | 1451 | 1430 | 50.36 | 30.64 | -0.002 | -0.0058 | -0.0124 |
| D5 | 2880 | 1469 | 1411 | 51.01 | 32.5 | -0.0016 | -0.0103 | -0.0185 |
| D6 | 2881 | 1536 | 1345 | 53.31 | 34.31 | -0.0022 | -0.0087 | -0.0154 |
| D7 | 2880 | 1530 | 1350 | 53.12 | 36.07 | -0.0036 | -0.0088 | -0.0158 |
| D8 | 2881 | 1497 | 1384 | 51.96 | 37.79 | -0.001 | -0.0072 | -0.0133 |
| D9 | 2880 | 1507 | 1373 | 52.33 | 40.0 | -0.002 | -0.0102 | -0.0191 |
| D10 | 2881 | 1219 | 1662 | 42.31 | 65.85 | -0.0028 | -0.0109 | -0.022 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 40.563 | 41.3206 | 0.7575 |
| volume_confirmation_score | -1.1046 | -0.9322 | 0.1723 |
| liquidity_score | 2.1813 | 2.108 | -0.0733 |
| overextension_penalty | 0.8053 | 0.7105 | -0.0948 |
| reversal_risk_penalty | 0.6779 | 0.66 | -0.0178 |
| news_risk_penalty | 0.0888 | 0.1125 | 0.0238 |
| attention_noise_penalty | 0.2049 | 0.2268 | 0.0219 |
| market_regime_penalty | 0.0479 | 0.0423 | -0.0056 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **22170**
- Benchmark-adjusted coverage: **38.15%**
- Benchmark-adjusted success rate: **51.81%**
- Benchmark rows available: **86**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261127.csv`
- Latest market index date: **2026-11-27**
- Latest price signal date: **2026-11-26**
- Latest candidate signal date: **2026-11-26**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **8**
- Eligible groups: **12**
- Groups close to activation: **4**
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