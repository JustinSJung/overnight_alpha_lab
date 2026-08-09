# Evaluation Integrity Audit - 2026-08-09

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **36671**
- Unique evaluation keys: **3984**
- Duplicate rows by candidate key: **32687**
- Duplicate rate: **89.14%**
- Exact same-day duplicate rows: **7308**
- Same stock_code + signal_date repeated keys: **3408**
- Same candidate re-evaluated across multiple files: **3519**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 7122 | 3679 | 3443 | 51.66 | -0.0126 | -0.0106 | -0.034 |
| v2_conservative_ranker | 11739 | 4996 | 6743 | 42.56 | 0.0057 | -0.001 | -0.008 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 130 | 64 | 66 | 49.23 | 0.0085 | -0.0205 | -0.0383 |
| Top 20 | 260 | 142 | 118 | 54.62 | 0.0091 | -0.0109 | -0.0333 |
| Top 50 | 650 | 331 | 319 | 50.92 | 0.007 | 0.0082 | -0.0039 |
| Top 100 | 1300 | 632 | 668 | 48.62 | 0.0086 | 0.0163 | 0.0074 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1174 | 511 | 663 | 43.53 | 16.76 | 0.0025 | 0.0151 | 0.0206 |
| D2 | 1174 | 537 | 637 | 45.74 | 21.64 | 0.0005 | -0.0156 | -0.0368 |
| D3 | 1174 | 438 | 736 | 37.31 | 24.7 | 0.0084 | 0.0169 | 0.0142 |
| D4 | 1174 | 455 | 719 | 38.76 | 27.27 | 0.0147 | 0.009 | -0.0084 |
| D5 | 1174 | 521 | 653 | 44.38 | 29.55 | 0.0071 | 0.0032 | -0.0223 |
| D6 | 1173 | 439 | 734 | 37.43 | 31.71 | 0.0087 | 0.0091 | -0.0102 |
| D7 | 1174 | 447 | 727 | 38.07 | 34.06 | 0.0085 | 0.001 | -0.012 |
| D8 | 1174 | 536 | 638 | 45.66 | 36.11 | -0.0043 | -0.0356 | -0.0226 |
| D9 | 1174 | 533 | 641 | 45.4 | 38.2 | 0.0064 | -0.0065 | 0.0003 |
| D10 | 1174 | 579 | 595 | 49.32 | 59.16 | 0.0042 | -0.0074 | 0.0009 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.6115 | 39.8147 | -2.7968 |
| volume_confirmation_score | -0.5438 | -0.6638 | -0.12 |
| liquidity_score | 2.3076 | 2.0807 | -0.227 |
| overextension_penalty | 2.0048 | 1.0 | -1.0047 |
| reversal_risk_penalty | 2.1893 | 1.5592 | -0.6301 |
| news_risk_penalty | 0.1471 | 0.0835 | -0.0636 |
| attention_noise_penalty | 0.2176 | 0.2244 | 0.0068 |
| market_regime_penalty | 0.0717 | 0.0567 | -0.015 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **12381**
- Benchmark-adjusted coverage: **33.76%**
- Benchmark-adjusted success rate: **51.51%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260809.csv`
- Latest market index date: **2026-08-07**
- Latest price signal date: **2026-08-07**
- Latest candidate signal date: **2026-08-07**
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