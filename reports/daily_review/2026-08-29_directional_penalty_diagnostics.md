# Directional Penalty Diagnostics - 2026-08-29

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **644**
- Overall success rate: **39.29%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 165 | 69 | 96 | 41.82 | ok |
| none | T2_mid | 141 | 56 | 85 | 39.72 | ok |
| none | T3_high | 100 | 48 | 52 | 48.0 | ok |
| low | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| low | T2_mid | 21 | 11 | 10 | 52.38 | ok |
| low | T3_high | 26 | 13 | 13 | 50.0 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 8 | 3 | 5 | 37.5 | insufficient |
| medium | T3_high | 32 | 13 | 19 | 40.62 | ok |
| high | T2_mid | 8 | 2 | 6 | 25.0 | insufficient |
| high | T3_high | 31 | 10 | 21 | 32.26 | ok |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 162 | 70 | 92 | 43.21 | ok |
| none | T2_mid | 157 | 66 | 91 | 42.04 | ok |
| none | T3_high | 159 | 69 | 90 | 43.4 | ok |
| low | T1_low | 12 | 3 | 9 | 25.0 | insufficient |
| low | T2_mid | 11 | 2 | 9 | 18.18 | insufficient |
| low | T3_high | 20 | 10 | 10 | 50.0 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 8 | 2 | 6 | 25.0 | insufficient |
| medium | T3_high | 8 | 4 | 4 | 50.0 | insufficient |
| high | T2_mid | 2 | 2 | 0 | 100.0 | insufficient |
| high | T3_high | 2 | 1 | 1 | 50.0 | insufficient |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2744**
- Overall success rate: **43.08%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 777 | 290 | 487 | 37.32 | ok |
| none | T2_mid | 770 | 284 | 486 | 36.88 | ok |
| none | T3_high | 444 | 211 | 233 | 47.52 | ok |
| low | T1_low | 14 | 3 | 11 | 21.43 | insufficient |
| low | T2_mid | 20 | 9 | 11 | 45.0 | ok |
| low | T3_high | 33 | 12 | 21 | 36.36 | ok |
| medium | T1_low | 9 | 5 | 4 | 55.56 | insufficient |
| medium | T2_mid | 13 | 4 | 9 | 30.77 | insufficient |
| medium | T3_high | 34 | 16 | 18 | 47.06 | ok |
| high | T1_low | 29 | 8 | 21 | 27.59 | ok |
| high | T2_mid | 19 | 10 | 9 | 52.63 | insufficient |
| high | T3_high | 280 | 154 | 126 | 55.0 | ok |
| missing | missing | 302 | 176 | 126 | 58.28 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 416 | 146 | 270 | 35.1 | ok |
| none | T2_mid | 503 | 178 | 325 | 35.39 | ok |
| none | T3_high | 132 | 54 | 78 | 40.91 | ok |
| low | T1_low | 167 | 52 | 115 | 31.14 | ok |
| low | T2_mid | 152 | 50 | 102 | 32.89 | ok |
| low | T3_high | 139 | 70 | 69 | 50.36 | ok |
| medium | T1_low | 145 | 62 | 83 | 42.76 | ok |
| medium | T2_mid | 119 | 54 | 65 | 45.38 | ok |
| medium | T3_high | 279 | 135 | 144 | 48.39 | ok |
| high | T1_low | 101 | 46 | 55 | 45.54 | ok |
| high | T2_mid | 48 | 25 | 23 | 52.08 | ok |
| high | T3_high | 241 | 134 | 107 | 55.6 | ok |
| missing | missing | 302 | 176 | 126 | 58.28 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.