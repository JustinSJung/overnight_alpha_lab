# Directional Penalty Diagnostics - 2026-08-11

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **324**
- Overall success rate: **47.84%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 78 | 46 | 32 | 58.97 | ok |
| none | T2_mid | 62 | 34 | 28 | 54.84 | ok |
| none | T3_high | 39 | 22 | 17 | 56.41 | ok |
| low | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| low | T2_mid | 10 | 7 | 3 | 70.0 | insufficient |
| low | T3_high | 13 | 7 | 6 | 53.85 | insufficient |
| medium | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| medium | T2_mid | 5 | 3 | 2 | 60.0 | insufficient |
| medium | T3_high | 12 | 5 | 7 | 41.67 | insufficient |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 0 | 3 | 0.0 | insufficient |
| high | T3_high | 14 | 5 | 9 | 35.71 | insufficient |
| missing | missing | 83 | 23 | 60 | 27.71 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 82 | 48 | 34 | 58.54 | ok |
| none | T2_mid | 76 | 42 | 34 | 55.26 | ok |
| none | T3_high | 70 | 33 | 37 | 47.14 | ok |
| low | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| low | T3_high | 7 | 6 | 1 | 85.71 | insufficient |
| medium | T2_mid | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T3_high | 1 | 0 | 1 | 0.0 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 83 | 23 | 60 | 27.71 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **1766**
- Overall success rate: **41.62%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 412 | 134 | 278 | 32.52 | ok |
| none | T2_mid | 474 | 169 | 305 | 35.65 | ok |
| none | T3_high | 292 | 121 | 171 | 41.44 | ok |
| low | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| low | T2_mid | 16 | 6 | 10 | 37.5 | insufficient |
| low | T3_high | 22 | 8 | 14 | 36.36 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T3_high | 22 | 13 | 9 | 59.09 | ok |
| high | T1_low | 18 | 3 | 15 | 16.67 | insufficient |
| high | T2_mid | 23 | 10 | 13 | 43.48 | ok |
| high | T3_high | 177 | 99 | 78 | 55.93 | ok |
| missing | missing | 284 | 165 | 119 | 58.1 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 214 | 59 | 155 | 27.57 | ok |
| none | T2_mid | 302 | 104 | 198 | 34.44 | ok |
| none | T3_high | 129 | 51 | 78 | 39.53 | ok |
| low | T1_low | 101 | 32 | 69 | 31.68 | ok |
| low | T2_mid | 77 | 24 | 53 | 31.17 | ok |
| low | T3_high | 63 | 26 | 37 | 41.27 | ok |
| medium | T1_low | 87 | 35 | 52 | 40.23 | ok |
| medium | T2_mid | 93 | 36 | 57 | 38.71 | ok |
| medium | T3_high | 154 | 68 | 86 | 44.16 | ok |
| high | T1_low | 44 | 16 | 28 | 36.36 | ok |
| high | T2_mid | 51 | 23 | 28 | 45.1 | ok |
| high | T3_high | 167 | 96 | 71 | 57.49 | ok |
| missing | missing | 284 | 165 | 119 | 58.1 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.