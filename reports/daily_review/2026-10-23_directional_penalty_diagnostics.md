# Directional Penalty Diagnostics - 2026-10-23

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1941**
- Overall success rate: **41.16%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 545 | 241 | 304 | 44.22 | ok |
| none | T2_mid | 523 | 209 | 314 | 39.96 | ok |
| none | T3_high | 398 | 170 | 228 | 42.71 | ok |
| low | T1_low | 17 | 6 | 11 | 35.29 | insufficient |
| low | T2_mid | 65 | 28 | 37 | 43.08 | ok |
| low | T3_high | 89 | 34 | 55 | 38.2 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 20 | 12 | 8 | 60.0 | ok |
| medium | T3_high | 78 | 34 | 44 | 43.59 | ok |
| high | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 83 | 35 | 48 | 42.17 | ok |
| missing | missing | 103 | 23 | 80 | 22.33 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 550 | 245 | 305 | 44.55 | ok |
| none | T2_mid | 593 | 241 | 352 | 40.64 | ok |
| none | T3_high | 584 | 245 | 339 | 41.95 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 13 | 4 | 9 | 30.77 | insufficient |
| low | T3_high | 35 | 11 | 24 | 31.43 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 21 | 11 | 10 | 52.38 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 103 | 23 | 80 | 22.33 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **13068**
- Overall success rate: **50.86%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4105 | 1958 | 2147 | 47.7 | ok |
| none | T2_mid | 4238 | 2190 | 2048 | 51.68 | ok |
| none | T3_high | 3183 | 1690 | 1493 | 53.09 | ok |
| low | T1_low | 32 | 8 | 24 | 25.0 | ok |
| low | T2_mid | 19 | 8 | 11 | 42.11 | insufficient |
| low | T3_high | 106 | 59 | 47 | 55.66 | ok |
| medium | T1_low | 13 | 6 | 7 | 46.15 | insufficient |
| medium | T2_mid | 16 | 6 | 10 | 37.5 | insufficient |
| medium | T3_high | 108 | 62 | 46 | 57.41 | ok |
| high | T1_low | 40 | 9 | 31 | 22.5 | ok |
| high | T2_mid | 15 | 9 | 6 | 60.0 | insufficient |
| high | T3_high | 892 | 465 | 427 | 52.13 | ok |
| missing | missing | 301 | 177 | 124 | 58.8 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3336 | 1610 | 1726 | 48.26 | ok |
| none | T2_mid | 3747 | 1989 | 1758 | 53.08 | ok |
| none | T3_high | 2132 | 1144 | 988 | 53.66 | ok |
| low | T1_low | 353 | 146 | 207 | 41.36 | ok |
| low | T2_mid | 250 | 103 | 147 | 41.2 | ok |
| low | T3_high | 655 | 330 | 325 | 50.38 | ok |
| medium | T1_low | 314 | 141 | 173 | 44.9 | ok |
| medium | T2_mid | 215 | 94 | 121 | 43.72 | ok |
| medium | T3_high | 992 | 530 | 462 | 53.43 | ok |
| high | T1_low | 187 | 84 | 103 | 44.92 | ok |
| high | T2_mid | 76 | 27 | 49 | 35.53 | ok |
| high | T3_high | 510 | 272 | 238 | 53.33 | ok |
| missing | missing | 301 | 177 | 124 | 58.8 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.