# Price Candidate Learned Rules Report - 2026-10-15

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261015.csv`
- Baseline evaluated count: **11660**
- Baseline success rate: **49.95%**
- Total rule rows: **45**
- Boost rules: **1**
- Penalize rules: **16**
- Watch rules: **2**
- Suspicious rules: **0**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | low | 50 | 28 | 22 | 56.0 | 49.95 | 6.05 | low | boost | False |  | 23 |
| volume_confirmation_score | high | 448 | 209 | 239 | 46.65 | 49.95 | -3.3 | high | penalize | False |  | 52 |
| reversal_risk_penalty | low | 1080 | 490 | 590 | 45.37 | 49.95 | -4.58 | high | penalize | False |  | 53 |
| volume_confirmation_score | moderate | 889 | 399 | 490 | 44.88 | 49.95 | -5.07 | high | penalize | False |  | 53 |
| candidate_rank | rank_11_20 | 379 | 170 | 209 | 44.85 | 49.95 | -5.1 | high | penalize | False |  | 46 |
| final_price_signal_score_v2 | score_lt_20 | 363 | 162 | 201 | 44.63 | 49.95 | -5.32 | high | penalize | False |  | 51 |
| selected_pick | selected | 852 | 374 | 478 | 43.9 | 49.95 | -6.05 | high | penalize | False |  | 54 |
| candidate_rank | top_10 | 473 | 204 | 269 | 43.13 | 49.95 | -6.82 | high | penalize | False |  | 54 |
| candidate_rank | rank_21_50 | 575 | 246 | 329 | 42.78 | 49.95 | -7.17 | high | penalize | False |  | 39 |
| final_price_signal_score_v2 | score_50_plus | 1756 | 744 | 1012 | 42.37 | 49.95 | -7.58 | high | penalize | False |  | 53 |
| volume_confirmation_score | none | 1497 | 579 | 918 | 38.68 | 49.95 | -11.27 | high | penalize | False |  | 53 |
| candidate_rank | rank_51_100 | 560 | 206 | 354 | 36.79 | 49.95 | -13.16 | high | penalize | False |  | 24 |
| liquidity_score | none | 370 | 18 | 352 | 4.86 | 49.95 | -45.09 | high | penalize | False |  | 53 |
| overextension_penalty | medium | 210 | 98 | 112 | 46.67 | 49.95 | -3.28 | medium | penalize | False |  | 50 |
| news_risk_penalty | high | 235 | 102 | 133 | 43.4 | 49.95 | -6.55 | medium | penalize | False |  | 40 |
| overextension_penalty | low | 293 | 127 | 166 | 43.34 | 49.95 | -6.61 | medium | penalize | False |  | 50 |
| news_risk_penalty | medium | 145 | 61 | 84 | 42.07 | 49.95 | -7.88 | medium | penalize | False |  | 48 |
| volume_confirmation_score | negative | 8421 | 4437 | 3984 | 52.69 | 49.95 | 2.74 | high | neutral | False |  | 53 |
| liquidity_score | basic | 9066 | 4736 | 4330 | 52.24 | 49.95 | 2.29 | high | neutral | False |  | 53 |
| final_price_signal_score_v2 | score_30_40 | 6620 | 3434 | 3186 | 51.87 | 49.95 | 1.92 | high | neutral | False |  | 53 |
| candidate_rank | rank_101_plus | 9336 | 4826 | 4510 | 51.69 | 49.95 | 1.74 | high | neutral | False |  | 53 |
| reversal_risk_penalty | high | 683 | 350 | 333 | 51.24 | 49.95 | 1.29 | high | neutral | False |  | 53 |
| candidate_rank | missing | 337 | 172 | 165 | 51.04 | 49.95 | 1.09 | high | neutral | False |  | 6 |
| final_price_signal_score_v2 | score_20_30 | 2312 | 1178 | 1134 | 50.95 | 49.95 | 1.0 | high | neutral | False |  | 53 |
| reversal_risk_penalty | medium | 1275 | 645 | 630 | 50.59 | 49.95 | 0.64 | high | neutral | False |  | 53 |
| selected_pick | broad_pool | 10808 | 5450 | 5358 | 50.43 | 49.95 | 0.48 | high | neutral | False |  | 60 |
| reversal_risk_penalty | none | 8217 | 4139 | 4078 | 50.37 | 49.95 | 0.42 | high | neutral | False |  | 53 |
| overextension_penalty | none | 9844 | 4952 | 4892 | 50.3 | 49.95 | 0.35 | high | neutral | False |  | 53 |
| news_risk_penalty | none | 10855 | 5450 | 5405 | 50.21 | 49.95 | 0.26 | high | neutral | False |  | 53 |
| attention_noise_penalty | none | 10663 | 5332 | 5331 | 50.0 | 49.95 | 0.05 | high | neutral | False |  | 53 |
| score_version | v2_conservative_ranker | 11255 | 5624 | 5631 | 49.97 | 49.95 | 0.02 | high | neutral | False |  | 53 |
| score_version | legacy_or_unknown | 405 | 200 | 205 | 49.38 | 49.95 | -0.57 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 405 | 200 | 205 | 49.38 | 49.95 | -0.57 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 405 | 200 | 205 | 49.38 | 49.95 | -0.57 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 405 | 200 | 205 | 49.38 | 49.95 | -0.57 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 405 | 200 | 205 | 49.38 | 49.95 | -0.57 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 405 | 200 | 205 | 49.38 | 49.95 | -0.57 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 405 | 200 | 205 | 49.38 | 49.95 | -0.57 | high | neutral | False |  | 7 |
| liquidity_score | missing | 405 | 200 | 205 | 49.38 | 49.95 | -0.57 | high | neutral | False |  | 7 |
| overextension_penalty | high | 908 | 447 | 461 | 49.23 | 49.95 | -0.72 | high | neutral | False |  | 53 |
| attention_noise_penalty | high | 520 | 251 | 269 | 48.27 | 49.95 | -1.68 | high | neutral | False |  | 39 |
| liquidity_score | confirmed | 1819 | 870 | 949 | 47.83 | 49.95 | -2.12 | high | neutral | False |  | 53 |
| final_price_signal_score_v2 | score_40_50 | 204 | 106 | 98 | 51.96 | 49.95 | 2.01 | medium | neutral | False |  | 8 |
| attention_noise_penalty | medium | 22 | 13 | 9 | 59.09 | 49.95 | 9.14 | insufficient | watch | False |  | 14 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 49.95 | 5.05 | insufficient | watch | False |  | 10 |