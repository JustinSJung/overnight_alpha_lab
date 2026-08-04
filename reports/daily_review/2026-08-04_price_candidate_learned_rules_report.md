# Price Candidate Learned Rules Report - 2026-08-04

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260804.csv`
- Baseline evaluated count: **1558**
- Baseline success rate: **42.55%**
- Total rule rows: **43**
- Boost rules: **15**
- Penalize rules: **11**
- Watch rules: **9**
- Suspicious rules: **11**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| score_version | legacy_or_unknown | 368 | 190 | 178 | 51.63 | 42.55 | 9.08 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 368 | 190 | 178 | 51.63 | 42.55 | 9.08 | high | boost | False |  | 7 |
| overextension_penalty | missing | 368 | 190 | 178 | 51.63 | 42.55 | 9.08 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 368 | 190 | 178 | 51.63 | 42.55 | 9.08 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 368 | 190 | 178 | 51.63 | 42.55 | 9.08 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 368 | 190 | 178 | 51.63 | 42.55 | 9.08 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 368 | 190 | 178 | 51.63 | 42.55 | 9.08 | high | boost | False |  | 7 |
| liquidity_score | missing | 368 | 190 | 178 | 51.63 | 42.55 | 9.08 | high | boost | False |  | 7 |
| volume_confirmation_score | high | 79 | 46 | 33 | 58.23 | 42.55 | 15.68 | low | boost | True | large_lift_with_under_100_cases | 9 |
| candidate_rank | top_10 | 71 | 39 | 32 | 54.93 | 42.55 | 12.38 | low | boost | True | large_lift_with_under_100_cases | 11 |
| final_price_signal_score_v2 | score_50_plus | 71 | 38 | 33 | 53.52 | 42.55 | 10.97 | low | boost | True | large_lift_with_under_100_cases | 10 |
| selected_pick | selected | 76 | 40 | 36 | 52.63 | 42.55 | 10.08 | low | boost | True | large_lift_with_under_100_cases | 11 |
| candidate_rank | missing | 294 | 159 | 135 | 54.08 | 42.55 | 11.53 | medium | boost | False |  | 6 |
| reversal_risk_penalty | high | 162 | 82 | 80 | 50.62 | 42.55 | 8.07 | medium | boost | True | boost_on_semantically_risky_bucket | 10 |
| overextension_penalty | high | 112 | 52 | 60 | 46.43 | 42.55 | 3.88 | medium | boost | True | boost_on_semantically_risky_bucket | 10 |
| candidate_rank | rank_101_plus | 777 | 305 | 472 | 39.25 | 42.55 | -3.3 | high | penalize | False |  | 10 |
| overextension_penalty | none | 1006 | 393 | 613 | 39.07 | 42.55 | -3.48 | high | penalize | False |  | 10 |
| news_risk_penalty | none | 1132 | 440 | 692 | 38.87 | 42.55 | -3.68 | high | penalize | False |  | 10 |
| final_price_signal_score_v2 | score_20_30 | 454 | 173 | 281 | 38.11 | 42.55 | -4.44 | high | penalize | False |  | 10 |
| candidate_rank | rank_51_100 | 377 | 140 | 237 | 37.14 | 42.55 | -5.41 | high | penalize | False |  | 10 |
| reversal_risk_penalty | none | 619 | 224 | 395 | 36.19 | 42.55 | -6.36 | high | penalize | False |  | 10 |
| liquidity_score | none | 58 | 3 | 55 | 5.17 | 42.55 | -37.38 | low | penalize | True | large_lift_with_under_100_cases | 10 |
| volume_confirmation_score | moderate | 174 | 66 | 108 | 37.93 | 42.55 | -4.62 | medium | penalize | False |  | 10 |
| final_price_signal_score_v2 | score_lt_20 | 138 | 52 | 86 | 37.68 | 42.55 | -4.87 | medium | penalize | False |  | 10 |
| reversal_risk_penalty | low | 185 | 68 | 117 | 36.76 | 42.55 | -5.79 | medium | penalize | False |  | 10 |
| volume_confirmation_score | none | 282 | 94 | 188 | 33.33 | 42.55 | -9.22 | medium | penalize | False |  | 10 |
| liquidity_score | confirmed | 345 | 156 | 189 | 45.22 | 42.55 | 2.67 | high | neutral | False |  | 10 |
| selected_pick | broad_pool | 1482 | 623 | 859 | 42.04 | 42.55 | -0.51 | high | neutral | False |  | 17 |
| volume_confirmation_score | negative | 655 | 267 | 388 | 40.76 | 42.55 | -1.79 | high | neutral | False |  | 10 |
| liquidity_score | basic | 787 | 314 | 473 | 39.9 | 42.55 | -2.65 | high | neutral | False |  | 10 |
| final_price_signal_score_v2 | score_30_40 | 527 | 210 | 317 | 39.85 | 42.55 | -2.7 | high | neutral | False |  | 10 |
| score_version | v2_conservative_ranker | 1190 | 473 | 717 | 39.75 | 42.55 | -2.8 | high | neutral | False |  | 10 |
| attention_noise_penalty | none | 1145 | 455 | 690 | 39.74 | 42.55 | -2.81 | high | neutral | False |  | 10 |
| reversal_risk_penalty | medium | 224 | 99 | 125 | 44.2 | 42.55 | 1.65 | medium | neutral | False |  | 10 |
| news_risk_penalty | high | 2 | 2 | 0 | 100.0 | 42.55 | 57.45 | insufficient | watch | True | large_lift_with_under_100_cases; only_one_or_two_signal_dates | 2 |
| news_risk_penalty | low | 17 | 12 | 5 | 70.59 | 42.55 | 28.04 | insufficient | watch | True | large_lift_with_under_100_cases | 8 |
| candidate_rank | rank_21_50 | 34 | 19 | 15 | 55.88 | 42.55 | 13.33 | insufficient | watch | True | large_lift_with_under_100_cases; only_one_or_two_signal_dates | 2 |
| attention_noise_penalty | low | 4 | 2 | 2 | 50.0 | 42.55 | 7.45 | insufficient | watch | False |  | 3 |
| news_risk_penalty | medium | 39 | 19 | 20 | 48.72 | 42.55 | 6.17 | insufficient | watch | False |  | 10 |
| overextension_penalty | low | 45 | 18 | 27 | 40.0 | 42.55 | -2.55 | insufficient | watch | False |  | 8 |
| attention_noise_penalty | high | 41 | 16 | 25 | 39.02 | 42.55 | -3.53 | insufficient | watch | False |  | 8 |
| overextension_penalty | medium | 27 | 10 | 17 | 37.04 | 42.55 | -5.51 | insufficient | watch | False |  | 7 |
| candidate_rank | rank_11_20 | 5 | 1 | 4 | 20.0 | 42.55 | -22.55 | insufficient | watch | True | large_lift_with_under_100_cases; only_one_or_two_signal_dates | 2 |