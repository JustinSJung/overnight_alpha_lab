# Price Candidate Learned Rules Report - 2026-08-19

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260819.csv`
- Baseline evaluated count: **2711**
- Baseline success rate: **41.9%**
- Total rule rows: **44**
- Boost rules: **17**
- Penalize rules: **9**
- Watch rules: **3**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 358 | 190 | 168 | 53.07 | 41.9 | 11.17 | high | boost | True | boost_on_semantically_risky_bucket | 20 |
| overextension_penalty | high | 312 | 161 | 151 | 51.6 | 41.9 | 9.7 | high | boost | True | boost_on_semantically_risky_bucket | 20 |
| score_version | legacy_or_unknown | 358 | 182 | 176 | 50.84 | 41.9 | 8.94 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 358 | 182 | 176 | 50.84 | 41.9 | 8.94 | high | boost | False |  | 7 |
| overextension_penalty | missing | 358 | 182 | 176 | 50.84 | 41.9 | 8.94 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 358 | 182 | 176 | 50.84 | 41.9 | 8.94 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 358 | 182 | 176 | 50.84 | 41.9 | 8.94 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 358 | 182 | 176 | 50.84 | 41.9 | 8.94 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 358 | 182 | 176 | 50.84 | 41.9 | 8.94 | high | boost | False |  | 7 |
| liquidity_score | missing | 358 | 182 | 176 | 50.84 | 41.9 | 8.94 | high | boost | False |  | 7 |
| selected_pick | selected | 307 | 143 | 164 | 46.58 | 41.9 | 4.68 | high | boost | False |  | 21 |
| liquidity_score | confirmed | 776 | 355 | 421 | 45.75 | 41.9 | 3.85 | high | boost | False |  | 20 |
| news_risk_penalty | medium | 77 | 37 | 40 | 48.05 | 41.9 | 6.15 | low | boost | False |  | 20 |
| candidate_rank | missing | 284 | 151 | 133 | 53.17 | 41.9 | 11.27 | medium | boost | False |  | 6 |
| candidate_rank | top_10 | 194 | 92 | 102 | 47.42 | 41.9 | 5.52 | medium | boost | False |  | 21 |
| volume_confirmation_score | high | 187 | 86 | 101 | 45.99 | 41.9 | 4.09 | medium | boost | False |  | 19 |
| candidate_rank | rank_11_20 | 113 | 51 | 62 | 45.13 | 41.9 | 3.23 | medium | boost | False |  | 12 |
| overextension_penalty | none | 1847 | 714 | 1133 | 38.66 | 41.9 | -3.24 | high | penalize | False |  | 20 |
| final_price_signal_score_v2 | score_20_30 | 624 | 239 | 385 | 38.3 | 41.9 | -3.6 | high | penalize | False |  | 20 |
| reversal_risk_penalty | none | 1216 | 454 | 762 | 37.34 | 41.9 | -4.56 | high | penalize | False |  | 20 |
| candidate_rank | rank_51_100 | 406 | 147 | 259 | 36.21 | 41.9 | -5.69 | high | penalize | False |  | 14 |
| reversal_risk_penalty | low | 337 | 120 | 217 | 35.61 | 41.9 | -6.29 | high | penalize | False |  | 20 |
| volume_confirmation_score | none | 599 | 213 | 386 | 35.56 | 41.9 | -6.34 | high | penalize | False |  | 20 |
| overextension_penalty | medium | 85 | 32 | 53 | 37.65 | 41.9 | -4.25 | low | penalize | False |  | 17 |
| candidate_rank | rank_21_50 | 231 | 84 | 147 | 36.36 | 41.9 | -5.54 | medium | penalize | False |  | 11 |
| liquidity_score | none | 132 | 5 | 127 | 3.79 | 41.9 | -38.11 | medium | penalize | False |  | 20 |
| reversal_risk_penalty | medium | 442 | 190 | 252 | 42.99 | 41.9 | 1.09 | high | neutral | False |  | 20 |
| final_price_signal_score_v2 | score_30_40 | 1024 | 432 | 592 | 42.19 | 41.9 | 0.29 | high | neutral | False |  | 20 |
| volume_confirmation_score | moderate | 382 | 161 | 221 | 42.15 | 41.9 | 0.25 | high | neutral | False |  | 20 |
| volume_confirmation_score | negative | 1185 | 494 | 691 | 41.69 | 41.9 | -0.21 | high | neutral | False |  | 20 |
| selected_pick | broad_pool | 2404 | 993 | 1411 | 41.31 | 41.9 | -0.59 | high | neutral | False |  | 27 |
| candidate_rank | rank_101_plus | 1483 | 611 | 872 | 41.2 | 41.9 | -0.7 | high | neutral | False |  | 20 |
| liquidity_score | basic | 1445 | 594 | 851 | 41.11 | 41.9 | -0.79 | high | neutral | False |  | 20 |
| score_version | v2_conservative_ranker | 2353 | 954 | 1399 | 40.54 | 41.9 | -1.36 | high | neutral | False |  | 20 |
| attention_noise_penalty | none | 2274 | 920 | 1354 | 40.46 | 41.9 | -1.44 | high | neutral | False |  | 20 |
| final_price_signal_score_v2 | score_50_plus | 527 | 213 | 314 | 40.42 | 41.9 | -1.48 | high | neutral | False |  | 20 |
| news_risk_penalty | none | 2170 | 868 | 1302 | 40.0 | 41.9 | -1.9 | high | neutral | False |  | 20 |
| attention_noise_penalty | high | 70 | 31 | 39 | 44.29 | 41.9 | 2.39 | low | neutral | False |  | 15 |
| news_risk_penalty | high | 84 | 36 | 48 | 42.86 | 41.9 | 0.96 | low | neutral | False |  | 10 |
| overextension_penalty | low | 109 | 47 | 62 | 43.12 | 41.9 | 1.22 | medium | neutral | False |  | 18 |
| final_price_signal_score_v2 | score_lt_20 | 178 | 70 | 108 | 39.33 | 41.9 | -2.57 | medium | neutral | False |  | 20 |
| news_risk_penalty | low | 22 | 13 | 9 | 59.09 | 41.9 | 17.19 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | low | 6 | 3 | 3 | 50.0 | 41.9 | 8.1 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 3 | 0 | 3 | 0.0 | 41.9 | -41.9 | insufficient | watch | True | large_lift_with_under_100_cases | 3 |