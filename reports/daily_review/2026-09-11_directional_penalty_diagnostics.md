# Directional Penalty Diagnostics - 2026-09-11

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **892**
- Overall success rate: **40.81%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 248 | 110 | 138 | 44.35 | ok |
| none | T2_mid | 217 | 90 | 127 | 41.47 | ok |
| none | T3_high | 159 | 74 | 85 | 46.54 | ok |
| low | T1_low | 8 | 3 | 5 | 37.5 | insufficient |
| low | T2_mid | 23 | 11 | 12 | 47.83 | ok |
| low | T3_high | 42 | 17 | 25 | 40.48 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 9 | 4 | 5 | 44.44 | insufficient |
| medium | T3_high | 35 | 14 | 21 | 40.0 | ok |
| high | T2_mid | 10 | 3 | 7 | 30.0 | insufficient |
| high | T3_high | 36 | 13 | 23 | 36.11 | ok |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 248 | 112 | 136 | 45.16 | ok |
| none | T2_mid | 241 | 104 | 137 | 43.15 | ok |
| none | T3_high | 235 | 99 | 136 | 42.13 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 13 | 3 | 10 | 23.08 | insufficient |
| low | T3_high | 21 | 10 | 11 | 47.62 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T3_high | 12 | 6 | 6 | 50.0 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **4415**
- Overall success rate: **46.36%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1310 | 535 | 775 | 40.84 | ok |
| none | T2_mid | 1307 | 604 | 703 | 46.21 | ok |
| none | T3_high | 845 | 402 | 443 | 47.57 | ok |
| low | T1_low | 21 | 3 | 18 | 14.29 | ok |
| low | T2_mid | 15 | 9 | 6 | 60.0 | insufficient |
| low | T3_high | 51 | 24 | 27 | 47.06 | ok |
| medium | T1_low | 12 | 5 | 7 | 41.67 | insufficient |
| medium | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T3_high | 49 | 24 | 25 | 48.98 | ok |
| high | T1_low | 36 | 7 | 29 | 19.44 | ok |
| high | T2_mid | 13 | 9 | 4 | 69.23 | insufficient |
| high | T3_high | 451 | 247 | 204 | 54.77 | ok |
| missing | missing | 295 | 174 | 121 | 58.98 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 823 | 327 | 496 | 39.73 | ok |
| none | T2_mid | 1034 | 481 | 553 | 46.52 | ok |
| none | T3_high | 378 | 172 | 206 | 45.5 | ok |
| low | T1_low | 235 | 82 | 153 | 34.89 | ok |
| low | T2_mid | 154 | 61 | 93 | 39.61 | ok |
| low | T3_high | 252 | 119 | 133 | 47.22 | ok |
| medium | T1_low | 195 | 84 | 111 | 43.08 | ok |
| medium | T2_mid | 107 | 58 | 49 | 54.21 | ok |
| medium | T3_high | 439 | 222 | 217 | 50.57 | ok |
| high | T1_low | 126 | 57 | 69 | 45.24 | ok |
| high | T2_mid | 50 | 26 | 24 | 52.0 | ok |
| high | T3_high | 327 | 184 | 143 | 56.27 | ok |
| missing | missing | 295 | 174 | 121 | 58.98 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.