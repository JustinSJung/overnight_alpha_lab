# Price Candidate Learned Rules Report - 2026-09-04

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260904.csv`
- Baseline evaluated count: **4168**
- Baseline success rate: **43.31%**
- Total rule rows: **45**
- Boost rules: **15**
- Penalize rules: **6**
- Watch rules: **4**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 427 | 230 | 197 | 53.86 | 43.31 | 10.55 | high | boost | True | boost_on_semantically_risky_bucket | 31 |
| candidate_rank | missing | 322 | 164 | 158 | 50.93 | 43.31 | 7.62 | high | boost | False |  | 6 |
| overextension_penalty | high | 457 | 229 | 228 | 50.11 | 43.31 | 6.8 | high | boost | True | boost_on_semantically_risky_bucket | 31 |
| score_version | legacy_or_unknown | 387 | 190 | 197 | 49.1 | 43.31 | 5.79 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 387 | 190 | 197 | 49.1 | 43.31 | 5.79 | high | boost | False |  | 7 |
| overextension_penalty | missing | 387 | 190 | 197 | 49.1 | 43.31 | 5.79 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 387 | 190 | 197 | 49.1 | 43.31 | 5.79 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 387 | 190 | 197 | 49.1 | 43.31 | 5.79 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 387 | 190 | 197 | 49.1 | 43.31 | 5.79 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 387 | 190 | 197 | 49.1 | 43.31 | 5.79 | high | boost | False |  | 7 |
| liquidity_score | missing | 387 | 190 | 197 | 49.1 | 43.31 | 5.79 | high | boost | False |  | 7 |
| reversal_risk_penalty | medium | 646 | 304 | 342 | 47.06 | 43.31 | 3.75 | high | boost | False |  | 31 |
| liquidity_score | confirmed | 971 | 452 | 519 | 46.55 | 43.31 | 3.24 | high | boost | False |  | 31 |
| news_risk_penalty | medium | 90 | 42 | 48 | 46.67 | 43.31 | 3.36 | low | boost | False |  | 28 |
| candidate_rank | top_10 | 267 | 126 | 141 | 47.19 | 43.31 | 3.88 | medium | boost | False |  | 32 |
| reversal_risk_penalty | low | 600 | 241 | 359 | 40.17 | 43.31 | -3.14 | high | penalize | False |  | 31 |
| reversal_risk_penalty | none | 2108 | 840 | 1268 | 39.85 | 43.31 | -3.46 | high | penalize | False |  | 31 |
| volume_confirmation_score | none | 802 | 298 | 504 | 37.16 | 43.31 | -6.15 | high | penalize | False |  | 31 |
| candidate_rank | rank_51_100 | 349 | 122 | 227 | 34.96 | 43.31 | -8.35 | high | penalize | False |  | 16 |
| candidate_rank | rank_21_50 | 225 | 90 | 135 | 40.0 | 43.31 | -3.31 | medium | penalize | False |  | 18 |
| liquidity_score | none | 193 | 9 | 184 | 4.66 | 43.31 | -38.65 | medium | penalize | False |  | 31 |
| selected_pick | selected | 452 | 207 | 245 | 45.8 | 43.31 | 2.49 | high | neutral | False |  | 32 |
| volume_confirmation_score | negative | 2286 | 1019 | 1267 | 44.58 | 43.31 | 1.27 | high | neutral | False |  | 31 |
| liquidity_score | basic | 2617 | 1154 | 1463 | 44.1 | 43.31 | 0.79 | high | neutral | False |  | 31 |
| final_price_signal_score_v2 | score_30_40 | 1925 | 848 | 1077 | 44.05 | 43.31 | 0.74 | high | neutral | False |  | 31 |
| candidate_rank | rank_101_plus | 2820 | 1222 | 1598 | 43.33 | 43.31 | 0.02 | high | neutral | False |  | 31 |
| selected_pick | broad_pool | 3716 | 1598 | 2118 | 43.0 | 43.31 | -0.31 | high | neutral | False |  | 38 |
| score_version | v2_conservative_ranker | 3781 | 1615 | 2166 | 42.71 | 43.31 | -0.6 | high | neutral | False |  | 31 |
| attention_noise_penalty | none | 3548 | 1513 | 2035 | 42.64 | 43.31 | -0.67 | high | neutral | False |  | 31 |
| news_risk_penalty | none | 3539 | 1505 | 2034 | 42.53 | 43.31 | -0.78 | high | neutral | False |  | 31 |
| final_price_signal_score_v2 | score_50_plus | 683 | 290 | 393 | 42.46 | 43.31 | -0.85 | high | neutral | False |  | 31 |
| overextension_penalty | none | 3083 | 1283 | 1800 | 41.62 | 43.31 | -1.69 | high | neutral | False |  | 31 |
| volume_confirmation_score | moderate | 471 | 196 | 275 | 41.61 | 43.31 | -1.7 | high | neutral | False |  | 31 |
| final_price_signal_score_v2 | score_20_30 | 931 | 378 | 553 | 40.6 | 43.31 | -2.71 | high | neutral | False |  | 31 |
| volume_confirmation_score | high | 222 | 102 | 120 | 45.95 | 43.31 | 2.64 | medium | neutral | False |  | 30 |
| candidate_rank | rank_11_20 | 185 | 81 | 104 | 43.78 | 43.31 | 0.47 | medium | neutral | False |  | 24 |
| overextension_penalty | low | 135 | 59 | 76 | 43.7 | 43.31 | 0.39 | medium | neutral | False |  | 29 |
| attention_noise_penalty | high | 215 | 93 | 122 | 43.26 | 43.31 | -0.05 | medium | neutral | False |  | 23 |
| news_risk_penalty | high | 133 | 57 | 76 | 42.86 | 43.31 | -0.45 | medium | neutral | False |  | 20 |
| overextension_penalty | medium | 106 | 44 | 62 | 41.51 | 43.31 | -1.8 | medium | neutral | False |  | 27 |
| final_price_signal_score_v2 | score_lt_20 | 222 | 90 | 132 | 40.54 | 43.31 | -2.77 | medium | neutral | False |  | 31 |
| attention_noise_penalty | low | 9 | 6 | 3 | 66.67 | 43.31 | 23.36 | insufficient | watch | True | large_lift_with_under_100_cases | 7 |
| news_risk_penalty | low | 19 | 11 | 8 | 57.89 | 43.31 | 14.58 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| final_price_signal_score_v2 | score_40_50 | 20 | 9 | 11 | 45.0 | 43.31 | 1.69 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 9 | 3 | 6 | 33.33 | 43.31 | -9.98 | insufficient | watch | False |  | 6 |