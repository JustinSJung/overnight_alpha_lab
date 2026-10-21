# Price Candidate Learned Rules Report - 2026-10-21

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261021.csv`
- Baseline evaluated count: **14171**
- Baseline success rate: **48.0%**
- Total rule rows: **45**
- Boost rules: **2**
- Penalize rules: **12**
- Watch rules: **2**
- Suspicious rules: **1**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | low | 62 | 37 | 25 | 59.68 | 48.0 | 11.68 | low | boost | True | large_lift_with_under_100_cases | 26 |
| final_price_signal_score_v2 | score_40_50 | 203 | 105 | 98 | 51.72 | 48.0 | 3.72 | medium | boost | False |  | 8 |
| candidate_rank | top_10 | 509 | 228 | 281 | 44.79 | 48.0 | -3.21 | high | penalize | False |  | 58 |
| volume_confirmation_score | moderate | 926 | 414 | 512 | 44.71 | 48.0 | -3.29 | high | penalize | False |  | 57 |
| final_price_signal_score_v2 | score_lt_20 | 457 | 202 | 255 | 44.2 | 48.0 | -3.8 | high | penalize | False |  | 57 |
| overextension_penalty | low | 317 | 140 | 177 | 44.16 | 48.0 | -3.84 | high | penalize | False |  | 54 |
| reversal_risk_penalty | low | 1253 | 552 | 701 | 44.05 | 48.0 | -3.95 | high | penalize | False |  | 57 |
| candidate_rank | rank_21_50 | 573 | 248 | 325 | 43.28 | 48.0 | -4.72 | high | penalize | False |  | 40 |
| final_price_signal_score_v2 | score_50_plus | 1820 | 785 | 1035 | 43.13 | 48.0 | -4.87 | high | penalize | False |  | 57 |
| candidate_rank | rank_51_100 | 562 | 210 | 352 | 37.37 | 48.0 | -10.63 | high | penalize | False |  | 24 |
| volume_confirmation_score | none | 1664 | 613 | 1051 | 36.84 | 48.0 | -11.16 | high | penalize | False |  | 57 |
| liquidity_score | none | 472 | 21 | 451 | 4.45 | 48.0 | -43.55 | high | penalize | False |  | 57 |
| news_risk_penalty | medium | 145 | 63 | 82 | 43.45 | 48.0 | -4.55 | medium | penalize | False |  | 50 |
| news_risk_penalty | high | 255 | 110 | 145 | 43.14 | 48.0 | -4.86 | medium | penalize | False |  | 45 |
| candidate_rank | missing | 336 | 171 | 165 | 50.89 | 48.0 | 2.89 | high | neutral | False |  | 6 |
| reversal_risk_penalty | high | 793 | 403 | 390 | 50.82 | 48.0 | 2.82 | high | neutral | False |  | 57 |
| volume_confirmation_score | negative | 10716 | 5356 | 5360 | 49.98 | 48.0 | 1.98 | high | neutral | False |  | 57 |
| final_price_signal_score_v2 | score_30_40 | 8101 | 4045 | 4056 | 49.93 | 48.0 | 1.93 | high | neutral | False |  | 57 |
| overextension_penalty | high | 1008 | 503 | 505 | 49.9 | 48.0 | 1.9 | high | neutral | False |  | 57 |
| liquidity_score | basic | 11388 | 5665 | 5723 | 49.75 | 48.0 | 1.75 | high | neutral | False |  | 57 |
| score_version | legacy_or_unknown | 405 | 201 | 204 | 49.63 | 48.0 | 1.63 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 405 | 201 | 204 | 49.63 | 48.0 | 1.63 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 405 | 201 | 204 | 49.63 | 48.0 | 1.63 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 405 | 201 | 204 | 49.63 | 48.0 | 1.63 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 405 | 201 | 204 | 49.63 | 48.0 | 1.63 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 405 | 201 | 204 | 49.63 | 48.0 | 1.63 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 405 | 201 | 204 | 49.63 | 48.0 | 1.63 | high | neutral | False |  | 7 |
| liquidity_score | missing | 405 | 201 | 204 | 49.63 | 48.0 | 1.63 | high | neutral | False |  | 7 |
| reversal_risk_penalty | medium | 1485 | 731 | 754 | 49.23 | 48.0 | 1.23 | high | neutral | False |  | 57 |
| candidate_rank | rank_101_plus | 11781 | 5759 | 6022 | 48.88 | 48.0 | 0.88 | high | neutral | False |  | 57 |
| selected_pick | broad_pool | 13252 | 6388 | 6864 | 48.2 | 48.0 | 0.2 | high | neutral | False |  | 64 |
| news_risk_penalty | none | 13347 | 6417 | 6930 | 48.08 | 48.0 | 0.08 | high | neutral | False |  | 57 |
| reversal_risk_penalty | none | 10235 | 4915 | 5320 | 48.02 | 48.0 | 0.02 | high | neutral | False |  | 57 |
| liquidity_score | confirmed | 1906 | 915 | 991 | 48.01 | 48.0 | 0.01 | high | neutral | False |  | 57 |
| score_version | v2_conservative_ranker | 13766 | 6601 | 7165 | 47.95 | 48.0 | -0.05 | high | neutral | False |  | 57 |
| attention_noise_penalty | none | 13066 | 6261 | 6805 | 47.92 | 48.0 | -0.08 | high | neutral | False |  | 57 |
| overextension_penalty | none | 12204 | 5845 | 6359 | 47.89 | 48.0 | -0.11 | high | neutral | False |  | 57 |
| volume_confirmation_score | high | 460 | 218 | 242 | 47.39 | 48.0 | -0.61 | high | neutral | False |  | 54 |
| attention_noise_penalty | high | 617 | 291 | 326 | 47.16 | 48.0 | -0.84 | high | neutral | False |  | 44 |
| final_price_signal_score_v2 | score_20_30 | 3185 | 1464 | 1721 | 45.97 | 48.0 | -2.03 | high | neutral | False |  | 57 |
| candidate_rank | rank_11_20 | 410 | 186 | 224 | 45.37 | 48.0 | -2.63 | high | neutral | False |  | 50 |
| selected_pick | selected | 919 | 414 | 505 | 45.05 | 48.0 | -2.95 | high | neutral | False |  | 58 |
| overextension_penalty | medium | 237 | 113 | 124 | 47.68 | 48.0 | -0.32 | medium | neutral | False |  | 52 |
| news_risk_penalty | low | 19 | 11 | 8 | 57.89 | 48.0 | 9.89 | insufficient | watch | False |  | 10 |
| attention_noise_penalty | medium | 21 | 12 | 9 | 57.14 | 48.0 | 9.14 | insufficient | watch | False |  | 14 |