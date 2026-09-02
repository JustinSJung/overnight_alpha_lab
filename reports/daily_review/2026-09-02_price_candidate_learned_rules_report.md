# Price Candidate Learned Rules Report - 2026-09-02

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260902.csv`
- Baseline evaluated count: **3669**
- Baseline success rate: **43.2%**
- Total rule rows: **45**
- Boost rules: **13**
- Penalize rules: **7**
- Watch rules: **4**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 409 | 217 | 192 | 53.06 | 43.2 | 9.86 | high | boost | True | boost_on_semantically_risky_bucket | 29 |
| overextension_penalty | high | 416 | 215 | 201 | 51.68 | 43.2 | 8.48 | high | boost | True | boost_on_semantically_risky_bucket | 28 |
| candidate_rank | missing | 321 | 162 | 159 | 50.47 | 43.2 | 7.27 | high | boost | False |  | 6 |
| score_version | legacy_or_unknown | 382 | 188 | 194 | 49.21 | 43.2 | 6.01 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 382 | 188 | 194 | 49.21 | 43.2 | 6.01 | high | boost | False |  | 7 |
| overextension_penalty | missing | 382 | 188 | 194 | 49.21 | 43.2 | 6.01 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 382 | 188 | 194 | 49.21 | 43.2 | 6.01 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 382 | 188 | 194 | 49.21 | 43.2 | 6.01 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 382 | 188 | 194 | 49.21 | 43.2 | 6.01 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 382 | 188 | 194 | 49.21 | 43.2 | 6.01 | high | boost | False |  | 7 |
| liquidity_score | missing | 382 | 188 | 194 | 49.21 | 43.2 | 6.01 | high | boost | False |  | 7 |
| reversal_risk_penalty | medium | 589 | 274 | 315 | 46.52 | 43.2 | 3.32 | high | boost | False |  | 29 |
| news_risk_penalty | medium | 86 | 40 | 46 | 46.51 | 43.2 | 3.31 | low | boost | False |  | 26 |
| reversal_risk_penalty | none | 1745 | 695 | 1050 | 39.83 | 43.2 | -3.37 | high | penalize | False |  | 29 |
| reversal_risk_penalty | low | 544 | 211 | 333 | 38.79 | 43.2 | -4.41 | high | penalize | False |  | 29 |
| volume_confirmation_score | none | 768 | 287 | 481 | 37.37 | 43.2 | -5.83 | high | penalize | False |  | 29 |
| candidate_rank | rank_51_100 | 342 | 121 | 221 | 35.38 | 43.2 | -7.82 | high | penalize | False |  | 16 |
| candidate_rank | rank_21_50 | 225 | 89 | 136 | 39.56 | 43.2 | -3.64 | medium | penalize | False |  | 18 |
| final_price_signal_score_v2 | score_lt_20 | 199 | 77 | 122 | 38.69 | 43.2 | -4.51 | medium | penalize | False |  | 29 |
| liquidity_score | none | 176 | 8 | 168 | 4.55 | 43.2 | -38.65 | medium | penalize | False |  | 29 |
| liquidity_score | confirmed | 943 | 433 | 510 | 45.92 | 43.2 | 2.72 | high | neutral | False |  | 29 |
| volume_confirmation_score | negative | 1843 | 822 | 1021 | 44.6 | 43.2 | 1.4 | high | neutral | False |  | 29 |
| liquidity_score | basic | 2168 | 956 | 1212 | 44.1 | 43.2 | 0.9 | high | neutral | False |  | 29 |
| final_price_signal_score_v2 | score_30_40 | 1634 | 720 | 914 | 44.06 | 43.2 | 0.86 | high | neutral | False |  | 29 |
| selected_pick | selected | 411 | 181 | 230 | 44.04 | 43.2 | 0.84 | high | neutral | False |  | 30 |
| candidate_rank | rank_101_plus | 2370 | 1032 | 1338 | 43.54 | 43.2 | 0.34 | high | neutral | False |  | 29 |
| selected_pick | broad_pool | 3258 | 1404 | 1854 | 43.09 | 43.2 | -0.11 | high | neutral | False |  | 36 |
| score_version | v2_conservative_ranker | 3287 | 1397 | 1890 | 42.5 | 43.2 | -0.7 | high | neutral | False |  | 29 |
| news_risk_penalty | none | 3057 | 1294 | 1763 | 42.33 | 43.2 | -0.87 | high | neutral | False |  | 29 |
| attention_noise_penalty | none | 3113 | 1317 | 1796 | 42.31 | 43.2 | -0.89 | high | neutral | False |  | 29 |
| final_price_signal_score_v2 | score_20_30 | 792 | 328 | 464 | 41.41 | 43.2 | -1.79 | high | neutral | False |  | 29 |
| overextension_penalty | none | 2635 | 1083 | 1552 | 41.1 | 43.2 | -2.1 | high | neutral | False |  | 29 |
| volume_confirmation_score | moderate | 458 | 188 | 270 | 41.05 | 43.2 | -2.15 | high | neutral | False |  | 29 |
| final_price_signal_score_v2 | score_50_plus | 642 | 263 | 379 | 40.97 | 43.2 | -2.23 | high | neutral | False |  | 29 |
| volume_confirmation_score | high | 218 | 100 | 118 | 45.87 | 43.2 | 2.67 | medium | neutral | False |  | 28 |
| attention_noise_penalty | high | 164 | 74 | 90 | 45.12 | 43.2 | 1.92 | medium | neutral | False |  | 21 |
| candidate_rank | top_10 | 240 | 108 | 132 | 45.0 | 43.2 | 1.8 | medium | neutral | False |  | 30 |
| candidate_rank | rank_11_20 | 171 | 73 | 98 | 42.69 | 43.2 | -0.51 | medium | neutral | False |  | 22 |
| overextension_penalty | low | 134 | 57 | 77 | 42.54 | 43.2 | -0.66 | medium | neutral | False |  | 27 |
| news_risk_penalty | high | 127 | 54 | 73 | 42.52 | 43.2 | -0.68 | medium | neutral | False |  | 18 |
| overextension_penalty | medium | 102 | 42 | 60 | 41.18 | 43.2 | -2.02 | medium | neutral | False |  | 25 |
| attention_noise_penalty | low | 6 | 5 | 1 | 83.33 | 43.2 | 40.13 | insufficient | watch | True | large_lift_with_under_100_cases | 5 |
| news_risk_penalty | low | 17 | 9 | 8 | 52.94 | 43.2 | 9.74 | insufficient | watch | False |  | 10 |
| final_price_signal_score_v2 | score_40_50 | 20 | 9 | 11 | 45.0 | 43.2 | 1.8 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 4 | 1 | 3 | 25.0 | 43.2 | -18.2 | insufficient | watch | True | large_lift_with_under_100_cases | 4 |