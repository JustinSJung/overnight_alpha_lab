# Directional Penalty Diagnostics - 2026-09-09

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **833**
- Overall success rate: **41.3%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 226 | 101 | 125 | 44.69 | ok |
| none | T2_mid | 206 | 87 | 119 | 42.23 | ok |
| none | T3_high | 148 | 70 | 78 | 47.3 | ok |
| low | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| low | T2_mid | 23 | 11 | 12 | 47.83 | ok |
| low | T3_high | 34 | 16 | 18 | 47.06 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 9 | 4 | 5 | 44.44 | insufficient |
| medium | T3_high | 34 | 13 | 21 | 38.24 | ok |
| high | T2_mid | 9 | 3 | 6 | 33.33 | insufficient |
| high | T3_high | 35 | 11 | 24 | 31.43 | ok |
| missing | missing | 97 | 24 | 73 | 24.74 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 225 | 103 | 122 | 45.78 | ok |
| none | T2_mid | 227 | 100 | 127 | 44.05 | ok |
| none | T3_high | 214 | 91 | 123 | 42.52 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| low | T3_high | 22 | 10 | 12 | 45.45 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 6 | 1 | 5 | 16.67 | insufficient |
| medium | T3_high | 11 | 6 | 5 | 54.55 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 97 | 24 | 73 | 24.74 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **3919**
- Overall success rate: **44.73%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1152 | 447 | 705 | 38.8 | ok |
| none | T2_mid | 1155 | 501 | 654 | 43.38 | ok |
| none | T3_high | 714 | 339 | 375 | 47.48 | ok |
| low | T1_low | 19 | 3 | 16 | 15.79 | insufficient |
| low | T2_mid | 16 | 8 | 8 | 50.0 | insufficient |
| low | T3_high | 48 | 24 | 24 | 50.0 | ok |
| medium | T1_low | 12 | 5 | 7 | 41.67 | insufficient |
| medium | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T3_high | 42 | 19 | 23 | 45.24 | ok |
| high | T1_low | 33 | 5 | 28 | 15.15 | ok |
| high | T2_mid | 14 | 9 | 5 | 64.29 | insufficient |
| high | T3_high | 410 | 220 | 190 | 53.66 | ok |
| missing | missing | 294 | 169 | 125 | 57.48 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 724 | 267 | 457 | 36.88 | ok |
| none | T2_mid | 885 | 383 | 502 | 43.28 | ok |
| none | T3_high | 304 | 139 | 165 | 45.72 | ok |
| low | T1_low | 212 | 73 | 139 | 34.43 | ok |
| low | T2_mid | 156 | 61 | 95 | 39.1 | ok |
| low | T3_high | 228 | 109 | 119 | 47.81 | ok |
| medium | T1_low | 166 | 71 | 95 | 42.77 | ok |
| medium | T2_mid | 107 | 52 | 55 | 48.6 | ok |
| medium | T3_high | 379 | 183 | 196 | 48.28 | ok |
| high | T1_low | 114 | 49 | 65 | 42.98 | ok |
| high | T2_mid | 47 | 26 | 21 | 55.32 | ok |
| high | T3_high | 303 | 171 | 132 | 56.44 | ok |
| missing | missing | 294 | 169 | 125 | 57.48 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.