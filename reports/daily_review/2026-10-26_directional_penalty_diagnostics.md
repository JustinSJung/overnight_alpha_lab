# Directional Penalty Diagnostics - 2026-10-26

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1958**
- Overall success rate: **40.91%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 556 | 248 | 308 | 44.6 | ok |
| none | T2_mid | 530 | 208 | 322 | 39.25 | ok |
| none | T3_high | 398 | 169 | 229 | 42.46 | ok |
| low | T1_low | 17 | 6 | 11 | 35.29 | insufficient |
| low | T2_mid | 68 | 29 | 39 | 42.65 | ok |
| low | T3_high | 87 | 34 | 53 | 39.08 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 21 | 12 | 9 | 57.14 | ok |
| medium | T3_high | 79 | 33 | 46 | 41.77 | ok |
| high | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| high | T2_mid | 12 | 4 | 8 | 33.33 | insufficient |
| high | T3_high | 81 | 33 | 48 | 40.74 | ok |
| missing | missing | 102 | 23 | 79 | 22.55 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 560 | 252 | 308 | 45.0 | ok |
| none | T2_mid | 605 | 240 | 365 | 39.67 | ok |
| none | T3_high | 584 | 242 | 342 | 41.44 | ok |
| low | T1_low | 12 | 2 | 10 | 16.67 | insufficient |
| low | T2_mid | 11 | 4 | 7 | 36.36 | insufficient |
| low | T3_high | 31 | 9 | 22 | 29.03 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 22 | 12 | 10 | 54.55 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 102 | 23 | 79 | 22.55 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **13619**
- Overall success rate: **51.44%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4238 | 2102 | 2136 | 49.6 | ok |
| none | T2_mid | 4445 | 2301 | 2144 | 51.77 | ok |
| none | T3_high | 3371 | 1784 | 1587 | 52.92 | ok |
| low | T1_low | 32 | 9 | 23 | 28.12 | ok |
| low | T2_mid | 19 | 8 | 11 | 42.11 | insufficient |
| low | T3_high | 108 | 58 | 50 | 53.7 | ok |
| medium | T1_low | 14 | 7 | 7 | 50.0 | insufficient |
| medium | T2_mid | 16 | 6 | 10 | 37.5 | insufficient |
| medium | T3_high | 110 | 62 | 48 | 56.36 | ok |
| high | T1_low | 39 | 9 | 30 | 23.08 | ok |
| high | T2_mid | 13 | 8 | 5 | 61.54 | insufficient |
| high | T3_high | 917 | 480 | 437 | 52.34 | ok |
| missing | missing | 297 | 172 | 125 | 57.91 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3479 | 1747 | 1732 | 50.22 | ok |
| none | T2_mid | 3934 | 2093 | 1841 | 53.2 | ok |
| none | T3_high | 2301 | 1232 | 1069 | 53.54 | ok |
| low | T1_low | 347 | 151 | 196 | 43.52 | ok |
| low | T2_mid | 260 | 110 | 150 | 42.31 | ok |
| low | T3_high | 662 | 331 | 331 | 50.0 | ok |
| medium | T1_low | 305 | 140 | 165 | 45.9 | ok |
| medium | T2_mid | 223 | 96 | 127 | 43.05 | ok |
| medium | T3_high | 992 | 527 | 465 | 53.12 | ok |
| high | T1_low | 192 | 89 | 103 | 46.35 | ok |
| high | T2_mid | 76 | 24 | 52 | 31.58 | ok |
| high | T3_high | 551 | 294 | 257 | 53.36 | ok |
| missing | missing | 297 | 172 | 125 | 57.91 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.