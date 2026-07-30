# Evaluation Integrity Audit - 2026-07-30

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **15405**
- Unique evaluation keys: **2175**
- Duplicate rows by candidate key: **13230**
- Duplicate rate: **85.88%**
- Exact same-day duplicate rows: **4347**
- Same stock_code + signal_date repeated keys: **1837**
- Same candidate re-evaluated across multiple files: **1941**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 007980 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 6bdf1cf3aa42e769 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 007980 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 6bdf1cf3aa42e769 | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 007980 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 6bdf1cf3aa42e769 | data/predictions/price_candidate_evaluation_20260713.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 4532 | 2340 | 2192 | 51.63 | -0.0125 | -0.0128 | -0.0379 |
| v2_conservative_ranker | 3064 | 1457 | 1607 | 47.55 | -0.0027 | -0.0384 | -0.0782 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 70 | 34 | 36 | 48.57 | -0.002 | -0.0518 | -0.0424 |
| Top 20 | 140 | 81 | 59 | 57.86 | -0.0042 | -0.0158 | -0.0445 |
| Top 50 | 350 | 181 | 169 | 51.71 | 0.0089 | -0.0038 | -0.0407 |
| Top 100 | 700 | 373 | 327 | 53.29 | -0.003 | -0.0266 | -0.0456 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 307 | 175 | 132 | 57.0 | 17.09 | -0.0257 | -0.0727 | -0.0935 |
| D2 | 306 | 160 | 146 | 52.29 | 21.91 | -0.0103 | -0.0548 | -0.1087 |
| D3 | 306 | 117 | 189 | 38.24 | 24.63 | -0.0018 | -0.0175 | -0.0731 |
| D4 | 307 | 143 | 164 | 46.58 | 27.35 | -0.0009 | -0.043 | -0.1223 |
| D5 | 306 | 150 | 156 | 49.02 | 29.55 | 0.0005 | -0.0395 | -0.1164 |
| D6 | 306 | 145 | 161 | 47.39 | 31.77 | 0.002 | -0.038 | -0.0175 |
| D7 | 307 | 109 | 198 | 35.5 | 33.93 | 0.0073 | 0.0117 | -0.0504 |
| D8 | 306 | 144 | 162 | 47.06 | 35.83 | -0.0031 | -0.0552 | -0.0542 |
| D9 | 306 | 169 | 137 | 55.23 | 37.84 | -0.015 | -0.0658 | -0.1026 |
| D10 | 307 | 145 | 162 | 47.23 | 56.36 | 0.0195 | -0.0089 | -0.0092 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.9319 | 40.6453 | -1.2866 |
| volume_confirmation_score | -0.8957 | -0.9463 | -0.0506 |
| liquidity_score | 2.2526 | 1.9994 | -0.2532 |
| overextension_penalty | 1.853 | 0.9592 | -0.8939 |
| reversal_risk_penalty | 2.2477 | 1.6595 | -0.5882 |
| news_risk_penalty | 0.1359 | 0.0915 | -0.0444 |
| attention_noise_penalty | 0.1988 | 0.2131 | 0.0142 |
| market_regime_penalty | 0.0755 | 0.066 | -0.0095 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **1116**
- Benchmark-adjusted coverage: **7.24%**
- Benchmark-adjusted success rate: **48.57%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260730.csv`
- Latest market index date: **2026-07-30**
- Latest price signal date: **2026-07-30**
- Latest candidate signal date: **2026-07-30**
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