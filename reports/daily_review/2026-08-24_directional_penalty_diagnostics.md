# Directional Penalty Diagnostics - 2026-08-24

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **666**
- Overall success rate: **39.49%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 188 | 77 | 111 | 40.96 | ok |
| none | T2_mid | 153 | 61 | 92 | 39.87 | ok |
| none | T3_high | 105 | 47 | 58 | 44.76 | ok |
| low | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| low | T2_mid | 27 | 14 | 13 | 51.85 | ok |
| low | T3_high | 30 | 15 | 15 | 50.0 | ok |
| medium | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T3_high | 34 | 11 | 23 | 32.35 | ok |
| high | T2_mid | 5 | 1 | 4 | 20.0 | insufficient |
| high | T3_high | 25 | 6 | 19 | 24.0 | ok |
| missing | missing | 80 | 23 | 57 | 28.75 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 181 | 77 | 104 | 42.54 | ok |
| none | T2_mid | 172 | 75 | 97 | 43.6 | ok |
| none | T3_high | 165 | 65 | 100 | 39.39 | ok |
| low | T1_low | 13 | 4 | 9 | 30.77 | insufficient |
| low | T2_mid | 13 | 2 | 11 | 15.38 | insufficient |
| low | T3_high | 21 | 11 | 10 | 52.38 | ok |
| medium | T1_low | 3 | 0 | 3 | 0.0 | insufficient |
| medium | T2_mid | 9 | 2 | 7 | 22.22 | insufficient |
| medium | T3_high | 7 | 2 | 5 | 28.57 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| high | T3_high | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 80 | 23 | 57 | 28.75 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2479**
- Overall success rate: **43.77%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 637 | 242 | 395 | 37.99 | ok |
| none | T2_mid | 694 | 262 | 432 | 37.75 | ok |
| none | T3_high | 447 | 211 | 236 | 47.2 | ok |
| low | T1_low | 12 | 3 | 9 | 25.0 | insufficient |
| low | T2_mid | 19 | 8 | 11 | 42.11 | insufficient |
| low | T3_high | 28 | 9 | 19 | 32.14 | ok |
| medium | T1_low | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| medium | T3_high | 28 | 15 | 13 | 53.57 | ok |
| high | T1_low | 28 | 7 | 21 | 25.0 | ok |
| high | T2_mid | 15 | 7 | 8 | 46.67 | insufficient |
| high | T3_high | 273 | 157 | 116 | 57.51 | ok |
| missing | missing | 278 | 157 | 121 | 56.47 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 319 | 109 | 210 | 34.17 | ok |
| none | T2_mid | 459 | 169 | 290 | 36.82 | ok |
| none | T3_high | 139 | 56 | 83 | 40.29 | ok |
| low | T1_low | 137 | 45 | 92 | 32.85 | ok |
| low | T2_mid | 123 | 38 | 85 | 30.89 | ok |
| low | T3_high | 122 | 61 | 61 | 50.0 | ok |
| medium | T1_low | 134 | 59 | 75 | 44.03 | ok |
| medium | T2_mid | 111 | 51 | 60 | 45.95 | ok |
| medium | T3_high | 254 | 122 | 132 | 48.03 | ok |
| high | T1_low | 93 | 42 | 51 | 45.16 | ok |
| high | T2_mid | 49 | 23 | 26 | 46.94 | ok |
| high | T3_high | 261 | 153 | 108 | 58.62 | ok |
| missing | missing | 278 | 157 | 121 | 56.47 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.