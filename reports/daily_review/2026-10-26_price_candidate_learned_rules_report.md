# Price Candidate Learned Rules Report - 2026-10-26

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261026.csv`
- Baseline evaluated count: **15577**
- Baseline success rate: **50.12%**
- Total rule rows: **45**
- Boost rules: **1**
- Penalize rules: **15**
- Watch rules: **2**
- Suspicious rules: **0**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | low | 67 | 40 | 27 | 59.7 | 50.12 | 9.58 | low | boost | False |  | 29 |
| volume_confirmation_score | high | 472 | 220 | 252 | 46.61 | 50.12 | -3.51 | high | penalize | False |  | 57 |
| reversal_risk_penalty | low | 1323 | 607 | 716 | 45.88 | 50.12 | -4.24 | high | penalize | False |  | 60 |
| final_price_signal_score_v2 | score_lt_20 | 459 | 210 | 249 | 45.75 | 50.12 | -4.37 | high | penalize | False |  | 60 |
| volume_confirmation_score | moderate | 938 | 418 | 520 | 44.56 | 50.12 | -5.56 | high | penalize | False |  | 60 |
| candidate_rank | rank_11_20 | 429 | 191 | 238 | 44.52 | 50.12 | -5.6 | high | penalize | False |  | 52 |
| overextension_penalty | low | 331 | 144 | 187 | 43.5 | 50.12 | -6.62 | high | penalize | False |  | 58 |
| selected_pick | selected | 967 | 419 | 548 | 43.33 | 50.12 | -6.79 | high | penalize | False |  | 61 |
| candidate_rank | rank_21_50 | 585 | 249 | 336 | 42.56 | 50.12 | -7.56 | high | penalize | False |  | 42 |
| candidate_rank | top_10 | 538 | 228 | 310 | 42.38 | 50.12 | -7.74 | high | penalize | False |  | 61 |
| final_price_signal_score_v2 | score_50_plus | 1878 | 792 | 1086 | 42.17 | 50.12 | -7.95 | high | penalize | False |  | 60 |
| candidate_rank | rank_51_100 | 567 | 211 | 356 | 37.21 | 50.12 | -12.91 | high | penalize | False |  | 24 |
| volume_confirmation_score | none | 1740 | 630 | 1110 | 36.21 | 50.12 | -13.91 | high | penalize | False |  | 60 |
| liquidity_score | none | 524 | 22 | 502 | 4.2 | 50.12 | -45.92 | high | penalize | False |  | 60 |
| news_risk_penalty | medium | 153 | 66 | 87 | 43.14 | 50.12 | -6.98 | medium | penalize | False |  | 53 |
| news_risk_penalty | high | 261 | 112 | 149 | 42.91 | 50.12 | -7.21 | medium | penalize | False |  | 48 |
| volume_confirmation_score | negative | 12028 | 6344 | 5684 | 52.74 | 50.12 | 2.62 | high | neutral | False |  | 60 |
| final_price_signal_score_v2 | score_30_40 | 9047 | 4742 | 4305 | 52.42 | 50.12 | 2.3 | high | neutral | False |  | 60 |
| liquidity_score | basic | 12715 | 6663 | 6052 | 52.4 | 50.12 | 2.28 | high | neutral | False |  | 60 |
| candidate_rank | rank_101_plus | 13126 | 6760 | 6366 | 51.5 | 50.12 | 1.38 | high | neutral | False |  | 60 |
| reversal_risk_penalty | none | 11463 | 5806 | 5657 | 50.65 | 50.12 | 0.53 | high | neutral | False |  | 60 |
| candidate_rank | missing | 332 | 168 | 164 | 50.6 | 50.12 | 0.48 | high | neutral | False |  | 6 |
| selected_pick | broad_pool | 14610 | 7388 | 7222 | 50.57 | 50.12 | 0.45 | high | neutral | False |  | 67 |
| news_risk_penalty | none | 14744 | 7423 | 7321 | 50.35 | 50.12 | 0.23 | high | neutral | False |  | 60 |
| overextension_penalty | none | 13538 | 6812 | 6726 | 50.32 | 50.12 | 0.2 | high | neutral | False |  | 60 |
| overextension_penalty | high | 1064 | 535 | 529 | 50.28 | 50.12 | 0.16 | high | neutral | False |  | 60 |
| attention_noise_penalty | none | 14435 | 7243 | 7192 | 50.18 | 50.12 | 0.06 | high | neutral | False |  | 60 |
| score_version | v2_conservative_ranker | 15178 | 7612 | 7566 | 50.15 | 50.12 | 0.03 | high | neutral | False |  | 60 |
| reversal_risk_penalty | medium | 1560 | 782 | 778 | 50.13 | 50.12 | 0.01 | high | neutral | False |  | 60 |
| reversal_risk_penalty | high | 832 | 417 | 415 | 50.12 | 50.12 | 0.0 | high | neutral | False |  | 60 |
| final_price_signal_score_v2 | score_20_30 | 3593 | 1763 | 1830 | 49.07 | 50.12 | -1.05 | high | neutral | False |  | 60 |
| score_version | legacy_or_unknown | 399 | 195 | 204 | 48.87 | 50.12 | -1.25 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 399 | 195 | 204 | 48.87 | 50.12 | -1.25 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 399 | 195 | 204 | 48.87 | 50.12 | -1.25 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 399 | 195 | 204 | 48.87 | 50.12 | -1.25 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 399 | 195 | 204 | 48.87 | 50.12 | -1.25 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 399 | 195 | 204 | 48.87 | 50.12 | -1.25 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 399 | 195 | 204 | 48.87 | 50.12 | -1.25 | high | neutral | False |  | 7 |
| liquidity_score | missing | 399 | 195 | 204 | 48.87 | 50.12 | -1.25 | high | neutral | False |  | 7 |
| attention_noise_penalty | high | 657 | 320 | 337 | 48.71 | 50.12 | -1.41 | high | neutral | False |  | 47 |
| liquidity_score | confirmed | 1939 | 927 | 1012 | 47.81 | 50.12 | -2.31 | high | neutral | False |  | 60 |
| final_price_signal_score_v2 | score_40_50 | 201 | 105 | 96 | 52.24 | 50.12 | 2.12 | medium | neutral | False |  | 8 |
| overextension_penalty | medium | 245 | 121 | 124 | 49.39 | 50.12 | -0.73 | medium | neutral | False |  | 56 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 50.12 | 4.88 | insufficient | watch | False |  | 10 |
| attention_noise_penalty | medium | 19 | 9 | 10 | 47.37 | 50.12 | -2.75 | insufficient | watch | False |  | 14 |