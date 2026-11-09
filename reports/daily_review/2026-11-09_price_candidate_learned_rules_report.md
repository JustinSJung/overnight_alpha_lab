# Price Candidate Learned Rules Report - 2026-11-09

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261109.csv`
- Baseline evaluated count: **20194**
- Baseline success rate: **50.92%**
- Total rule rows: **45**
- Boost rules: **1**
- Penalize rules: **13**
- Watch rules: **2**
- Suspicious rules: **0**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | low | 79 | 43 | 36 | 54.43 | 50.92 | 3.51 | low | boost | False |  | 34 |
| overextension_penalty | low | 388 | 183 | 205 | 47.16 | 50.92 | -3.76 | high | penalize | False |  | 65 |
| volume_confirmation_score | high | 648 | 303 | 345 | 46.76 | 50.92 | -4.16 | high | penalize | False |  | 65 |
| final_price_signal_score_v2 | score_40_50 | 315 | 146 | 169 | 46.35 | 50.92 | -4.57 | high | penalize | False |  | 9 |
| candidate_rank | rank_11_20 | 468 | 212 | 256 | 45.3 | 50.92 | -5.62 | high | penalize | False |  | 59 |
| selected_pick | selected | 1074 | 481 | 593 | 44.79 | 50.92 | -6.13 | high | penalize | False |  | 69 |
| candidate_rank | top_10 | 606 | 269 | 337 | 44.39 | 50.92 | -6.53 | high | penalize | False |  | 68 |
| final_price_signal_score_v2 | score_50_plus | 2065 | 888 | 1177 | 43.0 | 50.92 | -7.92 | high | penalize | False |  | 68 |
| volume_confirmation_score | none | 2508 | 1070 | 1438 | 42.66 | 50.92 | -8.26 | high | penalize | False |  | 68 |
| candidate_rank | rank_21_50 | 653 | 276 | 377 | 42.27 | 50.92 | -8.65 | high | penalize | False |  | 48 |
| candidate_rank | rank_51_100 | 549 | 208 | 341 | 37.89 | 50.92 | -13.03 | high | penalize | False |  | 27 |
| liquidity_score | none | 588 | 34 | 554 | 5.78 | 50.92 | -45.14 | high | penalize | False |  | 68 |
| news_risk_penalty | high | 298 | 132 | 166 | 44.3 | 50.92 | -6.62 | medium | penalize | False |  | 54 |
| news_risk_penalty | medium | 177 | 78 | 99 | 44.07 | 50.92 | -6.85 | medium | penalize | False |  | 60 |
| liquidity_score | basic | 16438 | 8652 | 7786 | 52.63 | 50.92 | 1.71 | high | neutral | False |  | 68 |
| volume_confirmation_score | negative | 15295 | 8050 | 7245 | 52.63 | 50.92 | 1.71 | high | neutral | False |  | 68 |
| final_price_signal_score_v2 | score_30_40 | 11648 | 6093 | 5555 | 52.31 | 50.92 | 1.39 | high | neutral | False |  | 68 |
| candidate_rank | rank_101_plus | 17587 | 9148 | 8439 | 52.02 | 50.92 | 1.1 | high | neutral | False |  | 68 |
| final_price_signal_score_v2 | score_20_30 | 5201 | 2686 | 2515 | 51.64 | 50.92 | 0.72 | high | neutral | False |  | 68 |
| candidate_rank | missing | 331 | 170 | 161 | 51.36 | 50.92 | 0.44 | high | neutral | False |  | 6 |
| reversal_risk_penalty | high | 900 | 462 | 438 | 51.33 | 50.92 | 0.41 | high | neutral | False |  | 67 |
| selected_pick | broad_pool | 19120 | 9802 | 9318 | 51.27 | 50.92 | 0.35 | high | neutral | False |  | 75 |
| reversal_risk_penalty | none | 15180 | 7766 | 7414 | 51.16 | 50.92 | 0.24 | high | neutral | False |  | 68 |
| reversal_risk_penalty | medium | 1883 | 963 | 920 | 51.14 | 50.92 | 0.22 | high | neutral | False |  | 68 |
| news_risk_penalty | none | 19305 | 9866 | 9439 | 51.11 | 50.92 | 0.19 | high | neutral | False |  | 68 |
| overextension_penalty | none | 17966 | 9172 | 8794 | 51.05 | 50.92 | 0.13 | high | neutral | False |  | 68 |
| overextension_penalty | high | 1164 | 594 | 570 | 51.03 | 50.92 | 0.11 | high | neutral | False |  | 67 |
| attention_noise_penalty | none | 18868 | 9623 | 9245 | 51.0 | 50.92 | 0.08 | high | neutral | False |  | 68 |
| score_version | v2_conservative_ranker | 19799 | 10087 | 9712 | 50.95 | 50.92 | 0.03 | high | neutral | False |  | 68 |
| liquidity_score | confirmed | 2773 | 1401 | 1372 | 50.52 | 50.92 | -0.4 | high | neutral | False |  | 68 |
| score_version | legacy_or_unknown | 395 | 196 | 199 | 49.62 | 50.92 | -1.3 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 395 | 196 | 199 | 49.62 | 50.92 | -1.3 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 395 | 196 | 199 | 49.62 | 50.92 | -1.3 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 395 | 196 | 199 | 49.62 | 50.92 | -1.3 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 395 | 196 | 199 | 49.62 | 50.92 | -1.3 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 395 | 196 | 199 | 49.62 | 50.92 | -1.3 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 395 | 196 | 199 | 49.62 | 50.92 | -1.3 | high | neutral | False |  | 7 |
| liquidity_score | missing | 395 | 196 | 199 | 49.62 | 50.92 | -1.3 | high | neutral | False |  | 7 |
| volume_confirmation_score | moderate | 1348 | 664 | 684 | 49.26 | 50.92 | -1.66 | high | neutral | False |  | 68 |
| attention_noise_penalty | high | 824 | 405 | 419 | 49.15 | 50.92 | -1.77 | high | neutral | False |  | 56 |
| reversal_risk_penalty | low | 1836 | 896 | 940 | 48.8 | 50.92 | -2.12 | high | neutral | False |  | 68 |
| final_price_signal_score_v2 | score_lt_20 | 570 | 274 | 296 | 48.07 | 50.92 | -2.85 | high | neutral | False |  | 68 |
| overextension_penalty | medium | 281 | 138 | 143 | 49.11 | 50.92 | -1.81 | medium | neutral | False |  | 62 |
| news_risk_penalty | low | 19 | 11 | 8 | 57.89 | 50.92 | 6.97 | insufficient | watch | False |  | 10 |
| attention_noise_penalty | medium | 28 | 16 | 12 | 57.14 | 50.92 | 6.22 | insufficient | watch | False |  | 18 |