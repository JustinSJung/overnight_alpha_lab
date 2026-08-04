# Evaluation Integrity Audit - 2026-08-04

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **23272**
- Unique evaluation keys: **3055**
- Duplicate rows by candidate key: **20217**
- Duplicate rate: **86.87%**
- Exact same-day duplicate rows: **5616**
- Same stock_code + signal_date repeated keys: **2497**
- Same candidate re-evaluated across multiple files: **2604**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 380540 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 755ebcef909574a1 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 380540 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 755ebcef909574a1 | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260713.csv | pending |
| 380540 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 755ebcef909574a1 | data/predictions/price_candidate_evaluation_20260713.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 5638 | 2916 | 2722 | 51.72 | -0.0127 | -0.0121 | -0.0363 |
| v2_conservative_ranker | 6243 | 2793 | 3450 | 44.74 | 0.0021 | -0.0287 | -0.0676 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 100 | 45 | 55 | 45.0 | 0.0062 | -0.0445 | -0.0723 |
| Top 20 | 200 | 108 | 92 | 54.0 | 0.0081 | -0.0112 | -0.0436 |
| Top 50 | 500 | 226 | 274 | 45.2 | 0.0088 | 0.0036 | -0.0235 |
| Top 100 | 1000 | 432 | 568 | 43.2 | 0.0116 | 0.0016 | -0.0294 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 625 | 300 | 325 | 48.0 | 16.81 | -0.0057 | -0.0397 | -0.0769 |
| D2 | 624 | 313 | 311 | 50.16 | 21.6 | -0.0063 | -0.04 | -0.0953 |
| D3 | 624 | 236 | 388 | 37.82 | 24.53 | 0.0061 | -0.0198 | -0.0396 |
| D4 | 624 | 255 | 369 | 40.87 | 27.06 | 0.0083 | -0.0288 | -0.0901 |
| D5 | 625 | 265 | 360 | 42.4 | 29.36 | 0.0126 | -0.022 | -0.1005 |
| D6 | 624 | 295 | 329 | 47.28 | 31.45 | -0.0011 | -0.0265 | -0.0731 |
| D7 | 624 | 212 | 412 | 33.97 | 33.8 | 0.0094 | -0.0116 | -0.0451 |
| D8 | 624 | 296 | 328 | 47.44 | 35.74 | -0.0031 | -0.0377 | -0.0701 |
| D9 | 624 | 319 | 305 | 51.12 | 37.85 | -0.0099 | -0.0505 | -0.0749 |
| D10 | 625 | 302 | 323 | 48.32 | 55.91 | 0.0107 | -0.0111 | -0.0114 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.7042 | 39.5891 | -2.1151 |
| volume_confirmation_score | -0.678 | -0.7405 | -0.0625 |
| liquidity_score | 2.2839 | 2.0603 | -0.2236 |
| overextension_penalty | 1.7949 | 0.9097 | -0.8852 |
| reversal_risk_penalty | 2.1888 | 1.5739 | -0.6149 |
| news_risk_penalty | 0.1339 | 0.0791 | -0.0548 |
| attention_noise_penalty | 0.1951 | 0.2313 | 0.0362 |
| market_regime_penalty | 0.0695 | 0.0632 | -0.0063 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **5401**
- Benchmark-adjusted coverage: **23.21%**
- Benchmark-adjusted success rate: **51.23%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260804.csv`
- Latest market index date: **2026-08-04**
- Latest price signal date: **2026-08-04**
- Latest candidate signal date: **2026-08-04**
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