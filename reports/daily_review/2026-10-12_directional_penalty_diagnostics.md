# Directional Penalty Diagnostics - 2026-10-12

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1783**
- Overall success rate: **41.9%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 489 | 225 | 264 | 46.01 | ok |
| none | T2_mid | 474 | 189 | 285 | 39.87 | ok |
| none | T3_high | 362 | 156 | 206 | 43.09 | ok |
| low | T1_low | 15 | 6 | 9 | 40.0 | insufficient |
| low | T2_mid | 62 | 26 | 36 | 41.94 | ok |
| low | T3_high | 82 | 34 | 48 | 41.46 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 19 | 11 | 8 | 57.89 | insufficient |
| medium | T3_high | 76 | 35 | 41 | 46.05 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 80 | 34 | 46 | 42.5 | ok |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 490 | 229 | 261 | 46.73 | ok |
| none | T2_mid | 540 | 218 | 322 | 40.37 | ok |
| none | T3_high | 537 | 228 | 309 | 42.46 | ok |
| low | T1_low | 12 | 2 | 10 | 16.67 | insufficient |
| low | T2_mid | 14 | 5 | 9 | 35.71 | insufficient |
| low | T3_high | 33 | 13 | 20 | 39.39 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 11 | 6 | 5 | 54.55 | insufficient |
| medium | T3_high | 22 | 12 | 10 | 54.55 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **8797**
- Overall success rate: **48.39%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2732 | 1276 | 1456 | 46.71 | ok |
| none | T2_mid | 2779 | 1339 | 1440 | 48.18 | ok |
| none | T3_high | 1898 | 926 | 972 | 48.79 | ok |
| low | T1_low | 28 | 5 | 23 | 17.86 | ok |
| low | T2_mid | 14 | 8 | 6 | 57.14 | insufficient |
| low | T3_high | 83 | 44 | 39 | 53.01 | ok |
| medium | T1_low | 17 | 7 | 10 | 41.18 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 89 | 43 | 46 | 48.31 | ok |
| high | T1_low | 51 | 13 | 38 | 25.49 | ok |
| high | T2_mid | 14 | 9 | 5 | 64.29 | insufficient |
| high | T3_high | 769 | 398 | 371 | 51.76 | ok |
| missing | missing | 311 | 182 | 129 | 58.52 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1995 | 926 | 1069 | 46.42 | ok |
| none | T2_mid | 2419 | 1188 | 1231 | 49.11 | ok |
| none | T3_high | 1130 | 546 | 584 | 48.32 | ok |
| low | T1_low | 341 | 144 | 197 | 42.23 | ok |
| low | T2_mid | 179 | 68 | 111 | 37.99 | ok |
| low | T3_high | 467 | 224 | 243 | 47.97 | ok |
| medium | T1_low | 302 | 144 | 158 | 47.68 | ok |
| medium | T2_mid | 150 | 76 | 74 | 50.67 | ok |
| medium | T3_high | 773 | 387 | 386 | 50.06 | ok |
| high | T1_low | 190 | 87 | 103 | 45.79 | ok |
| high | T2_mid | 71 | 31 | 40 | 43.66 | ok |
| high | T3_high | 469 | 254 | 215 | 54.16 | ok |
| missing | missing | 311 | 182 | 129 | 58.52 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.