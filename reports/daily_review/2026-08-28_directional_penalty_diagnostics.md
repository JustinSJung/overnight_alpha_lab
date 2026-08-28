# Directional Penalty Diagnostics - 2026-08-28

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **730**
- Overall success rate: **39.86%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 198 | 79 | 119 | 39.9 | ok |
| none | T2_mid | 170 | 71 | 99 | 41.76 | ok |
| none | T3_high | 120 | 57 | 63 | 47.5 | ok |
| low | T1_low | 7 | 2 | 5 | 28.57 | insufficient |
| low | T2_mid | 27 | 14 | 13 | 51.85 | ok |
| low | T3_high | 30 | 15 | 15 | 50.0 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T3_high | 37 | 12 | 25 | 32.43 | ok |
| high | T2_mid | 8 | 2 | 6 | 25.0 | insufficient |
| high | T3_high | 31 | 9 | 22 | 29.03 | ok |
| missing | missing | 87 | 24 | 63 | 27.59 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 193 | 80 | 113 | 41.45 | ok |
| none | T2_mid | 189 | 84 | 105 | 44.44 | ok |
| none | T3_high | 184 | 77 | 107 | 41.85 | ok |
| low | T1_low | 14 | 3 | 11 | 21.43 | insufficient |
| low | T2_mid | 15 | 3 | 12 | 20.0 | insufficient |
| low | T3_high | 25 | 12 | 13 | 48.0 | ok |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 9 | 2 | 7 | 22.22 | insufficient |
| medium | T3_high | 8 | 3 | 5 | 37.5 | insufficient |
| high | T2_mid | 2 | 2 | 0 | 100.0 | insufficient |
| high | T3_high | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 87 | 24 | 63 | 27.59 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2949**
- Overall success rate: **42.9%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 776 | 287 | 489 | 36.98 | ok |
| none | T2_mid | 864 | 314 | 550 | 36.34 | ok |
| none | T3_high | 515 | 246 | 269 | 47.77 | ok |
| low | T1_low | 13 | 3 | 10 | 23.08 | insufficient |
| low | T2_mid | 20 | 9 | 11 | 45.0 | ok |
| low | T3_high | 33 | 12 | 21 | 36.36 | ok |
| medium | T1_low | 8 | 4 | 4 | 50.0 | insufficient |
| medium | T2_mid | 13 | 4 | 9 | 30.77 | insufficient |
| medium | T3_high | 41 | 20 | 21 | 48.78 | ok |
| high | T1_low | 30 | 8 | 22 | 26.67 | ok |
| high | T2_mid | 16 | 8 | 8 | 50.0 | insufficient |
| high | T3_high | 322 | 179 | 143 | 55.59 | ok |
| missing | missing | 298 | 171 | 127 | 57.38 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 398 | 137 | 261 | 34.42 | ok |
| none | T2_mid | 570 | 202 | 368 | 35.44 | ok |
| none | T3_high | 154 | 61 | 93 | 39.61 | ok |
| low | T1_low | 171 | 53 | 118 | 30.99 | ok |
| low | T2_mid | 162 | 52 | 110 | 32.1 | ok |
| low | T3_high | 154 | 77 | 77 | 50.0 | ok |
| medium | T1_low | 150 | 65 | 85 | 43.33 | ok |
| medium | T2_mid | 131 | 57 | 74 | 43.51 | ok |
| medium | T3_high | 313 | 154 | 159 | 49.2 | ok |
| high | T1_low | 108 | 47 | 61 | 43.52 | ok |
| high | T2_mid | 50 | 24 | 26 | 48.0 | ok |
| high | T3_high | 290 | 165 | 125 | 56.9 | ok |
| missing | missing | 298 | 171 | 127 | 57.38 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.