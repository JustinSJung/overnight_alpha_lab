# Directional Penalty Diagnostics - 2026-08-27

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **708**
- Overall success rate: **39.69%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 198 | 83 | 115 | 41.92 | ok |
| none | T2_mid | 165 | 66 | 99 | 40.0 | ok |
| none | T3_high | 110 | 50 | 60 | 45.45 | ok |
| low | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| low | T2_mid | 27 | 14 | 13 | 51.85 | ok |
| low | T3_high | 30 | 15 | 15 | 50.0 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T3_high | 35 | 12 | 23 | 34.29 | ok |
| high | T2_mid | 6 | 1 | 5 | 16.67 | insufficient |
| high | T3_high | 29 | 8 | 21 | 27.59 | ok |
| missing | missing | 87 | 24 | 63 | 27.59 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 192 | 83 | 109 | 43.23 | ok |
| none | T2_mid | 185 | 80 | 105 | 43.24 | ok |
| none | T3_high | 171 | 69 | 102 | 40.35 | ok |
| low | T1_low | 14 | 4 | 10 | 28.57 | insufficient |
| low | T2_mid | 13 | 2 | 11 | 15.38 | insufficient |
| low | T3_high | 24 | 12 | 12 | 50.0 | ok |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 9 | 2 | 7 | 22.22 | insufficient |
| medium | T3_high | 8 | 3 | 5 | 37.5 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| high | T3_high | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 87 | 24 | 63 | 27.59 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2845**
- Overall success rate: **42.67%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 754 | 281 | 473 | 37.27 | ok |
| none | T2_mid | 834 | 300 | 534 | 35.97 | ok |
| none | T3_high | 497 | 232 | 265 | 46.68 | ok |
| low | T1_low | 13 | 3 | 10 | 23.08 | insufficient |
| low | T2_mid | 20 | 9 | 11 | 45.0 | ok |
| low | T3_high | 32 | 11 | 21 | 34.38 | ok |
| medium | T1_low | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| medium | T3_high | 37 | 18 | 19 | 48.65 | ok |
| high | T1_low | 29 | 8 | 21 | 27.59 | ok |
| high | T2_mid | 15 | 7 | 8 | 46.67 | insufficient |
| high | T3_high | 301 | 170 | 131 | 56.48 | ok |
| missing | missing | 293 | 168 | 125 | 57.34 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 389 | 134 | 255 | 34.45 | ok |
| none | T2_mid | 544 | 187 | 357 | 34.38 | ok |
| none | T3_high | 149 | 57 | 92 | 38.26 | ok |
| low | T1_low | 161 | 50 | 111 | 31.06 | ok |
| low | T2_mid | 159 | 52 | 107 | 32.7 | ok |
| low | T3_high | 143 | 70 | 73 | 48.95 | ok |
| medium | T1_low | 147 | 64 | 83 | 43.54 | ok |
| medium | T2_mid | 130 | 57 | 73 | 43.85 | ok |
| medium | T3_high | 291 | 141 | 150 | 48.45 | ok |
| high | T1_low | 105 | 47 | 58 | 44.76 | ok |
| high | T2_mid | 50 | 24 | 26 | 48.0 | ok |
| high | T3_high | 284 | 163 | 121 | 57.39 | ok |
| missing | missing | 293 | 168 | 125 | 57.34 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.