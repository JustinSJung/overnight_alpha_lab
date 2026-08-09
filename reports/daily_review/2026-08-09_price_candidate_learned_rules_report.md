# Price Candidate Learned Rules Report - 2026-08-09

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260809.csv`
- Baseline evaluated count: **1804**
- Baseline success rate: **42.9%**
- Total rule rows: **44**
- Boost rules: **17**
- Penalize rules: **9**
- Watch rules: **7**
- Suspicious rules: **7**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| score_version | legacy_or_unknown | 372 | 191 | 181 | 51.34 | 42.9 | 8.44 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 372 | 191 | 181 | 51.34 | 42.9 | 8.44 | high | boost | False |  | 7 |
| overextension_penalty | missing | 372 | 191 | 181 | 51.34 | 42.9 | 8.44 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 372 | 191 | 181 | 51.34 | 42.9 | 8.44 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 372 | 191 | 181 | 51.34 | 42.9 | 8.44 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 372 | 191 | 181 | 51.34 | 42.9 | 8.44 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 372 | 191 | 181 | 51.34 | 42.9 | 8.44 | high | boost | False |  | 7 |
| liquidity_score | missing | 372 | 191 | 181 | 51.34 | 42.9 | 8.44 | high | boost | False |  | 7 |
| liquidity_score | confirmed | 431 | 204 | 227 | 47.33 | 42.9 | 4.43 | high | boost | False |  | 13 |
| volume_confirmation_score | high | 97 | 56 | 41 | 57.73 | 42.9 | 14.83 | low | boost | True | large_lift_with_under_100_cases | 12 |
| news_risk_penalty | medium | 51 | 26 | 25 | 50.98 | 42.9 | 8.08 | low | boost | False |  | 13 |
| candidate_rank | top_10 | 104 | 60 | 44 | 57.69 | 42.9 | 14.79 | medium | boost | False |  | 14 |
| selected_pick | selected | 134 | 73 | 61 | 54.48 | 42.9 | 11.58 | medium | boost | False |  | 14 |
| candidate_rank | missing | 298 | 160 | 138 | 53.69 | 42.9 | 10.79 | medium | boost | False |  | 6 |
| final_price_signal_score_v2 | score_50_plus | 139 | 73 | 66 | 52.52 | 42.9 | 9.62 | medium | boost | False |  | 13 |
| reversal_risk_penalty | high | 211 | 109 | 102 | 51.66 | 42.9 | 8.76 | medium | boost | True | boost_on_semantically_risky_bucket | 13 |
| overextension_penalty | high | 185 | 95 | 90 | 51.35 | 42.9 | 8.45 | medium | boost | True | boost_on_semantically_risky_bucket | 13 |
| news_risk_penalty | none | 1349 | 538 | 811 | 39.88 | 42.9 | -3.02 | high | penalize | False |  | 13 |
| overextension_penalty | none | 1144 | 445 | 699 | 38.9 | 42.9 | -4.0 | high | penalize | False |  | 13 |
| final_price_signal_score_v2 | score_20_30 | 496 | 190 | 306 | 38.31 | 42.9 | -4.59 | high | penalize | False |  | 13 |
| reversal_risk_penalty | none | 726 | 272 | 454 | 37.47 | 42.9 | -5.43 | high | penalize | False |  | 13 |
| candidate_rank | rank_51_100 | 377 | 140 | 237 | 37.14 | 42.9 | -5.76 | high | penalize | False |  | 10 |
| volume_confirmation_score | none | 345 | 119 | 226 | 34.49 | 42.9 | -8.41 | high | penalize | False |  | 13 |
| liquidity_score | none | 74 | 3 | 71 | 4.05 | 42.9 | -38.85 | low | penalize | True | large_lift_with_under_100_cases | 13 |
| final_price_signal_score_v2 | score_lt_20 | 146 | 57 | 89 | 39.04 | 42.9 | -3.86 | medium | penalize | False |  | 13 |
| reversal_risk_penalty | low | 218 | 81 | 137 | 37.16 | 42.9 | -5.74 | medium | penalize | False |  | 13 |
| selected_pick | broad_pool | 1670 | 701 | 969 | 41.98 | 42.9 | -0.92 | high | neutral | False |  | 20 |
| volume_confirmation_score | negative | 769 | 317 | 452 | 41.22 | 42.9 | -1.68 | high | neutral | False |  | 13 |
| score_version | v2_conservative_ranker | 1432 | 583 | 849 | 40.71 | 42.9 | -2.19 | high | neutral | False |  | 13 |
| attention_noise_penalty | none | 1371 | 557 | 814 | 40.63 | 42.9 | -2.27 | high | neutral | False |  | 13 |
| liquidity_score | basic | 927 | 376 | 551 | 40.56 | 42.9 | -2.34 | high | neutral | False |  | 13 |
| final_price_signal_score_v2 | score_30_40 | 651 | 263 | 388 | 40.4 | 42.9 | -2.5 | high | neutral | False |  | 13 |
| candidate_rank | rank_101_plus | 951 | 380 | 571 | 39.96 | 42.9 | -2.94 | high | neutral | False |  | 13 |
| attention_noise_penalty | high | 55 | 24 | 31 | 43.64 | 42.9 | 0.74 | low | neutral | False |  | 10 |
| overextension_penalty | low | 61 | 25 | 36 | 40.98 | 42.9 | -1.92 | low | neutral | False |  | 11 |
| reversal_risk_penalty | medium | 277 | 121 | 156 | 43.68 | 42.9 | 0.78 | medium | neutral | False |  | 13 |
| volume_confirmation_score | moderate | 221 | 91 | 130 | 41.18 | 42.9 | -1.72 | medium | neutral | False |  | 13 |
| news_risk_penalty | high | 10 | 6 | 4 | 60.0 | 42.9 | 17.1 | insufficient | watch | True | large_lift_with_under_100_cases | 3 |
| news_risk_penalty | low | 22 | 13 | 9 | 59.09 | 42.9 | 16.19 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | low | 4 | 2 | 2 | 50.0 | 42.9 | 7.1 | insufficient | watch | False |  | 3 |
| candidate_rank | rank_21_50 | 44 | 21 | 23 | 47.73 | 42.9 | 4.83 | insufficient | watch | False |  | 4 |
| candidate_rank | rank_11_20 | 30 | 13 | 17 | 43.33 | 42.9 | 0.43 | insufficient | watch | False |  | 5 |
| overextension_penalty | medium | 42 | 18 | 24 | 42.86 | 42.9 | -0.04 | insufficient | watch | False |  | 10 |
| attention_noise_penalty | medium | 2 | 0 | 2 | 0.0 | 42.9 | -42.9 | insufficient | watch | True | large_lift_with_under_100_cases; only_one_or_two_signal_dates | 2 |