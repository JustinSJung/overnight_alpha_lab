# Directional Penalty Diagnostics - 2026-09-10

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **863**
- Overall success rate: **40.32%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 235 | 100 | 135 | 42.55 | ok |
| none | T2_mid | 213 | 88 | 125 | 41.31 | ok |
| none | T3_high | 151 | 71 | 80 | 47.02 | ok |
| low | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| low | T2_mid | 23 | 11 | 12 | 47.83 | ok |
| low | T3_high | 39 | 17 | 22 | 43.59 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 9 | 4 | 5 | 44.44 | insufficient |
| medium | T3_high | 36 | 14 | 22 | 38.89 | ok |
| high | T2_mid | 9 | 3 | 6 | 33.33 | insufficient |
| high | T3_high | 36 | 12 | 24 | 33.33 | ok |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 234 | 102 | 132 | 43.59 | ok |
| none | T2_mid | 234 | 101 | 133 | 43.16 | ok |
| none | T3_high | 225 | 95 | 130 | 42.22 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| low | T3_high | 22 | 10 | 12 | 45.45 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 6 | 1 | 5 | 16.67 | insufficient |
| medium | T3_high | 11 | 6 | 5 | 54.55 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **4149**
- Overall success rate: **46.59%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1220 | 506 | 714 | 41.48 | ok |
| none | T2_mid | 1231 | 567 | 664 | 46.06 | ok |
| none | T3_high | 783 | 379 | 404 | 48.4 | ok |
| low | T1_low | 20 | 3 | 17 | 15.0 | ok |
| low | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| low | T3_high | 50 | 25 | 25 | 50.0 | ok |
| medium | T1_low | 11 | 5 | 6 | 45.45 | insufficient |
| medium | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T3_high | 45 | 21 | 24 | 46.67 | ok |
| high | T1_low | 34 | 7 | 27 | 20.59 | ok |
| high | T2_mid | 13 | 9 | 4 | 69.23 | insufficient |
| high | T3_high | 425 | 230 | 195 | 54.12 | ok |
| missing | missing | 294 | 170 | 124 | 57.82 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 753 | 306 | 447 | 40.64 | ok |
| none | T2_mid | 960 | 448 | 512 | 46.67 | ok |
| none | T3_high | 337 | 159 | 178 | 47.18 | ok |
| low | T1_low | 222 | 79 | 143 | 35.59 | ok |
| low | T2_mid | 153 | 61 | 92 | 39.87 | ok |
| low | T3_high | 243 | 120 | 123 | 49.38 | ok |
| medium | T1_low | 187 | 80 | 107 | 42.78 | ok |
| medium | T2_mid | 106 | 52 | 54 | 49.06 | ok |
| medium | T3_high | 414 | 204 | 210 | 49.28 | ok |
| high | T1_low | 123 | 56 | 67 | 45.53 | ok |
| high | T2_mid | 48 | 26 | 22 | 54.17 | ok |
| high | T3_high | 309 | 172 | 137 | 55.66 | ok |
| missing | missing | 294 | 170 | 124 | 57.82 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.