# Directional Penalty Diagnostics - 2026-11-13

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2404**
- Overall success rate: **42.55%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 689 | 307 | 382 | 44.56 | ok |
| none | T2_mid | 663 | 286 | 377 | 43.14 | ok |
| none | T3_high | 506 | 213 | 293 | 42.09 | ok |
| low | T1_low | 19 | 7 | 12 | 36.84 | insufficient |
| low | T2_mid | 71 | 30 | 41 | 42.25 | ok |
| low | T3_high | 107 | 45 | 62 | 42.06 | ok |
| medium | T1_low | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T2_mid | 27 | 14 | 13 | 51.85 | ok |
| medium | T3_high | 97 | 43 | 54 | 44.33 | ok |
| high | T1_low | 3 | 2 | 1 | 66.67 | insufficient |
| high | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| high | T3_high | 99 | 41 | 58 | 41.41 | ok |
| missing | missing | 102 | 24 | 78 | 23.53 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 693 | 313 | 380 | 45.17 | ok |
| none | T2_mid | 737 | 319 | 418 | 43.28 | ok |
| none | T3_high | 728 | 307 | 421 | 42.17 | ok |
| low | T1_low | 13 | 3 | 10 | 23.08 | insufficient |
| low | T2_mid | 19 | 7 | 12 | 36.84 | insufficient |
| low | T3_high | 45 | 15 | 30 | 33.33 | ok |
| medium | T1_low | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| medium | T3_high | 24 | 13 | 11 | 54.17 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 5 | 4 | 1 | 80.0 | insufficient |
| high | T3_high | 12 | 7 | 5 | 58.33 | insufficient |
| missing | missing | 102 | 24 | 78 | 23.53 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **20522**
- Overall success rate: **50.24%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 6737 | 3272 | 3465 | 48.57 | ok |
| none | T2_mid | 6600 | 3279 | 3321 | 49.68 | ok |
| none | T3_high | 5405 | 2813 | 2592 | 52.04 | ok |
| low | T1_low | 65 | 27 | 38 | 41.54 | ok |
| low | T2_mid | 53 | 27 | 26 | 50.94 | ok |
| low | T3_high | 123 | 73 | 50 | 59.35 | ok |
| medium | T1_low | 26 | 13 | 13 | 50.0 | ok |
| medium | T2_mid | 32 | 12 | 20 | 37.5 | ok |
| medium | T3_high | 130 | 72 | 58 | 55.38 | ok |
| high | T1_low | 40 | 12 | 28 | 30.0 | ok |
| high | T2_mid | 30 | 15 | 15 | 50.0 | ok |
| high | T3_high | 990 | 526 | 464 | 53.13 | ok |
| missing | missing | 291 | 169 | 122 | 58.08 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5535 | 2711 | 2824 | 48.98 | ok |
| none | T2_mid | 5765 | 2924 | 2841 | 50.72 | ok |
| none | T3_high | 3969 | 2099 | 1870 | 52.88 | ok |
| low | T1_low | 738 | 333 | 405 | 45.12 | ok |
| low | T2_mid | 420 | 196 | 224 | 46.67 | ok |
| low | T3_high | 856 | 428 | 428 | 50.0 | ok |
| medium | T1_low | 429 | 201 | 228 | 46.85 | ok |
| medium | T2_mid | 415 | 171 | 244 | 41.2 | ok |
| medium | T3_high | 1187 | 611 | 576 | 51.47 | ok |
| high | T1_low | 166 | 79 | 87 | 47.59 | ok |
| high | T2_mid | 115 | 42 | 73 | 36.52 | ok |
| high | T3_high | 636 | 346 | 290 | 54.4 | ok |
| missing | missing | 291 | 169 | 122 | 58.08 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.