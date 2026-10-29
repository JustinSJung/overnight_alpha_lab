# Directional Penalty Diagnostics - 2026-10-06

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1451**
- Overall success rate: **44.45%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 420 | 199 | 221 | 47.38 | ok |
| none | T2_mid | 388 | 175 | 213 | 45.1 | ok |
| none | T3_high | 269 | 125 | 144 | 46.47 | ok |
| low | T1_low | 10 | 4 | 6 | 40.0 | insufficient |
| low | T2_mid | 40 | 18 | 22 | 45.0 | ok |
| low | T3_high | 64 | 28 | 36 | 43.75 | ok |
| medium | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T2_mid | 16 | 9 | 7 | 56.25 | insufficient |
| medium | T3_high | 59 | 28 | 31 | 47.46 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 11 | 5 | 6 | 45.45 | insufficient |
| high | T3_high | 62 | 27 | 35 | 43.55 | ok |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 418 | 201 | 217 | 48.09 | ok |
| none | T2_mid | 429 | 197 | 232 | 45.92 | ok |
| none | T3_high | 404 | 183 | 221 | 45.3 | ok |
| low | T1_low | 13 | 3 | 10 | 23.08 | insufficient |
| low | T2_mid | 15 | 4 | 11 | 26.67 | insufficient |
| low | T3_high | 24 | 10 | 14 | 41.67 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 10 | 6 | 4 | 60.0 | insufficient |
| medium | T3_high | 21 | 11 | 10 | 52.38 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 5 | 4 | 1 | 80.0 | insufficient |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **8054**
- Overall success rate: **47.13%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2531 | 1157 | 1374 | 45.71 | ok |
| none | T2_mid | 2523 | 1170 | 1353 | 46.37 | ok |
| none | T3_high | 1699 | 802 | 897 | 47.2 | ok |
| low | T1_low | 24 | 3 | 21 | 12.5 | ok |
| low | T2_mid | 14 | 8 | 6 | 57.14 | insufficient |
| low | T3_high | 81 | 42 | 39 | 51.85 | ok |
| medium | T1_low | 16 | 7 | 9 | 43.75 | insufficient |
| medium | T2_mid | 12 | 8 | 4 | 66.67 | insufficient |
| medium | T3_high | 82 | 39 | 43 | 47.56 | ok |
| high | T1_low | 49 | 12 | 37 | 24.49 | ok |
| high | T2_mid | 13 | 8 | 5 | 61.54 | insufficient |
| high | T3_high | 700 | 359 | 341 | 51.29 | ok |
| missing | missing | 310 | 181 | 129 | 58.39 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1827 | 822 | 1005 | 44.99 | ok |
| none | T2_mid | 2183 | 1025 | 1158 | 46.95 | ok |
| none | T3_high | 988 | 456 | 532 | 46.15 | ok |
| low | T1_low | 330 | 137 | 193 | 41.52 | ok |
| low | T2_mid | 171 | 67 | 104 | 39.18 | ok |
| low | T3_high | 428 | 202 | 226 | 47.2 | ok |
| medium | T1_low | 285 | 139 | 146 | 48.77 | ok |
| medium | T2_mid | 141 | 71 | 70 | 50.35 | ok |
| medium | T3_high | 713 | 352 | 361 | 49.37 | ok |
| high | T1_low | 178 | 81 | 97 | 45.51 | ok |
| high | T2_mid | 67 | 31 | 36 | 46.27 | ok |
| high | T3_high | 433 | 232 | 201 | 53.58 | ok |
| missing | missing | 310 | 181 | 129 | 58.39 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.