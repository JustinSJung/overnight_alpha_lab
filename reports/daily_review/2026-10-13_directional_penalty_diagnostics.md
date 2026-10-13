# Directional Penalty Diagnostics - 2026-10-13

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1786**
- Overall success rate: **40.99%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 503 | 223 | 280 | 44.33 | ok |
| none | T2_mid | 472 | 183 | 289 | 38.77 | ok |
| none | T3_high | 362 | 158 | 204 | 43.65 | ok |
| low | T1_low | 15 | 6 | 9 | 40.0 | insufficient |
| low | T2_mid | 63 | 24 | 39 | 38.1 | ok |
| low | T3_high | 78 | 32 | 46 | 41.03 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 19 | 10 | 9 | 52.63 | insufficient |
| medium | T3_high | 73 | 34 | 39 | 46.58 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 81 | 31 | 50 | 38.27 | ok |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 504 | 227 | 277 | 45.04 | ok |
| none | T2_mid | 539 | 208 | 331 | 38.59 | ok |
| none | T3_high | 535 | 228 | 307 | 42.62 | ok |
| low | T1_low | 12 | 2 | 10 | 16.67 | insufficient |
| low | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| low | T3_high | 31 | 11 | 20 | 35.48 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 20 | 11 | 9 | 55.0 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 5 | 3 | 62.5 | insufficient |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **8851**
- Overall success rate: **50.43%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2685 | 1322 | 1363 | 49.24 | ok |
| none | T2_mid | 2899 | 1462 | 1437 | 50.43 | ok |
| none | T3_high | 1945 | 992 | 953 | 51.0 | ok |
| low | T1_low | 25 | 5 | 20 | 20.0 | ok |
| low | T2_mid | 14 | 8 | 6 | 57.14 | insufficient |
| low | T3_high | 79 | 44 | 35 | 55.7 | ok |
| medium | T1_low | 17 | 7 | 10 | 41.18 | insufficient |
| medium | T2_mid | 11 | 6 | 5 | 54.55 | insufficient |
| medium | T3_high | 87 | 43 | 44 | 49.43 | ok |
| high | T1_low | 45 | 9 | 36 | 20.0 | ok |
| high | T2_mid | 14 | 9 | 5 | 64.29 | insufficient |
| high | T3_high | 727 | 381 | 346 | 52.41 | ok |
| missing | missing | 303 | 176 | 127 | 58.09 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2008 | 1000 | 1008 | 49.8 | ok |
| none | T2_mid | 2533 | 1303 | 1230 | 51.44 | ok |
| none | T3_high | 1204 | 612 | 592 | 50.83 | ok |
| low | T1_low | 323 | 140 | 183 | 43.34 | ok |
| low | T2_mid | 176 | 72 | 104 | 40.91 | ok |
| low | T3_high | 461 | 230 | 231 | 49.89 | ok |
| medium | T1_low | 275 | 127 | 148 | 46.18 | ok |
| medium | T2_mid | 154 | 77 | 77 | 50.0 | ok |
| medium | T3_high | 751 | 386 | 365 | 51.4 | ok |
| high | T1_low | 166 | 76 | 90 | 45.78 | ok |
| high | T2_mid | 75 | 33 | 42 | 44.0 | ok |
| high | T3_high | 422 | 232 | 190 | 54.98 | ok |
| missing | missing | 303 | 176 | 127 | 58.09 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.