# Price Candidate Learned Rules Report - 2026-10-30

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261030.csv`
- Baseline evaluated count: **16963**
- Baseline success rate: **49.18%**
- Total rule rows: **45**
- Boost rules: **2**
- Penalize rules: **13**
- Watch rules: **2**
- Suspicious rules: **1**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | low | 69 | 41 | 28 | 59.42 | 49.18 | 10.24 | low | boost | True | large_lift_with_under_100_cases | 30 |
| final_price_signal_score_v2 | score_40_50 | 198 | 105 | 93 | 53.03 | 49.18 | 3.85 | medium | boost | False |  | 8 |
| final_price_signal_score_v2 | score_lt_20 | 511 | 235 | 276 | 45.99 | 49.18 | -3.19 | high | penalize | False |  | 62 |
| candidate_rank | rank_11_20 | 412 | 188 | 224 | 45.63 | 49.18 | -3.55 | high | penalize | False |  | 53 |
| volume_confirmation_score | moderate | 949 | 427 | 522 | 44.99 | 49.18 | -4.19 | high | penalize | False |  | 62 |
| selected_pick | selected | 965 | 427 | 538 | 44.25 | 49.18 | -4.93 | high | penalize | False |  | 63 |
| overextension_penalty | low | 351 | 153 | 198 | 43.59 | 49.18 | -5.59 | high | penalize | False |  | 60 |
| candidate_rank | top_10 | 553 | 239 | 314 | 43.22 | 49.18 | -5.96 | high | penalize | False |  | 63 |
| final_price_signal_score_v2 | score_50_plus | 1858 | 787 | 1071 | 42.36 | 49.18 | -6.82 | high | penalize | False |  | 62 |
| candidate_rank | rank_21_50 | 570 | 238 | 332 | 41.75 | 49.18 | -7.43 | high | penalize | False |  | 42 |
| volume_confirmation_score | none | 1751 | 640 | 1111 | 36.55 | 49.18 | -12.63 | high | penalize | False |  | 62 |
| candidate_rank | rank_51_100 | 543 | 197 | 346 | 36.28 | 49.18 | -12.9 | high | penalize | False |  | 24 |
| liquidity_score | none | 506 | 25 | 481 | 4.94 | 49.18 | -44.24 | high | penalize | False |  | 62 |
| news_risk_penalty | high | 257 | 114 | 143 | 44.36 | 49.18 | -4.82 | medium | penalize | False |  | 48 |
| news_risk_penalty | medium | 157 | 68 | 89 | 43.31 | 49.18 | -5.87 | medium | penalize | False |  | 55 |
| reversal_risk_penalty | high | 859 | 443 | 416 | 51.57 | 49.18 | 2.39 | high | neutral | False |  | 62 |
| final_price_signal_score_v2 | score_30_40 | 9878 | 5083 | 4795 | 51.46 | 49.18 | 2.28 | high | neutral | False |  | 62 |
| overextension_penalty | high | 1093 | 561 | 532 | 51.33 | 49.18 | 2.15 | high | neutral | False |  | 62 |
| volume_confirmation_score | negative | 13391 | 6861 | 6530 | 51.24 | 49.18 | 2.06 | high | neutral | False |  | 62 |
| liquidity_score | basic | 14095 | 7184 | 6911 | 50.97 | 49.18 | 1.79 | high | neutral | False |  | 62 |
| candidate_rank | missing | 336 | 171 | 165 | 50.89 | 49.18 | 1.71 | high | neutral | False |  | 6 |
| candidate_rank | rank_101_plus | 14549 | 7310 | 7239 | 50.24 | 49.18 | 1.06 | high | neutral | False |  | 62 |
| reversal_risk_penalty | medium | 1658 | 826 | 832 | 49.82 | 49.18 | 0.64 | high | neutral | False |  | 62 |
| selected_pick | broad_pool | 15998 | 7916 | 8082 | 49.48 | 49.18 | 0.3 | high | neutral | False |  | 69 |
| news_risk_penalty | none | 16126 | 7952 | 8174 | 49.31 | 49.18 | 0.13 | high | neutral | False |  | 62 |
| reversal_risk_penalty | none | 12559 | 6190 | 6369 | 49.29 | 49.18 | 0.11 | high | neutral | False |  | 62 |
| score_version | v2_conservative_ranker | 16560 | 8145 | 8415 | 49.18 | 49.18 | 0.0 | high | neutral | False |  | 62 |
| overextension_penalty | none | 14855 | 7306 | 7549 | 49.18 | 49.18 | 0.0 | high | neutral | False |  | 62 |
| attention_noise_penalty | none | 15755 | 7745 | 8010 | 49.16 | 49.18 | -0.02 | high | neutral | False |  | 62 |
| score_version | legacy_or_unknown | 403 | 198 | 205 | 49.13 | 49.18 | -0.05 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 403 | 198 | 205 | 49.13 | 49.18 | -0.05 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 403 | 198 | 205 | 49.13 | 49.18 | -0.05 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 403 | 198 | 205 | 49.13 | 49.18 | -0.05 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 403 | 198 | 205 | 49.13 | 49.18 | -0.05 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 403 | 198 | 205 | 49.13 | 49.18 | -0.05 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 403 | 198 | 205 | 49.13 | 49.18 | -0.05 | high | neutral | False |  | 7 |
| liquidity_score | missing | 403 | 198 | 205 | 49.13 | 49.18 | -0.05 | high | neutral | False |  | 7 |
| attention_noise_penalty | high | 712 | 346 | 366 | 48.6 | 49.18 | -0.58 | high | neutral | False |  | 50 |
| liquidity_score | confirmed | 1959 | 936 | 1023 | 47.78 | 49.18 | -1.4 | high | neutral | False |  | 62 |
| final_price_signal_score_v2 | score_20_30 | 4115 | 1935 | 2180 | 47.02 | 49.18 | -2.16 | high | neutral | False |  | 62 |
| volume_confirmation_score | high | 469 | 217 | 252 | 46.27 | 49.18 | -2.91 | high | neutral | False |  | 58 |
| reversal_risk_penalty | low | 1484 | 686 | 798 | 46.23 | 49.18 | -2.95 | high | neutral | False |  | 62 |
| overextension_penalty | medium | 261 | 125 | 136 | 47.89 | 49.18 | -1.29 | medium | neutral | False |  | 58 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 49.18 | 5.82 | insufficient | watch | False |  | 10 |
| attention_noise_penalty | medium | 24 | 13 | 11 | 54.17 | 49.18 | 4.99 | insufficient | watch | False |  | 16 |