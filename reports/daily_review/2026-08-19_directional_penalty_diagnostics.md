# Directional Penalty Diagnostics - 2026-08-19

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **608**
- Overall success rate: **38.82%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 165 | 63 | 102 | 38.18 | ok |
| none | T2_mid | 140 | 59 | 81 | 42.14 | ok |
| none | T3_high | 101 | 44 | 57 | 43.56 | ok |
| low | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| low | T2_mid | 24 | 12 | 12 | 50.0 | ok |
| low | T3_high | 27 | 15 | 12 | 55.56 | ok |
| medium | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T2_mid | 9 | 4 | 5 | 44.44 | insufficient |
| medium | T3_high | 27 | 6 | 21 | 22.22 | ok |
| high | T2_mid | 5 | 1 | 4 | 20.0 | insufficient |
| high | T3_high | 20 | 5 | 15 | 25.0 | ok |
| missing | missing | 81 | 23 | 58 | 28.4 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 159 | 63 | 96 | 39.62 | ok |
| none | T2_mid | 159 | 71 | 88 | 44.65 | ok |
| none | T3_high | 152 | 59 | 93 | 38.82 | ok |
| low | T1_low | 12 | 4 | 8 | 33.33 | insufficient |
| low | T2_mid | 12 | 2 | 10 | 16.67 | insufficient |
| low | T3_high | 19 | 10 | 9 | 52.63 | insufficient |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T3_high | 4 | 1 | 3 | 25.0 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 81 | 23 | 58 | 28.4 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2103**
- Overall success rate: **42.8%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 521 | 184 | 337 | 35.32 | ok |
| none | T2_mid | 582 | 211 | 371 | 36.25 | ok |
| none | T3_high | 338 | 153 | 185 | 45.27 | ok |
| low | T1_low | 12 | 3 | 9 | 25.0 | insufficient |
| low | T2_mid | 19 | 8 | 11 | 42.11 | insufficient |
| low | T3_high | 22 | 7 | 15 | 31.82 | ok |
| medium | T1_low | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T2_mid | 12 | 3 | 9 | 25.0 | insufficient |
| medium | T3_high | 27 | 14 | 13 | 51.85 | ok |
| high | T1_low | 28 | 7 | 21 | 25.0 | ok |
| high | T2_mid | 14 | 6 | 8 | 42.86 | insufficient |
| high | T3_high | 245 | 142 | 103 | 57.96 | ok |
| missing | missing | 277 | 159 | 118 | 57.4 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 256 | 77 | 179 | 30.08 | ok |
| none | T2_mid | 390 | 141 | 249 | 36.15 | ok |
| none | T3_high | 100 | 43 | 57 | 43.0 | ok |
| low | T1_low | 121 | 40 | 81 | 33.06 | ok |
| low | T2_mid | 87 | 22 | 65 | 25.29 | ok |
| low | T3_high | 86 | 42 | 44 | 48.84 | ok |
| medium | T1_low | 115 | 48 | 67 | 41.74 | ok |
| medium | T2_mid | 102 | 45 | 57 | 44.12 | ok |
| medium | T3_high | 212 | 94 | 118 | 44.34 | ok |
| high | T1_low | 75 | 32 | 43 | 42.67 | ok |
| high | T2_mid | 48 | 20 | 28 | 41.67 | ok |
| high | T3_high | 234 | 137 | 97 | 58.55 | ok |
| missing | missing | 277 | 159 | 118 | 57.4 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.