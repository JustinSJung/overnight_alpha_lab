# Directional Penalty Diagnostics - 2026-09-01

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **716**
- Overall success rate: **39.66%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 191 | 83 | 108 | 43.46 | ok |
| none | T2_mid | 160 | 62 | 98 | 38.75 | ok |
| none | T3_high | 119 | 56 | 63 | 47.06 | ok |
| low | T1_low | 8 | 3 | 5 | 37.5 | insufficient |
| low | T2_mid | 23 | 10 | 13 | 43.48 | ok |
| low | T3_high | 30 | 16 | 14 | 53.33 | ok |
| medium | T1_low | 4 | 1 | 3 | 25.0 | insufficient |
| medium | T2_mid | 8 | 3 | 5 | 37.5 | insufficient |
| medium | T3_high | 33 | 13 | 20 | 39.39 | ok |
| high | T2_mid | 10 | 3 | 7 | 30.0 | insufficient |
| high | T3_high | 34 | 11 | 23 | 32.35 | ok |
| missing | missing | 96 | 23 | 73 | 23.96 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 190 | 85 | 105 | 44.74 | ok |
| none | T2_mid | 180 | 73 | 107 | 40.56 | ok |
| none | T3_high | 184 | 79 | 105 | 42.93 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 13 | 3 | 10 | 23.08 | insufficient |
| low | T3_high | 20 | 10 | 10 | 50.0 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 7 | 1 | 6 | 14.29 | insufficient |
| medium | T3_high | 9 | 5 | 4 | 55.56 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| high | T3_high | 3 | 2 | 1 | 66.67 | insufficient |
| missing | missing | 96 | 23 | 73 | 23.96 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **2804**
- Overall success rate: **43.9%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 781 | 297 | 484 | 38.03 | ok |
| none | T2_mid | 788 | 310 | 478 | 39.34 | ok |
| none | T3_high | 458 | 218 | 240 | 47.6 | ok |
| low | T1_low | 16 | 3 | 13 | 18.75 | insufficient |
| low | T2_mid | 17 | 9 | 8 | 52.94 | insufficient |
| low | T3_high | 37 | 15 | 22 | 40.54 | ok |
| medium | T1_low | 10 | 5 | 5 | 50.0 | insufficient |
| medium | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| medium | T3_high | 33 | 13 | 20 | 39.39 | ok |
| high | T1_low | 32 | 7 | 25 | 21.88 | ok |
| high | T2_mid | 19 | 12 | 7 | 63.16 | insufficient |
| high | T3_high | 312 | 172 | 140 | 55.13 | ok |
| missing | missing | 288 | 165 | 123 | 57.29 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 417 | 147 | 270 | 35.25 | ok |
| none | T2_mid | 513 | 195 | 318 | 38.01 | ok |
| none | T3_high | 151 | 66 | 85 | 43.71 | ok |
| low | T1_low | 176 | 57 | 119 | 32.39 | ok |
| low | T2_mid | 152 | 56 | 96 | 36.84 | ok |
| low | T3_high | 156 | 79 | 77 | 50.64 | ok |
| medium | T1_low | 143 | 62 | 81 | 43.36 | ok |
| medium | T2_mid | 113 | 50 | 63 | 44.25 | ok |
| medium | T3_high | 292 | 141 | 151 | 48.29 | ok |
| high | T1_low | 103 | 46 | 57 | 44.66 | ok |
| high | T2_mid | 59 | 35 | 24 | 59.32 | ok |
| high | T3_high | 241 | 132 | 109 | 54.77 | ok |
| missing | missing | 288 | 165 | 123 | 57.29 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.