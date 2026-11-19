# Price Candidate Learned Rules Report - 2026-11-19

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261119.csv`
- Baseline evaluated count: **25329**
- Baseline success rate: **49.97%**
- Total rule rows: **45**
- Boost rules: **0**
- Penalize rules: **15**
- Watch rules: **2**
- Suspicious rules: **1**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | high | 985 | 460 | 525 | 46.7 | 49.97 | -3.27 | high | penalize | False |  | 64 |
| overextension_penalty | low | 513 | 238 | 275 | 46.39 | 49.97 | -3.58 | high | penalize | False |  | 74 |
| volume_confirmation_score | moderate | 2296 | 1061 | 1235 | 46.21 | 49.97 | -3.76 | high | penalize | False |  | 76 |
| final_price_signal_score_v2 | score_40_50 | 308 | 140 | 168 | 45.45 | 49.97 | -4.52 | high | penalize | False |  | 9 |
| candidate_rank | rank_11_20 | 542 | 238 | 304 | 43.91 | 49.97 | -6.06 | high | penalize | False |  | 67 |
| news_risk_penalty | high | 364 | 159 | 205 | 43.68 | 49.97 | -6.29 | high | penalize | False |  | 63 |
| volume_confirmation_score | high | 1006 | 439 | 567 | 43.64 | 49.97 | -6.33 | high | penalize | False |  | 72 |
| selected_pick | selected | 1219 | 526 | 693 | 43.15 | 49.97 | -6.82 | high | penalize | False |  | 76 |
| volume_confirmation_score | none | 3771 | 1626 | 2145 | 43.12 | 49.97 | -6.85 | high | penalize | False |  | 76 |
| candidate_rank | top_10 | 677 | 288 | 389 | 42.54 | 49.97 | -7.43 | high | penalize | False |  | 75 |
| candidate_rank | rank_21_50 | 886 | 373 | 513 | 42.1 | 49.97 | -7.87 | high | penalize | False |  | 54 |
| final_price_signal_score_v2 | score_50_plus | 2675 | 1116 | 1559 | 41.72 | 49.97 | -8.25 | high | penalize | False |  | 76 |
| candidate_rank | rank_51_100 | 734 | 271 | 463 | 36.92 | 49.97 | -13.05 | high | penalize | False |  | 33 |
| liquidity_score | none | 667 | 41 | 626 | 6.15 | 49.97 | -43.82 | high | penalize | False |  | 75 |
| news_risk_penalty | medium | 207 | 89 | 118 | 43.0 | 49.97 | -6.97 | medium | penalize | False |  | 68 |
| reversal_risk_penalty | high | 1135 | 597 | 538 | 52.6 | 49.97 | 2.63 | high | neutral | False |  | 76 |
| volume_confirmation_score | negative | 17997 | 9400 | 8597 | 52.23 | 49.97 | 2.26 | high | neutral | False |  | 76 |
| overextension_penalty | high | 1387 | 724 | 663 | 52.2 | 49.97 | 2.23 | high | neutral | False |  | 76 |
| liquidity_score | basic | 19880 | 10329 | 9551 | 51.96 | 49.97 | 1.99 | high | neutral | False |  | 76 |
| final_price_signal_score_v2 | score_30_40 | 14475 | 7506 | 6969 | 51.85 | 49.97 | 1.88 | high | neutral | False |  | 76 |
| candidate_rank | rank_101_plus | 22231 | 11356 | 10875 | 51.08 | 49.97 | 1.11 | high | neutral | False |  | 76 |
| selected_pick | broad_pool | 24110 | 12131 | 11979 | 50.32 | 49.97 | 0.35 | high | neutral | False |  | 81 |
| reversal_risk_penalty | medium | 2386 | 1197 | 1189 | 50.17 | 49.97 | 0.2 | high | neutral | False |  | 76 |
| news_risk_penalty | none | 24479 | 12267 | 12212 | 50.11 | 49.97 | 0.14 | high | neutral | False |  | 76 |
| attention_noise_penalty | none | 23946 | 11992 | 11954 | 50.08 | 49.97 | 0.11 | high | neutral | False |  | 76 |
| reversal_risk_penalty | none | 19166 | 9591 | 9575 | 50.04 | 49.97 | 0.07 | high | neutral | False |  | 76 |
| score_version | v2_conservative_ranker | 25070 | 12526 | 12544 | 49.96 | 49.97 | -0.01 | high | neutral | False |  | 76 |
| overextension_penalty | none | 22801 | 11382 | 11419 | 49.92 | 49.97 | -0.05 | high | neutral | False |  | 76 |
| final_price_signal_score_v2 | score_20_30 | 6836 | 3393 | 3443 | 49.63 | 49.97 | -0.34 | high | neutral | False |  | 76 |
| overextension_penalty | medium | 369 | 182 | 187 | 49.32 | 49.97 | -0.65 | high | neutral | False |  | 70 |
| reversal_risk_penalty | low | 2383 | 1141 | 1242 | 47.88 | 49.97 | -2.09 | high | neutral | False |  | 76 |
| final_price_signal_score_v2 | score_lt_20 | 776 | 371 | 405 | 47.81 | 49.97 | -2.16 | high | neutral | False |  | 76 |
| liquidity_score | confirmed | 4523 | 2156 | 2367 | 47.67 | 49.97 | -2.3 | high | neutral | False |  | 76 |
| score_version | legacy_or_unknown | 259 | 131 | 128 | 50.58 | 49.97 | 0.61 | medium | neutral | False |  | 5 |
| candidate_rank | missing | 259 | 131 | 128 | 50.58 | 49.97 | 0.61 | medium | neutral | False |  | 5 |
| final_price_signal_score_v2 | missing | 259 | 131 | 128 | 50.58 | 49.97 | 0.61 | medium | neutral | False |  | 5 |
| overextension_penalty | missing | 259 | 131 | 128 | 50.58 | 49.97 | 0.61 | medium | neutral | False |  | 5 |
| reversal_risk_penalty | missing | 259 | 131 | 128 | 50.58 | 49.97 | 0.61 | medium | neutral | False |  | 5 |
| news_risk_penalty | missing | 259 | 131 | 128 | 50.58 | 49.97 | 0.61 | medium | neutral | False |  | 5 |
| attention_noise_penalty | missing | 259 | 131 | 128 | 50.58 | 49.97 | 0.61 | medium | neutral | False |  | 5 |
| volume_confirmation_score | missing | 259 | 131 | 128 | 50.58 | 49.97 | 0.61 | medium | neutral | False |  | 5 |
| liquidity_score | missing | 259 | 131 | 128 | 50.58 | 49.97 | 0.61 | medium | neutral | False |  | 5 |
| attention_noise_penalty | low | 104 | 52 | 52 | 50.0 | 49.97 | 0.03 | medium | neutral | False |  | 43 |
| attention_noise_penalty | medium | 35 | 22 | 13 | 62.86 | 49.97 | 12.89 | insufficient | watch | True | large_lift_with_under_100_cases | 23 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 49.97 | 5.03 | insufficient | watch | False |  | 10 |