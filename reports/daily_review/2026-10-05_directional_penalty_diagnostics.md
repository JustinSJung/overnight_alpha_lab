# Directional Penalty Diagnostics - 2026-10-05

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1317**
- Overall success rate: **43.28%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 373 | 177 | 196 | 47.45 | ok |
| none | T2_mid | 347 | 154 | 193 | 44.38 | ok |
| none | T3_high | 259 | 118 | 141 | 45.56 | ok |
| low | T1_low | 9 | 3 | 6 | 33.33 | insufficient |
| low | T2_mid | 33 | 14 | 19 | 42.42 | ok |
| low | T3_high | 55 | 23 | 32 | 41.82 | ok |
| medium | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T2_mid | 14 | 8 | 6 | 57.14 | insufficient |
| medium | T3_high | 54 | 23 | 31 | 42.59 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 9 | 3 | 6 | 33.33 | insufficient |
| high | T3_high | 53 | 20 | 33 | 37.74 | ok |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 373 | 180 | 193 | 48.26 | ok |
| none | T2_mid | 379 | 169 | 210 | 44.59 | ok |
| none | T3_high | 377 | 162 | 215 | 42.97 | ok |
| low | T1_low | 11 | 1 | 10 | 9.09 | insufficient |
| low | T2_mid | 14 | 5 | 9 | 35.71 | insufficient |
| low | T3_high | 25 | 10 | 15 | 40.0 | ok |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 9 | 5 | 4 | 55.56 | insufficient |
| medium | T3_high | 14 | 8 | 6 | 57.14 | insufficient |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 5 | 4 | 1 | 80.0 | insufficient |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **7620**
- Overall success rate: **47.31%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2404 | 1089 | 1315 | 45.3 | ok |
| none | T2_mid | 2423 | 1134 | 1289 | 46.8 | ok |
| none | T3_high | 1572 | 749 | 823 | 47.65 | ok |
| low | T1_low | 23 | 3 | 20 | 13.04 | ok |
| low | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| low | T3_high | 79 | 42 | 37 | 53.16 | ok |
| medium | T1_low | 15 | 6 | 9 | 40.0 | insufficient |
| medium | T2_mid | 11 | 8 | 3 | 72.73 | insufficient |
| medium | T3_high | 79 | 38 | 41 | 48.1 | ok |
| high | T1_low | 46 | 11 | 35 | 23.91 | ok |
| high | T2_mid | 13 | 8 | 5 | 61.54 | insufficient |
| high | T3_high | 638 | 333 | 305 | 52.19 | ok |
| missing | missing | 304 | 177 | 127 | 58.22 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1726 | 767 | 959 | 44.44 | ok |
| none | T2_mid | 2101 | 995 | 1106 | 47.36 | ok |
| none | T3_high | 898 | 421 | 477 | 46.88 | ok |
| low | T1_low | 324 | 133 | 191 | 41.05 | ok |
| low | T2_mid | 161 | 65 | 96 | 40.37 | ok |
| low | T3_high | 408 | 195 | 213 | 47.79 | ok |
| medium | T1_low | 270 | 133 | 137 | 49.26 | ok |
| medium | T2_mid | 136 | 69 | 67 | 50.74 | ok |
| medium | T3_high | 663 | 331 | 332 | 49.92 | ok |
| high | T1_low | 168 | 76 | 92 | 45.24 | ok |
| high | T2_mid | 62 | 28 | 34 | 45.16 | ok |
| high | T3_high | 399 | 215 | 184 | 53.88 | ok |
| missing | missing | 304 | 177 | 127 | 58.22 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.