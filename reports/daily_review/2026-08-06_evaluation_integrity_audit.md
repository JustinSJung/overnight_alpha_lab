# Evaluation Integrity Audit - 2026-08-06

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **29493**
- Unique evaluation keys: **3504**
- Duplicate rows by candidate key: **25989**
- Duplicate rate: **88.12%**
- Exact same-day duplicate rows: **6462**
- Same stock_code + signal_date repeated keys: **2933**
- Same candidate re-evaluated across multiple files: **3042**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 068240 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | eb4fc4f1f3913c40 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 068240 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | eb4fc4f1f3913c40 | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 068240 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | eb4fc4f1f3913c40 | data/predictions/price_candidate_evaluation_20260713.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 6378 | 3297 | 3081 | 51.69 | -0.0127 | -0.0114 | -0.0352 |
| v2_conservative_ranker | 8875 | 3832 | 5043 | 43.18 | 0.0045 | -0.0108 | -0.0323 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 120 | 62 | 58 | 51.67 | 0.0094 | -0.0307 | -0.0606 |
| Top 20 | 240 | 137 | 103 | 57.08 | 0.0108 | -0.0097 | -0.0427 |
| Top 50 | 600 | 296 | 304 | 49.33 | 0.0082 | 0.0068 | -0.0087 |
| Top 100 | 1173 | 518 | 655 | 44.16 | 0.0096 | 0.0107 | -0.0088 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 888 | 403 | 485 | 45.38 | 16.74 | -0.0003 | -0.0023 | -0.0207 |
| D2 | 887 | 418 | 469 | 47.13 | 21.57 | -0.0033 | -0.0242 | -0.0623 |
| D3 | 888 | 328 | 560 | 36.94 | 24.58 | 0.0091 | 0.0034 | -0.0088 |
| D4 | 887 | 357 | 530 | 40.25 | 27.11 | 0.0117 | -0.0021 | -0.0407 |
| D5 | 888 | 370 | 518 | 41.67 | 29.41 | 0.0126 | -0.0073 | -0.055 |
| D6 | 887 | 375 | 512 | 42.28 | 31.51 | 0.0035 | -0.0027 | -0.0331 |
| D7 | 887 | 328 | 559 | 36.98 | 33.89 | 0.009 | 0.0004 | -0.0262 |
| D8 | 888 | 407 | 481 | 45.83 | 35.9 | -0.0052 | -0.0425 | -0.0427 |
| D9 | 887 | 415 | 472 | 46.79 | 38.0 | 0.0004 | -0.0237 | -0.0252 |
| D10 | 888 | 431 | 457 | 48.54 | 57.07 | 0.008 | -0.0066 | -0.0048 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.0554 | 39.5488 | -2.5066 |
| volume_confirmation_score | -0.5997 | -0.6939 | -0.0941 |
| liquidity_score | 2.298 | 2.074 | -0.2241 |
| overextension_penalty | 1.8697 | 0.9397 | -0.9299 |
| reversal_risk_penalty | 2.1825 | 1.5614 | -0.6211 |
| news_risk_penalty | 0.1378 | 0.0757 | -0.062 |
| attention_noise_penalty | 0.2099 | 0.228 | 0.0181 |
| market_regime_penalty | 0.0705 | 0.0583 | -0.0122 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **8773**
- Benchmark-adjusted coverage: **29.75%**
- Benchmark-adjusted success rate: **51.38%**
- Benchmark rows available: **86**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260806.csv`
- Latest market index date: **2026-08-06**
- Latest price signal date: **2026-08-06**
- Latest candidate signal date: **2026-08-06**
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