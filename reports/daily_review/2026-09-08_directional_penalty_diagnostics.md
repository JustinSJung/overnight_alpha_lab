# Directional Penalty Diagnostics - 2026-09-08

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **806**
- Overall success rate: **39.95%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 222 | 95 | 127 | 42.79 | ok |
| none | T2_mid | 188 | 73 | 115 | 38.83 | ok |
| none | T3_high | 141 | 68 | 73 | 48.23 | ok |
| low | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| low | T2_mid | 23 | 11 | 12 | 47.83 | ok |
| low | T3_high | 34 | 16 | 18 | 47.06 | ok |
| medium | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T2_mid | 8 | 3 | 5 | 37.5 | insufficient |
| medium | T3_high | 34 | 13 | 21 | 38.24 | ok |
| high | T2_mid | 10 | 3 | 7 | 30.0 | insufficient |
| high | T3_high | 34 | 11 | 23 | 32.35 | ok |
| missing | missing | 99 | 24 | 75 | 24.24 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 222 | 98 | 124 | 44.14 | ok |
| none | T2_mid | 208 | 85 | 123 | 40.87 | ok |
| none | T3_high | 207 | 89 | 118 | 43.0 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| low | T3_high | 22 | 10 | 12 | 45.45 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 7 | 1 | 6 | 14.29 | insufficient |
| medium | T3_high | 10 | 6 | 4 | 60.0 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 99 | 24 | 75 | 24.24 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **3650**
- Overall success rate: **44.44%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1057 | 397 | 660 | 37.56 | ok |
| none | T2_mid | 1047 | 442 | 605 | 42.22 | ok |
| none | T3_high | 664 | 314 | 350 | 47.29 | ok |
| low | T1_low | 20 | 4 | 16 | 20.0 | ok |
| low | T2_mid | 14 | 8 | 6 | 57.14 | insufficient |
| low | T3_high | 48 | 22 | 26 | 45.83 | ok |
| medium | T1_low | 12 | 5 | 7 | 41.67 | insufficient |
| medium | T2_mid | 10 | 3 | 7 | 30.0 | insufficient |
| medium | T3_high | 44 | 23 | 21 | 52.27 | ok |
| high | T1_low | 35 | 8 | 27 | 22.86 | ok |
| high | T2_mid | 14 | 9 | 5 | 64.29 | insufficient |
| high | T3_high | 390 | 216 | 174 | 55.38 | ok |
| missing | missing | 295 | 171 | 124 | 57.97 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 628 | 219 | 409 | 34.87 | ok |
| none | T2_mid | 770 | 323 | 447 | 41.95 | ok |
| none | T3_high | 267 | 118 | 149 | 44.19 | ok |
| low | T1_low | 210 | 68 | 142 | 32.38 | ok |
| low | T2_mid | 156 | 62 | 94 | 39.74 | ok |
| low | T3_high | 212 | 101 | 111 | 47.64 | ok |
| medium | T1_low | 178 | 78 | 100 | 43.82 | ok |
| medium | T2_mid | 112 | 51 | 61 | 45.54 | ok |
| medium | T3_high | 374 | 187 | 187 | 50.0 | ok |
| high | T1_low | 108 | 49 | 59 | 45.37 | ok |
| high | T2_mid | 47 | 26 | 21 | 55.32 | ok |
| high | T3_high | 293 | 169 | 124 | 57.68 | ok |
| missing | missing | 295 | 171 | 124 | 57.97 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.