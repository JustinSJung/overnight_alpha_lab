# Directional Penalty Diagnostics - 2026-11-06

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2055**
- Overall success rate: **41.85%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 566 | 249 | 317 | 43.99 | ok |
| none | T2_mid | 574 | 230 | 344 | 40.07 | ok |
| none | T3_high | 419 | 186 | 233 | 44.39 | ok |
| low | T1_low | 18 | 7 | 11 | 38.89 | insufficient |
| low | T2_mid | 68 | 28 | 40 | 41.18 | ok |
| low | T3_high | 87 | 37 | 50 | 42.53 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 22 | 13 | 9 | 59.09 | ok |
| medium | T3_high | 87 | 38 | 49 | 43.68 | ok |
| high | T1_low | 3 | 2 | 1 | 66.67 | insufficient |
| high | T2_mid | 13 | 6 | 7 | 46.15 | insufficient |
| high | T3_high | 89 | 38 | 51 | 42.7 | ok |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 570 | 255 | 315 | 44.74 | ok |
| none | T2_mid | 647 | 262 | 385 | 40.49 | ok |
| none | T3_high | 612 | 267 | 345 | 43.63 | ok |
| low | T1_low | 13 | 2 | 11 | 15.38 | insufficient |
| low | T2_mid | 14 | 6 | 8 | 42.86 | insufficient |
| low | T3_high | 40 | 14 | 26 | 35.0 | ok |
| medium | T1_low | 7 | 1 | 6 | 14.29 | insufficient |
| medium | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| medium | T3_high | 21 | 11 | 10 | 52.38 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 9 | 7 | 2 | 77.78 | insufficient |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **17310**
- Overall success rate: **50.78%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5315 | 2666 | 2649 | 50.16 | ok |
| none | T2_mid | 5739 | 2862 | 2877 | 49.87 | ok |
| none | T3_high | 4654 | 2408 | 2246 | 51.74 | ok |
| low | T1_low | 36 | 11 | 25 | 30.56 | ok |
| low | T2_mid | 35 | 13 | 22 | 37.14 | ok |
| low | T3_high | 115 | 63 | 52 | 54.78 | ok |
| medium | T1_low | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T2_mid | 19 | 5 | 14 | 26.32 | insufficient |
| medium | T3_high | 121 | 62 | 59 | 51.24 | ok |
| high | T1_low | 37 | 9 | 28 | 24.32 | ok |
| high | T2_mid | 17 | 10 | 7 | 58.82 | insufficient |
| high | T3_high | 910 | 499 | 411 | 54.84 | ok |
| missing | missing | 300 | 175 | 125 | 58.33 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4362 | 2184 | 2178 | 50.07 | ok |
| none | T2_mid | 5067 | 2566 | 2501 | 50.64 | ok |
| none | T3_high | 3367 | 1755 | 1612 | 52.12 | ok |
| low | T1_low | 487 | 236 | 251 | 48.46 | ok |
| low | T2_mid | 344 | 155 | 189 | 45.06 | ok |
| low | T3_high | 790 | 400 | 390 | 50.63 | ok |
| medium | T1_low | 372 | 189 | 183 | 50.81 | ok |
| medium | T2_mid | 298 | 134 | 164 | 44.97 | ok |
| medium | T3_high | 1113 | 572 | 541 | 51.39 | ok |
| high | T1_low | 179 | 84 | 95 | 46.93 | ok |
| high | T2_mid | 101 | 35 | 66 | 34.65 | ok |
| high | T3_high | 530 | 305 | 225 | 57.55 | ok |
| missing | missing | 300 | 175 | 125 | 58.33 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.