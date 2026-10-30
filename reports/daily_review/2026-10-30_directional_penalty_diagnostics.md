# Directional Penalty Diagnostics - 2026-10-30

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1939**
- Overall success rate: **41.05%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 548 | 241 | 307 | 43.98 | ok |
| none | T2_mid | 509 | 200 | 309 | 39.29 | ok |
| none | T3_high | 401 | 172 | 229 | 42.89 | ok |
| low | T1_low | 17 | 6 | 11 | 35.29 | insufficient |
| low | T2_mid | 68 | 30 | 38 | 44.12 | ok |
| low | T3_high | 89 | 37 | 52 | 41.57 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 20 | 12 | 8 | 60.0 | ok |
| medium | T3_high | 83 | 35 | 48 | 42.17 | ok |
| high | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 80 | 32 | 48 | 40.0 | ok |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 555 | 247 | 308 | 44.5 | ok |
| none | T2_mid | 580 | 232 | 348 | 40.0 | ok |
| none | T3_high | 586 | 246 | 340 | 41.98 | ok |
| low | T1_low | 10 | 1 | 9 | 10.0 | insufficient |
| low | T2_mid | 15 | 6 | 9 | 40.0 | insufficient |
| low | T3_high | 38 | 13 | 25 | 34.21 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 21 | 11 | 10 | 52.38 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **15024**
- Overall success rate: **50.23%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4833 | 2275 | 2558 | 47.07 | ok |
| none | T2_mid | 4892 | 2474 | 2418 | 50.57 | ok |
| none | T3_high | 3672 | 1944 | 1728 | 52.94 | ok |
| low | T1_low | 37 | 11 | 26 | 29.73 | ok |
| low | T2_mid | 26 | 7 | 19 | 26.92 | ok |
| low | T3_high | 114 | 62 | 52 | 54.39 | ok |
| medium | T1_low | 16 | 7 | 9 | 43.75 | insufficient |
| medium | T2_mid | 17 | 6 | 11 | 35.29 | insufficient |
| medium | T3_high | 120 | 64 | 56 | 53.33 | ok |
| high | T1_low | 44 | 12 | 32 | 27.27 | ok |
| high | T2_mid | 19 | 10 | 9 | 52.63 | insufficient |
| high | T3_high | 935 | 501 | 434 | 53.58 | ok |
| missing | missing | 299 | 174 | 125 | 58.19 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3976 | 1881 | 2095 | 47.31 | ok |
| none | T2_mid | 4335 | 2233 | 2102 | 51.51 | ok |
| none | T3_high | 2527 | 1351 | 1176 | 53.46 | ok |
| low | T1_low | 411 | 173 | 238 | 42.09 | ok |
| low | T2_mid | 292 | 126 | 166 | 43.15 | ok |
| low | T3_high | 718 | 367 | 351 | 51.11 | ok |
| medium | T1_low | 338 | 158 | 180 | 46.75 | ok |
| medium | T2_mid | 239 | 106 | 133 | 44.35 | ok |
| medium | T3_high | 1042 | 544 | 498 | 52.21 | ok |
| high | T1_low | 205 | 93 | 112 | 45.37 | ok |
| high | T2_mid | 88 | 32 | 56 | 36.36 | ok |
| high | T3_high | 554 | 309 | 245 | 55.78 | ok |
| missing | missing | 299 | 174 | 125 | 58.19 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.