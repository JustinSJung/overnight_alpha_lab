# Price Candidate Learned Rules Report - 2026-10-27

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261027.csv`
- Baseline evaluated count: **16308**
- Baseline success rate: **49.44%**
- Total rule rows: **45**
- Boost rules: **2**
- Penalize rules: **14**
- Watch rules: **2**
- Suspicious rules: **0**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | low | 68 | 40 | 28 | 58.82 | 49.44 | 9.38 | low | boost | False |  | 29 |
| final_price_signal_score_v2 | score_40_50 | 200 | 106 | 94 | 53.0 | 49.44 | 3.56 | medium | boost | False |  | 8 |
| reversal_risk_penalty | low | 1430 | 658 | 772 | 46.01 | 49.44 | -3.43 | high | penalize | False |  | 61 |
| candidate_rank | rank_11_20 | 417 | 191 | 226 | 45.8 | 49.44 | -3.64 | high | penalize | False |  | 53 |
| final_price_signal_score_v2 | score_lt_20 | 490 | 222 | 268 | 45.31 | 49.44 | -4.13 | high | penalize | False |  | 61 |
| volume_confirmation_score | moderate | 945 | 425 | 520 | 44.97 | 49.44 | -4.47 | high | penalize | False |  | 61 |
| overextension_penalty | low | 337 | 149 | 188 | 44.21 | 49.44 | -5.23 | high | penalize | False |  | 59 |
| selected_pick | selected | 956 | 420 | 536 | 43.93 | 49.44 | -5.51 | high | penalize | False |  | 62 |
| candidate_rank | top_10 | 539 | 229 | 310 | 42.49 | 49.44 | -6.95 | high | penalize | False |  | 62 |
| candidate_rank | rank_21_50 | 575 | 244 | 331 | 42.43 | 49.44 | -7.01 | high | penalize | False |  | 42 |
| final_price_signal_score_v2 | score_50_plus | 1852 | 784 | 1068 | 42.33 | 49.44 | -7.11 | high | penalize | False |  | 61 |
| candidate_rank | rank_51_100 | 556 | 210 | 346 | 37.77 | 49.44 | -11.67 | high | penalize | False |  | 24 |
| volume_confirmation_score | none | 1757 | 644 | 1113 | 36.65 | 49.44 | -12.79 | high | penalize | False |  | 61 |
| liquidity_score | none | 532 | 24 | 508 | 4.51 | 49.44 | -44.93 | high | penalize | False |  | 61 |
| news_risk_penalty | high | 258 | 116 | 142 | 44.96 | 49.44 | -4.48 | medium | penalize | False |  | 49 |
| news_risk_penalty | medium | 153 | 66 | 87 | 43.14 | 49.44 | -6.3 | medium | penalize | False |  | 54 |
| final_price_signal_score_v2 | score_30_40 | 9418 | 4913 | 4505 | 52.17 | 49.44 | 2.73 | high | neutral | False |  | 61 |
| volume_confirmation_score | negative | 12731 | 6573 | 6158 | 51.63 | 49.44 | 2.19 | high | neutral | False |  | 61 |
| liquidity_score | basic | 13422 | 6899 | 6523 | 51.4 | 49.44 | 1.96 | high | neutral | False |  | 61 |
| candidate_rank | missing | 336 | 172 | 164 | 51.19 | 49.44 | 1.75 | high | neutral | False |  | 6 |
| candidate_rank | rank_101_plus | 13885 | 7016 | 6869 | 50.53 | 49.44 | 1.09 | high | neutral | False |  | 61 |
| overextension_penalty | high | 1106 | 556 | 550 | 50.27 | 49.44 | 0.83 | high | neutral | False |  | 61 |
| reversal_risk_penalty | high | 870 | 436 | 434 | 50.11 | 49.44 | 0.67 | high | neutral | False |  | 61 |
| selected_pick | broad_pool | 15352 | 7642 | 7710 | 49.78 | 49.44 | 0.34 | high | neutral | False |  | 68 |
| reversal_risk_penalty | none | 11990 | 5969 | 6021 | 49.78 | 49.44 | 0.34 | high | neutral | False |  | 61 |
| score_version | legacy_or_unknown | 405 | 201 | 204 | 49.63 | 49.44 | 0.19 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 405 | 201 | 204 | 49.63 | 49.44 | 0.19 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 405 | 201 | 204 | 49.63 | 49.44 | 0.19 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 405 | 201 | 204 | 49.63 | 49.44 | 0.19 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 405 | 201 | 204 | 49.63 | 49.44 | 0.19 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 405 | 201 | 204 | 49.63 | 49.44 | 0.19 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 405 | 201 | 204 | 49.63 | 49.44 | 0.19 | high | neutral | False |  | 7 |
| liquidity_score | missing | 405 | 201 | 204 | 49.63 | 49.44 | 0.19 | high | neutral | False |  | 7 |
| news_risk_penalty | none | 15472 | 7668 | 7804 | 49.56 | 49.44 | 0.12 | high | neutral | False |  | 61 |
| overextension_penalty | none | 14209 | 7035 | 7174 | 49.51 | 49.44 | 0.07 | high | neutral | False |  | 61 |
| reversal_risk_penalty | medium | 1613 | 798 | 815 | 49.47 | 49.44 | 0.03 | high | neutral | False |  | 61 |
| attention_noise_penalty | none | 15132 | 7482 | 7650 | 49.44 | 49.44 | 0.0 | high | neutral | False |  | 61 |
| score_version | v2_conservative_ranker | 15903 | 7861 | 8042 | 49.43 | 49.44 | -0.01 | high | neutral | False |  | 61 |
| liquidity_score | confirmed | 1949 | 938 | 1011 | 48.13 | 49.44 | -1.31 | high | neutral | False |  | 61 |
| attention_noise_penalty | high | 679 | 326 | 353 | 48.01 | 49.44 | -1.43 | high | neutral | False |  | 49 |
| volume_confirmation_score | high | 470 | 219 | 251 | 46.6 | 49.44 | -2.84 | high | neutral | False |  | 58 |
| final_price_signal_score_v2 | score_20_30 | 3943 | 1836 | 2107 | 46.56 | 49.44 | -2.88 | high | neutral | False |  | 61 |
| overextension_penalty | medium | 251 | 121 | 130 | 48.21 | 49.44 | -1.23 | medium | neutral | False |  | 57 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 49.44 | 5.56 | insufficient | watch | False |  | 10 |
| attention_noise_penalty | medium | 24 | 13 | 11 | 54.17 | 49.44 | 4.73 | insufficient | watch | False |  | 16 |