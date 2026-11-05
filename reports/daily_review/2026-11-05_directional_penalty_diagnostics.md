# Directional Penalty Diagnostics - 2026-11-05

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2042**
- Overall success rate: **41.33%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 555 | 247 | 308 | 44.5 | ok |
| none | T2_mid | 559 | 221 | 338 | 39.53 | ok |
| none | T3_high | 428 | 185 | 243 | 43.22 | ok |
| low | T1_low | 19 | 7 | 12 | 36.84 | insufficient |
| low | T2_mid | 68 | 27 | 41 | 39.71 | ok |
| low | T3_high | 95 | 40 | 55 | 42.11 | ok |
| medium | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T2_mid | 21 | 12 | 9 | 57.14 | ok |
| medium | T3_high | 84 | 34 | 50 | 40.48 | ok |
| high | T1_low | 3 | 2 | 1 | 66.67 | insufficient |
| high | T2_mid | 13 | 6 | 7 | 46.15 | insufficient |
| high | T3_high | 88 | 37 | 51 | 42.05 | ok |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 563 | 254 | 309 | 45.12 | ok |
| none | T2_mid | 631 | 251 | 380 | 39.78 | ok |
| none | T3_high | 623 | 263 | 360 | 42.22 | ok |
| low | T1_low | 12 | 2 | 10 | 16.67 | insufficient |
| low | T2_mid | 14 | 6 | 8 | 42.86 | insufficient |
| low | T3_high | 39 | 13 | 26 | 33.33 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| medium | T3_high | 23 | 13 | 10 | 56.52 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 10 | 7 | 3 | 70.0 | insufficient |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **17032**
- Overall success rate: **49.71%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5235 | 2498 | 2737 | 47.72 | ok |
| none | T2_mid | 5577 | 2748 | 2829 | 49.27 | ok |
| none | T3_high | 4523 | 2321 | 2202 | 51.32 | ok |
| low | T1_low | 34 | 10 | 24 | 29.41 | ok |
| low | T2_mid | 34 | 12 | 22 | 35.29 | ok |
| low | T3_high | 124 | 68 | 56 | 54.84 | ok |
| medium | T1_low | 14 | 7 | 7 | 50.0 | insufficient |
| medium | T2_mid | 20 | 6 | 14 | 30.0 | ok |
| medium | T3_high | 129 | 69 | 60 | 53.49 | ok |
| high | T1_low | 42 | 12 | 30 | 28.57 | ok |
| high | T2_mid | 19 | 9 | 10 | 47.37 | insufficient |
| high | T3_high | 978 | 529 | 449 | 54.09 | ok |
| missing | missing | 303 | 177 | 126 | 58.42 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4263 | 2034 | 2229 | 47.71 | ok |
| none | T2_mid | 4927 | 2477 | 2450 | 50.27 | ok |
| none | T3_high | 3231 | 1672 | 1559 | 51.75 | ok |
| low | T1_low | 478 | 204 | 274 | 42.68 | ok |
| low | T2_mid | 341 | 147 | 194 | 43.11 | ok |
| low | T3_high | 791 | 394 | 397 | 49.81 | ok |
| medium | T1_low | 385 | 192 | 193 | 49.87 | ok |
| medium | T2_mid | 288 | 122 | 166 | 42.36 | ok |
| medium | T3_high | 1112 | 582 | 530 | 52.34 | ok |
| high | T1_low | 199 | 97 | 102 | 48.74 | ok |
| high | T2_mid | 94 | 29 | 65 | 30.85 | ok |
| high | T3_high | 620 | 339 | 281 | 54.68 | ok |
| missing | missing | 303 | 177 | 126 | 58.42 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.