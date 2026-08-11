# Directional Penalty Diagnostics - 2026-08-11

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **325**
- Overall success rate: **47.38%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 76 | 43 | 33 | 56.58 | ok |
| none | T2_mid | 61 | 34 | 27 | 55.74 | ok |
| none | T3_high | 42 | 23 | 19 | 54.76 | ok |
| low | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| low | T2_mid | 9 | 6 | 3 | 66.67 | insufficient |
| low | T3_high | 14 | 8 | 6 | 57.14 | insufficient |
| medium | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| medium | T2_mid | 5 | 3 | 2 | 60.0 | insufficient |
| medium | T3_high | 12 | 5 | 7 | 41.67 | insufficient |
| high | T2_mid | 4 | 1 | 3 | 25.0 | insufficient |
| high | T3_high | 14 | 5 | 9 | 35.71 | insufficient |
| missing | missing | 84 | 24 | 60 | 28.57 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 79 | 44 | 35 | 55.7 | ok |
| none | T2_mid | 75 | 42 | 33 | 56.0 | ok |
| none | T3_high | 74 | 35 | 39 | 47.3 | ok |
| low | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| low | T3_high | 7 | 6 | 1 | 85.71 | insufficient |
| medium | T2_mid | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T3_high | 1 | 0 | 1 | 0.0 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 84 | 24 | 60 | 28.57 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **1771**
- Overall success rate: **42.07%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 412 | 135 | 277 | 32.77 | ok |
| none | T2_mid | 475 | 169 | 306 | 35.58 | ok |
| none | T3_high | 290 | 125 | 165 | 43.1 | ok |
| low | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| low | T2_mid | 16 | 7 | 9 | 43.75 | insufficient |
| low | T3_high | 22 | 8 | 14 | 36.36 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T3_high | 22 | 13 | 9 | 59.09 | ok |
| high | T1_low | 18 | 3 | 15 | 16.67 | insufficient |
| high | T2_mid | 23 | 10 | 13 | 43.48 | ok |
| high | T3_high | 177 | 100 | 77 | 56.5 | ok |
| missing | missing | 290 | 168 | 122 | 57.93 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 214 | 59 | 155 | 27.57 | ok |
| none | T2_mid | 304 | 105 | 199 | 34.54 | ok |
| none | T3_high | 127 | 50 | 77 | 39.37 | ok |
| low | T1_low | 101 | 32 | 69 | 31.68 | ok |
| low | T2_mid | 76 | 23 | 53 | 30.26 | ok |
| low | T3_high | 63 | 26 | 37 | 41.27 | ok |
| medium | T1_low | 87 | 35 | 52 | 40.23 | ok |
| medium | T2_mid | 93 | 37 | 56 | 39.78 | ok |
| medium | T3_high | 154 | 72 | 82 | 46.75 | ok |
| high | T1_low | 44 | 17 | 27 | 38.64 | ok |
| high | T2_mid | 51 | 23 | 28 | 45.1 | ok |
| high | T3_high | 167 | 98 | 69 | 58.68 | ok |
| missing | missing | 290 | 168 | 122 | 57.93 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.