# Price Candidate Learned Rules Report - 2026-11-26

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261126.csv`
- Baseline evaluated count: **28536**
- Baseline success rate: **50.85%**
- Total rule rows: **45**
- Boost rules: **0**
- Penalize rules: **12**
- Watch rules: **2**
- Suspicious rules: **0**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| final_price_signal_score_v2 | score_40_50 | 307 | 141 | 166 | 45.93 | 50.85 | -4.92 | high | penalize | False |  | 8 |
| candidate_rank | rank_11_20 | 589 | 268 | 321 | 45.5 | 50.85 | -5.35 | high | penalize | False |  | 69 |
| volume_confirmation_score | none | 4582 | 2075 | 2507 | 45.29 | 50.85 | -5.56 | high | penalize | False |  | 76 |
| volume_confirmation_score | high | 1174 | 526 | 648 | 44.8 | 50.85 | -6.05 | high | penalize | False |  | 73 |
| news_risk_penalty | high | 392 | 174 | 218 | 44.39 | 50.85 | -6.46 | high | penalize | False |  | 66 |
| selected_pick | selected | 1280 | 561 | 719 | 43.83 | 50.85 | -7.02 | high | penalize | False |  | 75 |
| candidate_rank | rank_21_50 | 1011 | 432 | 579 | 42.73 | 50.85 | -8.12 | high | penalize | False |  | 58 |
| candidate_rank | top_10 | 691 | 293 | 398 | 42.4 | 50.85 | -8.45 | high | penalize | False |  | 75 |
| final_price_signal_score_v2 | score_50_plus | 2902 | 1223 | 1679 | 42.14 | 50.85 | -8.71 | high | penalize | False |  | 76 |
| candidate_rank | rank_51_100 | 613 | 225 | 388 | 36.7 | 50.85 | -14.15 | high | penalize | False |  | 32 |
| liquidity_score | none | 693 | 46 | 647 | 6.64 | 50.85 | -44.21 | high | penalize | False |  | 75 |
| news_risk_penalty | medium | 202 | 88 | 114 | 43.56 | 50.85 | -7.29 | medium | penalize | False |  | 68 |
| volume_confirmation_score | negative | 19691 | 10408 | 9283 | 52.86 | 50.85 | 2.01 | high | neutral | False |  | 76 |
| liquidity_score | basic | 22099 | 11639 | 10460 | 52.67 | 50.85 | 1.82 | high | neutral | False |  | 76 |
| final_price_signal_score_v2 | score_30_40 | 16121 | 8460 | 7661 | 52.48 | 50.85 | 1.63 | high | neutral | False |  | 76 |
| candidate_rank | rank_101_plus | 25373 | 13162 | 12211 | 51.87 | 50.85 | 1.02 | high | neutral | False |  | 76 |
| overextension_penalty | high | 1425 | 730 | 695 | 51.23 | 50.85 | 0.38 | high | neutral | False |  | 76 |
| selected_pick | broad_pool | 27256 | 13950 | 13306 | 51.18 | 50.85 | 0.33 | high | neutral | False |  | 81 |
| final_price_signal_score_v2 | score_20_30 | 8099 | 4143 | 3956 | 51.15 | 50.85 | 0.3 | high | neutral | False |  | 76 |
| reversal_risk_penalty | medium | 2582 | 1320 | 1262 | 51.12 | 50.85 | 0.27 | high | neutral | False |  | 76 |
| news_risk_penalty | none | 27674 | 14113 | 13561 | 51.0 | 50.85 | 0.15 | high | neutral | False |  | 76 |
| reversal_risk_penalty | none | 21788 | 11107 | 10681 | 50.98 | 50.85 | 0.13 | high | neutral | False |  | 76 |
| attention_noise_penalty | none | 27065 | 13792 | 13273 | 50.96 | 50.85 | 0.11 | high | neutral | False |  | 76 |
| overextension_penalty | none | 25927 | 13203 | 12724 | 50.92 | 50.85 | 0.07 | high | neutral | False |  | 76 |
| reversal_risk_penalty | high | 1177 | 599 | 578 | 50.89 | 50.85 | 0.04 | high | neutral | False |  | 76 |
| score_version | v2_conservative_ranker | 28277 | 14380 | 13897 | 50.85 | 50.85 | 0.0 | high | neutral | False |  | 76 |
| reversal_risk_penalty | low | 2730 | 1354 | 1376 | 49.6 | 50.85 | -1.25 | high | neutral | False |  | 76 |
| liquidity_score | confirmed | 5485 | 2695 | 2790 | 49.13 | 50.85 | -1.72 | high | neutral | False |  | 76 |
| final_price_signal_score_v2 | score_lt_20 | 848 | 413 | 435 | 48.7 | 50.85 | -2.15 | high | neutral | False |  | 76 |
| overextension_penalty | low | 544 | 264 | 280 | 48.53 | 50.85 | -2.32 | high | neutral | False |  | 76 |
| volume_confirmation_score | moderate | 2830 | 1371 | 1459 | 48.45 | 50.85 | -2.4 | high | neutral | False |  | 76 |
| attention_noise_penalty | high | 1064 | 511 | 553 | 48.03 | 50.85 | -2.82 | high | neutral | False |  | 66 |
| overextension_penalty | medium | 381 | 183 | 198 | 48.03 | 50.85 | -2.82 | high | neutral | False |  | 72 |
| score_version | legacy_or_unknown | 259 | 131 | 128 | 50.58 | 50.85 | -0.27 | medium | neutral | False |  | 5 |
| candidate_rank | missing | 259 | 131 | 128 | 50.58 | 50.85 | -0.27 | medium | neutral | False |  | 5 |
| final_price_signal_score_v2 | missing | 259 | 131 | 128 | 50.58 | 50.85 | -0.27 | medium | neutral | False |  | 5 |
| overextension_penalty | missing | 259 | 131 | 128 | 50.58 | 50.85 | -0.27 | medium | neutral | False |  | 5 |
| reversal_risk_penalty | missing | 259 | 131 | 128 | 50.58 | 50.85 | -0.27 | medium | neutral | False |  | 5 |
| news_risk_penalty | missing | 259 | 131 | 128 | 50.58 | 50.85 | -0.27 | medium | neutral | False |  | 5 |
| attention_noise_penalty | missing | 259 | 131 | 128 | 50.58 | 50.85 | -0.27 | medium | neutral | False |  | 5 |
| volume_confirmation_score | missing | 259 | 131 | 128 | 50.58 | 50.85 | -0.27 | medium | neutral | False |  | 5 |
| liquidity_score | missing | 259 | 131 | 128 | 50.58 | 50.85 | -0.27 | medium | neutral | False |  | 5 |
| attention_noise_penalty | low | 107 | 53 | 54 | 49.53 | 50.85 | -1.32 | medium | neutral | False |  | 44 |
| attention_noise_penalty | medium | 41 | 24 | 17 | 58.54 | 50.85 | 7.69 | insufficient | watch | False |  | 26 |
| news_risk_penalty | low | 9 | 5 | 4 | 55.56 | 50.85 | 4.71 | insufficient | watch | False |  | 5 |