# Directional Penalty Diagnostics - 2026-11-27

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2964**
- Overall success rate: **41.94%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 883 | 382 | 501 | 43.26 | ok |
| none | T2_mid | 839 | 353 | 486 | 42.07 | ok |
| none | T3_high | 613 | 259 | 354 | 42.25 | ok |
| low | T1_low | 31 | 11 | 20 | 35.48 | ok |
| low | T2_mid | 88 | 33 | 55 | 37.5 | ok |
| low | T3_high | 142 | 62 | 80 | 43.66 | ok |
| medium | T1_low | 8 | 4 | 4 | 50.0 | insufficient |
| medium | T2_mid | 33 | 15 | 18 | 45.45 | ok |
| medium | T3_high | 116 | 47 | 69 | 40.52 | ok |
| high | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| high | T2_mid | 16 | 8 | 8 | 50.0 | insufficient |
| high | T3_high | 121 | 48 | 73 | 39.67 | ok |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 889 | 387 | 502 | 43.53 | ok |
| none | T2_mid | 925 | 390 | 535 | 42.16 | ok |
| none | T3_high | 878 | 364 | 514 | 41.46 | ok |
| low | T1_low | 25 | 8 | 17 | 32.0 | ok |
| low | T2_mid | 27 | 8 | 19 | 29.63 | ok |
| low | T3_high | 69 | 25 | 44 | 36.23 | ok |
| medium | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| medium | T2_mid | 21 | 9 | 12 | 42.86 | ok |
| medium | T3_high | 30 | 18 | 12 | 60.0 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 15 | 9 | 6 | 60.0 | insufficient |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **26101**
- Overall success rate: **51.55%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 8488 | 4290 | 4198 | 50.54 | ok |
| none | T2_mid | 8456 | 4352 | 4104 | 51.47 | ok |
| none | T3_high | 7139 | 3731 | 3408 | 52.26 | ok |
| low | T1_low | 74 | 33 | 41 | 44.59 | ok |
| low | T2_mid | 81 | 45 | 36 | 55.56 | ok |
| low | T3_high | 165 | 94 | 71 | 56.97 | ok |
| medium | T1_low | 36 | 17 | 19 | 47.22 | ok |
| medium | T2_mid | 50 | 24 | 26 | 48.0 | ok |
| medium | T3_high | 165 | 88 | 77 | 53.33 | ok |
| high | T1_low | 37 | 14 | 23 | 37.84 | ok |
| high | T2_mid | 66 | 25 | 41 | 37.88 | ok |
| high | T3_high | 1155 | 631 | 524 | 54.63 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 6944 | 3520 | 3424 | 50.69 | ok |
| none | T2_mid | 7166 | 3752 | 3414 | 52.36 | ok |
| none | T3_high | 5354 | 2826 | 2528 | 52.78 | ok |
| low | T1_low | 988 | 496 | 492 | 50.2 | ok |
| low | T2_mid | 600 | 281 | 319 | 46.83 | ok |
| low | T3_high | 1106 | 567 | 539 | 51.27 | ok |
| medium | T1_low | 547 | 274 | 273 | 50.09 | ok |
| medium | T2_mid | 663 | 316 | 347 | 47.66 | ok |
| medium | T3_high | 1375 | 719 | 656 | 52.29 | ok |
| high | T1_low | 156 | 64 | 92 | 41.03 | ok |
| high | T2_mid | 224 | 97 | 127 | 43.3 | ok |
| high | T3_high | 789 | 432 | 357 | 54.75 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.