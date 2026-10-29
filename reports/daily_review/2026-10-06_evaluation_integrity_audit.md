# Evaluation Integrity Audit - 2026-10-06

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **464019**
- Unique evaluation keys: **21221**
- Duplicate rows by candidate key: **442798**
- Duplicate rate: **95.43%**
- Exact same-day duplicate rows: **154097**
- Same stock_code + signal_date repeated keys: **20357**
- Same candidate re-evaluated across multiple files: **20358**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 007980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 0126Z0 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 007980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 0126Z0 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 007980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 0126Z0 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 007980 |  |  | 2026-07-20 |  | 6bdf1cf3aa42e769 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 0126Z0 |  |  | 2026-07-20 |  | 2ab2d2b2d8fba094 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 415 | 205 | 210 | 49.4 | -0.014 | 0.0089 | 0.0031 |
| v2_conservative_ranker | 9090 | 4236 | 4854 | 46.6 | 0.0025 | 0.0085 | 0.0119 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1346 | 621 | 725 | 46.14 | 0.0016 | -0.0 | -0.0015 |
| avoid | 7744 | 3615 | 4129 | 46.68 | 0.0027 | 0.0099 | 0.0142 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 417 | 194 | 223 | 46.52 | 0.0021 | 0.0003 | 0.0052 |
| Top 20 | 751 | 344 | 407 | 45.81 | 0.001 | -0.0013 | 0.0008 |
| Top 50 | 1207 | 556 | 651 | 46.06 | 0.0015 | -0.0007 | -0.0025 |
| Top 100 | 1627 | 721 | 906 | 44.31 | 0.0038 | 0.0047 | 0.0032 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 909 | 411 | 498 | 45.21 | 20.08 | 0.0 | 0.0145 | 0.0287 |
| D2 | 909 | 424 | 485 | 46.64 | 26.71 | 0.0068 | 0.0153 | 0.0227 |
| D3 | 909 | 402 | 507 | 44.22 | 29.96 | 0.0046 | 0.0127 | 0.0169 |
| D4 | 909 | 438 | 471 | 48.18 | 32.24 | 0.0006 | 0.0068 | 0.0044 |
| D5 | 909 | 443 | 466 | 48.73 | 34.15 | 0.0007 | 0.0065 | 0.0089 |
| D6 | 909 | 421 | 488 | 46.31 | 35.87 | 0.0003 | 0.0095 | 0.0102 |
| D7 | 909 | 431 | 478 | 47.41 | 37.44 | 0.0034 | 0.007 | 0.0108 |
| D8 | 909 | 436 | 473 | 47.96 | 38.84 | 0.004 | 0.0094 | 0.0123 |
| D9 | 909 | 407 | 502 | 44.77 | 50.7 | 0.0026 | 0.0024 | 0.0057 |
| D10 | 909 | 423 | 486 | 46.53 | 67.37 | 0.0022 | -0.0006 | -0.0036 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.1918 | 44.7007 | -0.4911 |
| volume_confirmation_score | -1.2047 | -1.0924 | 0.1123 |
| liquidity_score | 2.1622 | 2.0212 | -0.141 |
| overextension_penalty | 1.6098 | 1.335 | -0.2748 |
| reversal_risk_penalty | 1.1418 | 0.9761 | -0.1657 |
| news_risk_penalty | 0.1688 | 0.1813 | 0.0125 |
| attention_noise_penalty | 0.31 | 0.3161 | 0.0061 |
| market_regime_penalty | 0.0982 | 0.0795 | -0.0187 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **7727**
- Benchmark-adjusted coverage: **36.41%**
- Benchmark-adjusted success rate: **52.31%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261006.csv`
- Latest market index date: **2026-10-06**
- Latest price signal date: **2026-10-06**
- Latest candidate signal date: **2026-10-06**
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