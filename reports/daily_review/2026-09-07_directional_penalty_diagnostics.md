# Directional Penalty Diagnostics - 2026-09-07

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **778**
- Overall success rate: **39.85%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 204 | 88 | 116 | 43.14 | ok |
| none | T2_mid | 189 | 74 | 115 | 39.15 | ok |
| none | T3_high | 137 | 65 | 72 | 47.45 | ok |
| low | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| low | T2_mid | 22 | 10 | 12 | 45.45 | ok |
| low | T3_high | 34 | 16 | 18 | 47.06 | ok |
| medium | T1_low | 4 | 1 | 3 | 25.0 | insufficient |
| medium | T2_mid | 9 | 4 | 5 | 44.44 | insufficient |
| medium | T3_high | 34 | 13 | 21 | 38.24 | ok |
| high | T2_mid | 8 | 3 | 5 | 37.5 | insufficient |
| high | T3_high | 35 | 11 | 24 | 31.43 | ok |
| missing | missing | 95 | 22 | 73 | 23.16 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 203 | 90 | 113 | 44.33 | ok |
| none | T2_mid | 208 | 86 | 122 | 41.35 | ok |
| none | T3_high | 203 | 86 | 117 | 42.36 | ok |
| low | T1_low | 10 | 2 | 8 | 20.0 | insufficient |
| low | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| low | T3_high | 22 | 10 | 12 | 45.45 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 6 | 1 | 5 | 16.67 | insufficient |
| medium | T3_high | 11 | 6 | 5 | 54.55 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 95 | 22 | 73 | 23.16 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **3386**
- Overall success rate: **43.98%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 983 | 363 | 620 | 36.93 | ok |
| none | T2_mid | 957 | 398 | 559 | 41.59 | ok |
| none | T3_high | 593 | 278 | 315 | 46.88 | ok |
| low | T1_low | 17 | 3 | 14 | 17.65 | insufficient |
| low | T2_mid | 17 | 9 | 8 | 52.94 | insufficient |
| low | T3_high | 43 | 20 | 23 | 46.51 | ok |
| medium | T1_low | 10 | 5 | 5 | 50.0 | insufficient |
| medium | T2_mid | 12 | 5 | 7 | 41.67 | insufficient |
| medium | T3_high | 37 | 17 | 20 | 45.95 | ok |
| high | T1_low | 34 | 6 | 28 | 17.65 | ok |
| high | T2_mid | 16 | 11 | 5 | 68.75 | insufficient |
| high | T3_high | 373 | 206 | 167 | 55.23 | ok |
| missing | missing | 294 | 168 | 126 | 57.14 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 582 | 198 | 384 | 34.02 | ok |
| none | T2_mid | 680 | 278 | 402 | 40.88 | ok |
| none | T3_high | 226 | 97 | 129 | 42.92 | ok |
| low | T1_low | 188 | 60 | 128 | 31.91 | ok |
| low | T2_mid | 154 | 59 | 95 | 38.31 | ok |
| low | T3_high | 201 | 101 | 100 | 50.25 | ok |
| medium | T1_low | 167 | 71 | 96 | 42.51 | ok |
| medium | T2_mid | 115 | 53 | 62 | 46.09 | ok |
| medium | T3_high | 345 | 170 | 175 | 49.28 | ok |
| high | T1_low | 107 | 48 | 59 | 44.86 | ok |
| high | T2_mid | 53 | 33 | 20 | 62.26 | ok |
| high | T3_high | 274 | 153 | 121 | 55.84 | ok |
| missing | missing | 294 | 168 | 126 | 57.14 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.