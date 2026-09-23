# Directional Penalty Diagnostics - 2026-09-23

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1112**
- Overall success rate: **42.0%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 318 | 148 | 170 | 46.54 | ok |
| none | T2_mid | 287 | 127 | 160 | 44.25 | ok |
| none | T3_high | 210 | 92 | 118 | 43.81 | ok |
| low | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| low | T2_mid | 26 | 10 | 16 | 38.46 | ok |
| low | T3_high | 48 | 18 | 30 | 37.5 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 42 | 16 | 26 | 38.1 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| high | T3_high | 46 | 17 | 29 | 36.96 | ok |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 315 | 149 | 166 | 47.3 | ok |
| none | T2_mid | 313 | 141 | 172 | 45.05 | ok |
| none | T3_high | 308 | 124 | 184 | 40.26 | ok |
| low | T1_low | 13 | 3 | 10 | 23.08 | insufficient |
| low | T2_mid | 15 | 4 | 11 | 26.67 | insufficient |
| low | T3_high | 19 | 8 | 11 | 42.11 | insufficient |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T3_high | 14 | 7 | 7 | 50.0 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 5 | 4 | 1 | 80.0 | insufficient |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **6344**
- Overall success rate: **47.59%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1938 | 872 | 1066 | 44.99 | ok |
| none | T2_mid | 1987 | 950 | 1037 | 47.81 | ok |
| none | T3_high | 1309 | 616 | 693 | 47.06 | ok |
| low | T1_low | 21 | 3 | 18 | 14.29 | ok |
| low | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| low | T3_high | 69 | 32 | 37 | 46.38 | ok |
| medium | T1_low | 12 | 4 | 8 | 33.33 | insufficient |
| medium | T2_mid | 10 | 5 | 5 | 50.0 | insufficient |
| medium | T3_high | 64 | 32 | 32 | 50.0 | ok |
| high | T1_low | 37 | 11 | 26 | 29.73 | ok |
| high | T2_mid | 13 | 8 | 5 | 61.54 | insufficient |
| high | T3_high | 577 | 307 | 270 | 53.21 | ok |
| missing | missing | 295 | 172 | 123 | 58.31 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1366 | 611 | 755 | 44.73 | ok |
| none | T2_mid | 1693 | 824 | 869 | 48.67 | ok |
| none | T3_high | 709 | 331 | 378 | 46.69 | ok |
| low | T1_low | 277 | 111 | 166 | 40.07 | ok |
| low | T2_mid | 148 | 61 | 87 | 41.22 | ok |
| low | T3_high | 340 | 159 | 181 | 46.76 | ok |
| medium | T1_low | 215 | 98 | 117 | 45.58 | ok |
| medium | T2_mid | 118 | 58 | 60 | 49.15 | ok |
| medium | T3_high | 603 | 301 | 302 | 49.92 | ok |
| high | T1_low | 150 | 70 | 80 | 46.67 | ok |
| high | T2_mid | 63 | 27 | 36 | 42.86 | ok |
| high | T3_high | 367 | 196 | 171 | 53.41 | ok |
| missing | missing | 295 | 172 | 123 | 58.31 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.