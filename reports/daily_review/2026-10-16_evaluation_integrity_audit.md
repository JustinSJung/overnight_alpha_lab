# Evaluation Integrity Audit - 2026-10-16

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **656058**
- Unique evaluation keys: **27381**
- Duplicate rows by candidate key: **628677**
- Duplicate rate: **95.83%**
- Exact same-day duplicate rows: **231179**
- Same stock_code + signal_date repeated keys: **26506**
- Same candidate re-evaluated across multiple files: **26507**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 088790 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 088790 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 088790 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  | 2026-07-20 |  | 65698458accec52f | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 088790 |  |  | 2026-07-20 |  | 995995047c138c16 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 391 | 192 | 199 | 49.1 | -0.0129 | -0.0011 | -0.0113 |
| v2_conservative_ranker | 11816 | 5684 | 6132 | 48.1 | -0.0009 | -0.0013 | 0.002 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1675 | 707 | 968 | 42.21 | -0.0019 | -0.0115 | -0.0212 |
| avoid | 10141 | 4977 | 5164 | 49.08 | -0.0007 | 0.0006 | 0.0066 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 451 | 202 | 249 | 44.79 | 0.0011 | -0.005 | -0.0003 |
| Top 20 | 812 | 367 | 445 | 45.2 | 0.0004 | -0.0042 | -0.0017 |
| Top 50 | 1347 | 586 | 761 | 43.5 | -0.0006 | -0.0062 | -0.0089 |
| Top 100 | 1847 | 778 | 1069 | 42.12 | 0.0009 | -0.0043 | -0.0104 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1182 | 535 | 647 | 45.26 | 21.22 | 0.0002 | 0.0114 | 0.0272 |
| D2 | 1182 | 554 | 628 | 46.87 | 27.23 | 0.0005 | 0.0019 | 0.0156 |
| D3 | 1181 | 541 | 640 | 45.81 | 29.92 | 0.0005 | 0.0013 | 0.0089 |
| D4 | 1182 | 587 | 595 | 49.66 | 32.11 | -0.0008 | 0.0007 | 0.001 |
| D5 | 1181 | 603 | 578 | 51.06 | 34.03 | -0.0019 | -0.0012 | 0.0037 |
| D6 | 1182 | 582 | 600 | 49.24 | 35.79 | -0.0033 | -0.0016 | 0.0006 |
| D7 | 1181 | 594 | 587 | 50.3 | 37.39 | 0.0007 | -0.0017 | 0.0027 |
| D8 | 1182 | 618 | 564 | 52.28 | 38.78 | -0.0015 | -0.001 | 0.0005 |
| D9 | 1181 | 568 | 613 | 48.09 | 49.33 | -0.0021 | -0.0099 | -0.0112 |
| D10 | 1182 | 502 | 680 | 42.47 | 67.44 | -0.0013 | -0.0108 | -0.0219 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 43.8791 | 44.3161 | 0.4371 |
| volume_confirmation_score | -1.2658 | -1.1214 | 0.1444 |
| liquidity_score | 2.1483 | 2.0284 | -0.1199 |
| overextension_penalty | 1.3469 | 1.1865 | -0.1603 |
| reversal_risk_penalty | 0.9086 | 0.8404 | -0.0682 |
| news_risk_penalty | 0.1351 | 0.1575 | 0.0224 |
| attention_noise_penalty | 0.2654 | 0.2731 | 0.0077 |
| market_regime_penalty | 0.0757 | 0.0636 | -0.0121 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **10082**
- Benchmark-adjusted coverage: **36.82%**
- Benchmark-adjusted success rate: **48.09%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261016.csv`
- Latest market index date: **2026-10-16**
- Latest price signal date: **2026-10-16**
- Latest candidate signal date: **2026-10-16**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **7**
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