# Directional Penalty Diagnostics - 2026-09-03

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **769**
- Overall success rate: **39.53%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 203 | 84 | 119 | 41.38 | ok |
| none | T2_mid | 180 | 75 | 105 | 41.67 | ok |
| none | T3_high | 132 | 60 | 72 | 45.45 | ok |
| low | T1_low | 8 | 3 | 5 | 37.5 | insufficient |
| low | T2_mid | 23 | 10 | 13 | 43.48 | ok |
| low | T3_high | 32 | 16 | 16 | 50.0 | ok |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 8 | 3 | 5 | 37.5 | insufficient |
| medium | T3_high | 33 | 13 | 20 | 39.39 | ok |
| high | T2_mid | 10 | 3 | 7 | 30.0 | insufficient |
| high | T3_high | 34 | 11 | 23 | 32.35 | ok |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 203 | 87 | 116 | 42.86 | ok |
| none | T2_mid | 201 | 86 | 115 | 42.79 | ok |
| none | T3_high | 195 | 81 | 114 | 41.54 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 13 | 4 | 9 | 30.77 | insufficient |
| low | T3_high | 22 | 10 | 12 | 45.45 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 7 | 1 | 6 | 14.29 | insufficient |
| medium | T3_high | 10 | 6 | 4 | 60.0 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 101 | 24 | 77 | 23.76 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **3231**
- Overall success rate: **45.99%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 905 | 359 | 546 | 39.67 | ok |
| none | T2_mid | 925 | 405 | 520 | 43.78 | ok |
| none | T3_high | 556 | 269 | 287 | 48.38 | ok |
| low | T1_low | 18 | 3 | 15 | 16.67 | insufficient |
| low | T2_mid | 18 | 9 | 9 | 50.0 | insufficient |
| low | T3_high | 39 | 17 | 22 | 43.59 | ok |
| medium | T1_low | 11 | 5 | 6 | 45.45 | insufficient |
| medium | T2_mid | 12 | 5 | 7 | 41.67 | insufficient |
| medium | T3_high | 39 | 19 | 20 | 48.72 | ok |
| high | T1_low | 35 | 8 | 27 | 22.86 | ok |
| high | T2_mid | 15 | 11 | 4 | 73.33 | insufficient |
| high | T3_high | 354 | 200 | 154 | 56.5 | ok |
| missing | missing | 304 | 176 | 128 | 57.89 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 496 | 185 | 311 | 37.3 | ok |
| none | T2_mid | 629 | 272 | 357 | 43.24 | ok |
| none | T3_high | 212 | 93 | 119 | 43.87 | ok |
| low | T1_low | 192 | 64 | 128 | 33.33 | ok |
| low | T2_mid | 156 | 61 | 95 | 39.1 | ok |
| low | T3_high | 180 | 94 | 86 | 52.22 | ok |
| medium | T1_low | 169 | 76 | 93 | 44.97 | ok |
| medium | T2_mid | 127 | 60 | 67 | 47.24 | ok |
| medium | T3_high | 333 | 169 | 164 | 50.75 | ok |
| high | T1_low | 112 | 50 | 62 | 44.64 | ok |
| high | T2_mid | 58 | 37 | 21 | 63.79 | ok |
| high | T3_high | 263 | 149 | 114 | 56.65 | ok |
| missing | missing | 304 | 176 | 128 | 57.89 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.