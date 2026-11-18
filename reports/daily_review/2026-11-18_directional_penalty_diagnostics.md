# Directional Penalty Diagnostics - 2026-11-18

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2633**
- Overall success rate: **41.4%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 754 | 319 | 435 | 42.31 | ok |
| none | T2_mid | 736 | 311 | 425 | 42.26 | ok |
| none | T3_high | 571 | 231 | 340 | 40.46 | ok |
| low | T1_low | 23 | 8 | 15 | 34.78 | ok |
| low | T2_mid | 82 | 32 | 50 | 39.02 | ok |
| low | T3_high | 124 | 53 | 71 | 42.74 | ok |
| medium | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T2_mid | 29 | 14 | 15 | 48.28 | ok |
| medium | T3_high | 103 | 45 | 58 | 43.69 | ok |
| high | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| high | T2_mid | 15 | 7 | 8 | 46.67 | insufficient |
| high | T3_high | 110 | 44 | 66 | 40.0 | ok |
| missing | missing | 75 | 21 | 54 | 28.0 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 760 | 324 | 436 | 42.63 | ok |
| none | T2_mid | 819 | 346 | 473 | 42.25 | ok |
| none | T3_high | 814 | 332 | 482 | 40.79 | ok |
| low | T1_low | 17 | 5 | 12 | 29.41 | insufficient |
| low | T2_mid | 23 | 7 | 16 | 30.43 | ok |
| low | T3_high | 54 | 18 | 36 | 33.33 | ok |
| medium | T1_low | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T2_mid | 16 | 8 | 8 | 50.0 | insufficient |
| medium | T3_high | 27 | 16 | 11 | 59.26 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 4 | 3 | 1 | 75.0 | insufficient |
| high | T3_high | 13 | 7 | 6 | 53.85 | insufficient |
| missing | missing | 75 | 21 | 54 | 28.0 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **22107**
- Overall success rate: **51.26%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 7137 | 3538 | 3599 | 49.57 | ok |
| none | T2_mid | 7108 | 3626 | 3482 | 51.01 | ok |
| none | T3_high | 5886 | 3111 | 2775 | 52.85 | ok |
| low | T1_low | 76 | 31 | 45 | 40.79 | ok |
| low | T2_mid | 57 | 30 | 27 | 52.63 | ok |
| low | T3_high | 138 | 78 | 60 | 56.52 | ok |
| medium | T1_low | 31 | 18 | 13 | 58.06 | ok |
| medium | T2_mid | 37 | 15 | 22 | 40.54 | ok |
| medium | T3_high | 143 | 80 | 63 | 55.94 | ok |
| high | T1_low | 48 | 18 | 30 | 37.5 | ok |
| high | T2_mid | 49 | 21 | 28 | 42.86 | ok |
| high | T3_high | 1144 | 626 | 518 | 54.72 | ok |
| missing | missing | 253 | 139 | 114 | 54.94 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5819 | 2895 | 2924 | 49.75 | ok |
| none | T2_mid | 6151 | 3199 | 2952 | 52.01 | ok |
| none | T3_high | 4325 | 2299 | 2026 | 53.16 | ok |
| low | T1_low | 802 | 376 | 426 | 46.88 | ok |
| low | T2_mid | 475 | 222 | 253 | 46.74 | ok |
| low | T3_high | 944 | 492 | 452 | 52.12 | ok |
| medium | T1_low | 482 | 240 | 242 | 49.79 | ok |
| medium | T2_mid | 474 | 212 | 262 | 44.73 | ok |
| medium | T3_high | 1289 | 682 | 607 | 52.91 | ok |
| high | T1_low | 189 | 94 | 95 | 49.74 | ok |
| high | T2_mid | 151 | 59 | 92 | 39.07 | ok |
| high | T3_high | 753 | 422 | 331 | 56.04 | ok |
| missing | missing | 253 | 139 | 114 | 54.94 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.