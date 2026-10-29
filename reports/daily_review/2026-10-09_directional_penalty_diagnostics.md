# Directional Penalty Diagnostics - 2026-10-09

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1640**
- Overall success rate: **42.26%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 455 | 207 | 248 | 45.49 | ok |
| none | T2_mid | 432 | 177 | 255 | 40.97 | ok |
| none | T3_high | 325 | 140 | 185 | 43.08 | ok |
| low | T1_low | 12 | 5 | 7 | 41.67 | insufficient |
| low | T2_mid | 56 | 24 | 32 | 42.86 | ok |
| low | T3_high | 75 | 32 | 43 | 42.67 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 18 | 10 | 8 | 55.56 | insufficient |
| medium | T3_high | 71 | 35 | 36 | 49.3 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 74 | 32 | 42 | 43.24 | ok |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 455 | 210 | 245 | 46.15 | ok |
| none | T2_mid | 495 | 205 | 290 | 41.41 | ok |
| none | T3_high | 491 | 211 | 280 | 42.97 | ok |
| low | T1_low | 12 | 2 | 10 | 16.67 | insufficient |
| low | T2_mid | 12 | 4 | 8 | 33.33 | insufficient |
| low | T3_high | 27 | 12 | 15 | 44.44 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 10 | 6 | 4 | 60.0 | insufficient |
| medium | T3_high | 21 | 12 | 9 | 57.14 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 2 | 1 | 1 | 50.0 | insufficient |
| high | T3_high | 6 | 4 | 2 | 66.67 | insufficient |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **8166**
- Overall success rate: **47.75%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2551 | 1174 | 1377 | 46.02 | ok |
| none | T2_mid | 2634 | 1253 | 1381 | 47.57 | ok |
| none | T3_high | 1688 | 812 | 876 | 48.1 | ok |
| low | T1_low | 24 | 4 | 20 | 16.67 | ok |
| low | T2_mid | 11 | 8 | 3 | 72.73 | insufficient |
| low | T3_high | 79 | 42 | 37 | 53.16 | ok |
| medium | T1_low | 14 | 5 | 9 | 35.71 | insufficient |
| medium | T2_mid | 10 | 7 | 3 | 70.0 | insufficient |
| medium | T3_high | 86 | 41 | 45 | 47.67 | ok |
| high | T1_low | 48 | 12 | 36 | 25.0 | ok |
| high | T2_mid | 11 | 6 | 5 | 54.55 | insufficient |
| high | T3_high | 706 | 356 | 350 | 50.42 | ok |
| missing | missing | 304 | 179 | 125 | 58.88 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1873 | 846 | 1027 | 45.17 | ok |
| none | T2_mid | 2294 | 1108 | 1186 | 48.3 | ok |
| none | T3_high | 1003 | 470 | 533 | 46.86 | ok |
| low | T1_low | 311 | 135 | 176 | 43.41 | ok |
| low | T2_mid | 171 | 72 | 99 | 42.11 | ok |
| low | T3_high | 425 | 204 | 221 | 48.0 | ok |
| medium | T1_low | 274 | 134 | 140 | 48.91 | ok |
| medium | T2_mid | 134 | 64 | 70 | 47.76 | ok |
| medium | T3_high | 694 | 346 | 348 | 49.86 | ok |
| high | T1_low | 179 | 80 | 99 | 44.69 | ok |
| high | T2_mid | 67 | 30 | 37 | 44.78 | ok |
| high | T3_high | 437 | 231 | 206 | 52.86 | ok |
| missing | missing | 304 | 179 | 125 | 58.88 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.