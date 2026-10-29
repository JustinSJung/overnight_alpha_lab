# Directional Penalty Diagnostics - 2026-10-29

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1953**
- Overall success rate: **41.22%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 545 | 244 | 301 | 44.77 | ok |
| none | T2_mid | 523 | 207 | 316 | 39.58 | ok |
| none | T3_high | 399 | 172 | 227 | 43.11 | ok |
| low | T1_low | 17 | 6 | 11 | 35.29 | insufficient |
| low | T2_mid | 68 | 28 | 40 | 41.18 | ok |
| low | T3_high | 90 | 36 | 54 | 40.0 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 21 | 12 | 9 | 57.14 | ok |
| medium | T3_high | 82 | 35 | 47 | 42.68 | ok |
| high | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 84 | 34 | 50 | 40.48 | ok |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 550 | 249 | 301 | 45.27 | ok |
| none | T2_mid | 596 | 237 | 359 | 39.77 | ok |
| none | T3_high | 590 | 246 | 344 | 41.69 | ok |
| low | T1_low | 11 | 1 | 10 | 9.09 | insufficient |
| low | T2_mid | 14 | 6 | 8 | 42.86 | insufficient |
| low | T3_high | 35 | 13 | 22 | 37.14 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 22 | 12 | 10 | 54.55 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 104 | 24 | 80 | 23.08 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **15021**
- Overall success rate: **50.1%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4781 | 2257 | 2524 | 47.21 | ok |
| none | T2_mid | 4862 | 2444 | 2418 | 50.27 | ok |
| none | T3_high | 3758 | 1984 | 1774 | 52.79 | ok |
| low | T1_low | 34 | 10 | 24 | 29.41 | ok |
| low | T2_mid | 26 | 7 | 19 | 26.92 | ok |
| low | T3_high | 116 | 64 | 52 | 55.17 | ok |
| medium | T1_low | 14 | 6 | 8 | 42.86 | insufficient |
| medium | T2_mid | 18 | 6 | 12 | 33.33 | insufficient |
| medium | T3_high | 120 | 63 | 57 | 52.5 | ok |
| high | T1_low | 41 | 9 | 32 | 21.95 | ok |
| high | T2_mid | 19 | 10 | 9 | 52.63 | insufficient |
| high | T3_high | 926 | 489 | 437 | 52.81 | ok |
| missing | missing | 306 | 177 | 129 | 57.84 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3932 | 1865 | 2067 | 47.43 | ok |
| none | T2_mid | 4310 | 2209 | 2101 | 51.25 | ok |
| none | T3_high | 2613 | 1386 | 1227 | 53.04 | ok |
| low | T1_low | 409 | 170 | 239 | 41.56 | ok |
| low | T2_mid | 288 | 126 | 162 | 43.75 | ok |
| low | T3_high | 718 | 368 | 350 | 51.25 | ok |
| medium | T1_low | 335 | 157 | 178 | 46.87 | ok |
| medium | T2_mid | 238 | 99 | 139 | 41.6 | ok |
| medium | T3_high | 1037 | 545 | 492 | 52.56 | ok |
| high | T1_low | 194 | 90 | 104 | 46.39 | ok |
| high | T2_mid | 89 | 33 | 56 | 37.08 | ok |
| high | T3_high | 552 | 301 | 251 | 54.53 | ok |
| missing | missing | 306 | 177 | 129 | 57.84 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.