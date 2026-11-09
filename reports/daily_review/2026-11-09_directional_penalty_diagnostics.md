# Directional Penalty Diagnostics - 2026-11-09

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2126**
- Overall success rate: **41.96%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 570 | 252 | 318 | 44.21 | ok |
| none | T2_mid | 582 | 240 | 342 | 41.24 | ok |
| none | T3_high | 463 | 201 | 262 | 43.41 | ok |
| low | T1_low | 17 | 6 | 11 | 35.29 | insufficient |
| low | T2_mid | 71 | 30 | 41 | 42.25 | ok |
| low | T3_high | 94 | 39 | 55 | 41.49 | ok |
| medium | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T2_mid | 24 | 13 | 11 | 54.17 | ok |
| medium | T3_high | 88 | 38 | 50 | 43.18 | ok |
| high | T1_low | 3 | 2 | 1 | 66.67 | insufficient |
| high | T2_mid | 13 | 6 | 7 | 46.15 | insufficient |
| high | T3_high | 97 | 39 | 58 | 40.21 | ok |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 571 | 257 | 314 | 45.01 | ok |
| none | T2_mid | 657 | 273 | 384 | 41.55 | ok |
| none | T3_high | 666 | 283 | 383 | 42.49 | ok |
| low | T1_low | 13 | 2 | 11 | 15.38 | insufficient |
| low | T2_mid | 16 | 6 | 10 | 37.5 | insufficient |
| low | T3_high | 43 | 14 | 29 | 32.56 | ok |
| medium | T1_low | 8 | 1 | 7 | 12.5 | insufficient |
| medium | T2_mid | 14 | 8 | 6 | 57.14 | insufficient |
| medium | T3_high | 23 | 13 | 10 | 56.52 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 10 | 7 | 3 | 70.0 | insufficient |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **18068**
- Overall success rate: **51.98%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5568 | 2918 | 2650 | 52.41 | ok |
| none | T2_mid | 5921 | 3027 | 2894 | 51.12 | ok |
| none | T3_high | 4862 | 2534 | 2328 | 52.12 | ok |
| low | T1_low | 43 | 17 | 26 | 39.53 | ok |
| low | T2_mid | 39 | 18 | 21 | 46.15 | ok |
| low | T3_high | 124 | 73 | 51 | 58.87 | ok |
| medium | T1_low | 14 | 8 | 6 | 57.14 | insufficient |
| medium | T2_mid | 21 | 7 | 14 | 33.33 | ok |
| medium | T3_high | 130 | 70 | 60 | 53.85 | ok |
| high | T1_low | 44 | 13 | 31 | 29.55 | ok |
| high | T2_mid | 20 | 7 | 13 | 35.0 | ok |
| high | T3_high | 987 | 527 | 460 | 53.39 | ok |
| missing | missing | 295 | 172 | 123 | 58.31 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4525 | 2367 | 2158 | 52.31 | ok |
| none | T2_mid | 5219 | 2725 | 2494 | 52.21 | ok |
| none | T3_high | 3542 | 1861 | 1681 | 52.54 | ok |
| low | T1_low | 553 | 283 | 270 | 51.18 | ok |
| low | T2_mid | 382 | 173 | 209 | 45.29 | ok |
| low | T3_high | 829 | 418 | 411 | 50.42 | ok |
| medium | T1_low | 412 | 218 | 194 | 52.91 | ok |
| medium | T2_mid | 307 | 135 | 172 | 43.97 | ok |
| medium | T3_high | 1119 | 588 | 531 | 52.55 | ok |
| high | T1_low | 179 | 88 | 91 | 49.16 | ok |
| high | T2_mid | 93 | 26 | 67 | 27.96 | ok |
| high | T3_high | 613 | 337 | 276 | 54.98 | ok |
| missing | missing | 295 | 172 | 123 | 58.31 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.