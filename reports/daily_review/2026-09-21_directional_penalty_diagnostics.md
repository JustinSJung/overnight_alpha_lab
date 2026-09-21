# Directional Penalty Diagnostics - 2026-09-21

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1029**
- Overall success rate: **41.3%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 294 | 136 | 158 | 46.26 | ok |
| none | T2_mid | 257 | 112 | 145 | 43.58 | ok |
| none | T3_high | 193 | 84 | 109 | 43.52 | ok |
| low | T1_low | 9 | 4 | 5 | 44.44 | insufficient |
| low | T2_mid | 24 | 10 | 14 | 41.67 | ok |
| low | T3_high | 43 | 15 | 28 | 34.88 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 11 | 6 | 5 | 54.55 | insufficient |
| medium | T3_high | 39 | 15 | 24 | 38.46 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 10 | 4 | 6 | 40.0 | insufficient |
| high | T3_high | 44 | 14 | 30 | 31.82 | ok |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 292 | 137 | 155 | 46.92 | ok |
| none | T2_mid | 282 | 126 | 156 | 44.68 | ok |
| none | T3_high | 285 | 113 | 172 | 39.65 | ok |
| low | T1_low | 13 | 3 | 10 | 23.08 | insufficient |
| low | T2_mid | 13 | 3 | 10 | 23.08 | insufficient |
| low | T3_high | 17 | 6 | 11 | 35.29 | insufficient |
| medium | T1_low | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T2_mid | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T3_high | 13 | 6 | 7 | 46.15 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 4 | 3 | 1 | 75.0 | insufficient |
| missing | missing | 100 | 24 | 76 | 24.0 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **5888**
- Overall success rate: **46.82%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1799 | 786 | 1013 | 43.69 | ok |
| none | T2_mid | 1832 | 860 | 972 | 46.94 | ok |
| none | T3_high | 1195 | 562 | 633 | 47.03 | ok |
| low | T1_low | 20 | 3 | 17 | 15.0 | ok |
| low | T2_mid | 16 | 8 | 8 | 50.0 | insufficient |
| low | T3_high | 63 | 31 | 32 | 49.21 | ok |
| medium | T1_low | 13 | 5 | 8 | 38.46 | insufficient |
| medium | T2_mid | 10 | 5 | 5 | 50.0 | insufficient |
| medium | T3_high | 57 | 27 | 30 | 47.37 | ok |
| high | T1_low | 38 | 9 | 29 | 23.68 | ok |
| high | T2_mid | 14 | 9 | 5 | 64.29 | insufficient |
| high | T3_high | 537 | 281 | 256 | 52.33 | ok |
| missing | missing | 294 | 171 | 123 | 58.16 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1272 | 550 | 722 | 43.24 | ok |
| none | T2_mid | 1543 | 737 | 806 | 47.76 | ok |
| none | T3_high | 644 | 297 | 347 | 46.12 | ok |
| low | T1_low | 254 | 96 | 158 | 37.8 | ok |
| low | T2_mid | 151 | 61 | 90 | 40.4 | ok |
| low | T3_high | 307 | 143 | 164 | 46.58 | ok |
| medium | T1_low | 207 | 93 | 114 | 44.93 | ok |
| medium | T2_mid | 117 | 55 | 62 | 47.01 | ok |
| medium | T3_high | 555 | 278 | 277 | 50.09 | ok |
| high | T1_low | 137 | 64 | 73 | 46.72 | ok |
| high | T2_mid | 61 | 29 | 32 | 47.54 | ok |
| high | T3_high | 346 | 183 | 163 | 52.89 | ok |
| missing | missing | 294 | 171 | 123 | 58.16 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.