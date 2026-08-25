# Evaluation Integrity Audit - 2026-08-25

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **102614**
- Unique evaluation keys: **7412**
- Duplicate rows by candidate key: **95202**
- Duplicate rate: **92.78%**
- Exact same-day duplicate rows: **12384**
- Same stock_code + signal_date repeated keys: **6228**
- Same candidate re-evaluated across multiple files: **6867**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 229000 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 50cb3d910d8c51ef | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 066430 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 354e37246d8a38a5 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 229000 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 50cb3d910d8c51ef | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 066430 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 354e37246d8a38a5 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 229000 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 50cb3d910d8c51ef | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 066430 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 354e37246d8a38a5 | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 378 | 191 | 187 | 50.53 | -0.0119 | -0.0055 | -0.0282 |
| v2_conservative_ranker | 3005 | 1234 | 1771 | 41.06 | 0.005 | 0.0128 | 0.0259 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 599 | 246 | 353 | 41.07 | -0.0024 | -0.008 | -0.0158 |
| avoid | 2406 | 988 | 1418 | 41.06 | 0.0068 | 0.0185 | 0.0379 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 206 | 100 | 106 | 48.54 | 0.0051 | 0.0015 | 0.0023 |
| Top 20 | 340 | 158 | 182 | 46.47 | 0.0019 | -0.0052 | -0.0031 |
| Top 50 | 536 | 240 | 296 | 44.78 | 0.0005 | -0.0057 | -0.0114 |
| Top 100 | 837 | 351 | 486 | 41.94 | 0.0017 | 0.0028 | -0.0068 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 301 | 128 | 173 | 42.52 | 18.05 | 0.0068 | 0.0331 | 0.0597 |
| D2 | 300 | 117 | 183 | 39.0 | 24.18 | 0.0079 | 0.026 | 0.0543 |
| D3 | 301 | 109 | 192 | 36.21 | 27.68 | 0.0197 | 0.0304 | 0.0526 |
| D4 | 300 | 121 | 179 | 40.33 | 30.4 | 0.0037 | 0.0289 | 0.0364 |
| D5 | 301 | 132 | 169 | 43.85 | 32.83 | 0.002 | -0.0023 | -0.0013 |
| D6 | 300 | 131 | 169 | 43.67 | 34.98 | 0.0016 | 0.013 | 0.0312 |
| D7 | 300 | 122 | 178 | 40.67 | 37.04 | 0.0076 | 0.0038 | 0.0237 |
| D8 | 301 | 126 | 175 | 41.86 | 39.04 | 0.0056 | 0.0139 | 0.0393 |
| D9 | 300 | 119 | 181 | 39.67 | 61.97 | -0.0066 | -0.0135 | -0.0174 |
| D10 | 301 | 129 | 172 | 42.86 | 69.36 | 0.0017 | -0.0028 | -0.0146 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.9145 | 45.7517 | -2.1628 |
| volume_confirmation_score | -0.4477 | -0.4644 | -0.0166 |
| liquidity_score | 2.3379 | 2.1073 | -0.2306 |
| overextension_penalty | 2.4998 | 1.3944 | -1.1055 |
| reversal_risk_penalty | 2.1229 | 1.4398 | -0.6831 |
| news_risk_penalty | 0.3193 | 0.2767 | -0.0426 |
| attention_noise_penalty | 0.2209 | 0.1779 | -0.043 |
| market_regime_penalty | 0.0697 | 0.0542 | -0.0155 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3383**
- Benchmark-adjusted coverage: **45.64%**
- Benchmark-adjusted success rate: **50.46%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260825.csv`
- Latest market index date: **2026-08-25**
- Latest price signal date: **2026-08-25**
- Latest candidate signal date: **2026-08-25**
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