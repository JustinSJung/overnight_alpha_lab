# Directional Penalty Diagnostics - 2026-09-30

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1236**
- Overall success rate: **42.39%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 356 | 164 | 192 | 46.07 | ok |
| none | T2_mid | 331 | 149 | 182 | 45.02 | ok |
| none | T3_high | 238 | 104 | 134 | 43.7 | ok |
| low | T1_low | 9 | 3 | 6 | 33.33 | insufficient |
| low | T2_mid | 32 | 13 | 19 | 40.62 | ok |
| low | T3_high | 51 | 22 | 29 | 43.14 | ok |
| medium | T1_low | 4 | 1 | 3 | 25.0 | insufficient |
| medium | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| medium | T3_high | 48 | 18 | 30 | 37.5 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 9 | 3 | 6 | 33.33 | insufficient |
| high | T3_high | 45 | 15 | 30 | 33.33 | ok |
| missing | missing | 99 | 24 | 75 | 24.24 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 353 | 164 | 189 | 46.46 | ok |
| none | T2_mid | 364 | 163 | 201 | 44.78 | ok |
| none | T3_high | 341 | 139 | 202 | 40.76 | ok |
| low | T1_low | 12 | 3 | 9 | 25.0 | insufficient |
| low | T2_mid | 12 | 4 | 8 | 33.33 | insufficient |
| low | T3_high | 23 | 9 | 14 | 39.13 | ok |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 8 | 5 | 3 | 62.5 | insufficient |
| medium | T3_high | 13 | 7 | 6 | 53.85 | insufficient |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 5 | 4 | 1 | 80.0 | insufficient |
| missing | missing | 99 | 24 | 75 | 24.24 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **7239**
- Overall success rate: **47.35%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2220 | 1010 | 1210 | 45.5 | ok |
| none | T2_mid | 2279 | 1065 | 1214 | 46.73 | ok |
| none | T3_high | 1540 | 728 | 812 | 47.27 | ok |
| low | T1_low | 20 | 3 | 17 | 15.0 | ok |
| low | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| low | T3_high | 75 | 37 | 38 | 49.33 | ok |
| medium | T1_low | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 76 | 38 | 38 | 50.0 | ok |
| high | T1_low | 42 | 11 | 31 | 26.19 | ok |
| high | T2_mid | 13 | 8 | 5 | 61.54 | insufficient |
| high | T3_high | 639 | 336 | 303 | 52.58 | ok |
| missing | missing | 300 | 174 | 126 | 58.0 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1618 | 723 | 895 | 44.68 | ok |
| none | T2_mid | 1981 | 935 | 1046 | 47.2 | ok |
| none | T3_high | 888 | 415 | 473 | 46.73 | ok |
| low | T1_low | 276 | 115 | 161 | 41.67 | ok |
| low | T2_mid | 146 | 63 | 83 | 43.15 | ok |
| low | T3_high | 380 | 186 | 194 | 48.95 | ok |
| medium | T1_low | 242 | 115 | 127 | 47.52 | ok |
| medium | T2_mid | 125 | 61 | 64 | 48.8 | ok |
| medium | T3_high | 657 | 326 | 331 | 49.62 | ok |
| high | T1_low | 156 | 75 | 81 | 48.08 | ok |
| high | T2_mid | 65 | 28 | 37 | 43.08 | ok |
| high | T3_high | 405 | 212 | 193 | 52.35 | ok |
| missing | missing | 300 | 174 | 126 | 58.0 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.