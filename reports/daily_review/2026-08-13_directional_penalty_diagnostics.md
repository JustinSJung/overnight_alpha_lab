# Directional Penalty Diagnostics - 2026-08-13

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **441**
- Overall success rate: **44.44%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 110 | 52 | 58 | 47.27 | ok |
| none | T2_mid | 95 | 45 | 50 | 47.37 | ok |
| none | T3_high | 71 | 36 | 35 | 50.7 | ok |
| low | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| low | T2_mid | 14 | 10 | 4 | 71.43 | insufficient |
| low | T3_high | 19 | 11 | 8 | 57.89 | insufficient |
| medium | T1_low | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T2_mid | 6 | 4 | 2 | 66.67 | insufficient |
| medium | T3_high | 17 | 6 | 11 | 35.29 | insufficient |
| high | T2_mid | 4 | 1 | 3 | 25.0 | insufficient |
| high | T3_high | 15 | 5 | 10 | 33.33 | insufficient |
| missing | missing | 85 | 24 | 61 | 28.24 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 110 | 51 | 59 | 46.36 | ok |
| none | T2_mid | 112 | 57 | 55 | 50.89 | ok |
| none | T3_high | 108 | 48 | 60 | 44.44 | ok |
| low | T1_low | 4 | 3 | 1 | 75.0 | insufficient |
| low | T2_mid | 3 | 1 | 2 | 33.33 | insufficient |
| low | T3_high | 12 | 10 | 2 | 83.33 | insufficient |
| medium | T1_low | 1 | 0 | 1 | 0.0 | insufficient |
| medium | T2_mid | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T3_high | 2 | 0 | 2 | 0.0 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 85 | 24 | 61 | 28.24 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **1880**
- Overall success rate: **41.54%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 441 | 149 | 292 | 33.79 | ok |
| none | T2_mid | 512 | 184 | 328 | 35.94 | ok |
| none | T3_high | 309 | 122 | 187 | 39.48 | ok |
| low | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| low | T2_mid | 17 | 7 | 10 | 41.18 | insufficient |
| low | T3_high | 22 | 7 | 15 | 31.82 | ok |
| medium | T1_low | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T2_mid | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T3_high | 25 | 14 | 11 | 56.0 | ok |
| high | T1_low | 20 | 4 | 16 | 20.0 | ok |
| high | T2_mid | 21 | 9 | 12 | 42.86 | ok |
| high | T3_high | 196 | 109 | 87 | 55.61 | ok |
| missing | missing | 290 | 168 | 122 | 57.93 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 224 | 63 | 161 | 28.12 | ok |
| none | T2_mid | 336 | 121 | 215 | 36.01 | ok |
| none | T3_high | 120 | 44 | 76 | 36.67 | ok |
| low | T1_low | 110 | 36 | 74 | 32.73 | ok |
| low | T2_mid | 80 | 21 | 59 | 26.25 | ok |
| low | T3_high | 69 | 27 | 42 | 39.13 | ok |
| medium | T1_low | 89 | 37 | 52 | 41.57 | ok |
| medium | T2_mid | 95 | 37 | 58 | 38.95 | ok |
| medium | T3_high | 173 | 74 | 99 | 42.77 | ok |
| high | T1_low | 55 | 23 | 32 | 41.82 | ok |
| high | T2_mid | 49 | 23 | 26 | 46.94 | ok |
| high | T3_high | 190 | 107 | 83 | 56.32 | ok |
| missing | missing | 290 | 168 | 122 | 57.93 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.