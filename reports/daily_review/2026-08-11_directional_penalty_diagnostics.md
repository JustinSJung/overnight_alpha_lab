# Directional Penalty Diagnostics - 2026-08-11

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **271**
- Overall success rate: **49.08%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 61 | 37 | 24 | 60.66 | ok |
| none | T2_mid | 49 | 27 | 22 | 55.1 | ok |
| none | T3_high | 27 | 18 | 9 | 66.67 | ok |
| low | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| low | T2_mid | 8 | 6 | 2 | 75.0 | insufficient |
| low | T3_high | 13 | 8 | 5 | 61.54 | insufficient |
| medium | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| medium | T2_mid | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T3_high | 10 | 5 | 5 | 50.0 | insufficient |
| high | T2_mid | 4 | 1 | 3 | 25.0 | insufficient |
| high | T3_high | 8 | 3 | 5 | 37.5 | insufficient |
| missing | missing | 84 | 24 | 60 | 28.57 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 63 | 38 | 25 | 60.32 | ok |
| none | T2_mid | 61 | 34 | 27 | 55.74 | ok |
| none | T3_high | 52 | 29 | 23 | 55.77 | ok |
| low | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| low | T3_high | 5 | 5 | 0 | 100.0 | insufficient |
| medium | T2_mid | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T3_high | 1 | 0 | 1 | 0.0 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 84 | 24 | 60 | 28.57 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **1705**
- Overall success rate: **41.76%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 405 | 134 | 271 | 33.09 | ok |
| none | T2_mid | 451 | 160 | 291 | 35.48 | ok |
| none | T3_high | 285 | 118 | 167 | 41.4 | ok |
| low | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| low | T2_mid | 13 | 6 | 7 | 46.15 | insufficient |
| low | T3_high | 20 | 7 | 13 | 35.0 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T3_high | 22 | 13 | 9 | 59.09 | ok |
| high | T1_low | 18 | 3 | 15 | 16.67 | insufficient |
| high | T2_mid | 23 | 10 | 13 | 43.48 | ok |
| high | T3_high | 156 | 88 | 68 | 56.41 | ok |
| missing | missing | 286 | 166 | 120 | 58.04 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 211 | 59 | 152 | 27.96 | ok |
| none | T2_mid | 285 | 98 | 187 | 34.39 | ok |
| none | T3_high | 136 | 52 | 84 | 38.24 | ok |
| low | T1_low | 98 | 32 | 66 | 32.65 | ok |
| low | T2_mid | 73 | 23 | 50 | 31.51 | ok |
| low | T3_high | 61 | 26 | 35 | 42.62 | ok |
| medium | T1_low | 87 | 35 | 52 | 40.23 | ok |
| medium | T2_mid | 89 | 35 | 54 | 39.33 | ok |
| medium | T3_high | 138 | 61 | 77 | 44.2 | ok |
| high | T1_low | 43 | 16 | 27 | 37.21 | ok |
| high | T2_mid | 50 | 22 | 28 | 44.0 | ok |
| high | T3_high | 148 | 87 | 61 | 58.78 | ok |
| missing | missing | 286 | 166 | 120 | 58.04 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.