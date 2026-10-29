# Directional Penalty Diagnostics - 2026-10-22

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1919**
- Overall success rate: **41.22%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 542 | 243 | 299 | 44.83 | ok |
| none | T2_mid | 511 | 202 | 309 | 39.53 | ok |
| none | T3_high | 397 | 171 | 226 | 43.07 | ok |
| low | T1_low | 16 | 6 | 10 | 37.5 | insufficient |
| low | T2_mid | 67 | 27 | 40 | 40.3 | ok |
| low | T3_high | 83 | 33 | 50 | 39.76 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 21 | 12 | 9 | 57.14 | ok |
| medium | T3_high | 77 | 32 | 45 | 41.56 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 12 | 4 | 8 | 33.33 | insufficient |
| high | T3_high | 83 | 35 | 48 | 42.17 | ok |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 544 | 247 | 297 | 45.4 | ok |
| none | T2_mid | 582 | 230 | 352 | 39.52 | ok |
| none | T3_high | 578 | 242 | 336 | 41.87 | ok |
| low | T1_low | 12 | 2 | 10 | 16.67 | insufficient |
| low | T2_mid | 14 | 6 | 8 | 42.86 | insufficient |
| low | T3_high | 32 | 11 | 21 | 34.38 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 22 | 12 | 10 | 54.55 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **12643**
- Overall success rate: **49.26%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4107 | 1907 | 2200 | 46.43 | ok |
| none | T2_mid | 4056 | 2007 | 2049 | 49.48 | ok |
| none | T3_high | 2962 | 1525 | 1437 | 51.49 | ok |
| low | T1_low | 34 | 9 | 25 | 26.47 | ok |
| low | T2_mid | 18 | 8 | 10 | 44.44 | insufficient |
| low | T3_high | 107 | 59 | 48 | 55.14 | ok |
| medium | T1_low | 13 | 6 | 7 | 46.15 | insufficient |
| medium | T2_mid | 16 | 5 | 11 | 31.25 | insufficient |
| medium | T3_high | 103 | 56 | 47 | 54.37 | ok |
| high | T1_low | 41 | 11 | 30 | 26.83 | ok |
| high | T2_mid | 16 | 9 | 7 | 56.25 | insufficient |
| high | T3_high | 867 | 449 | 418 | 51.79 | ok |
| missing | missing | 303 | 177 | 126 | 58.42 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3360 | 1567 | 1793 | 46.64 | ok |
| none | T2_mid | 3596 | 1830 | 1766 | 50.89 | ok |
| none | T3_high | 1980 | 1023 | 957 | 51.67 | ok |
| low | T1_low | 360 | 150 | 210 | 41.67 | ok |
| low | T2_mid | 242 | 92 | 150 | 38.02 | ok |
| low | T3_high | 631 | 317 | 314 | 50.24 | ok |
| medium | T1_low | 302 | 139 | 163 | 46.03 | ok |
| medium | T2_mid | 205 | 83 | 122 | 40.49 | ok |
| medium | T3_high | 935 | 491 | 444 | 52.51 | ok |
| high | T1_low | 173 | 77 | 96 | 44.51 | ok |
| high | T2_mid | 63 | 24 | 39 | 38.1 | ok |
| high | T3_high | 493 | 258 | 235 | 52.33 | ok |
| missing | missing | 303 | 177 | 126 | 58.42 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.