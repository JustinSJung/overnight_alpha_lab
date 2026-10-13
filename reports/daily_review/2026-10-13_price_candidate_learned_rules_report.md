# Price Candidate Learned Rules Report - 2026-10-13

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261013.csv`
- Baseline evaluated count: **10637**
- Baseline success rate: **48.85%**
- Total rule rows: **45**
- Boost rules: **1**
- Penalize rules: **14**
- Watch rules: **3**
- Suspicious rules: **1**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| final_price_signal_score_v2 | score_40_50 | 202 | 106 | 96 | 52.48 | 48.85 | 3.63 | medium | boost | False |  | 8 |
| reversal_risk_penalty | low | 1016 | 460 | 556 | 45.28 | 48.85 | -3.57 | high | penalize | False |  | 51 |
| volume_confirmation_score | moderate | 843 | 381 | 462 | 45.2 | 48.85 | -3.65 | high | penalize | False |  | 51 |
| final_price_signal_score_v2 | score_lt_20 | 380 | 171 | 209 | 45.0 | 48.85 | -3.85 | high | penalize | False |  | 51 |
| candidate_rank | top_10 | 454 | 203 | 251 | 44.71 | 48.85 | -4.14 | high | penalize | False |  | 52 |
| selected_pick | selected | 814 | 362 | 452 | 44.47 | 48.85 | -4.38 | high | penalize | False |  | 52 |
| candidate_rank | rank_11_20 | 360 | 159 | 201 | 44.17 | 48.85 | -4.68 | high | penalize | False |  | 44 |
| final_price_signal_score_v2 | score_50_plus | 1707 | 723 | 984 | 42.36 | 48.85 | -6.49 | high | penalize | False |  | 51 |
| candidate_rank | rank_21_50 | 565 | 239 | 326 | 42.3 | 48.85 | -6.55 | high | penalize | False |  | 38 |
| volume_confirmation_score | none | 1414 | 540 | 874 | 38.19 | 48.85 | -10.66 | high | penalize | False |  | 51 |
| candidate_rank | rank_51_100 | 561 | 209 | 352 | 37.25 | 48.85 | -11.6 | high | penalize | False |  | 24 |
| liquidity_score | none | 373 | 19 | 354 | 5.09 | 48.85 | -43.76 | high | penalize | False |  | 51 |
| news_risk_penalty | medium | 142 | 62 | 80 | 43.66 | 48.85 | -5.19 | medium | penalize | False |  | 46 |
| overextension_penalty | low | 274 | 119 | 155 | 43.43 | 48.85 | -5.42 | medium | penalize | False |  | 48 |
| news_risk_penalty | high | 230 | 99 | 131 | 43.04 | 48.85 | -5.81 | medium | penalize | False |  | 39 |
| reversal_risk_penalty | high | 676 | 350 | 326 | 51.78 | 48.85 | 2.93 | high | neutral | False |  | 51 |
| candidate_rank | missing | 335 | 173 | 162 | 51.64 | 48.85 | 2.79 | high | neutral | False |  | 6 |
| volume_confirmation_score | negative | 7548 | 3873 | 3675 | 51.31 | 48.85 | 2.46 | high | neutral | False |  | 51 |
| liquidity_score | basic | 8132 | 4143 | 3989 | 50.95 | 48.85 | 2.1 | high | neutral | False |  | 51 |
| final_price_signal_score_v2 | score_30_40 | 5949 | 3020 | 2929 | 50.76 | 48.85 | 1.91 | high | neutral | False |  | 51 |
| candidate_rank | rank_101_plus | 8362 | 4213 | 4149 | 50.38 | 48.85 | 1.53 | high | neutral | False |  | 51 |
| reversal_risk_penalty | medium | 1218 | 608 | 610 | 49.92 | 48.85 | 1.07 | high | neutral | False |  | 51 |
| score_version | legacy_or_unknown | 404 | 200 | 204 | 49.5 | 48.85 | 0.65 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 404 | 200 | 204 | 49.5 | 48.85 | 0.65 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 404 | 200 | 204 | 49.5 | 48.85 | 0.65 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 404 | 200 | 204 | 49.5 | 48.85 | 0.65 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 404 | 200 | 204 | 49.5 | 48.85 | 0.65 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 404 | 200 | 204 | 49.5 | 48.85 | 0.65 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 404 | 200 | 204 | 49.5 | 48.85 | 0.65 | high | neutral | False |  | 7 |
| liquidity_score | missing | 404 | 200 | 204 | 49.5 | 48.85 | 0.65 | high | neutral | False |  | 7 |
| overextension_penalty | high | 881 | 436 | 445 | 49.49 | 48.85 | 0.64 | high | neutral | False |  | 51 |
| selected_pick | broad_pool | 9823 | 4834 | 4989 | 49.21 | 48.85 | 0.36 | high | neutral | False |  | 58 |
| attention_noise_penalty | high | 515 | 253 | 262 | 49.13 | 48.85 | 0.28 | high | neutral | False |  | 40 |
| news_risk_penalty | none | 9841 | 4824 | 5017 | 49.02 | 48.85 | 0.17 | high | neutral | False |  | 51 |
| overextension_penalty | none | 8866 | 4340 | 4526 | 48.95 | 48.85 | 0.1 | high | neutral | False |  | 51 |
| final_price_signal_score_v2 | score_20_30 | 1995 | 976 | 1019 | 48.92 | 48.85 | 0.07 | high | neutral | False |  | 51 |
| reversal_risk_penalty | none | 7323 | 3578 | 3745 | 48.86 | 48.85 | 0.01 | high | neutral | False |  | 51 |
| score_version | v2_conservative_ranker | 10233 | 4996 | 5237 | 48.82 | 48.85 | -0.03 | high | neutral | False |  | 51 |
| attention_noise_penalty | none | 9651 | 4705 | 4946 | 48.75 | 48.85 | -0.1 | high | neutral | False |  | 51 |
| liquidity_score | confirmed | 1728 | 834 | 894 | 48.26 | 48.85 | -0.59 | high | neutral | False |  | 51 |
| volume_confirmation_score | high | 428 | 202 | 226 | 47.2 | 48.85 | -1.65 | high | neutral | False |  | 50 |
| overextension_penalty | medium | 212 | 101 | 111 | 47.64 | 48.85 | -1.21 | medium | neutral | False |  | 47 |
| attention_noise_penalty | medium | 22 | 13 | 9 | 59.09 | 48.85 | 10.24 | insufficient | watch | True | large_lift_with_under_100_cases | 14 |
| attention_noise_penalty | low | 45 | 25 | 20 | 55.56 | 48.85 | 6.71 | insufficient | watch | False |  | 22 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 48.85 | 6.15 | insufficient | watch | False |  | 10 |