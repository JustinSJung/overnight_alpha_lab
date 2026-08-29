# Directional Penalty Diagnostics - 2026-08-29

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **636**
- Overall success rate: **39.62%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 162 | 67 | 95 | 41.36 | ok |
| none | T2_mid | 138 | 56 | 82 | 40.58 | ok |
| none | T3_high | 102 | 49 | 53 | 48.04 | ok |
| low | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| low | T2_mid | 20 | 10 | 10 | 50.0 | ok |
| low | T3_high | 27 | 14 | 13 | 51.85 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 8 | 3 | 5 | 37.5 | insufficient |
| medium | T3_high | 32 | 13 | 19 | 40.62 | ok |
| high | T2_mid | 8 | 2 | 6 | 25.0 | insufficient |
| high | T3_high | 31 | 10 | 21 | 32.26 | ok |
| missing | missing | 97 | 24 | 73 | 24.74 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 160 | 69 | 91 | 43.12 | ok |
| none | T2_mid | 152 | 64 | 88 | 42.11 | ok |
| none | T3_high | 162 | 71 | 91 | 43.83 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 12 | 3 | 9 | 25.0 | insufficient |
| low | T3_high | 20 | 10 | 10 | 50.0 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 8 | 2 | 6 | 25.0 | insufficient |
| medium | T3_high | 8 | 4 | 4 | 50.0 | insufficient |
| high | T2_mid | 2 | 2 | 0 | 100.0 | insufficient |
| high | T3_high | 2 | 1 | 1 | 50.0 | insufficient |
| missing | missing | 97 | 24 | 73 | 24.74 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2665**
- Overall success rate: **42.81%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 745 | 272 | 473 | 36.51 | ok |
| none | T2_mid | 751 | 278 | 473 | 37.02 | ok |
| none | T3_high | 430 | 203 | 227 | 47.21 | ok |
| low | T1_low | 14 | 3 | 11 | 21.43 | insufficient |
| low | T2_mid | 20 | 9 | 11 | 45.0 | ok |
| low | T3_high | 33 | 12 | 21 | 36.36 | ok |
| medium | T1_low | 9 | 5 | 4 | 55.56 | insufficient |
| medium | T2_mid | 13 | 4 | 9 | 30.77 | insufficient |
| medium | T3_high | 34 | 16 | 18 | 47.06 | ok |
| high | T1_low | 29 | 8 | 21 | 27.59 | ok |
| high | T2_mid | 20 | 11 | 9 | 55.0 | ok |
| high | T3_high | 276 | 150 | 126 | 54.35 | ok |
| missing | missing | 291 | 170 | 121 | 58.42 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 399 | 134 | 265 | 33.58 | ok |
| none | T2_mid | 486 | 173 | 313 | 35.6 | ok |
| none | T3_high | 132 | 54 | 78 | 40.91 | ok |
| low | T1_low | 163 | 50 | 113 | 30.67 | ok |
| low | T2_mid | 152 | 50 | 102 | 32.89 | ok |
| low | T3_high | 138 | 70 | 68 | 50.72 | ok |
| medium | T1_low | 139 | 61 | 78 | 43.88 | ok |
| medium | T2_mid | 117 | 53 | 64 | 45.3 | ok |
| medium | T3_high | 276 | 134 | 142 | 48.55 | ok |
| high | T1_low | 96 | 43 | 53 | 44.79 | ok |
| high | T2_mid | 49 | 26 | 23 | 53.06 | ok |
| high | T3_high | 227 | 123 | 104 | 54.19 | ok |
| missing | missing | 291 | 170 | 121 | 58.42 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.