# Directional Penalty Diagnostics - 2026-11-04

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2000**
- Overall success rate: **41.15%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 555 | 243 | 312 | 43.78 | ok |
| none | T2_mid | 545 | 216 | 329 | 39.63 | ok |
| none | T3_high | 412 | 178 | 234 | 43.2 | ok |
| low | T1_low | 17 | 7 | 10 | 41.18 | insufficient |
| low | T2_mid | 65 | 27 | 38 | 41.54 | ok |
| low | T3_high | 91 | 38 | 53 | 41.76 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 18 | 11 | 7 | 61.11 | insufficient |
| medium | T3_high | 87 | 36 | 51 | 41.38 | ok |
| high | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| high | T2_mid | 13 | 6 | 7 | 46.15 | insufficient |
| high | T3_high | 86 | 35 | 51 | 40.7 | ok |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 559 | 248 | 311 | 44.36 | ok |
| none | T2_mid | 612 | 246 | 366 | 40.2 | ok |
| none | T3_high | 603 | 255 | 348 | 42.29 | ok |
| low | T1_low | 12 | 2 | 10 | 16.67 | insufficient |
| low | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| low | T3_high | 41 | 14 | 27 | 34.15 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| medium | T3_high | 23 | 13 | 10 | 56.52 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 9 | 5 | 4 | 55.56 | insufficient |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **16354**
- Overall success rate: **50.26%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5144 | 2476 | 2668 | 48.13 | ok |
| none | T2_mid | 5297 | 2653 | 2644 | 50.08 | ok |
| none | T3_high | 4238 | 2209 | 2029 | 52.12 | ok |
| low | T1_low | 35 | 9 | 26 | 25.71 | ok |
| low | T2_mid | 27 | 8 | 19 | 29.63 | ok |
| low | T3_high | 118 | 65 | 53 | 55.08 | ok |
| medium | T1_low | 15 | 8 | 7 | 53.33 | insufficient |
| medium | T2_mid | 18 | 6 | 12 | 33.33 | insufficient |
| medium | T3_high | 121 | 65 | 56 | 53.72 | ok |
| high | T1_low | 37 | 9 | 28 | 24.32 | ok |
| high | T2_mid | 18 | 9 | 9 | 50.0 | insufficient |
| high | T3_high | 984 | 526 | 458 | 53.46 | ok |
| missing | missing | 302 | 177 | 125 | 58.61 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4226 | 2034 | 2192 | 48.13 | ok |
| none | T2_mid | 4707 | 2396 | 2311 | 50.9 | ok |
| none | T3_high | 3001 | 1578 | 1423 | 52.58 | ok |
| low | T1_low | 466 | 208 | 258 | 44.64 | ok |
| low | T2_mid | 317 | 141 | 176 | 44.48 | ok |
| low | T3_high | 778 | 391 | 387 | 50.26 | ok |
| medium | T1_low | 357 | 174 | 183 | 48.74 | ok |
| medium | T2_mid | 255 | 107 | 148 | 41.96 | ok |
| medium | T3_high | 1075 | 565 | 510 | 52.56 | ok |
| high | T1_low | 182 | 86 | 96 | 47.25 | ok |
| high | T2_mid | 81 | 32 | 49 | 39.51 | ok |
| high | T3_high | 607 | 331 | 276 | 54.53 | ok |
| missing | missing | 302 | 177 | 125 | 58.61 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.