# Directional Penalty Diagnostics - 2026-09-22

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1062**
- Overall success rate: **41.81%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 305 | 144 | 161 | 47.21 | ok |
| none | T2_mid | 272 | 123 | 149 | 45.22 | ok |
| none | T3_high | 197 | 84 | 113 | 42.64 | ok |
| low | T1_low | 9 | 4 | 5 | 44.44 | insufficient |
| low | T2_mid | 25 | 10 | 15 | 40.0 | ok |
| low | T3_high | 44 | 15 | 29 | 34.09 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 40 | 15 | 25 | 37.5 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| high | T3_high | 41 | 13 | 28 | 31.71 | ok |
| missing | missing | 102 | 24 | 78 | 23.53 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 304 | 146 | 158 | 48.03 | ok |
| none | T2_mid | 299 | 137 | 162 | 45.82 | ok |
| none | T3_high | 289 | 113 | 176 | 39.1 | ok |
| low | T1_low | 13 | 3 | 10 | 23.08 | insufficient |
| low | T2_mid | 12 | 3 | 9 | 25.0 | insufficient |
| low | T3_high | 16 | 5 | 11 | 31.25 | insufficient |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 7 | 4 | 3 | 57.14 | insufficient |
| medium | T3_high | 13 | 6 | 7 | 46.15 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 102 | 24 | 78 | 23.53 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **6142**
- Overall success rate: **46.74%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1885 | 827 | 1058 | 43.87 | ok |
| none | T2_mid | 1914 | 892 | 1022 | 46.6 | ok |
| none | T3_high | 1240 | 583 | 657 | 47.02 | ok |
| low | T1_low | 22 | 3 | 19 | 13.64 | ok |
| low | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| low | T3_high | 66 | 33 | 33 | 50.0 | ok |
| medium | T1_low | 12 | 4 | 8 | 33.33 | insufficient |
| medium | T2_mid | 11 | 6 | 5 | 54.55 | insufficient |
| medium | T3_high | 59 | 29 | 30 | 49.15 | ok |
| high | T1_low | 40 | 10 | 30 | 25.0 | ok |
| high | T2_mid | 15 | 9 | 6 | 60.0 | insufficient |
| high | T3_high | 567 | 297 | 270 | 52.38 | ok |
| missing | missing | 296 | 170 | 126 | 57.43 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1326 | 575 | 751 | 43.36 | ok |
| none | T2_mid | 1633 | 768 | 865 | 47.03 | ok |
| none | T3_high | 667 | 309 | 358 | 46.33 | ok |
| low | T1_low | 262 | 99 | 163 | 37.79 | ok |
| low | T2_mid | 147 | 60 | 87 | 40.82 | ok |
| low | T3_high | 312 | 145 | 167 | 46.47 | ok |
| medium | T1_low | 230 | 106 | 124 | 46.09 | ok |
| medium | T2_mid | 116 | 61 | 55 | 52.59 | ok |
| medium | T3_high | 593 | 294 | 299 | 49.58 | ok |
| high | T1_low | 141 | 64 | 77 | 45.39 | ok |
| high | T2_mid | 59 | 26 | 33 | 44.07 | ok |
| high | T3_high | 360 | 194 | 166 | 53.89 | ok |
| missing | missing | 296 | 170 | 126 | 57.43 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.