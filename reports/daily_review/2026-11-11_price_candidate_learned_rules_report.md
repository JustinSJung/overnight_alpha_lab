# Price Candidate Learned Rules Report - 2026-11-11

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261111.csv`
- Baseline evaluated count: **21624**
- Baseline success rate: **49.95%**
- Total rule rows: **45**
- Boost rules: **1**
- Penalize rules: **15**
- Watch rules: **2**
- Suspicious rules: **1**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | low | 85 | 47 | 38 | 55.29 | 49.95 | 5.34 | low | boost | False |  | 35 |
| final_price_signal_score_v2 | score_lt_20 | 595 | 278 | 317 | 46.72 | 49.95 | -3.23 | high | penalize | False |  | 69 |
| volume_confirmation_score | moderate | 1707 | 782 | 925 | 45.81 | 49.95 | -4.14 | high | penalize | False |  | 70 |
| final_price_signal_score_v2 | score_40_50 | 310 | 141 | 169 | 45.48 | 49.95 | -4.47 | high | penalize | False |  | 9 |
| overextension_penalty | low | 395 | 178 | 217 | 45.06 | 49.95 | -4.89 | high | penalize | False |  | 66 |
| candidate_rank | rank_11_20 | 482 | 216 | 266 | 44.81 | 49.95 | -5.14 | high | penalize | False |  | 60 |
| news_risk_penalty | high | 318 | 142 | 176 | 44.65 | 49.95 | -5.3 | high | penalize | False |  | 57 |
| selected_pick | selected | 1093 | 485 | 608 | 44.37 | 49.95 | -5.58 | high | penalize | False |  | 70 |
| volume_confirmation_score | high | 764 | 337 | 427 | 44.11 | 49.95 | -5.84 | high | penalize | False |  | 66 |
| candidate_rank | top_10 | 611 | 269 | 342 | 44.03 | 49.95 | -5.92 | high | penalize | False |  | 70 |
| candidate_rank | rank_21_50 | 721 | 310 | 411 | 43.0 | 49.95 | -6.95 | high | penalize | False |  | 50 |
| final_price_signal_score_v2 | score_50_plus | 2188 | 940 | 1248 | 42.96 | 49.95 | -6.99 | high | penalize | False |  | 70 |
| volume_confirmation_score | none | 2872 | 1194 | 1678 | 41.57 | 49.95 | -8.38 | high | penalize | False |  | 70 |
| candidate_rank | rank_51_100 | 592 | 228 | 364 | 38.51 | 49.95 | -11.44 | high | penalize | False |  | 28 |
| liquidity_score | none | 593 | 33 | 560 | 5.56 | 49.95 | -44.39 | high | penalize | False |  | 69 |
| news_risk_penalty | medium | 183 | 80 | 103 | 43.72 | 49.95 | -6.23 | medium | penalize | False |  | 61 |
| volume_confirmation_score | negative | 15884 | 8292 | 7592 | 52.2 | 49.95 | 2.25 | high | neutral | False |  | 70 |
| overextension_penalty | high | 1137 | 592 | 545 | 52.07 | 49.95 | 2.12 | high | neutral | False |  | 70 |
| liquidity_score | basic | 17251 | 8970 | 8281 | 52.0 | 49.95 | 2.05 | high | neutral | False |  | 70 |
| reversal_risk_penalty | high | 926 | 476 | 450 | 51.4 | 49.95 | 1.45 | high | neutral | False |  | 70 |
| final_price_signal_score_v2 | score_30_40 | 12413 | 6366 | 6047 | 51.28 | 49.95 | 1.33 | high | neutral | False |  | 70 |
| candidate_rank | missing | 333 | 170 | 163 | 51.05 | 49.95 | 1.1 | high | neutral | False |  | 6 |
| candidate_rank | rank_101_plus | 18885 | 9608 | 9277 | 50.88 | 49.95 | 0.93 | high | neutral | False |  | 70 |
| final_price_signal_score_v2 | score_20_30 | 5721 | 2880 | 2841 | 50.34 | 49.95 | 0.39 | high | neutral | False |  | 70 |
| selected_pick | broad_pool | 20531 | 10316 | 10215 | 50.25 | 49.95 | 0.3 | high | neutral | False |  | 77 |
| reversal_risk_penalty | none | 16350 | 8195 | 8155 | 50.12 | 49.95 | 0.17 | high | neutral | False |  | 70 |
| news_risk_penalty | none | 20707 | 10372 | 10335 | 50.09 | 49.95 | 0.14 | high | neutral | False |  | 70 |
| attention_noise_penalty | none | 20265 | 10135 | 10130 | 50.01 | 49.95 | 0.06 | high | neutral | False |  | 70 |
| score_version | v2_conservative_ranker | 21227 | 10605 | 10622 | 49.96 | 49.95 | 0.01 | high | neutral | False |  | 70 |
| overextension_penalty | none | 19412 | 9694 | 9718 | 49.94 | 49.95 | -0.01 | high | neutral | False |  | 70 |
| reversal_risk_penalty | medium | 1993 | 993 | 1000 | 49.82 | 49.95 | -0.13 | high | neutral | False |  | 70 |
| score_version | legacy_or_unknown | 397 | 196 | 201 | 49.37 | 49.95 | -0.58 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 397 | 196 | 201 | 49.37 | 49.95 | -0.58 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 397 | 196 | 201 | 49.37 | 49.95 | -0.58 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 397 | 196 | 201 | 49.37 | 49.95 | -0.58 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 397 | 196 | 201 | 49.37 | 49.95 | -0.58 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 397 | 196 | 201 | 49.37 | 49.95 | -0.58 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 397 | 196 | 201 | 49.37 | 49.95 | -0.58 | high | neutral | False |  | 7 |
| liquidity_score | missing | 397 | 196 | 201 | 49.37 | 49.95 | -0.58 | high | neutral | False |  | 7 |
| reversal_risk_penalty | low | 1958 | 941 | 1017 | 48.06 | 49.95 | -1.89 | high | neutral | False |  | 70 |
| attention_noise_penalty | high | 847 | 404 | 443 | 47.7 | 49.95 | -2.25 | high | neutral | False |  | 58 |
| liquidity_score | confirmed | 3383 | 1602 | 1781 | 47.35 | 49.95 | -2.6 | high | neutral | False |  | 70 |
| overextension_penalty | medium | 283 | 141 | 142 | 49.82 | 49.95 | -0.13 | medium | neutral | False |  | 63 |
| attention_noise_penalty | medium | 30 | 19 | 11 | 63.33 | 49.95 | 13.38 | insufficient | watch | True | large_lift_with_under_100_cases | 18 |
| news_risk_penalty | low | 19 | 11 | 8 | 57.89 | 49.95 | 7.94 | insufficient | watch | False |  | 10 |