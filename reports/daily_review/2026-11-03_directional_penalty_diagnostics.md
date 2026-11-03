# Directional Penalty Diagnostics - 2026-11-03

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1940**
- Overall success rate: **41.24%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 526 | 232 | 294 | 44.11 | ok |
| none | T2_mid | 533 | 214 | 319 | 40.15 | ok |
| none | T3_high | 402 | 175 | 227 | 43.53 | ok |
| low | T1_low | 15 | 6 | 9 | 40.0 | insufficient |
| low | T2_mid | 67 | 27 | 40 | 40.3 | ok |
| low | T3_high | 86 | 35 | 51 | 40.7 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 19 | 11 | 8 | 57.89 | insufficient |
| medium | T3_high | 85 | 35 | 50 | 41.18 | ok |
| high | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 82 | 34 | 48 | 41.46 | ok |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 529 | 236 | 293 | 44.61 | ok |
| none | T2_mid | 604 | 242 | 362 | 40.07 | ok |
| none | T3_high | 588 | 251 | 337 | 42.69 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 13 | 6 | 7 | 46.15 | insufficient |
| low | T3_high | 38 | 11 | 27 | 28.95 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 21 | 11 | 10 | 52.38 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **15732**
- Overall success rate: **49.1%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5007 | 2300 | 2707 | 45.94 | ok |
| none | T2_mid | 5047 | 2468 | 2579 | 48.9 | ok |
| none | T3_high | 4008 | 2078 | 1930 | 51.85 | ok |
| low | T1_low | 37 | 11 | 26 | 29.73 | ok |
| low | T2_mid | 25 | 6 | 19 | 24.0 | ok |
| low | T3_high | 118 | 64 | 54 | 54.24 | ok |
| medium | T1_low | 15 | 8 | 7 | 53.33 | insufficient |
| medium | T2_mid | 20 | 6 | 14 | 30.0 | ok |
| medium | T3_high | 124 | 68 | 56 | 54.84 | ok |
| high | T1_low | 43 | 12 | 31 | 27.91 | ok |
| high | T2_mid | 20 | 10 | 10 | 50.0 | ok |
| high | T3_high | 972 | 521 | 451 | 53.6 | ok |
| missing | missing | 296 | 172 | 124 | 58.11 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4098 | 1885 | 2213 | 46.0 | ok |
| none | T2_mid | 4464 | 2225 | 2239 | 49.84 | ok |
| none | T3_high | 2797 | 1463 | 1334 | 52.31 | ok |
| low | T1_low | 442 | 181 | 261 | 40.95 | ok |
| low | T2_mid | 311 | 128 | 183 | 41.16 | ok |
| low | T3_high | 757 | 378 | 379 | 49.93 | ok |
| medium | T1_low | 362 | 170 | 192 | 46.96 | ok |
| medium | T2_mid | 252 | 104 | 148 | 41.27 | ok |
| medium | T3_high | 1075 | 565 | 510 | 52.56 | ok |
| high | T1_low | 200 | 95 | 105 | 47.5 | ok |
| high | T2_mid | 85 | 33 | 52 | 38.82 | ok |
| high | T3_high | 593 | 325 | 268 | 54.81 | ok |
| missing | missing | 296 | 172 | 124 | 58.11 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.