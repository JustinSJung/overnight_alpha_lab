# Price Candidate Learned Rules Report - 2026-08-07

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260807.csv`
- Baseline evaluated count: **1804**
- Baseline success rate: **42.79%**
- Total rule rows: **44**
- Boost rules: **17**
- Penalize rules: **8**
- Watch rules: **7**
- Suspicious rules: **6**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| score_version | legacy_or_unknown | 372 | 191 | 181 | 51.34 | 42.79 | 8.55 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 372 | 191 | 181 | 51.34 | 42.79 | 8.55 | high | boost | False |  | 7 |
| overextension_penalty | missing | 372 | 191 | 181 | 51.34 | 42.79 | 8.55 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 372 | 191 | 181 | 51.34 | 42.79 | 8.55 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 372 | 191 | 181 | 51.34 | 42.79 | 8.55 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 372 | 191 | 181 | 51.34 | 42.79 | 8.55 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 372 | 191 | 181 | 51.34 | 42.79 | 8.55 | high | boost | False |  | 7 |
| liquidity_score | missing | 372 | 191 | 181 | 51.34 | 42.79 | 8.55 | high | boost | False |  | 7 |
| liquidity_score | confirmed | 431 | 203 | 228 | 47.1 | 42.79 | 4.31 | high | boost | False |  | 13 |
| volume_confirmation_score | high | 97 | 57 | 40 | 58.76 | 42.79 | 15.97 | low | boost | True | large_lift_with_under_100_cases | 12 |
| news_risk_penalty | medium | 51 | 25 | 26 | 49.02 | 42.79 | 6.23 | low | boost | False |  | 13 |
| candidate_rank | top_10 | 104 | 59 | 45 | 56.73 | 42.79 | 13.94 | medium | boost | False |  | 14 |
| candidate_rank | missing | 298 | 160 | 138 | 53.69 | 42.79 | 10.9 | medium | boost | False |  | 6 |
| reversal_risk_penalty | high | 211 | 112 | 99 | 53.08 | 42.79 | 10.29 | medium | boost | True | boost_on_semantically_risky_bucket | 13 |
| overextension_penalty | high | 185 | 98 | 87 | 52.97 | 42.79 | 10.18 | medium | boost | True | boost_on_semantically_risky_bucket | 13 |
| selected_pick | selected | 134 | 70 | 64 | 52.24 | 42.79 | 9.45 | medium | boost | False |  | 14 |
| final_price_signal_score_v2 | score_50_plus | 139 | 69 | 70 | 49.64 | 42.79 | 6.85 | medium | boost | False |  | 13 |
| final_price_signal_score_v2 | score_20_30 | 496 | 194 | 302 | 39.11 | 42.79 | -3.68 | high | penalize | False |  | 13 |
| overextension_penalty | none | 1144 | 440 | 704 | 38.46 | 42.79 | -4.33 | high | penalize | False |  | 13 |
| candidate_rank | rank_51_100 | 377 | 140 | 237 | 37.14 | 42.79 | -5.65 | high | penalize | False |  | 10 |
| reversal_risk_penalty | none | 726 | 267 | 459 | 36.78 | 42.79 | -6.01 | high | penalize | False |  | 13 |
| volume_confirmation_score | none | 345 | 117 | 228 | 33.91 | 42.79 | -8.88 | high | penalize | False |  | 13 |
| liquidity_score | none | 74 | 3 | 71 | 4.05 | 42.79 | -38.74 | low | penalize | True | large_lift_with_under_100_cases | 13 |
| final_price_signal_score_v2 | score_lt_20 | 146 | 57 | 89 | 39.04 | 42.79 | -3.75 | medium | penalize | False |  | 13 |
| reversal_risk_penalty | low | 218 | 81 | 137 | 37.16 | 42.79 | -5.63 | medium | penalize | False |  | 13 |
| selected_pick | broad_pool | 1670 | 702 | 968 | 42.04 | 42.79 | -0.75 | high | neutral | False |  | 20 |
| volume_confirmation_score | negative | 769 | 317 | 452 | 41.22 | 42.79 | -1.57 | high | neutral | False |  | 13 |
| score_version | v2_conservative_ranker | 1432 | 581 | 851 | 40.57 | 42.79 | -2.22 | high | neutral | False |  | 13 |
| attention_noise_penalty | none | 1371 | 555 | 816 | 40.48 | 42.79 | -2.31 | high | neutral | False |  | 13 |
| liquidity_score | basic | 927 | 375 | 552 | 40.45 | 42.79 | -2.34 | high | neutral | False |  | 13 |
| candidate_rank | rank_101_plus | 951 | 382 | 569 | 40.17 | 42.79 | -2.62 | high | neutral | False |  | 13 |
| final_price_signal_score_v2 | score_30_40 | 651 | 261 | 390 | 40.09 | 42.79 | -2.7 | high | neutral | False |  | 13 |
| news_risk_penalty | none | 1349 | 539 | 810 | 39.96 | 42.79 | -2.83 | high | neutral | False |  | 13 |
| attention_noise_penalty | high | 55 | 24 | 31 | 43.64 | 42.79 | 0.85 | low | neutral | False |  | 10 |
| overextension_penalty | low | 61 | 25 | 36 | 40.98 | 42.79 | -1.81 | low | neutral | False |  | 11 |
| reversal_risk_penalty | medium | 277 | 121 | 156 | 43.68 | 42.79 | 0.89 | medium | neutral | False |  | 13 |
| volume_confirmation_score | moderate | 221 | 90 | 131 | 40.72 | 42.79 | -2.07 | medium | neutral | False |  | 13 |
| news_risk_penalty | low | 22 | 13 | 9 | 59.09 | 42.79 | 16.3 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | low | 4 | 2 | 2 | 50.0 | 42.79 | 7.21 | insufficient | watch | False |  | 3 |
| candidate_rank | rank_21_50 | 44 | 20 | 24 | 45.45 | 42.79 | 2.66 | insufficient | watch | False |  | 4 |
| overextension_penalty | medium | 42 | 18 | 24 | 42.86 | 42.79 | 0.07 | insufficient | watch | False |  | 10 |
| news_risk_penalty | high | 10 | 4 | 6 | 40.0 | 42.79 | -2.79 | insufficient | watch | False |  | 3 |
| candidate_rank | rank_11_20 | 30 | 11 | 19 | 36.67 | 42.79 | -6.12 | insufficient | watch | False |  | 5 |
| attention_noise_penalty | medium | 2 | 0 | 2 | 0.0 | 42.79 | -42.79 | insufficient | watch | True | large_lift_with_under_100_cases; only_one_or_two_signal_dates | 2 |