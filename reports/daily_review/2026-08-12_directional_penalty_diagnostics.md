# Directional Penalty Diagnostics - 2026-08-12

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **385**
- Overall success rate: **44.94%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 89 | 46 | 43 | 51.69 | ok |
| none | T2_mid | 83 | 40 | 43 | 48.19 | ok |
| none | T3_high | 58 | 31 | 27 | 53.45 | ok |
| low | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| low | T2_mid | 12 | 8 | 4 | 66.67 | insufficient |
| low | T3_high | 17 | 9 | 8 | 52.94 | insufficient |
| medium | T1_low | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T2_mid | 5 | 3 | 2 | 60.0 | insufficient |
| medium | T3_high | 15 | 6 | 9 | 40.0 | insufficient |
| high | T2_mid | 4 | 1 | 3 | 25.0 | insufficient |
| high | T3_high | 15 | 5 | 10 | 33.33 | insufficient |
| missing | missing | 82 | 22 | 60 | 26.83 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 91 | 47 | 44 | 51.65 | ok |
| none | T2_mid | 97 | 49 | 48 | 50.52 | ok |
| none | T3_high | 94 | 43 | 51 | 45.74 | ok |
| low | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| low | T2_mid | 3 | 1 | 2 | 33.33 | insufficient |
| low | T3_high | 9 | 8 | 1 | 88.89 | insufficient |
| medium | T1_low | 1 | 0 | 1 | 0.0 | insufficient |
| medium | T2_mid | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T3_high | 2 | 0 | 2 | 0.0 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 82 | 22 | 60 | 26.83 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **1824**
- Overall success rate: **41.61%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 423 | 139 | 284 | 32.86 | ok |
| none | T2_mid | 496 | 176 | 320 | 35.48 | ok |
| none | T3_high | 297 | 122 | 175 | 41.08 | ok |
| low | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| low | T2_mid | 16 | 6 | 10 | 37.5 | insufficient |
| low | T3_high | 23 | 8 | 15 | 34.78 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T3_high | 23 | 13 | 10 | 56.52 | ok |
| high | T1_low | 19 | 3 | 16 | 15.79 | insufficient |
| high | T2_mid | 22 | 10 | 12 | 45.45 | ok |
| high | T3_high | 186 | 105 | 81 | 56.45 | ok |
| missing | missing | 293 | 170 | 123 | 58.02 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 219 | 62 | 157 | 28.31 | ok |
| none | T2_mid | 321 | 111 | 210 | 34.58 | ok |
| none | T3_high | 122 | 49 | 73 | 40.16 | ok |
| low | T1_low | 104 | 32 | 72 | 30.77 | ok |
| low | T2_mid | 79 | 24 | 55 | 30.38 | ok |
| low | T3_high | 64 | 26 | 38 | 40.62 | ok |
| medium | T1_low | 87 | 35 | 52 | 40.23 | ok |
| medium | T2_mid | 94 | 36 | 58 | 38.3 | ok |
| medium | T3_high | 162 | 69 | 93 | 42.59 | ok |
| high | T1_low | 48 | 18 | 30 | 37.5 | ok |
| high | T2_mid | 50 | 23 | 27 | 46.0 | ok |
| high | T3_high | 181 | 104 | 77 | 57.46 | ok |
| missing | missing | 293 | 170 | 123 | 58.02 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.