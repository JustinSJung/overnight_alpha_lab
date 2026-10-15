# Directional Penalty Diagnostics - 2026-10-15

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1837**
- Overall success rate: **40.99%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 519 | 229 | 290 | 44.12 | ok |
| none | T2_mid | 489 | 193 | 296 | 39.47 | ok |
| none | T3_high | 367 | 157 | 210 | 42.78 | ok |
| low | T1_low | 16 | 6 | 10 | 37.5 | insufficient |
| low | T2_mid | 66 | 27 | 39 | 40.91 | ok |
| low | T3_high | 81 | 33 | 48 | 40.74 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 19 | 10 | 9 | 52.63 | insufficient |
| medium | T3_high | 76 | 34 | 42 | 44.74 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 81 | 33 | 48 | 40.74 | ok |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 522 | 233 | 289 | 44.64 | ok |
| none | T2_mid | 558 | 221 | 337 | 39.61 | ok |
| none | T3_high | 544 | 229 | 315 | 42.1 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 14 | 5 | 9 | 35.71 | insufficient |
| low | T3_high | 32 | 11 | 21 | 34.38 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 21 | 11 | 10 | 52.38 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **9823**
- Overall success rate: **51.62%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2946 | 1523 | 1423 | 51.7 | ok |
| none | T2_mid | 3249 | 1663 | 1586 | 51.18 | ok |
| none | T3_high | 2274 | 1187 | 1087 | 52.2 | ok |
| low | T1_low | 25 | 5 | 20 | 20.0 | ok |
| low | T2_mid | 16 | 7 | 9 | 43.75 | insufficient |
| low | T3_high | 89 | 49 | 40 | 55.06 | ok |
| medium | T1_low | 8 | 4 | 4 | 50.0 | insufficient |
| medium | T2_mid | 16 | 6 | 10 | 37.5 | insufficient |
| medium | T3_high | 86 | 43 | 43 | 50.0 | ok |
| high | T1_low | 40 | 9 | 31 | 22.5 | ok |
| high | T2_mid | 17 | 11 | 6 | 64.71 | insufficient |
| high | T3_high | 756 | 388 | 368 | 51.32 | ok |
| missing | missing | 301 | 176 | 125 | 58.47 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2283 | 1207 | 1076 | 52.87 | ok |
| none | T2_mid | 2847 | 1481 | 1366 | 52.02 | ok |
| none | T3_high | 1463 | 768 | 695 | 52.49 | ok |
| low | T1_low | 324 | 140 | 184 | 43.21 | ok |
| low | T2_mid | 195 | 81 | 114 | 41.54 | ok |
| low | T3_high | 504 | 251 | 253 | 49.8 | ok |
| medium | T1_low | 251 | 118 | 133 | 47.01 | ok |
| medium | T2_mid | 187 | 90 | 97 | 48.13 | ok |
| medium | T3_high | 798 | 419 | 379 | 52.51 | ok |
| high | T1_low | 161 | 76 | 85 | 47.2 | ok |
| high | T2_mid | 69 | 35 | 34 | 50.72 | ok |
| high | T3_high | 440 | 229 | 211 | 52.05 | ok |
| missing | missing | 301 | 176 | 125 | 58.47 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.