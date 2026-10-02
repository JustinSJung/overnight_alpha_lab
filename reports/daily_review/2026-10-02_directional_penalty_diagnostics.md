# Directional Penalty Diagnostics - 2026-10-02

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1327**
- Overall success rate: **43.63%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 384 | 183 | 201 | 47.66 | ok |
| none | T2_mid | 351 | 156 | 195 | 44.44 | ok |
| none | T3_high | 255 | 117 | 138 | 45.88 | ok |
| low | T1_low | 10 | 4 | 6 | 40.0 | insufficient |
| low | T2_mid | 35 | 15 | 20 | 42.86 | ok |
| low | T3_high | 53 | 23 | 30 | 43.4 | ok |
| medium | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T2_mid | 15 | 9 | 6 | 60.0 | insufficient |
| medium | T3_high | 52 | 22 | 30 | 42.31 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 9 | 3 | 6 | 33.33 | insufficient |
| high | T3_high | 51 | 20 | 31 | 39.22 | ok |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 384 | 185 | 199 | 48.18 | ok |
| none | T2_mid | 389 | 174 | 215 | 44.73 | ok |
| none | T3_high | 371 | 160 | 211 | 43.13 | ok |
| low | T1_low | 12 | 3 | 9 | 25.0 | insufficient |
| low | T2_mid | 11 | 4 | 7 | 36.36 | insufficient |
| low | T3_high | 21 | 10 | 11 | 47.62 | ok |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 9 | 5 | 4 | 55.56 | insufficient |
| medium | T3_high | 14 | 8 | 6 | 57.14 | insufficient |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 5 | 4 | 1 | 80.0 | insufficient |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **7564**
- Overall success rate: **47.44%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2348 | 1073 | 1275 | 45.7 | ok |
| none | T2_mid | 2411 | 1134 | 1277 | 47.03 | ok |
| none | T3_high | 1574 | 747 | 827 | 47.46 | ok |
| low | T1_low | 21 | 2 | 19 | 9.52 | ok |
| low | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| low | T3_high | 79 | 41 | 38 | 51.9 | ok |
| medium | T1_low | 15 | 6 | 9 | 40.0 | insufficient |
| medium | T2_mid | 10 | 6 | 4 | 60.0 | insufficient |
| medium | T3_high | 77 | 37 | 40 | 48.05 | ok |
| high | T1_low | 44 | 11 | 33 | 25.0 | ok |
| high | T2_mid | 13 | 8 | 5 | 61.54 | insufficient |
| high | T3_high | 656 | 339 | 317 | 51.68 | ok |
| missing | missing | 303 | 177 | 126 | 58.42 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1688 | 755 | 933 | 44.73 | ok |
| none | T2_mid | 2092 | 994 | 1098 | 47.51 | ok |
| none | T3_high | 920 | 427 | 493 | 46.41 | ok |
| low | T1_low | 307 | 130 | 177 | 42.35 | ok |
| low | T2_mid | 151 | 61 | 90 | 40.4 | ok |
| low | T3_high | 393 | 188 | 205 | 47.84 | ok |
| medium | T1_low | 264 | 131 | 133 | 49.62 | ok |
| medium | T2_mid | 137 | 68 | 69 | 49.64 | ok |
| medium | T3_high | 673 | 333 | 340 | 49.48 | ok |
| high | T1_low | 169 | 76 | 93 | 44.97 | ok |
| high | T2_mid | 67 | 32 | 35 | 47.76 | ok |
| high | T3_high | 400 | 216 | 184 | 54.0 | ok |
| missing | missing | 303 | 177 | 126 | 58.42 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.