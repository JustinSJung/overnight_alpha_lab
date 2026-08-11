# Evaluation Integrity Audit - 2026-08-11

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **40628**
- Unique evaluation keys: **4232**
- Duplicate rows by candidate key: **36396**
- Duplicate rate: **89.58%**
- Exact same-day duplicate rows: **7731**
- Same stock_code + signal_date repeated keys: **3408**
- Same candidate re-evaluated across multiple files: **3759**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 189330 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | d13d794b4b0bb573 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 368970 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 02a02e89ea75282a | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 008930 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 445bd57d12ab54d2 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 223220 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 8cb3e3d1fc871be8 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 189330 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | d13d794b4b0bb573 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 368970 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 02a02e89ea75282a | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 008930 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 445bd57d12ab54d2 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 223220 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 8cb3e3d1fc871be8 | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 189330 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | d13d794b4b0bb573 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 368970 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 02a02e89ea75282a | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 008930 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 445bd57d12ab54d2 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 223220 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 8cb3e3d1fc871be8 | data/predictions/price_candidate_evaluation_20260713.csv | pending |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260713.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 370 | 190 | 180 | 51.35 | -0.0115 | -0.0037 | -0.0257 |
| v2_conservative_ranker | 1606 | 655 | 951 | 40.78 | 0.0111 | 0.0237 | 0.0456 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 187 | 109 | 78 | 58.29 | 0.0109 | 0.0114 | 0.0183 |
| avoid | 1419 | 546 | 873 | 38.48 | 0.0111 | 0.0248 | 0.0474 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 140 | 79 | 61 | 56.43 | 0.0094 | 0.0182 | 0.0212 |
| Top 20 | 280 | 145 | 135 | 51.79 | 0.0051 | 0.0125 | 0.0266 |
| Top 50 | 700 | 324 | 376 | 46.29 | 0.0081 | 0.0138 | 0.021 |
| Top 100 | 1267 | 552 | 715 | 43.57 | 0.0073 | 0.0173 | 0.0305 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 161 | 60 | 101 | 37.27 | 17.1 | 0.0125 | 0.0505 | 0.0859 |
| D2 | 161 | 68 | 93 | 42.24 | 22.36 | 0.0054 | 0.0109 | 0.0256 |
| D3 | 160 | 52 | 108 | 32.5 | 25.57 | 0.0227 | 0.049 | 0.08 |
| D4 | 161 | 62 | 99 | 38.51 | 28.27 | 0.0158 | 0.0241 | 0.0391 |
| D5 | 160 | 53 | 107 | 33.12 | 30.49 | 0.0104 | 0.0447 | 0.0615 |
| D6 | 161 | 68 | 93 | 42.24 | 32.88 | 0.006 | 0.0018 | 0.0119 |
| D7 | 160 | 67 | 93 | 41.88 | 35.12 | 0.0027 | 0.0123 | 0.0347 |
| D8 | 161 | 63 | 98 | 39.13 | 37.23 | 0.0172 | 0.0086 | 0.0258 |
| D9 | 160 | 66 | 94 | 41.25 | 42.62 | 0.0076 | 0.0136 | 0.0551 |
| D10 | 161 | 96 | 65 | 59.63 | 66.92 | 0.0107 | 0.0118 | 0.0099 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 46.1616 | 41.2739 | -4.8876 |
| volume_confirmation_score | -0.3573 | -0.6167 | -0.2594 |
| liquidity_score | 2.345 | 2.0894 | -0.2557 |
| overextension_penalty | 2.482 | 1.3664 | -1.1156 |
| reversal_risk_penalty | 2.2017 | 1.6126 | -0.5891 |
| news_risk_penalty | 0.2656 | 0.1062 | -0.1594 |
| attention_noise_penalty | 0.2429 | 0.2102 | -0.0327 |
| market_regime_penalty | 0.0672 | 0.0463 | -0.0209 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **1976**
- Benchmark-adjusted coverage: **46.69%**
- Benchmark-adjusted success rate: **53.09%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260810.csv`
- Latest market index date: **2026-08-10**
- Latest price signal date: **2026-08-10**
- Latest candidate signal date: **2026-08-10**
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