# Directional Penalty Diagnostics - 2026-08-23

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **650**
- Overall success rate: **39.08%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 181 | 71 | 110 | 39.23 | ok |
| none | T2_mid | 147 | 62 | 85 | 42.18 | ok |
| none | T3_high | 104 | 45 | 59 | 43.27 | ok |
| low | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| low | T2_mid | 27 | 14 | 13 | 51.85 | ok |
| low | T3_high | 28 | 15 | 13 | 53.57 | ok |
| medium | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T3_high | 32 | 9 | 23 | 28.12 | ok |
| high | T2_mid | 5 | 1 | 4 | 20.0 | insufficient |
| high | T3_high | 22 | 5 | 17 | 22.73 | ok |
| missing | missing | 85 | 24 | 61 | 28.24 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 174 | 71 | 103 | 40.8 | ok |
| none | T2_mid | 169 | 76 | 93 | 44.97 | ok |
| none | T3_high | 161 | 62 | 99 | 38.51 | ok |
| low | T1_low | 13 | 4 | 9 | 30.77 | insufficient |
| low | T2_mid | 13 | 2 | 11 | 15.38 | insufficient |
| low | T3_high | 19 | 10 | 9 | 52.63 | insufficient |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T3_high | 5 | 1 | 4 | 20.0 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| high | T3_high | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 85 | 24 | 61 | 28.24 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2358**
- Overall success rate: **44.19%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 593 | 220 | 373 | 37.1 | ok |
| none | T2_mid | 637 | 239 | 398 | 37.52 | ok |
| none | T3_high | 420 | 202 | 218 | 48.1 | ok |
| low | T1_low | 12 | 3 | 9 | 25.0 | insufficient |
| low | T2_mid | 19 | 8 | 11 | 42.11 | insufficient |
| low | T3_high | 27 | 9 | 18 | 33.33 | ok |
| medium | T1_low | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T2_mid | 13 | 4 | 9 | 30.77 | insufficient |
| medium | T3_high | 28 | 15 | 13 | 53.57 | ok |
| high | T1_low | 29 | 8 | 21 | 27.59 | ok |
| high | T2_mid | 15 | 7 | 8 | 46.67 | insufficient |
| high | T3_high | 264 | 153 | 111 | 57.95 | ok |
| missing | missing | 295 | 171 | 124 | 57.97 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 289 | 95 | 194 | 32.87 | ok |
| none | T2_mid | 434 | 162 | 272 | 37.33 | ok |
| none | T3_high | 129 | 53 | 76 | 41.09 | ok |
| low | T1_low | 132 | 45 | 87 | 34.09 | ok |
| low | T2_mid | 104 | 30 | 74 | 28.85 | ok |
| low | T3_high | 111 | 57 | 54 | 51.35 | ok |
| medium | T1_low | 130 | 55 | 75 | 42.31 | ok |
| medium | T2_mid | 98 | 45 | 53 | 45.92 | ok |
| medium | T3_high | 246 | 118 | 128 | 47.97 | ok |
| high | T1_low | 89 | 39 | 50 | 43.82 | ok |
| high | T2_mid | 48 | 21 | 27 | 43.75 | ok |
| high | T3_high | 253 | 151 | 102 | 59.68 | ok |
| missing | missing | 295 | 171 | 124 | 57.97 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.