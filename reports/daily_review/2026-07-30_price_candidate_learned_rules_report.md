# Price Candidate Learned Rules Report - 2026-07-30

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260730.csv`
- Baseline evaluated count: **1116**
- Baseline success rate: **52.69%**
- Total rule rows: **43**
- Boost rules: **7**
- Penalize rules: **5**
- Watch rules: **11**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action |
|---|---|---|---|---|---|---|---|---|---|
| candidate_rank | rank_101_plus | 441 | 263 | 178 | 59.64 | 52.69 | 6.95 | high | boost |
| final_price_signal_score_v2 | score_lt_20 | 74 | 47 | 27 | 63.51 | 52.69 | 10.82 | low | boost |
| volume_confirmation_score | high | 52 | 32 | 20 | 61.54 | 52.69 | 8.85 | low | boost |
| overextension_penalty | high | 55 | 32 | 23 | 58.18 | 52.69 | 5.49 | low | boost |
| reversal_risk_penalty | medium | 144 | 89 | 55 | 61.81 | 52.69 | 9.12 | medium | boost |
| liquidity_score | confirmed | 218 | 131 | 87 | 60.09 | 52.69 | 7.4 | medium | boost |
| reversal_risk_penalty | high | 119 | 70 | 49 | 58.82 | 52.69 | 6.13 | medium | boost |
| reversal_risk_penalty | none | 375 | 180 | 195 | 48.0 | 52.69 | -4.69 | high | penalize |
| candidate_rank | top_10 | 50 | 23 | 27 | 46.0 | 52.69 | -6.69 | low | penalize |
| selected_pick | selected | 52 | 23 | 29 | 44.23 | 52.69 | -8.46 | low | penalize |
| volume_confirmation_score | none | 170 | 80 | 90 | 47.06 | 52.69 | -5.63 | medium | penalize |
| candidate_rank | rank_51_100 | 297 | 124 | 173 | 41.75 | 52.69 | -10.94 | medium | penalize |
| volume_confirmation_score | negative | 427 | 231 | 196 | 54.1 | 52.69 | 1.41 | high | neutral |
| liquidity_score | basic | 494 | 265 | 229 | 53.64 | 52.69 | 0.95 | high | neutral |
| attention_noise_penalty | none | 711 | 381 | 330 | 53.59 | 52.69 | 0.9 | high | neutral |
| news_risk_penalty | none | 710 | 378 | 332 | 53.24 | 52.69 | 0.55 | high | neutral |
| selected_pick | broad_pool | 1064 | 565 | 499 | 53.1 | 52.69 | 0.41 | high | neutral |
| score_version | v2_conservative_ranker | 750 | 398 | 352 | 53.07 | 52.69 | 0.38 | high | neutral |
| overextension_penalty | none | 672 | 353 | 319 | 52.53 | 52.69 | -0.16 | high | neutral |
| score_version | legacy_or_unknown | 366 | 190 | 176 | 51.91 | 52.69 | -0.78 | high | neutral |
| final_price_signal_score_v2 | missing | 366 | 190 | 176 | 51.91 | 52.69 | -0.78 | high | neutral |
| overextension_penalty | missing | 366 | 190 | 176 | 51.91 | 52.69 | -0.78 | high | neutral |
| reversal_risk_penalty | missing | 366 | 190 | 176 | 51.91 | 52.69 | -0.78 | high | neutral |
| news_risk_penalty | missing | 366 | 190 | 176 | 51.91 | 52.69 | -0.78 | high | neutral |
| attention_noise_penalty | missing | 366 | 190 | 176 | 51.91 | 52.69 | -0.78 | high | neutral |
| volume_confirmation_score | missing | 366 | 190 | 176 | 51.91 | 52.69 | -0.78 | high | neutral |
| liquidity_score | missing | 366 | 190 | 176 | 51.91 | 52.69 | -0.78 | high | neutral |
| final_price_signal_score_v2 | score_30_40 | 361 | 187 | 174 | 51.8 | 52.69 | -0.89 | high | neutral |
| volume_confirmation_score | moderate | 101 | 55 | 46 | 54.46 | 52.69 | 1.77 | medium | neutral |
| candidate_rank | missing | 292 | 159 | 133 | 54.45 | 52.69 | 1.76 | medium | neutral |
| final_price_signal_score_v2 | score_20_30 | 268 | 143 | 125 | 53.36 | 52.69 | 0.67 | medium | neutral |
| reversal_risk_penalty | low | 112 | 59 | 53 | 52.68 | 52.69 | -0.01 | medium | neutral |
| news_risk_penalty | high | 2 | 2 | 0 | 100.0 | 52.69 | 47.31 | insufficient | watch |
| news_risk_penalty | low | 14 | 9 | 5 | 64.29 | 52.69 | 11.6 | insufficient | watch |
| overextension_penalty | medium | 8 | 5 | 3 | 62.5 | 52.69 | 9.81 | insufficient | watch |
| candidate_rank | rank_21_50 | 34 | 19 | 15 | 55.88 | 52.69 | 3.19 | insufficient | watch |
| overextension_penalty | low | 15 | 8 | 7 | 53.33 | 52.69 | 0.64 | insufficient | watch |
| attention_noise_penalty | high | 35 | 16 | 19 | 45.71 | 52.69 | -6.98 | insufficient | watch |
| final_price_signal_score_v2 | score_50_plus | 47 | 21 | 26 | 44.68 | 52.69 | -8.01 | insufficient | watch |
| news_risk_penalty | medium | 24 | 9 | 15 | 37.5 | 52.69 | -15.19 | insufficient | watch |
| attention_noise_penalty | low | 4 | 1 | 3 | 25.0 | 52.69 | -27.69 | insufficient | watch |
| liquidity_score | none | 38 | 2 | 36 | 5.26 | 52.69 | -47.43 | insufficient | watch |
| candidate_rank | rank_11_20 | 2 | 0 | 2 | 0.0 | 52.69 | -52.69 | insufficient | watch |