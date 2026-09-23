# Price Candidate Learned Rules Report - 2026-09-23

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260923.csv`
- Baseline evaluated count: **7456**
- Baseline success rate: **46.75%**
- Total rule rows: **45**
- Boost rules: **3**
- Penalize rules: **8**
- Watch rules: **4**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| candidate_rank | missing | 330 | 168 | 162 | 50.91 | 46.75 | 4.16 | high | boost | False |  | 6 |
| overextension_penalty | high | 684 | 348 | 336 | 50.88 | 46.75 | 4.13 | high | boost | True | boost_on_semantically_risky_bucket | 42 |
| reversal_risk_penalty | high | 586 | 297 | 289 | 50.68 | 46.75 | 3.93 | high | boost | True | boost_on_semantically_risky_bucket | 42 |
| volume_confirmation_score | moderate | 526 | 227 | 299 | 43.16 | 46.75 | -3.59 | high | penalize | False |  | 42 |
| reversal_risk_penalty | low | 812 | 346 | 466 | 42.61 | 46.75 | -4.14 | high | penalize | False |  | 42 |
| candidate_rank | rank_51_100 | 359 | 131 | 228 | 36.49 | 46.75 | -10.26 | high | penalize | False |  | 17 |
| volume_confirmation_score | none | 1007 | 365 | 642 | 36.25 | 46.75 | -10.5 | high | penalize | False |  | 42 |
| liquidity_score | none | 304 | 18 | 286 | 5.92 | 46.75 | -40.83 | high | penalize | False |  | 42 |
| candidate_rank | rank_11_20 | 283 | 123 | 160 | 43.46 | 46.75 | -3.29 | medium | penalize | False |  | 35 |
| news_risk_penalty | high | 177 | 72 | 105 | 40.68 | 46.75 | -6.07 | medium | penalize | False |  | 29 |
| overextension_penalty | low | 183 | 73 | 110 | 39.89 | 46.75 | -6.86 | medium | penalize | False |  | 40 |
| score_version | legacy_or_unknown | 396 | 196 | 200 | 49.49 | 46.75 | 2.74 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 396 | 196 | 200 | 49.49 | 46.75 | 2.74 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 396 | 196 | 200 | 49.49 | 46.75 | 2.74 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 396 | 196 | 200 | 49.49 | 46.75 | 2.74 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 396 | 196 | 200 | 49.49 | 46.75 | 2.74 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 396 | 196 | 200 | 49.49 | 46.75 | 2.74 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 396 | 196 | 200 | 49.49 | 46.75 | 2.74 | high | neutral | False |  | 7 |
| liquidity_score | missing | 396 | 196 | 200 | 49.49 | 46.75 | 2.74 | high | neutral | False |  | 7 |
| volume_confirmation_score | negative | 5273 | 2579 | 2694 | 48.91 | 46.75 | 2.16 | high | neutral | False |  | 42 |
| reversal_risk_penalty | medium | 958 | 467 | 491 | 48.75 | 46.75 | 2.0 | high | neutral | False |  | 42 |
| liquidity_score | basic | 5657 | 2752 | 2905 | 48.65 | 46.75 | 1.9 | high | neutral | False |  | 42 |
| final_price_signal_score_v2 | score_30_40 | 4124 | 1963 | 2161 | 47.6 | 46.75 | 0.85 | high | neutral | False |  | 42 |
| candidate_rank | rank_101_plus | 5762 | 2738 | 3024 | 47.52 | 46.75 | 0.77 | high | neutral | False |  | 42 |
| liquidity_score | confirmed | 1099 | 520 | 579 | 47.32 | 46.75 | 0.57 | high | neutral | False |  | 42 |
| selected_pick | broad_pool | 6804 | 3193 | 3611 | 46.93 | 46.75 | 0.18 | high | neutral | False |  | 49 |
| attention_noise_penalty | high | 438 | 205 | 233 | 46.8 | 46.75 | 0.05 | high | neutral | False |  | 34 |
| news_risk_penalty | none | 6755 | 3160 | 3595 | 46.78 | 46.75 | 0.03 | high | neutral | False |  | 42 |
| score_version | v2_conservative_ranker | 7060 | 3290 | 3770 | 46.6 | 46.75 | -0.15 | high | neutral | False |  | 42 |
| attention_noise_penalty | none | 6571 | 3055 | 3516 | 46.49 | 46.75 | -0.26 | high | neutral | False |  | 42 |
| overextension_penalty | none | 6049 | 2805 | 3244 | 46.37 | 46.75 | -0.38 | high | neutral | False |  | 42 |
| reversal_risk_penalty | none | 4704 | 2180 | 2524 | 46.34 | 46.75 | -0.41 | high | neutral | False |  | 42 |
| candidate_rank | top_10 | 369 | 170 | 199 | 46.07 | 46.75 | -0.68 | high | neutral | False |  | 43 |
| final_price_signal_score_v2 | score_lt_20 | 318 | 146 | 172 | 45.91 | 46.75 | -0.84 | high | neutral | False |  | 42 |
| final_price_signal_score_v2 | score_20_30 | 1553 | 708 | 845 | 45.59 | 46.75 | -1.16 | high | neutral | False |  | 42 |
| selected_pick | selected | 652 | 293 | 359 | 44.94 | 46.75 | -1.81 | high | neutral | False |  | 43 |
| candidate_rank | rank_21_50 | 353 | 156 | 197 | 44.19 | 46.75 | -2.56 | high | neutral | False |  | 29 |
| final_price_signal_score_v2 | score_50_plus | 1016 | 445 | 571 | 43.8 | 46.75 | -2.95 | high | neutral | False |  | 42 |
| volume_confirmation_score | high | 254 | 119 | 135 | 46.85 | 46.75 | 0.1 | medium | neutral | False |  | 41 |
| overextension_penalty | medium | 144 | 64 | 80 | 44.44 | 46.75 | -2.31 | medium | neutral | False |  | 39 |
| news_risk_penalty | medium | 109 | 48 | 61 | 44.04 | 46.75 | -2.71 | medium | neutral | False |  | 37 |
| attention_noise_penalty | medium | 15 | 10 | 5 | 66.67 | 46.75 | 19.92 | insufficient | watch | True | large_lift_with_under_100_cases | 9 |
| final_price_signal_score_v2 | score_40_50 | 49 | 28 | 21 | 57.14 | 46.75 | 10.39 | insufficient | watch | True | large_lift_with_under_100_cases | 5 |
| attention_noise_penalty | low | 36 | 20 | 16 | 55.56 | 46.75 | 8.81 | insufficient | watch | False |  | 17 |
| news_risk_penalty | low | 19 | 10 | 9 | 52.63 | 46.75 | 5.88 | insufficient | watch | False |  | 9 |