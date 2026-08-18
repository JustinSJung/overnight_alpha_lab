# Directional Penalty Diagnostics - 2026-08-18

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **583**
- Overall success rate: **38.94%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 157 | 60 | 97 | 38.22 | ok |
| none | T2_mid | 131 | 56 | 75 | 42.75 | ok |
| none | T3_high | 100 | 44 | 56 | 44.0 | ok |
| low | T1_low | 4 | 1 | 3 | 25.0 | insufficient |
| low | T2_mid | 22 | 11 | 11 | 50.0 | ok |
| low | T3_high | 26 | 14 | 12 | 53.85 | ok |
| medium | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T2_mid | 9 | 4 | 5 | 44.44 | insufficient |
| medium | T3_high | 25 | 6 | 19 | 24.0 | ok |
| high | T2_mid | 5 | 1 | 4 | 20.0 | insufficient |
| high | T3_high | 20 | 5 | 15 | 25.0 | ok |
| missing | missing | 80 | 23 | 57 | 28.75 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 152 | 59 | 93 | 38.82 | ok |
| none | T2_mid | 151 | 68 | 83 | 45.03 | ok |
| none | T3_high | 149 | 58 | 91 | 38.93 | ok |
| low | T1_low | 10 | 4 | 6 | 40.0 | insufficient |
| low | T2_mid | 9 | 1 | 8 | 11.11 | insufficient |
| low | T3_high | 19 | 10 | 9 | 52.63 | insufficient |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T3_high | 3 | 1 | 2 | 33.33 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 80 | 23 | 57 | 28.75 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2030**
- Overall success rate: **42.12%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 500 | 179 | 321 | 35.8 | ok |
| none | T2_mid | 552 | 191 | 361 | 34.6 | ok |
| none | T3_high | 328 | 141 | 187 | 42.99 | ok |
| low | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| low | T2_mid | 19 | 8 | 11 | 42.11 | insufficient |
| low | T3_high | 20 | 6 | 14 | 30.0 | ok |
| medium | T1_low | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T2_mid | 12 | 3 | 9 | 25.0 | insufficient |
| medium | T3_high | 25 | 13 | 12 | 52.0 | ok |
| high | T1_low | 21 | 5 | 16 | 23.81 | ok |
| high | T2_mid | 21 | 8 | 13 | 38.1 | ok |
| high | T3_high | 232 | 134 | 98 | 57.76 | ok |
| missing | missing | 283 | 161 | 122 | 56.89 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 249 | 74 | 175 | 29.72 | ok |
| none | T2_mid | 368 | 130 | 238 | 35.33 | ok |
| none | T3_high | 109 | 44 | 65 | 40.37 | ok |
| low | T1_low | 116 | 39 | 77 | 33.62 | ok |
| low | T2_mid | 86 | 20 | 66 | 23.26 | ok |
| low | T3_high | 75 | 33 | 42 | 44.0 | ok |
| medium | T1_low | 103 | 47 | 56 | 45.63 | ok |
| medium | T2_mid | 103 | 41 | 62 | 39.81 | ok |
| medium | T3_high | 197 | 87 | 110 | 44.16 | ok |
| high | T1_low | 70 | 30 | 40 | 42.86 | ok |
| high | T2_mid | 47 | 19 | 28 | 40.43 | ok |
| high | T3_high | 224 | 130 | 94 | 58.04 | ok |
| missing | missing | 283 | 161 | 122 | 56.89 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.