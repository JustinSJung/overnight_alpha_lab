# Evaluation Integrity Audit - 2026-10-14

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **603228**
- Unique evaluation keys: **25627**
- Duplicate rows by candidate key: **577601**
- Duplicate rate: **95.75%**
- Exact same-day duplicate rows: **210173**
- Same stock_code + signal_date repeated keys: **24758**
- Same candidate re-evaluated across multiple files: **24759**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 024720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 024720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 024720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 024720 |  |  | 2026-07-20 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 025980 |  |  | 2026-07-20 |  | 331c322c17fab620 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 394 | 196 | 198 | 49.75 | -0.0139 | 0.0073 | 0.0039 |
| v2_conservative_ranker | 10752 | 5163 | 5589 | 48.02 | 0.0002 | 0.0029 | 0.0081 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1680 | 719 | 961 | 42.8 | -0.0018 | -0.0107 | -0.0094 |
| avoid | 9072 | 4444 | 4628 | 48.99 | 0.0006 | 0.0056 | 0.0114 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 447 | 205 | 242 | 45.86 | 0.002 | -0.0023 | 0.0026 |
| Top 20 | 810 | 366 | 444 | 45.19 | 0.0005 | -0.0037 | -0.0007 |
| Top 50 | 1351 | 596 | 755 | 44.12 | -0.0004 | -0.0053 | -0.0049 |
| Top 100 | 1862 | 790 | 1072 | 42.43 | 0.001 | -0.003 | -0.0016 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1076 | 489 | 587 | 45.45 | 20.89 | 0.0007 | 0.0113 | 0.0277 |
| D2 | 1075 | 523 | 552 | 48.65 | 27.3 | 0.0025 | 0.0137 | 0.0224 |
| D3 | 1075 | 504 | 571 | 46.88 | 30.26 | 0.0012 | 0.0085 | 0.0118 |
| D4 | 1075 | 538 | 537 | 50.05 | 32.48 | -0.0007 | 0.0035 | 0.0007 |
| D5 | 1075 | 543 | 532 | 50.51 | 34.37 | -0.0008 | 0.0028 | 0.0081 |
| D6 | 1075 | 523 | 552 | 48.65 | 36.09 | -0.0003 | 0.0037 | 0.0069 |
| D7 | 1075 | 518 | 557 | 48.19 | 37.64 | 0.002 | 0.0027 | 0.0083 |
| D8 | 1075 | 565 | 510 | 52.56 | 39.02 | 0.0004 | 0.0036 | 0.0079 |
| D9 | 1075 | 505 | 570 | 46.98 | 52.59 | -0.0015 | -0.0084 | -0.0009 |
| D10 | 1076 | 455 | 621 | 42.29 | 67.91 | -0.0015 | -0.0104 | -0.013 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 44.6642 | 45.1362 | 0.472 |
| volume_confirmation_score | -1.1958 | -1.0529 | 0.1429 |
| liquidity_score | 2.1635 | 2.0331 | -0.1304 |
| overextension_penalty | 1.4831 | 1.3242 | -0.1589 |
| reversal_risk_penalty | 0.9868 | 0.8916 | -0.0951 |
| news_risk_penalty | 0.1451 | 0.1766 | 0.0315 |
| attention_noise_penalty | 0.2859 | 0.2872 | 0.0013 |
| market_regime_penalty | 0.0852 | 0.0741 | -0.0111 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **8970**
- Benchmark-adjusted coverage: **35.0%**
- Benchmark-adjusted success rate: **50.01%**
- Benchmark rows available: **76**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261014.csv`
- Latest market index date: **2026-10-14**
- Latest price signal date: **2026-10-14**
- Latest candidate signal date: **2026-10-14**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **8**
- Eligible groups: **11**
- Groups close to activation: **3**
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