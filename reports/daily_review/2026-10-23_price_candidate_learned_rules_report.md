# Price Candidate Learned Rules Report - 2026-10-23

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261023.csv`
- Baseline evaluated count: **15009**
- Baseline success rate: **49.61%**
- Total rule rows: **45**
- Boost rules: **2**
- Penalize rules: **14**
- Watch rules: **2**
- Suspicious rules: **0**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | low | 61 | 36 | 25 | 59.02 | 49.61 | 9.41 | low | boost | False |  | 28 |
| final_price_signal_score_v2 | score_40_50 | 203 | 107 | 96 | 52.71 | 49.61 | 3.1 | medium | boost | False |  | 8 |
| reversal_risk_penalty | low | 1317 | 596 | 721 | 45.25 | 49.61 | -4.36 | high | penalize | False |  | 59 |
| candidate_rank | rank_11_20 | 423 | 190 | 233 | 44.92 | 49.61 | -4.69 | high | penalize | False |  | 52 |
| volume_confirmation_score | moderate | 923 | 413 | 510 | 44.75 | 49.61 | -4.86 | high | penalize | False |  | 58 |
| final_price_signal_score_v2 | score_lt_20 | 443 | 197 | 246 | 44.47 | 49.61 | -5.14 | high | penalize | False |  | 59 |
| selected_pick | selected | 951 | 418 | 533 | 43.95 | 49.61 | -5.66 | high | penalize | False |  | 60 |
| overextension_penalty | low | 328 | 143 | 185 | 43.6 | 49.61 | -6.01 | high | penalize | False |  | 57 |
| candidate_rank | top_10 | 528 | 228 | 300 | 43.18 | 49.61 | -6.43 | high | penalize | False |  | 60 |
| candidate_rank | rank_21_50 | 583 | 249 | 334 | 42.71 | 49.61 | -6.9 | high | penalize | False |  | 42 |
| final_price_signal_score_v2 | score_50_plus | 1861 | 791 | 1070 | 42.5 | 49.61 | -7.11 | high | penalize | False |  | 59 |
| candidate_rank | rank_51_100 | 557 | 208 | 349 | 37.34 | 49.61 | -12.27 | high | penalize | False |  | 24 |
| volume_confirmation_score | none | 1711 | 627 | 1084 | 36.65 | 49.61 | -12.96 | high | penalize | False |  | 59 |
| liquidity_score | none | 499 | 22 | 477 | 4.41 | 49.61 | -45.2 | high | penalize | False |  | 59 |
| news_risk_penalty | high | 257 | 111 | 146 | 43.19 | 49.61 | -6.42 | medium | penalize | False |  | 47 |
| news_risk_penalty | medium | 152 | 65 | 87 | 42.76 | 49.61 | -6.85 | medium | penalize | False |  | 52 |
| final_price_signal_score_v2 | score_30_40 | 8720 | 4544 | 4176 | 52.11 | 49.61 | 2.5 | high | neutral | False |  | 59 |
| volume_confirmation_score | negative | 11499 | 5985 | 5514 | 52.05 | 49.61 | 2.44 | high | neutral | False |  | 59 |
| liquidity_score | basic | 12191 | 6309 | 5882 | 51.75 | 49.61 | 2.14 | high | neutral | False |  | 59 |
| candidate_rank | missing | 336 | 171 | 165 | 50.89 | 49.61 | 1.28 | high | neutral | False |  | 6 |
| candidate_rank | rank_101_plus | 12582 | 6400 | 6182 | 50.87 | 49.61 | 1.26 | high | neutral | False |  | 59 |
| reversal_risk_penalty | medium | 1560 | 783 | 777 | 50.19 | 49.61 | 0.58 | high | neutral | False |  | 59 |
| overextension_penalty | high | 1045 | 524 | 521 | 50.14 | 49.61 | 0.53 | high | neutral | False |  | 59 |
| reversal_risk_penalty | none | 10942 | 5474 | 5468 | 50.03 | 49.61 | 0.42 | high | neutral | False |  | 59 |
| reversal_risk_penalty | high | 786 | 393 | 393 | 50.0 | 49.61 | 0.39 | high | neutral | False |  | 59 |
| selected_pick | broad_pool | 14058 | 7028 | 7030 | 49.99 | 49.61 | 0.38 | high | neutral | False |  | 66 |
| news_risk_penalty | none | 14176 | 7059 | 7117 | 49.8 | 49.61 | 0.19 | high | neutral | False |  | 59 |
| overextension_penalty | none | 12992 | 6458 | 6534 | 49.71 | 49.61 | 0.1 | high | neutral | False |  | 59 |
| attention_noise_penalty | none | 13887 | 6893 | 6994 | 49.64 | 49.61 | 0.03 | high | neutral | False |  | 59 |
| score_version | v2_conservative_ranker | 14605 | 7246 | 7359 | 49.61 | 49.61 | 0.0 | high | neutral | False |  | 59 |
| score_version | legacy_or_unknown | 404 | 200 | 204 | 49.5 | 49.61 | -0.11 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 404 | 200 | 204 | 49.5 | 49.61 | -0.11 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 404 | 200 | 204 | 49.5 | 49.61 | -0.11 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 404 | 200 | 204 | 49.5 | 49.61 | -0.11 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 404 | 200 | 204 | 49.5 | 49.61 | -0.11 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 404 | 200 | 204 | 49.5 | 49.61 | -0.11 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 404 | 200 | 204 | 49.5 | 49.61 | -0.11 | high | neutral | False |  | 7 |
| liquidity_score | missing | 404 | 200 | 204 | 49.5 | 49.61 | -0.11 | high | neutral | False |  | 7 |
| attention_noise_penalty | high | 638 | 308 | 330 | 48.28 | 49.61 | -1.33 | high | neutral | False |  | 47 |
| liquidity_score | confirmed | 1915 | 915 | 1000 | 47.78 | 49.61 | -1.83 | high | neutral | False |  | 59 |
| final_price_signal_score_v2 | score_20_30 | 3378 | 1607 | 1771 | 47.57 | 49.61 | -2.04 | high | neutral | False |  | 59 |
| volume_confirmation_score | high | 472 | 221 | 251 | 46.82 | 49.61 | -2.79 | high | neutral | False |  | 56 |
| overextension_penalty | medium | 240 | 121 | 119 | 50.42 | 49.61 | 0.81 | medium | neutral | False |  | 53 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 49.61 | 5.39 | insufficient | watch | False |  | 10 |
| attention_noise_penalty | medium | 19 | 9 | 10 | 47.37 | 49.61 | -2.24 | insufficient | watch | False |  | 14 |