# Directional Penalty Diagnostics - 2026-10-14

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1779**
- Overall success rate: **41.77%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 499 | 227 | 272 | 45.49 | ok |
| none | T2_mid | 467 | 180 | 287 | 38.54 | ok |
| none | T3_high | 361 | 161 | 200 | 44.6 | ok |
| low | T1_low | 15 | 6 | 9 | 40.0 | insufficient |
| low | T2_mid | 66 | 28 | 38 | 42.42 | ok |
| low | T3_high | 78 | 32 | 46 | 41.03 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 19 | 10 | 9 | 52.63 | insufficient |
| medium | T3_high | 76 | 35 | 41 | 46.05 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 12 | 5 | 7 | 41.67 | insufficient |
| high | T3_high | 81 | 33 | 48 | 40.74 | ok |
| missing | missing | 99 | 24 | 75 | 24.24 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 500 | 231 | 269 | 46.2 | ok |
| none | T2_mid | 535 | 209 | 326 | 39.07 | ok |
| none | T3_high | 536 | 233 | 303 | 43.47 | ok |
| low | T1_low | 12 | 2 | 10 | 16.67 | insufficient |
| low | T2_mid | 14 | 5 | 9 | 35.71 | insufficient |
| low | T3_high | 31 | 10 | 21 | 32.26 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 21 | 12 | 9 | 57.14 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 99 | 24 | 75 | 24.24 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **9367**
- Overall success rate: **49.28%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2884 | 1379 | 1505 | 47.82 | ok |
| none | T2_mid | 3030 | 1482 | 1548 | 48.91 | ok |
| none | T3_high | 2076 | 1049 | 1027 | 50.53 | ok |
| low | T1_low | 25 | 5 | 20 | 20.0 | ok |
| low | T2_mid | 16 | 7 | 9 | 43.75 | insufficient |
| low | T3_high | 82 | 44 | 38 | 53.66 | ok |
| medium | T1_low | 16 | 7 | 9 | 43.75 | insufficient |
| medium | T2_mid | 13 | 6 | 7 | 46.15 | insufficient |
| medium | T3_high | 93 | 48 | 45 | 51.61 | ok |
| high | T1_low | 45 | 10 | 35 | 22.22 | ok |
| high | T2_mid | 14 | 9 | 5 | 64.29 | insufficient |
| high | T3_high | 778 | 398 | 380 | 51.16 | ok |
| missing | missing | 295 | 172 | 123 | 58.31 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2213 | 1062 | 1151 | 47.99 | ok |
| none | T2_mid | 2647 | 1319 | 1328 | 49.83 | ok |
| none | T3_high | 1315 | 668 | 647 | 50.8 | ok |
| low | T1_low | 327 | 139 | 188 | 42.51 | ok |
| low | T2_mid | 184 | 74 | 110 | 40.22 | ok |
| low | T3_high | 478 | 232 | 246 | 48.54 | ok |
| medium | T1_low | 272 | 130 | 142 | 47.79 | ok |
| medium | T2_mid | 166 | 77 | 89 | 46.39 | ok |
| medium | T3_high | 778 | 395 | 383 | 50.77 | ok |
| high | T1_low | 158 | 70 | 88 | 44.3 | ok |
| high | T2_mid | 76 | 34 | 42 | 44.74 | ok |
| high | T3_high | 458 | 244 | 214 | 53.28 | ok |
| missing | missing | 295 | 172 | 123 | 58.31 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.