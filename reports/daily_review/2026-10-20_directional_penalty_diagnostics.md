# Directional Penalty Diagnostics - 2026-10-20

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1826**
- Overall success rate: **41.57%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 509 | 225 | 284 | 44.2 | ok |
| none | T2_mid | 491 | 200 | 291 | 40.73 | ok |
| none | T3_high | 371 | 161 | 210 | 43.4 | ok |
| low | T1_low | 16 | 6 | 10 | 37.5 | insufficient |
| low | T2_mid | 64 | 26 | 38 | 40.62 | ok |
| low | T3_high | 81 | 35 | 46 | 43.21 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 21 | 11 | 10 | 52.38 | ok |
| medium | T3_high | 79 | 34 | 45 | 43.04 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 11 | 4 | 7 | 36.36 | insufficient |
| high | T3_high | 78 | 32 | 46 | 41.03 | ok |
| missing | missing | 99 | 23 | 76 | 23.23 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 513 | 229 | 284 | 44.64 | ok |
| none | T2_mid | 559 | 227 | 332 | 40.61 | ok |
| none | T3_high | 548 | 233 | 315 | 42.52 | ok |
| low | T1_low | 10 | 2 | 8 | 20.0 | insufficient |
| low | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| low | T3_high | 33 | 12 | 21 | 36.36 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 21 | 11 | 10 | 52.38 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 7 | 6 | 1 | 85.71 | insufficient |
| missing | missing | 99 | 23 | 76 | 23.23 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **11480**
- Overall success rate: **49.4%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3655 | 1702 | 1953 | 46.57 | ok |
| none | T2_mid | 3704 | 1858 | 1846 | 50.16 | ok |
| none | T3_high | 2672 | 1368 | 1304 | 51.2 | ok |
| low | T1_low | 34 | 8 | 26 | 23.53 | ok |
| low | T2_mid | 20 | 9 | 11 | 45.0 | ok |
| low | T3_high | 93 | 52 | 41 | 55.91 | ok |
| medium | T1_low | 13 | 6 | 7 | 46.15 | insufficient |
| medium | T2_mid | 15 | 5 | 10 | 33.33 | insufficient |
| medium | T3_high | 99 | 53 | 46 | 53.54 | ok |
| high | T1_low | 37 | 10 | 27 | 27.03 | ok |
| high | T2_mid | 18 | 10 | 8 | 55.56 | insufficient |
| high | T3_high | 827 | 421 | 406 | 50.91 | ok |
| missing | missing | 293 | 169 | 124 | 57.68 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2963 | 1387 | 1576 | 46.81 | ok |
| none | T2_mid | 3272 | 1678 | 1594 | 51.28 | ok |
| none | T3_high | 1774 | 914 | 860 | 51.52 | ok |
| low | T1_low | 327 | 140 | 187 | 42.81 | ok |
| low | T2_mid | 213 | 87 | 126 | 40.85 | ok |
| low | T3_high | 571 | 281 | 290 | 49.21 | ok |
| medium | T1_low | 274 | 119 | 155 | 43.43 | ok |
| medium | T2_mid | 196 | 88 | 108 | 44.9 | ok |
| medium | T3_high | 875 | 455 | 420 | 52.0 | ok |
| high | T1_low | 175 | 80 | 95 | 45.71 | ok |
| high | T2_mid | 76 | 29 | 47 | 38.16 | ok |
| high | T3_high | 471 | 244 | 227 | 51.8 | ok |
| missing | missing | 293 | 169 | 124 | 57.68 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.