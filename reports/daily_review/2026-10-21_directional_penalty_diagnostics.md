# Directional Penalty Diagnostics - 2026-10-21

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1901**
- Overall success rate: **41.71%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 541 | 240 | 301 | 44.36 | ok |
| none | T2_mid | 508 | 207 | 301 | 40.75 | ok |
| none | T3_high | 388 | 169 | 219 | 43.56 | ok |
| low | T1_low | 15 | 5 | 10 | 33.33 | insufficient |
| low | T2_mid | 65 | 27 | 38 | 41.54 | ok |
| low | T3_high | 83 | 35 | 48 | 42.17 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 21 | 12 | 9 | 57.14 | ok |
| medium | T3_high | 78 | 33 | 45 | 42.31 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 12 | 4 | 8 | 33.33 | insufficient |
| high | T3_high | 81 | 35 | 46 | 43.21 | ok |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 543 | 243 | 300 | 44.75 | ok |
| none | T2_mid | 577 | 236 | 341 | 40.9 | ok |
| none | T3_high | 567 | 242 | 325 | 42.68 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 14 | 5 | 9 | 35.71 | insufficient |
| low | T3_high | 34 | 12 | 22 | 35.29 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 21 | 12 | 9 | 57.14 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **12270**
- Overall success rate: **48.97%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3920 | 1808 | 2112 | 46.12 | ok |
| none | T2_mid | 3966 | 1959 | 2007 | 49.39 | ok |
| none | T3_high | 2881 | 1462 | 1419 | 50.75 | ok |
| low | T1_low | 33 | 8 | 25 | 24.24 | ok |
| low | T2_mid | 18 | 7 | 11 | 38.89 | insufficient |
| low | T3_high | 103 | 58 | 45 | 56.31 | ok |
| medium | T1_low | 14 | 7 | 7 | 50.0 | insufficient |
| medium | T2_mid | 16 | 5 | 11 | 31.25 | insufficient |
| medium | T3_high | 103 | 55 | 48 | 53.4 | ok |
| high | T1_low | 45 | 11 | 34 | 24.44 | ok |
| high | T2_mid | 17 | 10 | 7 | 58.82 | insufficient |
| high | T3_high | 852 | 442 | 410 | 51.88 | ok |
| missing | missing | 302 | 177 | 125 | 58.61 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3150 | 1457 | 1693 | 46.25 | ok |
| none | T2_mid | 3492 | 1762 | 1730 | 50.46 | ok |
| none | T3_high | 1906 | 975 | 931 | 51.15 | ok |
| low | T1_low | 357 | 147 | 210 | 41.18 | ok |
| low | T2_mid | 231 | 90 | 141 | 38.96 | ok |
| low | T3_high | 606 | 296 | 310 | 48.84 | ok |
| medium | T1_low | 307 | 139 | 168 | 45.28 | ok |
| medium | T2_mid | 214 | 96 | 118 | 44.86 | ok |
| medium | T3_high | 925 | 477 | 448 | 51.57 | ok |
| high | T1_low | 198 | 91 | 107 | 45.96 | ok |
| high | T2_mid | 80 | 33 | 47 | 41.25 | ok |
| high | T3_high | 502 | 269 | 233 | 53.59 | ok |
| missing | missing | 302 | 177 | 125 | 58.61 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.