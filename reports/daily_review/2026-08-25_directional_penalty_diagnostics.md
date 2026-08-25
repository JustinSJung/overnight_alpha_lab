# Directional Penalty Diagnostics - 2026-08-25

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **686**
- Overall success rate: **39.36%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 185 | 74 | 111 | 40.0 | ok |
| none | T2_mid | 161 | 67 | 94 | 41.61 | ok |
| none | T3_high | 110 | 49 | 61 | 44.55 | ok |
| low | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| low | T2_mid | 26 | 14 | 12 | 53.85 | ok |
| low | T3_high | 30 | 15 | 15 | 50.0 | ok |
| medium | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T3_high | 35 | 12 | 23 | 34.29 | ok |
| high | T2_mid | 6 | 1 | 5 | 16.67 | insufficient |
| high | T3_high | 26 | 6 | 20 | 23.08 | ok |
| missing | missing | 87 | 24 | 63 | 27.59 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 179 | 74 | 105 | 41.34 | ok |
| none | T2_mid | 180 | 81 | 99 | 45.0 | ok |
| none | T3_high | 170 | 67 | 103 | 39.41 | ok |
| low | T1_low | 13 | 4 | 9 | 30.77 | insufficient |
| low | T2_mid | 13 | 2 | 11 | 15.38 | insufficient |
| low | T3_high | 23 | 12 | 11 | 52.17 | ok |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 9 | 2 | 7 | 22.22 | insufficient |
| medium | T3_high | 7 | 2 | 5 | 28.57 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| high | T3_high | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 87 | 24 | 63 | 27.59 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2697**
- Overall success rate: **42.83%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 707 | 262 | 445 | 37.06 | ok |
| none | T2_mid | 767 | 280 | 487 | 36.51 | ok |
| none | T3_high | 491 | 222 | 269 | 45.21 | ok |
| low | T1_low | 12 | 3 | 9 | 25.0 | insufficient |
| low | T2_mid | 19 | 8 | 11 | 42.11 | insufficient |
| low | T3_high | 29 | 10 | 19 | 34.48 | ok |
| medium | T1_low | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| medium | T3_high | 33 | 17 | 16 | 51.52 | ok |
| high | T1_low | 29 | 8 | 21 | 27.59 | ok |
| high | T2_mid | 15 | 7 | 8 | 46.67 | insufficient |
| high | T3_high | 284 | 164 | 120 | 57.75 | ok |
| missing | missing | 291 | 167 | 124 | 57.39 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 361 | 120 | 241 | 33.24 | ok |
| none | T2_mid | 506 | 180 | 326 | 35.57 | ok |
| none | T3_high | 156 | 61 | 95 | 39.1 | ok |
| low | T1_low | 152 | 47 | 105 | 30.92 | ok |
| low | T2_mid | 137 | 41 | 96 | 29.93 | ok |
| low | T3_high | 138 | 65 | 73 | 47.1 | ok |
| medium | T1_low | 144 | 64 | 80 | 44.44 | ok |
| medium | T2_mid | 120 | 53 | 67 | 44.17 | ok |
| medium | T3_high | 273 | 130 | 143 | 47.62 | ok |
| high | T1_low | 97 | 45 | 52 | 46.39 | ok |
| high | T2_mid | 52 | 25 | 27 | 48.08 | ok |
| high | T3_high | 270 | 157 | 113 | 58.15 | ok |
| missing | missing | 291 | 167 | 124 | 57.39 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.