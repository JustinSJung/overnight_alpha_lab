# Directional Penalty Diagnostics - 2026-11-16

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2442**
- Overall success rate: **42.47%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 703 | 313 | 390 | 44.52 | ok |
| none | T2_mid | 689 | 298 | 391 | 43.25 | ok |
| none | T3_high | 505 | 207 | 298 | 40.99 | ok |
| low | T1_low | 20 | 8 | 12 | 40.0 | ok |
| low | T2_mid | 79 | 31 | 48 | 39.24 | ok |
| low | T3_high | 115 | 49 | 66 | 42.61 | ok |
| medium | T1_low | 8 | 3 | 5 | 37.5 | insufficient |
| medium | T2_mid | 28 | 14 | 14 | 50.0 | ok |
| medium | T3_high | 100 | 43 | 57 | 43.0 | ok |
| high | T1_low | 3 | 2 | 1 | 66.67 | insufficient |
| high | T2_mid | 15 | 7 | 8 | 46.67 | insufficient |
| high | T3_high | 102 | 41 | 61 | 40.2 | ok |
| missing | missing | 75 | 21 | 54 | 28.0 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 707 | 318 | 389 | 44.98 | ok |
| none | T2_mid | 771 | 332 | 439 | 43.06 | ok |
| none | T3_high | 738 | 303 | 435 | 41.06 | ok |
| low | T1_low | 16 | 5 | 11 | 31.25 | insufficient |
| low | T2_mid | 19 | 6 | 13 | 31.58 | insufficient |
| low | T3_high | 46 | 15 | 31 | 32.61 | ok |
| medium | T1_low | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T2_mid | 16 | 8 | 8 | 50.0 | insufficient |
| medium | T3_high | 26 | 15 | 11 | 57.69 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 5 | 4 | 1 | 80.0 | insufficient |
| high | T3_high | 12 | 7 | 5 | 58.33 | insufficient |
| missing | missing | 75 | 21 | 54 | 28.0 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **21369**
- Overall success rate: **50.26%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 7043 | 3452 | 3591 | 49.01 | ok |
| none | T2_mid | 6868 | 3406 | 3462 | 49.59 | ok |
| none | T3_high | 5561 | 2884 | 2677 | 51.86 | ok |
| low | T1_low | 76 | 32 | 44 | 42.11 | ok |
| low | T2_mid | 58 | 29 | 29 | 50.0 | ok |
| low | T3_high | 137 | 80 | 57 | 58.39 | ok |
| medium | T1_low | 33 | 19 | 14 | 57.58 | ok |
| medium | T2_mid | 38 | 15 | 23 | 39.47 | ok |
| medium | T3_high | 140 | 78 | 62 | 55.71 | ok |
| high | T1_low | 52 | 20 | 32 | 38.46 | ok |
| high | T2_mid | 40 | 17 | 23 | 42.5 | ok |
| high | T3_high | 1073 | 570 | 503 | 53.12 | ok |
| missing | missing | 250 | 137 | 113 | 54.8 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5745 | 2825 | 2920 | 49.17 | ok |
| none | T2_mid | 5996 | 3032 | 2964 | 50.57 | ok |
| none | T3_high | 4096 | 2149 | 1947 | 52.47 | ok |
| low | T1_low | 791 | 369 | 422 | 46.65 | ok |
| low | T2_mid | 464 | 211 | 253 | 45.47 | ok |
| low | T3_high | 882 | 449 | 433 | 50.91 | ok |
| medium | T1_low | 489 | 239 | 250 | 48.88 | ok |
| medium | T2_mid | 430 | 180 | 250 | 41.86 | ok |
| medium | T3_high | 1246 | 643 | 603 | 51.61 | ok |
| high | T1_low | 179 | 90 | 89 | 50.28 | ok |
| high | T2_mid | 114 | 44 | 70 | 38.6 | ok |
| high | T3_high | 687 | 371 | 316 | 54.0 | ok |
| missing | missing | 250 | 137 | 113 | 54.8 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.