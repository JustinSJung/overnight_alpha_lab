# Price Candidate Learned Rules Report - 2026-11-05

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261105.csv`
- Baseline evaluated count: **19074**
- Baseline success rate: **48.81%**
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
| overextension_penalty | high | 1143 | 595 | 548 | 52.06 | 48.81 | 3.25 | high | boost | True | boost_on_semantically_risky_bucket | 66 |
| attention_noise_penalty | low | 74 | 40 | 34 | 54.05 | 48.81 | 5.24 | low | boost | False |  | 33 |
| final_price_signal_score_v2 | score_40_50 | 317 | 145 | 172 | 45.74 | 48.81 | -3.07 | high | penalize | False |  | 9 |
| reversal_risk_penalty | low | 1675 | 766 | 909 | 45.73 | 48.81 | -3.08 | high | penalize | False |  | 66 |
| volume_confirmation_score | moderate | 1172 | 527 | 645 | 44.97 | 48.81 | -3.84 | high | penalize | False |  | 66 |
| candidate_rank | rank_11_20 | 447 | 197 | 250 | 44.07 | 48.81 | -4.74 | high | penalize | False |  | 57 |
| overextension_penalty | low | 374 | 164 | 210 | 43.85 | 48.81 | -4.96 | high | penalize | False |  | 63 |
| selected_pick | selected | 1022 | 448 | 574 | 43.84 | 48.81 | -4.97 | high | penalize | False |  | 67 |
| candidate_rank | top_10 | 575 | 251 | 324 | 43.65 | 48.81 | -5.16 | high | penalize | False |  | 67 |
| candidate_rank | rank_21_50 | 618 | 266 | 352 | 43.04 | 48.81 | -5.77 | high | penalize | False |  | 46 |
| final_price_signal_score_v2 | score_50_plus | 1978 | 840 | 1138 | 42.47 | 48.81 | -6.34 | high | penalize | False |  | 66 |
| volume_confirmation_score | none | 2244 | 841 | 1403 | 37.48 | 48.81 | -11.33 | high | penalize | False |  | 66 |
| candidate_rank | rank_51_100 | 579 | 212 | 367 | 36.61 | 48.81 | -12.2 | high | penalize | False |  | 25 |
| liquidity_score | none | 594 | 30 | 564 | 5.05 | 48.81 | -43.76 | high | penalize | False |  | 66 |
| news_risk_penalty | medium | 163 | 73 | 90 | 44.79 | 48.81 | -4.02 | medium | penalize | False |  | 56 |
| news_risk_penalty | high | 292 | 127 | 165 | 43.49 | 48.81 | -5.32 | medium | penalize | False |  | 54 |
| reversal_risk_penalty | high | 928 | 476 | 452 | 51.29 | 48.81 | 2.48 | high | neutral | False |  | 66 |
| candidate_rank | missing | 335 | 171 | 164 | 51.04 | 48.81 | 2.23 | high | neutral | False |  | 6 |
| volume_confirmation_score | negative | 14683 | 7478 | 7205 | 50.93 | 48.81 | 2.12 | high | neutral | False |  | 66 |
| liquidity_score | basic | 15647 | 7928 | 7719 | 50.67 | 48.81 | 1.86 | high | neutral | False |  | 66 |
| final_price_signal_score_v2 | score_30_40 | 11099 | 5618 | 5481 | 50.62 | 48.81 | 1.81 | high | neutral | False |  | 66 |
| reversal_risk_penalty | medium | 1827 | 916 | 911 | 50.14 | 48.81 | 1.33 | high | neutral | False |  | 66 |
| candidate_rank | rank_101_plus | 16520 | 8213 | 8307 | 49.72 | 48.81 | 0.91 | high | neutral | False |  | 66 |
| score_version | legacy_or_unknown | 406 | 201 | 205 | 49.51 | 48.81 | 0.7 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 406 | 201 | 205 | 49.51 | 48.81 | 0.7 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 406 | 201 | 205 | 49.51 | 48.81 | 0.7 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 406 | 201 | 205 | 49.51 | 48.81 | 0.7 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 406 | 201 | 205 | 49.51 | 48.81 | 0.7 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 406 | 201 | 205 | 49.51 | 48.81 | 0.7 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 406 | 201 | 205 | 49.51 | 48.81 | 0.7 | high | neutral | False |  | 7 |
| liquidity_score | missing | 406 | 201 | 205 | 49.51 | 48.81 | 0.7 | high | neutral | False |  | 7 |
| selected_pick | broad_pool | 18052 | 8862 | 9190 | 49.09 | 48.81 | 0.28 | high | neutral | False |  | 73 |
| news_risk_penalty | none | 18196 | 8900 | 9296 | 48.91 | 48.81 | 0.1 | high | neutral | False |  | 66 |
| reversal_risk_penalty | none | 14238 | 6951 | 7287 | 48.82 | 48.81 | 0.01 | high | neutral | False |  | 66 |
| attention_noise_penalty | none | 17777 | 8675 | 9102 | 48.8 | 48.81 | -0.01 | high | neutral | False |  | 66 |
| score_version | v2_conservative_ranker | 18668 | 9109 | 9559 | 48.79 | 48.81 | -0.02 | high | neutral | False |  | 66 |
| overextension_penalty | none | 16877 | 8220 | 8657 | 48.71 | 48.81 | -0.1 | high | neutral | False |  | 66 |
| attention_noise_penalty | high | 791 | 380 | 411 | 48.04 | 48.81 | -0.77 | high | neutral | False |  | 54 |
| final_price_signal_score_v2 | score_20_30 | 4710 | 2239 | 2471 | 47.54 | 48.81 | -1.27 | high | neutral | False |  | 66 |
| liquidity_score | confirmed | 2427 | 1151 | 1276 | 47.42 | 48.81 | -1.39 | high | neutral | False |  | 66 |
| final_price_signal_score_v2 | score_lt_20 | 564 | 267 | 297 | 47.34 | 48.81 | -1.47 | high | neutral | False |  | 65 |
| volume_confirmation_score | high | 569 | 263 | 306 | 46.22 | 48.81 | -2.59 | high | neutral | False |  | 63 |
| overextension_penalty | medium | 274 | 130 | 144 | 47.45 | 48.81 | -1.36 | medium | neutral | False |  | 60 |
| attention_noise_penalty | medium | 26 | 14 | 12 | 53.85 | 48.81 | 5.04 | insufficient | watch | False |  | 17 |
| news_risk_penalty | low | 17 | 9 | 8 | 52.94 | 48.81 | 4.13 | insufficient | watch | False |  | 10 |