# Directional Penalty Diagnostics - 2026-09-04

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **779**
- Overall success rate: **40.18%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 212 | 92 | 120 | 43.4 | ok |
| none | T2_mid | 184 | 74 | 110 | 40.22 | ok |
| none | T3_high | 135 | 63 | 72 | 46.67 | ok |
| low | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| low | T2_mid | 21 | 9 | 12 | 42.86 | ok |
| low | T3_high | 32 | 16 | 16 | 50.0 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 8 | 3 | 5 | 37.5 | insufficient |
| medium | T3_high | 34 | 13 | 21 | 38.24 | ok |
| high | T2_mid | 10 | 3 | 7 | 30.0 | insufficient |
| high | T3_high | 34 | 11 | 23 | 32.35 | ok |
| missing | missing | 97 | 24 | 73 | 24.74 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 211 | 95 | 116 | 45.02 | ok |
| none | T2_mid | 203 | 84 | 119 | 41.38 | ok |
| none | T3_high | 199 | 84 | 115 | 42.21 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 13 | 4 | 9 | 30.77 | insufficient |
| low | T3_high | 22 | 10 | 12 | 45.45 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 7 | 1 | 6 | 14.29 | insufficient |
| medium | T3_high | 10 | 6 | 4 | 60.0 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 97 | 24 | 73 | 24.74 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **3389**
- Overall success rate: **44.02%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 972 | 358 | 614 | 36.83 | ok |
| none | T2_mid | 976 | 404 | 572 | 41.39 | ok |
| none | T3_high | 604 | 292 | 312 | 48.34 | ok |
| low | T1_low | 16 | 3 | 13 | 18.75 | insufficient |
| low | T2_mid | 16 | 8 | 8 | 50.0 | insufficient |
| low | T3_high | 43 | 20 | 23 | 46.51 | ok |
| medium | T1_low | 11 | 5 | 6 | 45.45 | insufficient |
| medium | T2_mid | 10 | 3 | 7 | 30.0 | insufficient |
| medium | T3_high | 38 | 18 | 20 | 47.37 | ok |
| high | T1_low | 33 | 5 | 28 | 15.15 | ok |
| high | T2_mid | 16 | 11 | 5 | 68.75 | insufficient |
| high | T3_high | 364 | 199 | 165 | 54.67 | ok |
| missing | missing | 290 | 166 | 124 | 57.24 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 571 | 194 | 377 | 33.98 | ok |
| none | T2_mid | 697 | 282 | 415 | 40.46 | ok |
| none | T3_high | 227 | 101 | 126 | 44.49 | ok |
| low | T1_low | 192 | 62 | 130 | 32.29 | ok |
| low | T2_mid | 158 | 61 | 97 | 38.61 | ok |
| low | T3_high | 204 | 102 | 102 | 50.0 | ok |
| medium | T1_low | 163 | 69 | 94 | 42.33 | ok |
| medium | T2_mid | 111 | 51 | 60 | 45.95 | ok |
| medium | T3_high | 353 | 177 | 176 | 50.14 | ok |
| high | T1_low | 106 | 46 | 60 | 43.4 | ok |
| high | T2_mid | 52 | 32 | 20 | 61.54 | ok |
| high | T3_high | 265 | 149 | 116 | 56.23 | ok |
| missing | missing | 290 | 166 | 124 | 57.24 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.