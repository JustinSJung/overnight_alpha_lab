# Price Candidate Learned Rules Report - 2026-11-20

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261120.csv`
- Baseline evaluated count: **25758**
- Baseline success rate: **49.65%**
- Total rule rows: **45**
- Boost rules: **1**
- Penalize rules: **14**
- Watch rules: **2**
- Suspicious rules: **2**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 1130 | 602 | 528 | 53.27 | 49.65 | 3.62 | high | boost | True | boost_on_semantically_risky_bucket | 76 |
| attention_noise_penalty | high | 997 | 465 | 532 | 46.64 | 49.65 | -3.01 | high | penalize | False |  | 64 |
| volume_confirmation_score | moderate | 2397 | 1111 | 1286 | 46.35 | 49.65 | -3.3 | high | penalize | False |  | 76 |
| news_risk_penalty | high | 360 | 164 | 196 | 45.56 | 49.65 | -4.09 | high | penalize | False |  | 63 |
| final_price_signal_score_v2 | score_40_50 | 313 | 142 | 171 | 45.37 | 49.65 | -4.28 | high | penalize | False |  | 9 |
| candidate_rank | rank_11_20 | 551 | 248 | 303 | 45.01 | 49.65 | -4.64 | high | penalize | False |  | 67 |
| selected_pick | selected | 1232 | 544 | 688 | 44.16 | 49.65 | -5.49 | high | penalize | False |  | 75 |
| volume_confirmation_score | high | 1036 | 456 | 580 | 44.02 | 49.65 | -5.63 | high | penalize | False |  | 73 |
| candidate_rank | rank_21_50 | 896 | 392 | 504 | 43.75 | 49.65 | -5.9 | high | penalize | False |  | 55 |
| candidate_rank | top_10 | 681 | 296 | 385 | 43.47 | 49.65 | -6.18 | high | penalize | False |  | 75 |
| volume_confirmation_score | none | 3874 | 1670 | 2204 | 43.11 | 49.65 | -6.54 | high | penalize | False |  | 76 |
| final_price_signal_score_v2 | score_50_plus | 2711 | 1159 | 1552 | 42.75 | 49.65 | -6.9 | high | penalize | False |  | 76 |
| candidate_rank | rank_51_100 | 676 | 250 | 426 | 36.98 | 49.65 | -12.67 | high | penalize | False |  | 33 |
| liquidity_score | none | 647 | 42 | 605 | 6.49 | 49.65 | -43.16 | high | penalize | False |  | 75 |
| news_risk_penalty | medium | 203 | 88 | 115 | 43.35 | 49.65 | -6.3 | medium | penalize | False |  | 67 |
| volume_confirmation_score | negative | 18192 | 9421 | 8771 | 51.79 | 49.65 | 2.14 | high | neutral | False |  | 76 |
| overextension_penalty | high | 1391 | 720 | 671 | 51.76 | 49.65 | 2.11 | high | neutral | False |  | 76 |
| liquidity_score | basic | 20159 | 10379 | 9780 | 51.49 | 49.65 | 1.84 | high | neutral | False |  | 76 |
| final_price_signal_score_v2 | score_30_40 | 14694 | 7542 | 7152 | 51.33 | 49.65 | 1.68 | high | neutral | False |  | 76 |
| candidate_rank | rank_101_plus | 22695 | 11472 | 11223 | 50.55 | 49.65 | 0.9 | high | neutral | False |  | 76 |
| reversal_risk_penalty | medium | 2392 | 1201 | 1191 | 50.21 | 49.65 | 0.56 | high | neutral | False |  | 76 |
| selected_pick | broad_pool | 24526 | 12245 | 12281 | 49.93 | 49.65 | 0.28 | high | neutral | False |  | 81 |
| news_risk_penalty | none | 24917 | 12395 | 12522 | 49.75 | 49.65 | 0.1 | high | neutral | False |  | 76 |
| attention_noise_penalty | none | 24365 | 12120 | 12245 | 49.74 | 49.65 | 0.09 | high | neutral | False |  | 76 |
| score_version | v2_conservative_ranker | 25499 | 12658 | 12841 | 49.64 | 49.65 | -0.01 | high | neutral | False |  | 76 |
| reversal_risk_penalty | none | 19559 | 9702 | 9857 | 49.6 | 49.65 | -0.05 | high | neutral | False |  | 76 |
| overextension_penalty | none | 23233 | 11514 | 11719 | 49.56 | 49.65 | -0.09 | high | neutral | False |  | 76 |
| overextension_penalty | medium | 362 | 179 | 183 | 49.45 | 49.65 | -0.2 | high | neutral | False |  | 71 |
| final_price_signal_score_v2 | score_20_30 | 7001 | 3439 | 3562 | 49.12 | 49.65 | -0.53 | high | neutral | False |  | 76 |
| final_price_signal_score_v2 | score_lt_20 | 780 | 376 | 404 | 48.21 | 49.65 | -1.44 | high | neutral | False |  | 76 |
| overextension_penalty | low | 513 | 245 | 268 | 47.76 | 49.65 | -1.89 | high | neutral | False |  | 73 |
| reversal_risk_penalty | low | 2418 | 1153 | 1265 | 47.68 | 49.65 | -1.97 | high | neutral | False |  | 76 |
| liquidity_score | confirmed | 4693 | 2237 | 2456 | 47.67 | 49.65 | -1.98 | high | neutral | False |  | 76 |
| attention_noise_penalty | low | 102 | 52 | 50 | 50.98 | 49.65 | 1.33 | medium | neutral | False |  | 44 |
| score_version | legacy_or_unknown | 259 | 131 | 128 | 50.58 | 49.65 | 0.93 | medium | neutral | False |  | 5 |
| candidate_rank | missing | 259 | 131 | 128 | 50.58 | 49.65 | 0.93 | medium | neutral | False |  | 5 |
| final_price_signal_score_v2 | missing | 259 | 131 | 128 | 50.58 | 49.65 | 0.93 | medium | neutral | False |  | 5 |
| overextension_penalty | missing | 259 | 131 | 128 | 50.58 | 49.65 | 0.93 | medium | neutral | False |  | 5 |
| reversal_risk_penalty | missing | 259 | 131 | 128 | 50.58 | 49.65 | 0.93 | medium | neutral | False |  | 5 |
| news_risk_penalty | missing | 259 | 131 | 128 | 50.58 | 49.65 | 0.93 | medium | neutral | False |  | 5 |
| attention_noise_penalty | missing | 259 | 131 | 128 | 50.58 | 49.65 | 0.93 | medium | neutral | False |  | 5 |
| volume_confirmation_score | missing | 259 | 131 | 128 | 50.58 | 49.65 | 0.93 | medium | neutral | False |  | 5 |
| liquidity_score | missing | 259 | 131 | 128 | 50.58 | 49.65 | 0.93 | medium | neutral | False |  | 5 |
| attention_noise_penalty | medium | 35 | 21 | 14 | 60.0 | 49.65 | 10.35 | insufficient | watch | True | large_lift_with_under_100_cases | 24 |
| news_risk_penalty | low | 19 | 11 | 8 | 57.89 | 49.65 | 8.24 | insufficient | watch | False |  | 9 |