# Directional Penalty Diagnostics - 2026-08-20

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **627**
- Overall success rate: **39.55%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 172 | 67 | 105 | 38.95 | ok |
| none | T2_mid | 143 | 62 | 81 | 43.36 | ok |
| none | T3_high | 104 | 46 | 58 | 44.23 | ok |
| low | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| low | T2_mid | 25 | 12 | 13 | 48.0 | ok |
| low | T3_high | 29 | 16 | 13 | 55.17 | ok |
| medium | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T2_mid | 9 | 4 | 5 | 44.44 | insufficient |
| medium | T3_high | 28 | 7 | 21 | 25.0 | ok |
| high | T2_mid | 5 | 1 | 4 | 20.0 | insufficient |
| high | T3_high | 21 | 5 | 16 | 23.81 | ok |
| missing | missing | 82 | 24 | 58 | 29.27 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 165 | 67 | 98 | 40.61 | ok |
| none | T2_mid | 163 | 74 | 89 | 45.4 | ok |
| none | T3_high | 158 | 62 | 96 | 39.24 | ok |
| low | T1_low | 13 | 4 | 9 | 30.77 | insufficient |
| low | T2_mid | 12 | 2 | 10 | 16.67 | insufficient |
| low | T3_high | 19 | 10 | 9 | 52.63 | insufficient |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T3_high | 4 | 1 | 3 | 25.0 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| high | T3_high | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 82 | 24 | 58 | 29.27 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2228**
- Overall success rate: **42.37%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 550 | 195 | 355 | 35.45 | ok |
| none | T2_mid | 622 | 225 | 397 | 36.17 | ok |
| none | T3_high | 369 | 158 | 211 | 42.82 | ok |
| low | T1_low | 12 | 3 | 9 | 25.0 | insufficient |
| low | T2_mid | 19 | 8 | 11 | 42.11 | insufficient |
| low | T3_high | 24 | 8 | 16 | 33.33 | ok |
| medium | T1_low | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T2_mid | 12 | 3 | 9 | 25.0 | insufficient |
| medium | T3_high | 27 | 14 | 13 | 51.85 | ok |
| high | T1_low | 29 | 8 | 21 | 27.59 | ok |
| high | T2_mid | 14 | 6 | 8 | 42.86 | insufficient |
| high | T3_high | 256 | 147 | 109 | 57.42 | ok |
| missing | missing | 288 | 166 | 122 | 57.64 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 269 | 80 | 189 | 29.74 | ok |
| none | T2_mid | 418 | 152 | 266 | 36.36 | ok |
| none | T3_high | 111 | 39 | 72 | 35.14 | ok |
| low | T1_low | 124 | 41 | 83 | 33.06 | ok |
| low | T2_mid | 98 | 24 | 74 | 24.49 | ok |
| low | T3_high | 96 | 46 | 50 | 47.92 | ok |
| medium | T1_low | 122 | 52 | 70 | 42.62 | ok |
| medium | T2_mid | 104 | 47 | 57 | 45.19 | ok |
| medium | T3_high | 226 | 99 | 127 | 43.81 | ok |
| high | T1_low | 82 | 36 | 46 | 43.9 | ok |
| high | T2_mid | 47 | 19 | 28 | 40.43 | ok |
| high | T3_high | 243 | 143 | 100 | 58.85 | ok |
| missing | missing | 288 | 166 | 122 | 57.64 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.