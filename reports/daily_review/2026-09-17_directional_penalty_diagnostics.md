# Directional Penalty Diagnostics - 2026-09-17

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1007**
- Overall success rate: **41.41%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 283 | 131 | 152 | 46.29 | ok |
| none | T2_mid | 252 | 108 | 144 | 42.86 | ok |
| none | T3_high | 183 | 81 | 102 | 44.26 | ok |
| low | T1_low | 9 | 4 | 5 | 44.44 | insufficient |
| low | T2_mid | 25 | 11 | 14 | 44.0 | ok |
| low | T3_high | 47 | 17 | 30 | 36.17 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 10 | 6 | 4 | 60.0 | insufficient |
| medium | T3_high | 40 | 15 | 25 | 37.5 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 11 | 4 | 7 | 36.36 | insufficient |
| high | T3_high | 42 | 15 | 27 | 35.71 | ok |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 282 | 132 | 150 | 46.81 | ok |
| none | T2_mid | 276 | 121 | 155 | 43.84 | ok |
| none | T3_high | 274 | 109 | 165 | 39.78 | ok |
| low | T1_low | 12 | 3 | 9 | 25.0 | insufficient |
| low | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| low | T3_high | 22 | 10 | 12 | 45.45 | ok |
| medium | T1_low | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T2_mid | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T3_high | 12 | 6 | 6 | 50.0 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **5613**
- Overall success rate: **47.18%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1705 | 745 | 960 | 43.7 | ok |
| none | T2_mid | 1727 | 811 | 916 | 46.96 | ok |
| none | T3_high | 1137 | 539 | 598 | 47.41 | ok |
| low | T1_low | 21 | 3 | 18 | 14.29 | ok |
| low | T2_mid | 15 | 7 | 8 | 46.67 | insufficient |
| low | T3_high | 63 | 32 | 31 | 50.79 | ok |
| medium | T1_low | 12 | 5 | 7 | 41.67 | insufficient |
| medium | T2_mid | 10 | 5 | 5 | 50.0 | insufficient |
| medium | T3_high | 54 | 29 | 25 | 53.7 | ok |
| high | T1_low | 38 | 9 | 29 | 23.68 | ok |
| high | T2_mid | 13 | 9 | 4 | 69.23 | insufficient |
| high | T3_high | 518 | 278 | 240 | 53.67 | ok |
| missing | missing | 300 | 176 | 124 | 58.67 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1186 | 515 | 671 | 43.42 | ok |
| none | T2_mid | 1433 | 680 | 753 | 47.45 | ok |
| none | T3_high | 585 | 276 | 309 | 47.18 | ok |
| low | T1_low | 250 | 94 | 156 | 37.6 | ok |
| low | T2_mid | 151 | 65 | 86 | 43.05 | ok |
| low | T3_high | 305 | 143 | 162 | 46.89 | ok |
| medium | T1_low | 213 | 94 | 119 | 44.13 | ok |
| medium | T2_mid | 122 | 59 | 63 | 48.36 | ok |
| medium | T3_high | 546 | 274 | 272 | 50.18 | ok |
| high | T1_low | 127 | 59 | 68 | 46.46 | ok |
| high | T2_mid | 59 | 28 | 31 | 47.46 | ok |
| high | T3_high | 336 | 185 | 151 | 55.06 | ok |
| missing | missing | 300 | 176 | 124 | 58.67 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.