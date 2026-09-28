# Price Candidate Learned Rules Report - 2026-09-28

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260928.csv`
- Baseline evaluated count: **8076**
- Baseline success rate: **46.11%**
- Total rule rows: **45**
- Boost rules: **11**
- Penalize rules: **8**
- Watch rules: **3**
- Suspicious rules: **3**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| candidate_rank | missing | 341 | 174 | 167 | 51.03 | 46.11 | 4.92 | high | boost | False |  | 6 |
| reversal_risk_penalty | high | 627 | 319 | 308 | 50.88 | 46.11 | 4.77 | high | boost | True | boost_on_semantically_risky_bucket | 43 |
| overextension_penalty | high | 736 | 367 | 369 | 49.86 | 46.11 | 3.75 | high | boost | True | boost_on_semantically_risky_bucket | 43 |
| score_version | legacy_or_unknown | 415 | 205 | 210 | 49.4 | 46.11 | 3.29 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 415 | 205 | 210 | 49.4 | 46.11 | 3.29 | high | boost | False |  | 7 |
| overextension_penalty | missing | 415 | 205 | 210 | 49.4 | 46.11 | 3.29 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 415 | 205 | 210 | 49.4 | 46.11 | 3.29 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 415 | 205 | 210 | 49.4 | 46.11 | 3.29 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 415 | 205 | 210 | 49.4 | 46.11 | 3.29 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 415 | 205 | 210 | 49.4 | 46.11 | 3.29 | high | boost | False |  | 7 |
| liquidity_score | missing | 415 | 205 | 210 | 49.4 | 46.11 | 3.29 | high | boost | False |  | 7 |
| reversal_risk_penalty | low | 868 | 367 | 501 | 42.28 | 46.11 | -3.83 | high | penalize | False |  | 43 |
| volume_confirmation_score | moderate | 612 | 257 | 355 | 41.99 | 46.11 | -4.12 | high | penalize | False |  | 43 |
| candidate_rank | rank_51_100 | 413 | 158 | 255 | 38.26 | 46.11 | -7.85 | high | penalize | False |  | 18 |
| volume_confirmation_score | none | 1144 | 425 | 719 | 37.15 | 46.11 | -8.96 | high | penalize | False |  | 43 |
| liquidity_score | none | 324 | 18 | 306 | 5.56 | 46.11 | -40.55 | high | penalize | False |  | 43 |
| news_risk_penalty | high | 188 | 80 | 108 | 42.55 | 46.11 | -3.56 | medium | penalize | False |  | 31 |
| overextension_penalty | low | 198 | 82 | 116 | 41.41 | 46.11 | -4.7 | medium | penalize | False |  | 41 |
| final_price_signal_score_v2 | score_40_50 | 110 | 43 | 67 | 39.09 | 46.11 | -7.02 | medium | penalize | False |  | 6 |
| reversal_risk_penalty | medium | 1051 | 512 | 539 | 48.72 | 46.11 | 2.61 | high | neutral | False |  | 43 |
| volume_confirmation_score | negative | 5609 | 2694 | 2915 | 48.03 | 46.11 | 1.92 | high | neutral | False |  | 43 |
| liquidity_score | basic | 6059 | 2895 | 3164 | 47.78 | 46.11 | 1.67 | high | neutral | False |  | 43 |
| liquidity_score | confirmed | 1278 | 606 | 672 | 47.42 | 46.11 | 1.31 | high | neutral | False |  | 43 |
| final_price_signal_score_v2 | score_30_40 | 4424 | 2074 | 2350 | 46.88 | 46.11 | 0.77 | high | neutral | False |  | 43 |
| candidate_rank | top_10 | 384 | 180 | 204 | 46.88 | 46.11 | 0.77 | high | neutral | False |  | 44 |
| candidate_rank | rank_101_plus | 6266 | 2919 | 3347 | 46.58 | 46.11 | 0.47 | high | neutral | False |  | 43 |
| selected_pick | broad_pool | 7398 | 3415 | 3983 | 46.16 | 46.11 | 0.05 | high | neutral | False |  | 50 |
| news_risk_penalty | none | 7339 | 3376 | 3963 | 46.0 | 46.11 | -0.11 | high | neutral | False |  | 43 |
| attention_noise_penalty | high | 461 | 212 | 249 | 45.99 | 46.11 | -0.12 | high | neutral | False |  | 35 |
| score_version | v2_conservative_ranker | 7661 | 3519 | 4142 | 45.93 | 46.11 | -0.18 | high | neutral | False |  | 43 |
| attention_noise_penalty | none | 7147 | 3277 | 3870 | 45.85 | 46.11 | -0.26 | high | neutral | False |  | 43 |
| overextension_penalty | none | 6571 | 2998 | 3573 | 45.62 | 46.11 | -0.49 | high | neutral | False |  | 43 |
| final_price_signal_score_v2 | score_lt_20 | 353 | 161 | 192 | 45.61 | 46.11 | -0.5 | high | neutral | False |  | 43 |
| selected_pick | selected | 678 | 309 | 369 | 45.58 | 46.11 | -0.53 | high | neutral | False |  | 44 |
| reversal_risk_penalty | none | 5115 | 2321 | 2794 | 45.38 | 46.11 | -0.73 | high | neutral | False |  | 43 |
| final_price_signal_score_v2 | score_20_30 | 1672 | 752 | 920 | 44.98 | 46.11 | -1.13 | high | neutral | False |  | 43 |
| final_price_signal_score_v2 | score_50_plus | 1102 | 489 | 613 | 44.37 | 46.11 | -1.74 | high | neutral | False |  | 43 |
| candidate_rank | rank_21_50 | 378 | 164 | 214 | 43.39 | 46.11 | -2.72 | high | neutral | False |  | 30 |
| volume_confirmation_score | high | 296 | 143 | 153 | 48.31 | 46.11 | 2.2 | medium | neutral | False |  | 42 |
| overextension_penalty | medium | 156 | 72 | 84 | 46.15 | 46.11 | 0.04 | medium | neutral | False |  | 40 |
| news_risk_penalty | medium | 114 | 52 | 62 | 45.61 | 46.11 | -0.5 | medium | neutral | False |  | 38 |
| candidate_rank | rank_11_20 | 294 | 129 | 165 | 43.88 | 46.11 | -2.23 | medium | neutral | False |  | 36 |
| attention_noise_penalty | medium | 17 | 10 | 7 | 58.82 | 46.11 | 12.71 | insufficient | watch | True | large_lift_with_under_100_cases | 11 |
| attention_noise_penalty | low | 36 | 20 | 16 | 55.56 | 46.11 | 9.45 | insufficient | watch | False |  | 17 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 46.11 | 8.89 | insufficient | watch | False |  | 10 |