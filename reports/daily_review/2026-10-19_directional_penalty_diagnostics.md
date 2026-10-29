# Directional Penalty Diagnostics - 2026-10-19

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1863**
- Overall success rate: **41.22%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 526 | 231 | 295 | 43.92 | ok |
| none | T2_mid | 505 | 203 | 302 | 40.2 | ok |
| none | T3_high | 373 | 160 | 213 | 42.9 | ok |
| low | T1_low | 16 | 6 | 10 | 37.5 | insufficient |
| low | T2_mid | 65 | 26 | 39 | 40.0 | ok |
| low | T3_high | 79 | 32 | 47 | 40.51 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 19 | 10 | 9 | 52.63 | insufficient |
| medium | T3_high | 79 | 35 | 44 | 44.3 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 81 | 34 | 47 | 41.98 | ok |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 528 | 235 | 293 | 44.51 | ok |
| none | T2_mid | 573 | 230 | 343 | 40.14 | ok |
| none | T3_high | 550 | 233 | 317 | 42.36 | ok |
| low | T1_low | 12 | 2 | 10 | 16.67 | insufficient |
| low | T2_mid | 14 | 5 | 9 | 35.71 | insufficient |
| low | T3_high | 32 | 10 | 22 | 31.25 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 22 | 12 | 10 | 54.55 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **11197**
- Overall success rate: **49.4%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3532 | 1692 | 1840 | 47.9 | ok |
| none | T2_mid | 3597 | 1775 | 1822 | 49.35 | ok |
| none | T3_high | 2597 | 1301 | 1296 | 50.1 | ok |
| low | T1_low | 33 | 8 | 25 | 24.24 | ok |
| low | T2_mid | 20 | 9 | 11 | 45.0 | ok |
| low | T3_high | 102 | 56 | 46 | 54.9 | ok |
| medium | T1_low | 14 | 7 | 7 | 50.0 | insufficient |
| medium | T2_mid | 15 | 5 | 10 | 33.33 | insufficient |
| medium | T3_high | 100 | 52 | 48 | 52.0 | ok |
| high | T1_low | 41 | 11 | 30 | 26.83 | ok |
| high | T2_mid | 18 | 10 | 8 | 55.56 | insufficient |
| high | T3_high | 826 | 427 | 399 | 51.69 | ok |
| missing | missing | 302 | 178 | 124 | 58.94 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2835 | 1366 | 1469 | 48.18 | ok |
| none | T2_mid | 3174 | 1591 | 1583 | 50.13 | ok |
| none | T3_high | 1720 | 870 | 850 | 50.58 | ok |
| low | T1_low | 342 | 145 | 197 | 42.4 | ok |
| low | T2_mid | 210 | 86 | 124 | 40.95 | ok |
| low | T3_high | 555 | 272 | 283 | 49.01 | ok |
| medium | T1_low | 273 | 127 | 146 | 46.52 | ok |
| medium | T2_mid | 200 | 93 | 107 | 46.5 | ok |
| medium | T3_high | 864 | 443 | 421 | 51.27 | ok |
| high | T1_low | 170 | 80 | 90 | 47.06 | ok |
| high | T2_mid | 66 | 29 | 37 | 43.94 | ok |
| high | T3_high | 486 | 251 | 235 | 51.65 | ok |
| missing | missing | 302 | 178 | 124 | 58.94 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.