# Evaluation Integrity Audit - 2026-10-22

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **772600**
- Unique evaluation keys: **31052**
- Duplicate rows by candidate key: **741548**
- Duplicate rate: **95.98%**
- Exact same-day duplicate rows: **280391**
- Same stock_code + signal_date repeated keys: **30124**
- Same candidate re-evaluated across multiple files: **30125**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 142760 |  |  | 2026-07-20 |  | c16f76d404f3524f | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 025980 |  |  | 2026-07-20 |  | 331c322c17fab620 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 407 | 201 | 206 | 49.39 | -0.0138 | -0.0034 | -0.0137 |
| v2_conservative_ranker | 14155 | 6818 | 7337 | 48.17 | -0.0003 | -0.0004 | 0.0015 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1815 | 767 | 1048 | 42.26 | -0.0019 | -0.0113 | -0.0208 |
| avoid | 12340 | 6051 | 6289 | 49.04 | -0.0001 | 0.0013 | 0.0053 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 507 | 219 | 288 | 43.2 | 0.0002 | -0.0049 | -0.0042 |
| Top 20 | 920 | 405 | 515 | 44.02 | 0.0 | -0.0048 | -0.0046 |
| Top 50 | 1484 | 645 | 839 | 43.46 | -0.0006 | -0.0065 | -0.0102 |
| Top 100 | 2008 | 843 | 1165 | 41.98 | 0.0006 | -0.0045 | -0.0111 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1416 | 630 | 786 | 44.49 | 21.52 | 0.0015 | 0.0103 | 0.026 |
| D2 | 1415 | 657 | 758 | 46.43 | 27.21 | 0.0015 | 0.0013 | 0.0074 |
| D3 | 1416 | 653 | 763 | 46.12 | 29.71 | 0.0017 | 0.0039 | 0.0099 |
| D4 | 1415 | 694 | 721 | 49.05 | 31.85 | -0.0002 | 0.0012 | 0.0017 |
| D5 | 1416 | 707 | 709 | 49.93 | 33.76 | -0.0011 | 0.0003 | 0.0007 |
| D6 | 1415 | 703 | 712 | 49.68 | 35.51 | -0.0022 | -0.0 | 0.003 |
| D7 | 1415 | 738 | 677 | 52.16 | 37.12 | 0.0003 | 0.0 | 0.0026 |
| D8 | 1416 | 729 | 687 | 51.48 | 38.54 | -0.0018 | -0.0023 | -0.0019 |
| D9 | 1415 | 698 | 717 | 49.33 | 46.2 | -0.0014 | -0.0076 | -0.0094 |
| D10 | 1416 | 609 | 807 | 43.01 | 66.76 | -0.0014 | -0.0101 | -0.0204 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 43.286 | 43.5749 | 0.2889 |
| volume_confirmation_score | -1.3715 | -1.2244 | 0.1471 |
| liquidity_score | 2.1264 | 2.008 | -0.1184 |
| overextension_penalty | 1.2387 | 1.0742 | -0.1645 |
| reversal_risk_penalty | 0.8195 | 0.7663 | -0.0532 |
| news_risk_penalty | 0.1263 | 0.1467 | 0.0204 |
| attention_noise_penalty | 0.2408 | 0.254 | 0.0132 |
| market_regime_penalty | 0.0601 | 0.0504 | -0.0097 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **11825**
- Benchmark-adjusted coverage: **38.08%**
- Benchmark-adjusted success rate: **47.97%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261022.csv`
- Latest market index date: **2026-10-22**
- Latest price signal date: **2026-10-22**
- Latest candidate signal date: **2026-10-22**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **9**
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