# Price Candidate Learned Rules Report - 2026-11-18

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261118.csv`
- Baseline evaluated count: **24740**
- Baseline success rate: **50.21%**
- Total rule rows: **45**
- Boost rules: **1**
- Penalize rules: **14**
- Watch rules: **2**
- Suspicious rules: **1**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | low | 103 | 57 | 46 | 55.34 | 50.21 | 5.13 | medium | boost | False |  | 41 |
| volume_confirmation_score | moderate | 2203 | 1024 | 1179 | 46.48 | 50.21 | -3.73 | high | penalize | False |  | 75 |
| overextension_penalty | low | 500 | 232 | 268 | 46.4 | 50.21 | -3.81 | high | penalize | False |  | 72 |
| candidate_rank | rank_11_20 | 532 | 238 | 294 | 44.74 | 50.21 | -5.47 | high | penalize | False |  | 65 |
| final_price_signal_score_v2 | score_40_50 | 308 | 137 | 171 | 44.48 | 50.21 | -5.73 | high | penalize | False |  | 9 |
| news_risk_penalty | high | 359 | 157 | 202 | 43.73 | 50.21 | -6.48 | high | penalize | False |  | 62 |
| selected_pick | selected | 1208 | 525 | 683 | 43.46 | 50.21 | -6.75 | high | penalize | False |  | 75 |
| volume_confirmation_score | none | 3618 | 1565 | 2053 | 43.26 | 50.21 | -6.95 | high | penalize | False |  | 75 |
| volume_confirmation_score | high | 962 | 415 | 547 | 43.14 | 50.21 | -7.07 | high | penalize | False |  | 72 |
| candidate_rank | rank_21_50 | 876 | 375 | 501 | 42.81 | 50.21 | -7.4 | high | penalize | False |  | 54 |
| candidate_rank | top_10 | 676 | 287 | 389 | 42.46 | 50.21 | -7.75 | high | penalize | False |  | 75 |
| final_price_signal_score_v2 | score_50_plus | 2599 | 1091 | 1508 | 41.98 | 50.21 | -8.23 | high | penalize | False |  | 75 |
| candidate_rank | rank_51_100 | 740 | 271 | 469 | 36.62 | 50.21 | -13.59 | high | penalize | False |  | 34 |
| liquidity_score | none | 656 | 42 | 614 | 6.4 | 50.21 | -43.81 | high | penalize | False |  | 74 |
| news_risk_penalty | medium | 202 | 89 | 113 | 44.06 | 50.21 | -6.15 | medium | penalize | False |  | 66 |
| reversal_risk_penalty | high | 1111 | 586 | 525 | 52.75 | 50.21 | 2.54 | high | neutral | False |  | 75 |
| volume_confirmation_score | negative | 17629 | 9257 | 8372 | 52.51 | 50.21 | 2.3 | high | neutral | False |  | 75 |
| overextension_penalty | high | 1370 | 718 | 652 | 52.41 | 50.21 | 2.2 | high | neutral | False |  | 74 |
| liquidity_score | basic | 19421 | 10153 | 9268 | 52.28 | 50.21 | 2.07 | high | neutral | False |  | 75 |
| final_price_signal_score_v2 | score_30_40 | 14042 | 7327 | 6715 | 52.18 | 50.21 | 1.97 | high | neutral | False |  | 75 |
| candidate_rank | rank_101_plus | 21657 | 11119 | 10538 | 51.34 | 50.21 | 1.13 | high | neutral | False |  | 75 |
| selected_pick | broad_pool | 23532 | 11896 | 11636 | 50.55 | 50.21 | 0.34 | high | neutral | False |  | 81 |
| reversal_risk_penalty | medium | 2298 | 1160 | 1138 | 50.48 | 50.21 | 0.27 | high | neutral | False |  | 75 |
| news_risk_penalty | none | 23831 | 12004 | 11827 | 50.37 | 50.21 | 0.16 | high | neutral | False |  | 75 |
| attention_noise_penalty | none | 23299 | 11720 | 11579 | 50.3 | 50.21 | 0.09 | high | neutral | False |  | 75 |
| reversal_risk_penalty | none | 18688 | 9395 | 9293 | 50.27 | 50.21 | 0.06 | high | neutral | False |  | 75 |
| score_version | v2_conservative_ranker | 24412 | 12261 | 12151 | 50.23 | 50.21 | 0.02 | high | neutral | False |  | 75 |
| overextension_penalty | none | 22192 | 11136 | 11056 | 50.18 | 50.21 | -0.03 | high | neutral | False |  | 75 |
| overextension_penalty | medium | 350 | 175 | 175 | 50.0 | 50.21 | -0.21 | high | neutral | False |  | 69 |
| final_price_signal_score_v2 | score_20_30 | 6699 | 3337 | 3362 | 49.81 | 50.21 | -0.4 | high | neutral | False |  | 75 |
| score_version | legacy_or_unknown | 328 | 160 | 168 | 48.78 | 50.21 | -1.43 | high | neutral | False |  | 6 |
| final_price_signal_score_v2 | missing | 328 | 160 | 168 | 48.78 | 50.21 | -1.43 | high | neutral | False |  | 6 |
| overextension_penalty | missing | 328 | 160 | 168 | 48.78 | 50.21 | -1.43 | high | neutral | False |  | 6 |
| reversal_risk_penalty | missing | 328 | 160 | 168 | 48.78 | 50.21 | -1.43 | high | neutral | False |  | 6 |
| news_risk_penalty | missing | 328 | 160 | 168 | 48.78 | 50.21 | -1.43 | high | neutral | False |  | 6 |
| attention_noise_penalty | missing | 328 | 160 | 168 | 48.78 | 50.21 | -1.43 | high | neutral | False |  | 6 |
| volume_confirmation_score | missing | 328 | 160 | 168 | 48.78 | 50.21 | -1.43 | high | neutral | False |  | 6 |
| liquidity_score | missing | 328 | 160 | 168 | 48.78 | 50.21 | -1.43 | high | neutral | False |  | 6 |
| reversal_risk_penalty | low | 2315 | 1120 | 1195 | 48.38 | 50.21 | -1.83 | high | neutral | False |  | 75 |
| final_price_signal_score_v2 | score_lt_20 | 764 | 369 | 395 | 48.3 | 50.21 | -1.91 | high | neutral | False |  | 75 |
| liquidity_score | confirmed | 4335 | 2066 | 2269 | 47.66 | 50.21 | -2.55 | high | neutral | False |  | 75 |
| attention_noise_penalty | high | 976 | 462 | 514 | 47.34 | 50.21 | -2.87 | high | neutral | False |  | 63 |
| candidate_rank | missing | 259 | 131 | 128 | 50.58 | 50.21 | 0.37 | medium | neutral | False |  | 5 |
| attention_noise_penalty | medium | 34 | 22 | 12 | 64.71 | 50.21 | 14.5 | insufficient | watch | True | large_lift_with_under_100_cases | 21 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 50.21 | 4.79 | insufficient | watch | False |  | 10 |