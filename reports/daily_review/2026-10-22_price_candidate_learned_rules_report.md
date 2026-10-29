# Price Candidate Learned Rules Report - 2026-10-22

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261022.csv`
- Baseline evaluated count: **14562**
- Baseline success rate: **48.2%**
- Total rule rows: **45**
- Boost rules: **2**
- Penalize rules: **14**
- Watch rules: **2**
- Suspicious rules: **1**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | low | 61 | 37 | 24 | 60.66 | 48.2 | 12.46 | low | boost | True | large_lift_with_under_100_cases | 27 |
| final_price_signal_score_v2 | score_40_50 | 204 | 107 | 97 | 52.45 | 48.2 | 4.25 | medium | boost | False |  | 8 |
| volume_confirmation_score | moderate | 915 | 413 | 502 | 45.14 | 48.2 | -3.06 | high | penalize | False |  | 58 |
| reversal_risk_penalty | low | 1291 | 578 | 713 | 44.77 | 48.2 | -3.43 | high | penalize | False |  | 58 |
| candidate_rank | rank_11_20 | 414 | 185 | 229 | 44.69 | 48.2 | -3.51 | high | penalize | False |  | 51 |
| selected_pick | selected | 929 | 407 | 522 | 43.81 | 48.2 | -4.39 | high | penalize | False |  | 59 |
| overextension_penalty | low | 325 | 142 | 183 | 43.69 | 48.2 | -4.51 | high | penalize | False |  | 56 |
| final_price_signal_score_v2 | score_lt_20 | 428 | 185 | 243 | 43.22 | 48.2 | -4.98 | high | penalize | False |  | 58 |
| candidate_rank | rank_21_50 | 582 | 251 | 331 | 43.13 | 48.2 | -5.07 | high | penalize | False |  | 41 |
| candidate_rank | top_10 | 515 | 222 | 293 | 43.11 | 48.2 | -5.09 | high | penalize | False |  | 59 |
| final_price_signal_score_v2 | score_50_plus | 1838 | 782 | 1056 | 42.55 | 48.2 | -5.65 | high | penalize | False |  | 58 |
| candidate_rank | rank_51_100 | 565 | 213 | 352 | 37.7 | 48.2 | -10.5 | high | penalize | False |  | 24 |
| volume_confirmation_score | none | 1667 | 608 | 1059 | 36.47 | 48.2 | -11.73 | high | penalize | False |  | 58 |
| liquidity_score | none | 482 | 22 | 460 | 4.56 | 48.2 | -43.64 | high | penalize | False |  | 58 |
| news_risk_penalty | high | 257 | 114 | 143 | 44.36 | 48.2 | -3.84 | medium | penalize | False |  | 46 |
| news_risk_penalty | medium | 148 | 64 | 84 | 43.24 | 48.2 | -4.96 | medium | penalize | False |  | 51 |
| candidate_rank | missing | 336 | 172 | 164 | 51.19 | 48.2 | 2.99 | high | neutral | False |  | 6 |
| final_price_signal_score_v2 | score_30_40 | 8399 | 4241 | 4158 | 50.49 | 48.2 | 2.29 | high | neutral | False |  | 58 |
| volume_confirmation_score | negative | 11110 | 5579 | 5531 | 50.22 | 48.2 | 2.02 | high | neutral | False |  | 58 |
| liquidity_score | basic | 11788 | 5890 | 5898 | 49.97 | 48.2 | 1.77 | high | neutral | False |  | 58 |
| overextension_penalty | high | 1020 | 509 | 511 | 49.9 | 48.2 | 1.7 | high | neutral | False |  | 58 |
| reversal_risk_penalty | high | 742 | 369 | 373 | 49.73 | 48.2 | 1.53 | high | neutral | False |  | 58 |
| reversal_risk_penalty | medium | 1482 | 732 | 750 | 49.39 | 48.2 | 1.19 | high | neutral | False |  | 58 |
| score_version | legacy_or_unknown | 407 | 201 | 206 | 49.39 | 48.2 | 1.19 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 407 | 201 | 206 | 49.39 | 48.2 | 1.19 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 407 | 201 | 206 | 49.39 | 48.2 | 1.19 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 407 | 201 | 206 | 49.39 | 48.2 | 1.19 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 407 | 201 | 206 | 49.39 | 48.2 | 1.19 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 407 | 201 | 206 | 49.39 | 48.2 | 1.19 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 407 | 201 | 206 | 49.39 | 48.2 | 1.19 | high | neutral | False |  | 7 |
| liquidity_score | missing | 407 | 201 | 206 | 49.39 | 48.2 | 1.19 | high | neutral | False |  | 7 |
| candidate_rank | rank_101_plus | 12150 | 5976 | 6174 | 49.19 | 48.2 | 0.99 | high | neutral | False |  | 58 |
| selected_pick | broad_pool | 13633 | 6612 | 7021 | 48.5 | 48.2 | 0.3 | high | neutral | False |  | 65 |
| reversal_risk_penalty | none | 10640 | 5139 | 5501 | 48.3 | 48.2 | 0.1 | high | neutral | False |  | 58 |
| news_risk_penalty | none | 13731 | 6629 | 7102 | 48.28 | 48.2 | 0.08 | high | neutral | False |  | 58 |
| attention_noise_penalty | none | 13471 | 6490 | 6981 | 48.18 | 48.2 | -0.02 | high | neutral | False |  | 58 |
| score_version | v2_conservative_ranker | 14155 | 6818 | 7337 | 48.17 | 48.2 | -0.03 | high | neutral | False |  | 58 |
| overextension_penalty | none | 12575 | 6055 | 6520 | 48.15 | 48.2 | -0.05 | high | neutral | False |  | 58 |
| liquidity_score | confirmed | 1885 | 906 | 979 | 48.06 | 48.2 | -0.14 | high | neutral | False |  | 58 |
| volume_confirmation_score | high | 463 | 218 | 245 | 47.08 | 48.2 | -1.12 | high | neutral | False |  | 55 |
| attention_noise_penalty | high | 604 | 281 | 323 | 46.52 | 48.2 | -1.68 | high | neutral | False |  | 46 |
| final_price_signal_score_v2 | score_20_30 | 3286 | 1503 | 1783 | 45.74 | 48.2 | -2.46 | high | neutral | False |  | 58 |
| overextension_penalty | medium | 235 | 112 | 123 | 47.66 | 48.2 | -0.54 | medium | neutral | False |  | 54 |
| news_risk_penalty | low | 19 | 11 | 8 | 57.89 | 48.2 | 9.69 | insufficient | watch | False |  | 10 |
| attention_noise_penalty | medium | 19 | 10 | 9 | 52.63 | 48.2 | 4.43 | insufficient | watch | False |  | 13 |