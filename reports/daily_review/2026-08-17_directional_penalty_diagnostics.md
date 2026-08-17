# Directional Penalty Diagnostics - 2026-08-17

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **480**
- Overall success rate: **44.17%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 119 | 57 | 62 | 47.9 | ok |
| none | T2_mid | 107 | 49 | 58 | 45.79 | ok |
| none | T3_high | 78 | 38 | 40 | 48.72 | ok |
| low | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| low | T2_mid | 18 | 12 | 6 | 66.67 | insufficient |
| low | T3_high | 21 | 13 | 8 | 61.9 | ok |
| medium | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T2_mid | 7 | 4 | 3 | 57.14 | insufficient |
| medium | T3_high | 18 | 6 | 12 | 33.33 | insufficient |
| high | T2_mid | 5 | 1 | 4 | 20.0 | insufficient |
| high | T3_high | 16 | 5 | 11 | 31.25 | insufficient |
| missing | missing | 85 | 24 | 61 | 28.24 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 118 | 56 | 62 | 47.46 | ok |
| none | T2_mid | 128 | 62 | 66 | 48.44 | ok |
| none | T3_high | 116 | 51 | 65 | 43.97 | ok |
| low | T1_low | 6 | 4 | 2 | 66.67 | insufficient |
| low | T2_mid | 4 | 1 | 3 | 25.0 | insufficient |
| low | T3_high | 14 | 10 | 4 | 71.43 | insufficient |
| medium | T1_low | 1 | 0 | 1 | 0.0 | insufficient |
| medium | T2_mid | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T3_high | 3 | 1 | 2 | 33.33 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 85 | 24 | 61 | 28.24 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **1935**
- Overall success rate: **41.34%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 468 | 166 | 302 | 35.47 | ok |
| none | T2_mid | 527 | 180 | 347 | 34.16 | ok |
| none | T3_high | 308 | 121 | 187 | 39.29 | ok |
| low | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| low | T2_mid | 18 | 8 | 10 | 44.44 | insufficient |
| low | T3_high | 21 | 6 | 15 | 28.57 | ok |
| medium | T1_low | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T2_mid | 11 | 3 | 8 | 27.27 | insufficient |
| medium | T3_high | 24 | 13 | 11 | 54.17 | ok |
| high | T1_low | 20 | 4 | 16 | 20.0 | ok |
| high | T2_mid | 22 | 9 | 13 | 40.91 | ok |
| high | T3_high | 206 | 114 | 92 | 55.34 | ok |
| missing | missing | 293 | 170 | 123 | 58.02 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 240 | 72 | 168 | 30.0 | ok |
| none | T2_mid | 349 | 122 | 227 | 34.96 | ok |
| none | T3_high | 108 | 40 | 68 | 37.04 | ok |
| low | T1_low | 112 | 37 | 75 | 33.04 | ok |
| low | T2_mid | 83 | 20 | 63 | 24.1 | ok |
| low | T3_high | 70 | 27 | 43 | 38.57 | ok |
| medium | T1_low | 91 | 39 | 52 | 42.86 | ok |
| medium | T2_mid | 99 | 39 | 60 | 39.39 | ok |
| medium | T3_high | 181 | 75 | 106 | 41.44 | ok |
| high | T1_low | 62 | 28 | 34 | 45.16 | ok |
| high | T2_mid | 47 | 19 | 28 | 40.43 | ok |
| high | T3_high | 200 | 112 | 88 | 56.0 | ok |
| missing | missing | 293 | 170 | 123 | 58.02 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.