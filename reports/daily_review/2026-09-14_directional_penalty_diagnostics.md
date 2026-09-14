# Directional Penalty Diagnostics - 2026-09-14

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **919**
- Overall success rate: **40.26%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 254 | 113 | 141 | 44.49 | ok |
| none | T2_mid | 229 | 96 | 133 | 41.92 | ok |
| none | T3_high | 164 | 73 | 91 | 44.51 | ok |
| low | T1_low | 8 | 3 | 5 | 37.5 | insufficient |
| low | T2_mid | 22 | 10 | 12 | 45.45 | ok |
| low | T3_high | 43 | 17 | 26 | 39.53 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 9 | 4 | 5 | 44.44 | insufficient |
| medium | T3_high | 36 | 14 | 22 | 38.89 | ok |
| high | T2_mid | 10 | 3 | 7 | 30.0 | insufficient |
| high | T3_high | 38 | 13 | 25 | 34.21 | ok |
| missing | missing | 101 | 23 | 78 | 22.77 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 254 | 115 | 139 | 45.28 | ok |
| none | T2_mid | 249 | 107 | 142 | 42.97 | ok |
| none | T3_high | 244 | 98 | 146 | 40.16 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| low | T3_high | 21 | 10 | 11 | 47.62 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T3_high | 12 | 6 | 6 | 50.0 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 101 | 23 | 78 | 22.77 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **4610**
- Overall success rate: **47.38%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1372 | 590 | 782 | 43.0 | ok |
| none | T2_mid | 1393 | 666 | 727 | 47.81 | ok |
| none | T3_high | 899 | 432 | 467 | 48.05 | ok |
| low | T1_low | 20 | 3 | 17 | 15.0 | ok |
| low | T2_mid | 17 | 9 | 8 | 52.94 | insufficient |
| low | T3_high | 52 | 27 | 25 | 51.92 | ok |
| medium | T1_low | 10 | 3 | 7 | 30.0 | insufficient |
| medium | T2_mid | 11 | 4 | 7 | 36.36 | insufficient |
| medium | T3_high | 51 | 25 | 26 | 49.02 | ok |
| high | T1_low | 34 | 7 | 27 | 20.59 | ok |
| high | T2_mid | 10 | 6 | 4 | 60.0 | insufficient |
| high | T3_high | 445 | 240 | 205 | 53.93 | ok |
| missing | missing | 296 | 172 | 124 | 58.11 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 908 | 395 | 513 | 43.5 | ok |
| none | T2_mid | 1121 | 545 | 576 | 48.62 | ok |
| none | T3_high | 428 | 199 | 229 | 46.5 | ok |
| low | T1_low | 232 | 80 | 152 | 34.48 | ok |
| low | T2_mid | 152 | 63 | 89 | 41.45 | ok |
| low | T3_high | 271 | 130 | 141 | 47.97 | ok |
| medium | T1_low | 178 | 77 | 101 | 43.26 | ok |
| medium | T2_mid | 112 | 54 | 58 | 48.21 | ok |
| medium | T3_high | 450 | 231 | 219 | 51.33 | ok |
| high | T1_low | 118 | 51 | 67 | 43.22 | ok |
| high | T2_mid | 46 | 23 | 23 | 50.0 | ok |
| high | T3_high | 298 | 164 | 134 | 55.03 | ok |
| missing | missing | 296 | 172 | 124 | 58.11 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.