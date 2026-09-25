# Price Candidate Learned Rules Report - 2026-09-25

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260925.csv`
- Baseline evaluated count: **7735**
- Baseline success rate: **46.36%**
- Total rule rows: **45**
- Boost rules: **12**
- Penalize rules: **7**
- Watch rules: **3**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 613 | 315 | 298 | 51.39 | 46.36 | 5.03 | high | boost | True | boost_on_semantically_risky_bucket | 42 |
| candidate_rank | missing | 341 | 174 | 167 | 51.03 | 46.36 | 4.67 | high | boost | False |  | 6 |
| overextension_penalty | high | 718 | 360 | 358 | 50.14 | 46.36 | 3.78 | high | boost | True | boost_on_semantically_risky_bucket | 42 |
| score_version | legacy_or_unknown | 415 | 205 | 210 | 49.4 | 46.36 | 3.04 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 415 | 205 | 210 | 49.4 | 46.36 | 3.04 | high | boost | False |  | 7 |
| overextension_penalty | missing | 415 | 205 | 210 | 49.4 | 46.36 | 3.04 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 415 | 205 | 210 | 49.4 | 46.36 | 3.04 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 415 | 205 | 210 | 49.4 | 46.36 | 3.04 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 415 | 205 | 210 | 49.4 | 46.36 | 3.04 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 415 | 205 | 210 | 49.4 | 46.36 | 3.04 | high | boost | False |  | 7 |
| liquidity_score | missing | 415 | 205 | 210 | 49.4 | 46.36 | 3.04 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | score_40_50 | 51 | 30 | 21 | 58.82 | 46.36 | 12.46 | low | boost | True | large_lift_with_under_100_cases | 5 |
| volume_confirmation_score | moderate | 562 | 243 | 319 | 43.24 | 46.36 | -3.12 | high | penalize | False |  | 42 |
| reversal_risk_penalty | low | 847 | 362 | 485 | 42.74 | 46.36 | -3.62 | high | penalize | False |  | 42 |
| volume_confirmation_score | none | 1078 | 398 | 680 | 36.92 | 46.36 | -9.44 | high | penalize | False |  | 42 |
| candidate_rank | rank_51_100 | 394 | 144 | 250 | 36.55 | 46.36 | -9.81 | high | penalize | False |  | 17 |
| liquidity_score | none | 316 | 18 | 298 | 5.7 | 46.36 | -40.66 | high | penalize | False |  | 42 |
| overextension_penalty | low | 194 | 81 | 113 | 41.75 | 46.36 | -4.61 | medium | penalize | False |  | 40 |
| news_risk_penalty | high | 182 | 75 | 107 | 41.21 | 46.36 | -5.15 | medium | penalize | False |  | 30 |
| reversal_risk_penalty | medium | 1014 | 491 | 523 | 48.42 | 46.36 | 2.06 | high | neutral | False |  | 42 |
| volume_confirmation_score | negative | 5407 | 2611 | 2796 | 48.29 | 46.36 | 1.93 | high | neutral | False |  | 42 |
| liquidity_score | basic | 5823 | 2797 | 3026 | 48.03 | 46.36 | 1.67 | high | neutral | False |  | 42 |
| liquidity_score | confirmed | 1181 | 566 | 615 | 47.93 | 46.36 | 1.57 | high | neutral | False |  | 42 |
| final_price_signal_score_v2 | score_30_40 | 4251 | 2009 | 2242 | 47.26 | 46.36 | 0.9 | high | neutral | False |  | 42 |
| candidate_rank | rank_101_plus | 5968 | 2809 | 3159 | 47.07 | 46.36 | 0.71 | high | neutral | False |  | 42 |
| selected_pick | broad_pool | 7070 | 3287 | 3783 | 46.49 | 46.36 | 0.13 | high | neutral | False |  | 49 |
| news_risk_penalty | none | 7007 | 3245 | 3762 | 46.31 | 46.36 | -0.05 | high | neutral | False |  | 42 |
| score_version | v2_conservative_ranker | 7320 | 3381 | 3939 | 46.19 | 46.36 | -0.17 | high | neutral | False |  | 42 |
| attention_noise_penalty | high | 446 | 206 | 240 | 46.19 | 46.36 | -0.17 | high | neutral | False |  | 34 |
| attention_noise_penalty | none | 6822 | 3145 | 3677 | 46.1 | 46.36 | -0.26 | high | neutral | False |  | 42 |
| candidate_rank | top_10 | 376 | 173 | 203 | 46.01 | 46.36 | -0.35 | high | neutral | False |  | 43 |
| overextension_penalty | none | 6260 | 2872 | 3388 | 45.88 | 46.36 | -0.48 | high | neutral | False |  | 42 |
| reversal_risk_penalty | none | 4846 | 2213 | 2633 | 45.67 | 46.36 | -0.69 | high | neutral | False |  | 42 |
| final_price_signal_score_v2 | score_lt_20 | 343 | 156 | 187 | 45.48 | 46.36 | -0.88 | high | neutral | False |  | 42 |
| selected_pick | selected | 665 | 299 | 366 | 44.96 | 46.36 | -1.4 | high | neutral | False |  | 43 |
| final_price_signal_score_v2 | score_20_30 | 1630 | 732 | 898 | 44.91 | 46.36 | -1.45 | high | neutral | False |  | 42 |
| candidate_rank | rank_21_50 | 367 | 160 | 207 | 43.6 | 46.36 | -2.76 | high | neutral | False |  | 29 |
| final_price_signal_score_v2 | score_50_plus | 1045 | 454 | 591 | 43.44 | 46.36 | -2.92 | high | neutral | False |  | 42 |
| volume_confirmation_score | high | 273 | 129 | 144 | 47.25 | 46.36 | 0.89 | medium | neutral | False |  | 41 |
| overextension_penalty | medium | 148 | 68 | 80 | 45.95 | 46.36 | -0.41 | medium | neutral | False |  | 39 |
| news_risk_penalty | medium | 111 | 50 | 61 | 45.05 | 46.36 | -1.31 | medium | neutral | False |  | 37 |
| candidate_rank | rank_11_20 | 289 | 126 | 163 | 43.6 | 46.36 | -2.76 | medium | neutral | False |  | 35 |
| attention_noise_penalty | medium | 16 | 10 | 6 | 62.5 | 46.36 | 16.14 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | low | 36 | 20 | 16 | 55.56 | 46.36 | 9.2 | insufficient | watch | False |  | 17 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 46.36 | 8.64 | insufficient | watch | False |  | 10 |