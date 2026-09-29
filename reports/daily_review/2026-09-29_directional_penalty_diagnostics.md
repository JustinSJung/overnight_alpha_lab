# Directional Penalty Diagnostics - 2026-09-29

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1218**
- Overall success rate: **41.63%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 349 | 162 | 187 | 46.42 | ok |
| none | T2_mid | 321 | 138 | 183 | 42.99 | ok |
| none | T3_high | 239 | 105 | 134 | 43.93 | ok |
| low | T1_low | 7 | 2 | 5 | 28.57 | insufficient |
| low | T2_mid | 30 | 12 | 18 | 40.0 | ok |
| low | T3_high | 45 | 16 | 29 | 35.56 | ok |
| medium | T1_low | 5 | 0 | 5 | 0.0 | insufficient |
| medium | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| medium | T3_high | 47 | 18 | 29 | 38.3 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 8 | 3 | 5 | 37.5 | insufficient |
| high | T3_high | 50 | 19 | 31 | 38.0 | ok |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 344 | 160 | 184 | 46.51 | ok |
| none | T2_mid | 352 | 152 | 200 | 43.18 | ok |
| none | T3_high | 342 | 140 | 202 | 40.94 | ok |
| low | T1_low | 13 | 3 | 10 | 23.08 | insufficient |
| low | T2_mid | 12 | 4 | 8 | 33.33 | insufficient |
| low | T3_high | 21 | 8 | 13 | 38.1 | ok |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 7 | 4 | 3 | 57.14 | insufficient |
| medium | T3_high | 13 | 6 | 7 | 46.15 | insufficient |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 5 | 4 | 1 | 80.0 | insufficient |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **6875**
- Overall success rate: **48.22%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2089 | 965 | 1124 | 46.19 | ok |
| none | T2_mid | 2157 | 1047 | 1110 | 48.54 | ok |
| none | T3_high | 1450 | 690 | 760 | 47.59 | ok |
| low | T1_low | 22 | 3 | 19 | 13.64 | ok |
| low | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| low | T3_high | 75 | 38 | 37 | 50.67 | ok |
| medium | T1_low | 12 | 5 | 7 | 41.67 | insufficient |
| medium | T2_mid | 10 | 6 | 4 | 60.0 | insufficient |
| medium | T3_high | 69 | 33 | 36 | 47.83 | ok |
| high | T1_low | 40 | 10 | 30 | 25.0 | ok |
| high | T2_mid | 11 | 8 | 3 | 72.73 | insufficient |
| high | T3_high | 629 | 329 | 300 | 52.31 | ok |
| missing | missing | 298 | 174 | 124 | 58.39 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1500 | 681 | 819 | 45.4 | ok |
| none | T2_mid | 1864 | 921 | 943 | 49.41 | ok |
| none | T3_high | 827 | 383 | 444 | 46.31 | ok |
| low | T1_low | 280 | 111 | 169 | 39.64 | ok |
| low | T2_mid | 145 | 60 | 85 | 41.38 | ok |
| low | T3_high | 369 | 182 | 187 | 49.32 | ok |
| medium | T1_low | 232 | 118 | 114 | 50.86 | ok |
| medium | T2_mid | 120 | 61 | 59 | 50.83 | ok |
| medium | T3_high | 639 | 321 | 318 | 50.23 | ok |
| high | T1_low | 151 | 73 | 78 | 48.34 | ok |
| high | T2_mid | 62 | 26 | 36 | 41.94 | ok |
| high | T3_high | 388 | 204 | 184 | 52.58 | ok |
| missing | missing | 298 | 174 | 124 | 58.39 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.