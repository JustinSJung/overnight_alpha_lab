# Price Candidate Learned Rules Report - 2026-07-30

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260730.csv`
- Baseline evaluated count: **1116**
- Baseline success rate: **51.7%**
- Total rule rows: **43**
- Boost rules: **7**
- Penalize rules: **6**
- Watch rules: **11**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action |
|---|---|---|---|---|---|---|---|---|---|
| candidate_rank | rank_101_plus | 441 | 252 | 189 | 57.14 | 51.7 | 5.44 | high | boost |
| final_price_signal_score_v2 | score_lt_20 | 74 | 47 | 27 | 63.51 | 51.7 | 11.81 | low | boost |
| volume_confirmation_score | high | 52 | 33 | 19 | 63.46 | 51.7 | 11.76 | low | boost |
| overextension_penalty | high | 55 | 33 | 22 | 60.0 | 51.7 | 8.3 | low | boost |
| reversal_risk_penalty | medium | 144 | 85 | 59 | 59.03 | 51.7 | 7.33 | medium | boost |
| reversal_risk_penalty | high | 119 | 70 | 49 | 58.82 | 51.7 | 7.12 | medium | boost |
| liquidity_score | confirmed | 218 | 124 | 94 | 56.88 | 51.7 | 5.18 | medium | boost |
| reversal_risk_penalty | none | 375 | 174 | 201 | 46.4 | 51.7 | -5.3 | high | penalize |
| candidate_rank | top_10 | 50 | 24 | 26 | 48.0 | 51.7 | -3.7 | low | penalize |
| selected_pick | selected | 52 | 24 | 28 | 46.15 | 51.7 | -5.55 | low | penalize |
| volume_confirmation_score | moderate | 101 | 47 | 54 | 46.53 | 51.7 | -5.17 | medium | penalize |
| volume_confirmation_score | none | 170 | 78 | 92 | 45.88 | 51.7 | -5.82 | medium | penalize |
| candidate_rank | rank_51_100 | 297 | 123 | 174 | 41.41 | 51.7 | -10.29 | medium | penalize |
| volume_confirmation_score | negative | 427 | 229 | 198 | 53.63 | 51.7 | 1.93 | high | neutral |
| liquidity_score | basic | 494 | 261 | 233 | 52.83 | 51.7 | 1.13 | high | neutral |
| attention_noise_penalty | none | 711 | 370 | 341 | 52.04 | 51.7 | 0.34 | high | neutral |
| selected_pick | broad_pool | 1064 | 553 | 511 | 51.97 | 51.7 | 0.27 | high | neutral |
| score_version | legacy_or_unknown | 366 | 190 | 176 | 51.91 | 51.7 | 0.21 | high | neutral |
| final_price_signal_score_v2 | missing | 366 | 190 | 176 | 51.91 | 51.7 | 0.21 | high | neutral |
| overextension_penalty | missing | 366 | 190 | 176 | 51.91 | 51.7 | 0.21 | high | neutral |
| reversal_risk_penalty | missing | 366 | 190 | 176 | 51.91 | 51.7 | 0.21 | high | neutral |
| news_risk_penalty | missing | 366 | 190 | 176 | 51.91 | 51.7 | 0.21 | high | neutral |
| attention_noise_penalty | missing | 366 | 190 | 176 | 51.91 | 51.7 | 0.21 | high | neutral |
| volume_confirmation_score | missing | 366 | 190 | 176 | 51.91 | 51.7 | 0.21 | high | neutral |
| liquidity_score | missing | 366 | 190 | 176 | 51.91 | 51.7 | 0.21 | high | neutral |
| news_risk_penalty | none | 710 | 367 | 343 | 51.69 | 51.7 | -0.01 | high | neutral |
| score_version | v2_conservative_ranker | 750 | 387 | 363 | 51.6 | 51.7 | -0.1 | high | neutral |
| overextension_penalty | none | 672 | 341 | 331 | 50.74 | 51.7 | -0.96 | high | neutral |
| final_price_signal_score_v2 | score_30_40 | 361 | 180 | 181 | 49.86 | 51.7 | -1.84 | high | neutral |
| candidate_rank | missing | 292 | 159 | 133 | 54.45 | 51.7 | 2.75 | medium | neutral |
| reversal_risk_penalty | low | 112 | 58 | 54 | 51.79 | 51.7 | 0.09 | medium | neutral |
| final_price_signal_score_v2 | score_20_30 | 268 | 138 | 130 | 51.49 | 51.7 | -0.21 | medium | neutral |
| news_risk_penalty | high | 2 | 2 | 0 | 100.0 | 51.7 | 48.3 | insufficient | watch |
| news_risk_penalty | low | 14 | 9 | 5 | 64.29 | 51.7 | 12.59 | insufficient | watch |
| overextension_penalty | medium | 8 | 5 | 3 | 62.5 | 51.7 | 10.8 | insufficient | watch |
| candidate_rank | rank_21_50 | 34 | 19 | 15 | 55.88 | 51.7 | 4.18 | insufficient | watch |
| overextension_penalty | low | 15 | 8 | 7 | 53.33 | 51.7 | 1.63 | insufficient | watch |
| final_price_signal_score_v2 | score_50_plus | 47 | 22 | 25 | 46.81 | 51.7 | -4.89 | insufficient | watch |
| attention_noise_penalty | high | 35 | 16 | 19 | 45.71 | 51.7 | -5.99 | insufficient | watch |
| news_risk_penalty | medium | 24 | 9 | 15 | 37.5 | 51.7 | -14.2 | insufficient | watch |
| attention_noise_penalty | low | 4 | 1 | 3 | 25.0 | 51.7 | -26.7 | insufficient | watch |
| liquidity_score | none | 38 | 2 | 36 | 5.26 | 51.7 | -46.44 | insufficient | watch |
| candidate_rank | rank_11_20 | 2 | 0 | 2 | 0.0 | 51.7 | -51.7 | insufficient | watch |