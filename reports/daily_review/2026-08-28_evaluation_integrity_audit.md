# Evaluation Integrity Audit - 2026-08-28

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **117860**
- Unique evaluation keys: **8061**
- Duplicate rows by candidate key: **109799**
- Duplicate rate: **93.16%**
- Exact same-day duplicate rows: **13230**
- Same stock_code + signal_date repeated keys: **6867**
- Same candidate re-evaluated across multiple files: **7510**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 385 | 195 | 190 | 50.65 | -0.0117 | -0.005 | -0.0268 |
| v2_conservative_ranker | 3294 | 1361 | 1933 | 41.32 | 0.0055 | 0.0175 | 0.0253 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 643 | 267 | 376 | 41.52 | -0.002 | -0.0055 | -0.0124 |
| avoid | 2651 | 1094 | 1557 | 41.27 | 0.0073 | 0.0231 | 0.0352 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 227 | 110 | 117 | 48.46 | 0.0043 | 0.0044 | 0.0093 |
| Top 20 | 381 | 179 | 202 | 46.98 | 0.0023 | -0.0012 | 0.0009 |
| Top 50 | 580 | 261 | 319 | 45.0 | 0.0008 | -0.0032 | -0.008 |
| Top 100 | 883 | 372 | 511 | 42.13 | 0.0023 | 0.0044 | -0.0045 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 330 | 140 | 190 | 42.42 | 18.2 | 0.0079 | 0.0295 | 0.0517 |
| D2 | 329 | 127 | 202 | 38.6 | 24.35 | 0.0122 | 0.0409 | 0.061 |
| D3 | 329 | 126 | 203 | 38.3 | 27.81 | 0.017 | 0.0251 | 0.0404 |
| D4 | 330 | 133 | 197 | 40.3 | 30.54 | 0.0031 | 0.0285 | 0.0393 |
| D5 | 329 | 143 | 186 | 43.47 | 32.94 | 0.0027 | 0.0046 | -0.0029 |
| D6 | 329 | 141 | 188 | 42.86 | 35.02 | 0.0027 | 0.0305 | 0.0362 |
| D7 | 330 | 138 | 192 | 41.82 | 36.99 | 0.007 | 0.0088 | 0.0174 |
| D8 | 329 | 140 | 189 | 42.55 | 38.95 | 0.0065 | 0.0186 | 0.0383 |
| D9 | 329 | 131 | 198 | 39.82 | 60.98 | -0.0055 | -0.011 | -0.0158 |
| D10 | 330 | 142 | 188 | 43.03 | 69.29 | 0.0012 | -0.0008 | -0.0089 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.9761 | 45.8524 | -2.1237 |
| volume_confirmation_score | -0.515 | -0.4945 | 0.0205 |
| liquidity_score | 2.3255 | 2.0988 | -0.2267 |
| overextension_penalty | 2.5088 | 1.5068 | -1.002 |
| reversal_risk_penalty | 2.0864 | 1.4584 | -0.628 |
| news_risk_penalty | 0.3079 | 0.2649 | -0.043 |
| attention_noise_penalty | 0.2126 | 0.2012 | -0.0114 |
| market_regime_penalty | 0.0647 | 0.0517 | -0.0129 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3679**
- Benchmark-adjusted coverage: **45.64%**
- Benchmark-adjusted success rate: **49.82%**
- Benchmark rows available: **86**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260828.csv`
- Latest market index date: **2026-08-28**
- Latest price signal date: **2026-08-28**
- Latest candidate signal date: **2026-08-28**
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