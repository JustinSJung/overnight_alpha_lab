# Directional Penalty Diagnostics - 2026-09-02

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **739**
- Overall success rate: **38.7%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 197 | 81 | 116 | 41.12 | ok |
| none | T2_mid | 167 | 65 | 102 | 38.92 | ok |
| none | T3_high | 127 | 56 | 71 | 44.09 | ok |
| low | T1_low | 8 | 3 | 5 | 37.5 | insufficient |
| low | T2_mid | 22 | 10 | 12 | 45.45 | ok |
| low | T3_high | 31 | 16 | 15 | 51.61 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 8 | 3 | 5 | 37.5 | insufficient |
| medium | T3_high | 33 | 13 | 20 | 39.39 | ok |
| high | T2_mid | 10 | 3 | 7 | 30.0 | insufficient |
| high | T3_high | 33 | 10 | 23 | 30.3 | ok |
| missing | missing | 98 | 24 | 74 | 24.49 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 197 | 84 | 113 | 42.64 | ok |
| none | T2_mid | 188 | 76 | 112 | 40.43 | ok |
| none | T3_high | 189 | 77 | 112 | 40.74 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 12 | 3 | 9 | 25.0 | insufficient |
| low | T3_high | 22 | 10 | 12 | 45.45 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 7 | 2 | 5 | 28.57 | insufficient |
| medium | T3_high | 9 | 5 | 4 | 55.56 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 98 | 24 | 74 | 24.49 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2930**
- Overall success rate: **44.33%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 811 | 302 | 509 | 37.24 | ok |
| none | T2_mid | 844 | 346 | 498 | 41.0 | ok |
| none | T3_high | 489 | 233 | 256 | 47.65 | ok |
| low | T1_low | 17 | 3 | 14 | 17.65 | insufficient |
| low | T2_mid | 18 | 10 | 8 | 55.56 | insufficient |
| low | T3_high | 38 | 15 | 23 | 39.47 | ok |
| medium | T1_low | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T2_mid | 11 | 4 | 7 | 36.36 | insufficient |
| medium | T3_high | 35 | 16 | 19 | 45.71 | ok |
| high | T1_low | 28 | 5 | 23 | 17.86 | ok |
| high | T2_mid | 17 | 12 | 5 | 70.59 | insufficient |
| high | T3_high | 328 | 185 | 143 | 56.4 | ok |
| missing | missing | 284 | 164 | 120 | 57.75 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 444 | 159 | 285 | 35.81 | ok |
| none | T2_mid | 554 | 221 | 333 | 39.89 | ok |
| none | T3_high | 173 | 78 | 95 | 45.09 | ok |
| low | T1_low | 173 | 52 | 121 | 30.06 | ok |
| low | T2_mid | 157 | 61 | 96 | 38.85 | ok |
| low | T3_high | 169 | 83 | 86 | 49.11 | ok |
| medium | T1_low | 146 | 60 | 86 | 41.1 | ok |
| medium | T2_mid | 121 | 56 | 65 | 46.28 | ok |
| medium | T3_high | 304 | 151 | 153 | 49.67 | ok |
| high | T1_low | 103 | 43 | 60 | 41.75 | ok |
| high | T2_mid | 58 | 34 | 24 | 58.62 | ok |
| high | T3_high | 244 | 137 | 107 | 56.15 | ok |
| missing | missing | 284 | 164 | 120 | 57.75 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.