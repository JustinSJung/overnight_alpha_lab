# Directional Penalty Diagnostics - 2026-09-16

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **956**
- Overall success rate: **40.38%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 266 | 122 | 144 | 45.86 | ok |
| none | T2_mid | 242 | 100 | 142 | 41.32 | ok |
| none | T3_high | 167 | 74 | 93 | 44.31 | ok |
| low | T1_low | 9 | 4 | 5 | 44.44 | insufficient |
| low | T2_mid | 24 | 10 | 14 | 41.67 | ok |
| low | T3_high | 45 | 17 | 28 | 37.78 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 8 | 4 | 4 | 50.0 | insufficient |
| medium | T3_high | 38 | 13 | 25 | 34.21 | ok |
| high | T1_low | 1 | 0 | 1 | 0.0 | insufficient |
| high | T2_mid | 10 | 3 | 7 | 30.0 | insufficient |
| high | T3_high | 42 | 15 | 27 | 35.71 | ok |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 265 | 122 | 143 | 46.04 | ok |
| none | T2_mid | 262 | 110 | 152 | 41.98 | ok |
| none | T3_high | 256 | 101 | 155 | 39.45 | ok |
| low | T1_low | 12 | 3 | 9 | 25.0 | insufficient |
| low | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| low | T3_high | 20 | 9 | 11 | 45.0 | ok |
| medium | T1_low | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T2_mid | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T3_high | 12 | 6 | 6 | 50.0 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **5219**
- Overall success rate: **48.29%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1572 | 692 | 880 | 44.02 | ok |
| none | T2_mid | 1617 | 792 | 825 | 48.98 | ok |
| none | T3_high | 1048 | 513 | 535 | 48.95 | ok |
| low | T1_low | 20 | 3 | 17 | 15.0 | ok |
| low | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| low | T3_high | 61 | 33 | 28 | 54.1 | ok |
| medium | T1_low | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T3_high | 49 | 26 | 23 | 53.06 | ok |
| high | T1_low | 32 | 6 | 26 | 18.75 | ok |
| high | T2_mid | 12 | 8 | 4 | 66.67 | insufficient |
| high | T3_high | 479 | 261 | 218 | 54.49 | ok |
| missing | missing | 296 | 171 | 125 | 57.77 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1079 | 484 | 595 | 44.86 | ok |
| none | T2_mid | 1332 | 667 | 665 | 50.08 | ok |
| none | T3_high | 530 | 253 | 277 | 47.74 | ok |
| low | T1_low | 251 | 92 | 159 | 36.65 | ok |
| low | T2_mid | 151 | 64 | 87 | 42.38 | ok |
| low | T3_high | 296 | 145 | 151 | 48.99 | ok |
| medium | T1_low | 186 | 77 | 109 | 41.4 | ok |
| medium | T2_mid | 115 | 54 | 61 | 46.96 | ok |
| medium | T3_high | 489 | 258 | 231 | 52.76 | ok |
| high | T1_low | 118 | 52 | 66 | 44.07 | ok |
| high | T2_mid | 54 | 26 | 28 | 48.15 | ok |
| high | T3_high | 322 | 177 | 145 | 54.97 | ok |
| missing | missing | 296 | 171 | 125 | 57.77 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.