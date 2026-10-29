# Directional Penalty Diagnostics - 2026-10-16

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1775**
- Overall success rate: **41.18%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 507 | 223 | 284 | 43.98 | ok |
| none | T2_mid | 467 | 185 | 282 | 39.61 | ok |
| none | T3_high | 355 | 152 | 203 | 42.82 | ok |
| low | T1_low | 15 | 6 | 9 | 40.0 | insufficient |
| low | T2_mid | 64 | 26 | 38 | 40.62 | ok |
| low | T3_high | 80 | 33 | 47 | 41.25 | ok |
| medium | T1_low | 4 | 1 | 3 | 25.0 | insufficient |
| medium | T2_mid | 19 | 10 | 9 | 52.63 | insufficient |
| medium | T3_high | 75 | 34 | 41 | 45.33 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 12 | 5 | 7 | 41.67 | insufficient |
| high | T3_high | 76 | 31 | 45 | 40.79 | ok |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 509 | 227 | 282 | 44.6 | ok |
| none | T2_mid | 533 | 212 | 321 | 39.77 | ok |
| none | T3_high | 526 | 220 | 306 | 41.83 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 14 | 5 | 9 | 35.71 | insufficient |
| low | T3_high | 30 | 12 | 18 | 40.0 | ok |
| medium | T1_low | 5 | 0 | 5 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 22 | 12 | 10 | 54.55 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **10432**
- Overall success rate: **49.32%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3247 | 1533 | 1714 | 47.21 | ok |
| none | T2_mid | 3395 | 1675 | 1720 | 49.34 | ok |
| none | T3_high | 2407 | 1226 | 1181 | 50.93 | ok |
| low | T1_low | 23 | 5 | 18 | 21.74 | ok |
| low | T2_mid | 15 | 6 | 9 | 40.0 | insufficient |
| low | T3_high | 93 | 52 | 41 | 55.91 | ok |
| medium | T1_low | 11 | 6 | 5 | 54.55 | insufficient |
| medium | T2_mid | 16 | 6 | 10 | 37.5 | insufficient |
| medium | T3_high | 93 | 50 | 43 | 53.76 | ok |
| high | T1_low | 39 | 9 | 30 | 23.08 | ok |
| high | T2_mid | 18 | 10 | 8 | 55.56 | insufficient |
| high | T3_high | 784 | 399 | 385 | 50.89 | ok |
| missing | missing | 291 | 168 | 123 | 57.73 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2568 | 1224 | 1344 | 47.66 | ok |
| none | T2_mid | 2972 | 1497 | 1475 | 50.37 | ok |
| none | T3_high | 1579 | 811 | 768 | 51.36 | ok |
| low | T1_low | 326 | 138 | 188 | 42.33 | ok |
| low | T2_mid | 202 | 77 | 125 | 38.12 | ok |
| low | T3_high | 520 | 253 | 267 | 48.65 | ok |
| medium | T1_low | 255 | 115 | 140 | 45.1 | ok |
| medium | T2_mid | 194 | 91 | 103 | 46.91 | ok |
| medium | T3_high | 815 | 423 | 392 | 51.9 | ok |
| high | T1_low | 171 | 76 | 95 | 44.44 | ok |
| high | T2_mid | 76 | 32 | 44 | 42.11 | ok |
| high | T3_high | 463 | 240 | 223 | 51.84 | ok |
| missing | missing | 291 | 168 | 123 | 57.73 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.