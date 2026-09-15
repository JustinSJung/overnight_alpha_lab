# Directional Penalty Diagnostics - 2026-09-15

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **939**
- Overall success rate: **39.4%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 266 | 117 | 149 | 43.98 | ok |
| none | T2_mid | 232 | 95 | 137 | 40.95 | ok |
| none | T3_high | 165 | 71 | 94 | 43.03 | ok |
| low | T1_low | 9 | 3 | 6 | 33.33 | insufficient |
| low | T2_mid | 24 | 11 | 13 | 45.83 | ok |
| low | T3_high | 43 | 16 | 27 | 37.21 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T3_high | 39 | 14 | 25 | 35.9 | ok |
| high | T2_mid | 10 | 3 | 7 | 30.0 | insufficient |
| high | T3_high | 39 | 13 | 26 | 33.33 | ok |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 265 | 118 | 147 | 44.53 | ok |
| none | T2_mid | 252 | 106 | 146 | 42.06 | ok |
| none | T3_high | 250 | 97 | 153 | 38.8 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| low | T3_high | 22 | 10 | 12 | 45.45 | ok |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T3_high | 11 | 5 | 6 | 45.45 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 3 | 2 | 1 | 66.67 | insufficient |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **4993**
- Overall success rate: **46.49%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1504 | 634 | 870 | 42.15 | ok |
| none | T2_mid | 1505 | 698 | 807 | 46.38 | ok |
| none | T3_high | 976 | 455 | 521 | 46.62 | ok |
| low | T1_low | 21 | 3 | 18 | 14.29 | ok |
| low | T2_mid | 15 | 9 | 6 | 60.0 | insufficient |
| low | T3_high | 58 | 29 | 29 | 50.0 | ok |
| medium | T1_low | 13 | 5 | 8 | 38.46 | insufficient |
| medium | T2_mid | 10 | 5 | 5 | 50.0 | insufficient |
| medium | T3_high | 53 | 27 | 26 | 50.94 | ok |
| high | T1_low | 37 | 8 | 29 | 21.62 | ok |
| high | T2_mid | 13 | 9 | 4 | 69.23 | insufficient |
| high | T3_high | 490 | 264 | 226 | 53.88 | ok |
| missing | missing | 298 | 175 | 123 | 58.72 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1005 | 416 | 589 | 41.39 | ok |
| none | T2_mid | 1228 | 577 | 651 | 46.99 | ok |
| none | T3_high | 472 | 214 | 258 | 45.34 | ok |
| low | T1_low | 244 | 89 | 155 | 36.48 | ok |
| low | T2_mid | 147 | 62 | 85 | 42.18 | ok |
| low | T3_high | 284 | 133 | 151 | 46.83 | ok |
| medium | T1_low | 196 | 86 | 110 | 43.88 | ok |
| medium | T2_mid | 116 | 54 | 62 | 46.55 | ok |
| medium | T3_high | 486 | 245 | 241 | 50.41 | ok |
| high | T1_low | 130 | 59 | 71 | 45.38 | ok |
| high | T2_mid | 52 | 28 | 24 | 53.85 | ok |
| high | T3_high | 335 | 183 | 152 | 54.63 | ok |
| missing | missing | 298 | 175 | 123 | 58.72 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.