# Directional Penalty Diagnostics - 2026-08-31

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **690**
- Overall success rate: **38.12%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 184 | 72 | 112 | 39.13 | ok |
| none | T2_mid | 148 | 57 | 91 | 38.51 | ok |
| none | T3_high | 113 | 53 | 60 | 46.9 | ok |
| low | T1_low | 8 | 2 | 6 | 25.0 | insufficient |
| low | T2_mid | 23 | 10 | 13 | 43.48 | ok |
| low | T3_high | 29 | 15 | 14 | 51.72 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 8 | 3 | 5 | 37.5 | insufficient |
| medium | T3_high | 33 | 13 | 20 | 39.39 | ok |
| high | T2_mid | 9 | 2 | 7 | 22.22 | insufficient |
| high | T3_high | 33 | 10 | 23 | 30.3 | ok |
| missing | missing | 97 | 24 | 73 | 24.74 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 184 | 74 | 110 | 40.22 | ok |
| none | T2_mid | 166 | 65 | 101 | 39.16 | ok |
| none | T3_high | 177 | 75 | 102 | 42.37 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 12 | 3 | 9 | 25.0 | insufficient |
| low | T3_high | 20 | 10 | 10 | 50.0 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 8 | 2 | 6 | 25.0 | insufficient |
| medium | T3_high | 9 | 5 | 4 | 55.56 | insufficient |
| high | T2_mid | 2 | 2 | 0 | 100.0 | insufficient |
| high | T3_high | 2 | 1 | 1 | 50.0 | insufficient |
| missing | missing | 97 | 24 | 73 | 24.74 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2695**
- Overall success rate: **43.82%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 752 | 283 | 469 | 37.63 | ok |
| none | T2_mid | 754 | 289 | 465 | 38.33 | ok |
| none | T3_high | 435 | 210 | 225 | 48.28 | ok |
| low | T1_low | 17 | 3 | 14 | 17.65 | insufficient |
| low | T2_mid | 14 | 7 | 7 | 50.0 | insufficient |
| low | T3_high | 34 | 13 | 21 | 38.24 | ok |
| medium | T1_low | 9 | 5 | 4 | 55.56 | insufficient |
| medium | T2_mid | 15 | 6 | 9 | 40.0 | insufficient |
| medium | T3_high | 33 | 15 | 18 | 45.45 | ok |
| high | T1_low | 29 | 8 | 21 | 27.59 | ok |
| high | T2_mid | 20 | 12 | 8 | 60.0 | ok |
| high | T3_high | 292 | 160 | 132 | 54.79 | ok |
| missing | missing | 291 | 170 | 121 | 58.42 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 403 | 138 | 265 | 34.24 | ok |
| none | T2_mid | 479 | 180 | 299 | 37.58 | ok |
| none | T3_high | 137 | 60 | 77 | 43.8 | ok |
| low | T1_low | 167 | 54 | 113 | 32.34 | ok |
| low | T2_mid | 152 | 49 | 103 | 32.24 | ok |
| low | T3_high | 148 | 78 | 70 | 52.7 | ok |
| medium | T1_low | 141 | 63 | 78 | 44.68 | ok |
| medium | T2_mid | 121 | 57 | 64 | 47.11 | ok |
| medium | T3_high | 282 | 137 | 145 | 48.58 | ok |
| high | T1_low | 96 | 44 | 52 | 45.83 | ok |
| high | T2_mid | 51 | 28 | 23 | 54.9 | ok |
| high | T3_high | 227 | 123 | 104 | 54.19 | ok |
| missing | missing | 291 | 170 | 121 | 58.42 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.