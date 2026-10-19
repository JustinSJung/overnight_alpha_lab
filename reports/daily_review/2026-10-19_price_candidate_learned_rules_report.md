# Price Candidate Learned Rules Report - 2026-10-19

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261019.csv`
- Baseline evaluated count: **13060**
- Baseline success rate: **48.23%**
- Total rule rows: **45**
- Boost rules: **3**
- Penalize rules: **14**
- Watch rules: **2**
- Suspicious rules: **0**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| candidate_rank | missing | 335 | 173 | 162 | 51.64 | 48.23 | 3.41 | high | boost | False |  | 6 |
| attention_noise_penalty | low | 54 | 30 | 24 | 55.56 | 48.23 | 7.33 | low | boost | False |  | 25 |
| final_price_signal_score_v2 | score_40_50 | 206 | 106 | 100 | 51.46 | 48.23 | 3.23 | medium | boost | False |  | 8 |
| final_price_signal_score_v2 | score_lt_20 | 398 | 179 | 219 | 44.97 | 48.23 | -3.26 | high | penalize | False |  | 55 |
| reversal_risk_penalty | low | 1165 | 520 | 645 | 44.64 | 48.23 | -3.59 | high | penalize | False |  | 55 |
| volume_confirmation_score | moderate | 917 | 407 | 510 | 44.38 | 48.23 | -3.85 | high | penalize | False |  | 55 |
| candidate_rank | top_10 | 486 | 215 | 271 | 44.24 | 48.23 | -3.99 | high | penalize | False |  | 56 |
| selected_pick | selected | 883 | 390 | 493 | 44.17 | 48.23 | -4.06 | high | penalize | False |  | 56 |
| candidate_rank | rank_11_20 | 397 | 175 | 222 | 44.08 | 48.23 | -4.15 | high | penalize | False |  | 48 |
| overextension_penalty | low | 315 | 137 | 178 | 43.49 | 48.23 | -4.74 | high | penalize | False |  | 52 |
| candidate_rank | rank_21_50 | 575 | 245 | 330 | 42.61 | 48.23 | -5.62 | high | penalize | False |  | 40 |
| final_price_signal_score_v2 | score_50_plus | 1785 | 759 | 1026 | 42.52 | 48.23 | -5.71 | high | penalize | False |  | 55 |
| volume_confirmation_score | none | 1601 | 612 | 989 | 38.23 | 48.23 | -10.0 | high | penalize | False |  | 55 |
| candidate_rank | rank_51_100 | 566 | 212 | 354 | 37.46 | 48.23 | -10.77 | high | penalize | False |  | 24 |
| liquidity_score | none | 419 | 22 | 397 | 5.25 | 48.23 | -42.98 | high | penalize | False |  | 55 |
| news_risk_penalty | medium | 145 | 64 | 81 | 44.14 | 48.23 | -4.09 | medium | penalize | False |  | 49 |
| news_risk_penalty | high | 244 | 107 | 137 | 43.85 | 48.23 | -4.38 | medium | penalize | False |  | 42 |
| reversal_risk_penalty | high | 735 | 370 | 365 | 50.34 | 48.23 | 2.11 | high | neutral | False |  | 55 |
| volume_confirmation_score | negative | 9683 | 4867 | 4816 | 50.26 | 48.23 | 2.03 | high | neutral | False |  | 55 |
| score_version | legacy_or_unknown | 403 | 202 | 201 | 50.12 | 48.23 | 1.89 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 403 | 202 | 201 | 50.12 | 48.23 | 1.89 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 403 | 202 | 201 | 50.12 | 48.23 | 1.89 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 403 | 202 | 201 | 50.12 | 48.23 | 1.89 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 403 | 202 | 201 | 50.12 | 48.23 | 1.89 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 403 | 202 | 201 | 50.12 | 48.23 | 1.89 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 403 | 202 | 201 | 50.12 | 48.23 | 1.89 | high | neutral | False |  | 7 |
| liquidity_score | missing | 403 | 202 | 201 | 50.12 | 48.23 | 1.89 | high | neutral | False |  | 7 |
| liquidity_score | basic | 10357 | 5176 | 5181 | 49.98 | 48.23 | 1.75 | high | neutral | False |  | 55 |
| overextension_penalty | high | 980 | 488 | 492 | 49.8 | 48.23 | 1.57 | high | neutral | False |  | 55 |
| final_price_signal_score_v2 | score_30_40 | 7431 | 3698 | 3733 | 49.76 | 48.23 | 1.53 | high | neutral | False |  | 55 |
| reversal_risk_penalty | medium | 1377 | 682 | 695 | 49.53 | 48.23 | 1.3 | high | neutral | False |  | 55 |
| candidate_rank | rank_101_plus | 10701 | 5279 | 5422 | 49.33 | 48.23 | 1.1 | high | neutral | False |  | 55 |
| selected_pick | broad_pool | 12177 | 5909 | 6268 | 48.53 | 48.23 | 0.3 | high | neutral | False |  | 62 |
| news_risk_penalty | none | 12248 | 5915 | 6333 | 48.29 | 48.23 | 0.06 | high | neutral | False |  | 55 |
| reversal_risk_penalty | none | 9380 | 4525 | 4855 | 48.24 | 48.23 | 0.01 | high | neutral | False |  | 55 |
| attention_noise_penalty | none | 12020 | 5793 | 6227 | 48.19 | 48.23 | -0.04 | high | neutral | False |  | 55 |
| overextension_penalty | none | 11130 | 5362 | 5768 | 48.18 | 48.23 | -0.05 | high | neutral | False |  | 55 |
| score_version | v2_conservative_ranker | 12657 | 6097 | 6560 | 48.17 | 48.23 | -0.06 | high | neutral | False |  | 55 |
| liquidity_score | confirmed | 1881 | 899 | 982 | 47.79 | 48.23 | -0.44 | high | neutral | False |  | 55 |
| final_price_signal_score_v2 | score_20_30 | 2837 | 1355 | 1482 | 47.76 | 48.23 | -0.47 | high | neutral | False |  | 55 |
| attention_noise_penalty | high | 564 | 264 | 300 | 46.81 | 48.23 | -1.42 | high | neutral | False |  | 41 |
| volume_confirmation_score | high | 456 | 211 | 245 | 46.27 | 48.23 | -1.96 | high | neutral | False |  | 53 |
| overextension_penalty | medium | 232 | 110 | 122 | 47.41 | 48.23 | -0.82 | medium | neutral | False |  | 52 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 48.23 | 6.77 | insufficient | watch | False |  | 10 |
| attention_noise_penalty | medium | 19 | 10 | 9 | 52.63 | 48.23 | 4.4 | insufficient | watch | False |  | 13 |