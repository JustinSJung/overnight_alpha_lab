# Price Candidate Learned Rules Report - 2026-09-21

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260921.csv`
- Baseline evaluated count: **6917**
- Baseline success rate: **46.0%**
- Total rule rows: **45**
- Boost rules: **11**
- Penalize rules: **8**
- Watch rules: **4**
- Suspicious rules: **5**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| candidate_rank | missing | 328 | 168 | 160 | 51.22 | 46.0 | 5.22 | high | boost | False |  | 6 |
| reversal_risk_penalty | high | 549 | 279 | 270 | 50.82 | 46.0 | 4.82 | high | boost | True | boost_on_semantically_risky_bucket | 40 |
| score_version | legacy_or_unknown | 394 | 195 | 199 | 49.49 | 46.0 | 3.49 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 394 | 195 | 199 | 49.49 | 46.0 | 3.49 | high | boost | False |  | 7 |
| overextension_penalty | missing | 394 | 195 | 199 | 49.49 | 46.0 | 3.49 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 394 | 195 | 199 | 49.49 | 46.0 | 3.49 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 394 | 195 | 199 | 49.49 | 46.0 | 3.49 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 394 | 195 | 199 | 49.49 | 46.0 | 3.49 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 394 | 195 | 199 | 49.49 | 46.0 | 3.49 | high | boost | False |  | 7 |
| liquidity_score | missing | 394 | 195 | 199 | 49.49 | 46.0 | 3.49 | high | boost | False |  | 7 |
| overextension_penalty | high | 644 | 318 | 326 | 49.38 | 46.0 | 3.38 | high | boost | True | boost_on_semantically_risky_bucket | 40 |
| volume_confirmation_score | moderate | 518 | 219 | 299 | 42.28 | 46.0 | -3.72 | high | penalize | False |  | 40 |
| reversal_risk_penalty | low | 755 | 312 | 443 | 41.32 | 46.0 | -4.68 | high | penalize | False |  | 40 |
| volume_confirmation_score | none | 1005 | 366 | 639 | 36.42 | 46.0 | -9.58 | high | penalize | False |  | 40 |
| candidate_rank | rank_51_100 | 366 | 133 | 233 | 36.34 | 46.0 | -9.66 | high | penalize | False |  | 17 |
| candidate_rank | rank_11_20 | 264 | 113 | 151 | 42.8 | 46.0 | -3.2 | medium | penalize | False |  | 33 |
| news_risk_penalty | high | 176 | 74 | 102 | 42.05 | 46.0 | -3.95 | medium | penalize | False |  | 29 |
| overextension_penalty | low | 175 | 71 | 104 | 40.57 | 46.0 | -5.43 | medium | penalize | False |  | 38 |
| liquidity_score | none | 295 | 17 | 278 | 5.76 | 46.0 | -40.24 | medium | penalize | False |  | 40 |
| reversal_risk_penalty | medium | 901 | 436 | 465 | 48.39 | 46.0 | 2.39 | high | neutral | False |  | 40 |
| volume_confirmation_score | negative | 4748 | 2285 | 2463 | 48.13 | 46.0 | 2.13 | high | neutral | False |  | 40 |
| liquidity_score | basic | 5136 | 2455 | 2681 | 47.8 | 46.0 | 1.8 | high | neutral | False |  | 40 |
| liquidity_score | confirmed | 1092 | 515 | 577 | 47.16 | 46.0 | 1.16 | high | neutral | False |  | 40 |
| final_price_signal_score_v2 | score_30_40 | 3762 | 1769 | 1993 | 47.02 | 46.0 | 1.02 | high | neutral | False |  | 40 |
| candidate_rank | rank_101_plus | 5299 | 2472 | 2827 | 46.65 | 46.0 | 0.65 | high | neutral | False |  | 40 |
| attention_noise_penalty | high | 407 | 188 | 219 | 46.19 | 46.0 | 0.19 | high | neutral | False |  | 32 |
| selected_pick | broad_pool | 6305 | 2910 | 3395 | 46.15 | 46.0 | 0.15 | high | neutral | False |  | 47 |
| news_risk_penalty | none | 6226 | 2857 | 3369 | 45.89 | 46.0 | -0.11 | high | neutral | False |  | 40 |
| score_version | v2_conservative_ranker | 6523 | 2987 | 3536 | 45.79 | 46.0 | -0.21 | high | neutral | False |  | 40 |
| candidate_rank | top_10 | 348 | 159 | 189 | 45.69 | 46.0 | -0.31 | high | neutral | False |  | 41 |
| attention_noise_penalty | none | 6070 | 2772 | 3298 | 45.67 | 46.0 | -0.33 | high | neutral | False |  | 40 |
| overextension_penalty | none | 5570 | 2540 | 3030 | 45.6 | 46.0 | -0.4 | high | neutral | False |  | 40 |
| reversal_risk_penalty | none | 4318 | 1960 | 2358 | 45.39 | 46.0 | -0.61 | high | neutral | False |  | 40 |
| selected_pick | selected | 612 | 272 | 340 | 44.44 | 46.0 | -1.56 | high | neutral | False |  | 41 |
| candidate_rank | rank_21_50 | 312 | 137 | 175 | 43.91 | 46.0 | -2.09 | high | neutral | False |  | 27 |
| final_price_signal_score_v2 | score_20_30 | 1479 | 649 | 830 | 43.88 | 46.0 | -2.12 | high | neutral | False |  | 40 |
| final_price_signal_score_v2 | score_50_plus | 934 | 403 | 531 | 43.15 | 46.0 | -2.85 | high | neutral | False |  | 40 |
| volume_confirmation_score | high | 252 | 117 | 135 | 46.43 | 46.0 | 0.43 | medium | neutral | False |  | 39 |
| final_price_signal_score_v2 | score_lt_20 | 299 | 137 | 162 | 45.82 | 46.0 | -0.18 | medium | neutral | False |  | 40 |
| news_risk_penalty | medium | 103 | 46 | 57 | 44.66 | 46.0 | -1.34 | medium | neutral | False |  | 35 |
| overextension_penalty | medium | 134 | 58 | 76 | 43.28 | 46.0 | -2.72 | medium | neutral | False |  | 35 |
| attention_noise_penalty | medium | 15 | 9 | 6 | 60.0 | 46.0 | 14.0 | insufficient | watch | True | large_lift_with_under_100_cases | 9 |
| final_price_signal_score_v2 | score_40_50 | 49 | 29 | 20 | 59.18 | 46.0 | 13.18 | insufficient | watch | True | large_lift_with_under_100_cases | 5 |
| attention_noise_penalty | low | 31 | 18 | 13 | 58.06 | 46.0 | 12.06 | insufficient | watch | True | large_lift_with_under_100_cases | 15 |
| news_risk_penalty | low | 18 | 10 | 8 | 55.56 | 46.0 | 9.56 | insufficient | watch | False |  | 10 |