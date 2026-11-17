# Directional Penalty Diagnostics - 2026-11-17

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2477**
- Overall success rate: **42.27%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 701 | 307 | 394 | 43.79 | ok |
| none | T2_mid | 699 | 309 | 390 | 44.21 | ok |
| none | T3_high | 532 | 211 | 321 | 39.66 | ok |
| low | T1_low | 21 | 8 | 13 | 38.1 | ok |
| low | T2_mid | 79 | 32 | 47 | 40.51 | ok |
| low | T3_high | 115 | 50 | 65 | 43.48 | ok |
| medium | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T2_mid | 28 | 13 | 15 | 46.43 | ok |
| medium | T3_high | 100 | 44 | 56 | 44.0 | ok |
| high | T1_low | 3 | 2 | 1 | 66.67 | insufficient |
| high | T2_mid | 15 | 7 | 8 | 46.67 | insufficient |
| high | T3_high | 102 | 40 | 62 | 39.22 | ok |
| missing | missing | 75 | 21 | 54 | 28.0 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 705 | 312 | 393 | 44.26 | ok |
| none | T2_mid | 780 | 342 | 438 | 43.85 | ok |
| none | T3_high | 763 | 310 | 453 | 40.63 | ok |
| low | T1_low | 16 | 5 | 11 | 31.25 | insufficient |
| low | T2_mid | 22 | 9 | 13 | 40.91 | ok |
| low | T3_high | 50 | 14 | 36 | 28.0 | ok |
| medium | T1_low | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T2_mid | 14 | 6 | 8 | 42.86 | insufficient |
| medium | T3_high | 24 | 14 | 10 | 58.33 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 5 | 4 | 1 | 80.0 | insufficient |
| high | T3_high | 12 | 7 | 5 | 58.33 | insufficient |
| missing | missing | 75 | 21 | 54 | 28.0 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **21785**
- Overall success rate: **50.99%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 7188 | 3574 | 3614 | 49.72 | ok |
| none | T2_mid | 6998 | 3519 | 3479 | 50.29 | ok |
| none | T3_high | 5671 | 2994 | 2677 | 52.79 | ok |
| low | T1_low | 77 | 31 | 46 | 40.26 | ok |
| low | T2_mid | 56 | 27 | 29 | 48.21 | ok |
| low | T3_high | 134 | 79 | 55 | 58.96 | ok |
| medium | T1_low | 34 | 20 | 14 | 58.82 | ok |
| medium | T2_mid | 37 | 15 | 22 | 40.54 | ok |
| medium | T3_high | 143 | 79 | 64 | 55.24 | ok |
| high | T1_low | 51 | 20 | 31 | 39.22 | ok |
| high | T2_mid | 45 | 18 | 27 | 40.0 | ok |
| high | T3_high | 1098 | 592 | 506 | 53.92 | ok |
| missing | missing | 253 | 140 | 113 | 55.34 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5814 | 2899 | 2915 | 49.86 | ok |
| none | T2_mid | 6077 | 3122 | 2955 | 51.37 | ok |
| none | T3_high | 4131 | 2204 | 1927 | 53.35 | ok |
| low | T1_low | 817 | 388 | 429 | 47.49 | ok |
| low | T2_mid | 467 | 214 | 253 | 45.82 | ok |
| low | T3_high | 940 | 479 | 461 | 50.96 | ok |
| medium | T1_low | 514 | 256 | 258 | 49.81 | ok |
| medium | T2_mid | 450 | 194 | 256 | 43.11 | ok |
| medium | T3_high | 1248 | 657 | 591 | 52.64 | ok |
| high | T1_low | 205 | 102 | 103 | 49.76 | ok |
| high | T2_mid | 142 | 49 | 93 | 34.51 | ok |
| high | T3_high | 727 | 404 | 323 | 55.57 | ok |
| missing | missing | 253 | 140 | 113 | 55.34 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.