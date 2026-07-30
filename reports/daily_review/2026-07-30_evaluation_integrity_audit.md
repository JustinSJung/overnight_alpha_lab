# Evaluation Integrity Audit - 2026-07-30

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **15399**
- Unique evaluation keys: **2169**
- Duplicate rows by candidate key: **13230**
- Duplicate rate: **85.91%**
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
| v2_conservative_ranker | 3064 | 1456 | 1608 | 47.52 | -0.0026 | -0.0383 | -0.0777 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 70 | 33 | 37 | 47.14 | -0.0015 | -0.0504 | -0.0419 |
| Top 20 | 140 | 80 | 60 | 57.14 | -0.0038 | -0.0151 | -0.0443 |
| Top 50 | 350 | 178 | 172 | 50.86 | 0.0095 | -0.0031 | -0.0401 |
| Top 100 | 700 | 369 | 331 | 52.71 | -0.0026 | -0.0257 | -0.0454 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 307 | 176 | 131 | 57.33 | 17.09 | -0.0253 | -0.0727 | -0.0937 |
| D2 | 306 | 160 | 146 | 52.29 | 21.91 | -0.0102 | -0.0546 | -0.1078 |
| D3 | 306 | 119 | 187 | 38.89 | 24.63 | -0.0016 | -0.0171 | -0.0735 |
| D4 | 307 | 143 | 164 | 46.58 | 27.35 | -0.0009 | -0.043 | -0.1226 |
| D5 | 306 | 150 | 156 | 49.02 | 29.55 | 0.0007 | -0.0395 | -0.116 |
| D6 | 306 | 146 | 160 | 47.71 | 31.77 | 0.0018 | -0.0384 | -0.0169 |
| D7 | 307 | 107 | 200 | 34.85 | 33.93 | 0.0078 | 0.0115 | -0.048 |
| D8 | 306 | 143 | 163 | 46.73 | 35.83 | -0.0029 | -0.0545 | -0.054 |
| D9 | 306 | 168 | 138 | 54.9 | 37.84 | -0.0149 | -0.0658 | -0.1015 |
| D10 | 307 | 144 | 163 | 46.91 | 56.36 | 0.0197 | -0.0081 | -0.0093 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.9136 | 40.6627 | -1.2509 |
| volume_confirmation_score | -0.9041 | -0.9387 | -0.0346 |
| liquidity_score | 2.2527 | 1.9994 | -0.2534 |
| overextension_penalty | 1.8543 | 0.9586 | -0.8958 |
| reversal_risk_penalty | 2.2574 | 1.6511 | -0.6063 |
| news_risk_penalty | 0.136 | 0.0914 | -0.0446 |
| attention_noise_penalty | 0.2049 | 0.2075 | 0.0026 |
| market_regime_penalty | 0.0755 | 0.0659 | -0.0096 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **1116**
- Benchmark-adjusted coverage: **7.25%**
- Benchmark-adjusted success rate: **48.39%**
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