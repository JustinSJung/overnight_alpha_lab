# Directional Penalty Diagnostics - 2026-10-08

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1667**
- Overall success rate: **42.89%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 478 | 219 | 259 | 45.82 | ok |
| none | T2_mid | 435 | 183 | 252 | 42.07 | ok |
| none | T3_high | 330 | 147 | 183 | 44.55 | ok |
| low | T1_low | 12 | 5 | 7 | 41.67 | insufficient |
| low | T2_mid | 55 | 27 | 28 | 49.09 | ok |
| low | T3_high | 77 | 31 | 46 | 40.26 | ok |
| medium | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T2_mid | 18 | 9 | 9 | 50.0 | insufficient |
| medium | T3_high | 68 | 31 | 37 | 45.59 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 72 | 31 | 41 | 43.06 | ok |
| missing | missing | 102 | 24 | 78 | 23.53 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 478 | 222 | 256 | 46.44 | ok |
| none | T2_mid | 496 | 213 | 283 | 42.94 | ok |
| none | T3_high | 490 | 213 | 277 | 43.47 | ok |
| low | T1_low | 13 | 3 | 10 | 23.08 | insufficient |
| low | T2_mid | 13 | 4 | 9 | 30.77 | insufficient |
| low | T3_high | 29 | 11 | 18 | 37.93 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 10 | 6 | 4 | 60.0 | insufficient |
| medium | T3_high | 22 | 12 | 10 | 54.55 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 2 | 1 | 1 | 50.0 | insufficient |
| high | T3_high | 6 | 4 | 2 | 66.67 | insufficient |
| missing | missing | 102 | 24 | 78 | 23.53 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **8259**
- Overall success rate: **47.54%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2577 | 1186 | 1391 | 46.02 | ok |
| none | T2_mid | 2643 | 1256 | 1387 | 47.52 | ok |
| none | T3_high | 1752 | 835 | 917 | 47.66 | ok |
| low | T1_low | 26 | 4 | 22 | 15.38 | ok |
| low | T2_mid | 14 | 8 | 6 | 57.14 | insufficient |
| low | T3_high | 81 | 42 | 39 | 51.85 | ok |
| medium | T1_low | 16 | 6 | 10 | 37.5 | insufficient |
| medium | T2_mid | 12 | 8 | 4 | 66.67 | insufficient |
| medium | T3_high | 79 | 37 | 42 | 46.84 | ok |
| high | T1_low | 47 | 12 | 35 | 25.53 | ok |
| high | T2_mid | 13 | 8 | 5 | 61.54 | insufficient |
| high | T3_high | 700 | 351 | 349 | 50.14 | ok |
| missing | missing | 299 | 173 | 126 | 57.86 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1900 | 862 | 1038 | 45.37 | ok |
| none | T2_mid | 2305 | 1121 | 1184 | 48.63 | ok |
| none | T3_high | 1040 | 487 | 553 | 46.83 | ok |
| low | T1_low | 323 | 138 | 185 | 42.72 | ok |
| low | T2_mid | 176 | 65 | 111 | 36.93 | ok |
| low | T3_high | 435 | 204 | 231 | 46.9 | ok |
| medium | T1_low | 264 | 125 | 139 | 47.35 | ok |
| medium | T2_mid | 136 | 66 | 70 | 48.53 | ok |
| medium | T3_high | 713 | 353 | 360 | 49.51 | ok |
| high | T1_low | 179 | 83 | 96 | 46.37 | ok |
| high | T2_mid | 65 | 28 | 37 | 43.08 | ok |
| high | T3_high | 424 | 221 | 203 | 52.12 | ok |
| missing | missing | 299 | 173 | 126 | 57.86 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.