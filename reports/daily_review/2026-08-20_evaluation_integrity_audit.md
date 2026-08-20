# Evaluation Integrity Audit - 2026-08-20

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **82158**
- Unique evaluation keys: **6474**
- Duplicate rows by candidate key: **75684**
- Duplicate rate: **92.12%**
- Exact same-day duplicate rows: **11115**
- Same stock_code + signal_date repeated keys: **5312**
- Same candidate re-evaluated across multiple files: **5946**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 013520 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 013520 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 013520 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 370 | 190 | 180 | 51.35 | -0.0111 | -0.0032 | -0.0239 |
| v2_conservative_ranker | 2485 | 1002 | 1483 | 40.32 | 0.0063 | 0.0181 | 0.039 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 545 | 224 | 321 | 41.1 | -0.003 | -0.0081 | -0.0049 |
| avoid | 1940 | 778 | 1162 | 40.1 | 0.0089 | 0.0256 | 0.0489 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 177 | 88 | 89 | 49.72 | 0.0049 | -0.0029 | 0.0071 |
| Top 20 | 287 | 136 | 151 | 47.39 | 0.0014 | -0.0047 | 0.0054 |
| Top 50 | 482 | 218 | 264 | 45.23 | 0.0002 | -0.0055 | -0.0047 |
| Top 100 | 785 | 329 | 456 | 41.91 | 0.0021 | 0.0042 | 0.002 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 249 | 101 | 148 | 40.56 | 17.88 | 0.0116 | 0.0396 | 0.0676 |
| D2 | 248 | 96 | 152 | 38.71 | 23.94 | 0.0095 | 0.0283 | 0.0511 |
| D3 | 249 | 88 | 161 | 35.34 | 27.51 | 0.0212 | 0.033 | 0.0589 |
| D4 | 248 | 91 | 157 | 36.69 | 30.32 | 0.0069 | 0.0307 | 0.0429 |
| D5 | 249 | 107 | 142 | 42.97 | 32.85 | 0.0012 | 0.01 | 0.0228 |
| D6 | 248 | 110 | 138 | 44.35 | 35.21 | 0.0011 | 0.0216 | 0.0442 |
| D7 | 248 | 100 | 148 | 40.32 | 37.36 | 0.0107 | 0.0184 | 0.0436 |
| D8 | 249 | 100 | 149 | 40.16 | 43.31 | 0.0055 | 0.0112 | 0.0443 |
| D9 | 248 | 102 | 146 | 41.13 | 62.8 | -0.0065 | -0.0059 | -0.0028 |
| D10 | 249 | 107 | 142 | 42.97 | 69.8 | 0.0014 | -0.0079 | -0.0051 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 48.8332 | 46.2387 | -2.5945 |
| volume_confirmation_score | -0.3387 | -0.3836 | -0.0449 |
| liquidity_score | 2.3603 | 2.1167 | -0.2436 |
| overextension_penalty | 2.7404 | 1.4956 | -1.2448 |
| reversal_risk_penalty | 2.1975 | 1.5035 | -0.694 |
| news_risk_penalty | 0.3393 | 0.2738 | -0.0656 |
| attention_noise_penalty | 0.2126 | 0.1829 | -0.0296 |
| market_regime_penalty | 0.0659 | 0.0539 | -0.0119 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **2855**
- Benchmark-adjusted coverage: **44.1%**
- Benchmark-adjusted success rate: **51.14%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260820.csv`
- Latest market index date: **2026-08-20**
- Latest price signal date: **2026-08-20**
- Latest candidate signal date: **2026-08-20**
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