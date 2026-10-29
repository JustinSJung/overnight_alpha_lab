# Directional Penalty Diagnostics - 2026-10-07

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1518**
- Overall success rate: **43.74%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 433 | 204 | 229 | 47.11 | ok |
| none | T2_mid | 403 | 178 | 225 | 44.17 | ok |
| none | T3_high | 281 | 127 | 154 | 45.2 | ok |
| low | T1_low | 11 | 5 | 6 | 45.45 | insufficient |
| low | T2_mid | 45 | 21 | 24 | 46.67 | ok |
| low | T3_high | 71 | 29 | 42 | 40.85 | ok |
| medium | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T2_mid | 18 | 9 | 9 | 50.0 | insufficient |
| medium | T3_high | 67 | 31 | 36 | 46.27 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 66 | 28 | 38 | 42.42 | ok |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 433 | 208 | 225 | 48.04 | ok |
| none | T2_mid | 453 | 202 | 251 | 44.59 | ok |
| none | T3_high | 431 | 188 | 243 | 43.62 | ok |
| low | T1_low | 12 | 2 | 10 | 16.67 | insufficient |
| low | T2_mid | 14 | 4 | 10 | 28.57 | insufficient |
| low | T3_high | 27 | 11 | 16 | 40.74 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 10 | 6 | 4 | 60.0 | insufficient |
| medium | T3_high | 21 | 12 | 9 | 57.14 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 2 | 1 | 1 | 50.0 | insufficient |
| high | T3_high | 6 | 4 | 2 | 66.67 | insufficient |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **7994**
- Overall success rate: **46.99%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2498 | 1144 | 1354 | 45.8 | ok |
| none | T2_mid | 2542 | 1181 | 1361 | 46.46 | ok |
| none | T3_high | 1687 | 788 | 899 | 46.71 | ok |
| low | T1_low | 25 | 4 | 21 | 16.0 | ok |
| low | T2_mid | 12 | 6 | 6 | 50.0 | insufficient |
| low | T3_high | 78 | 39 | 39 | 50.0 | ok |
| medium | T1_low | 16 | 6 | 10 | 37.5 | insufficient |
| medium | T2_mid | 12 | 8 | 4 | 66.67 | insufficient |
| medium | T3_high | 80 | 38 | 42 | 47.5 | ok |
| high | T1_low | 45 | 12 | 33 | 26.67 | ok |
| high | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| high | T3_high | 696 | 354 | 342 | 50.86 | ok |
| missing | missing | 291 | 169 | 122 | 58.08 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1828 | 827 | 1001 | 45.24 | ok |
| none | T2_mid | 2213 | 1041 | 1172 | 47.04 | ok |
| none | T3_high | 995 | 456 | 539 | 45.83 | ok |
| low | T1_low | 326 | 138 | 188 | 42.33 | ok |
| low | T2_mid | 170 | 68 | 102 | 40.0 | ok |
| low | T3_high | 421 | 192 | 229 | 45.61 | ok |
| medium | T1_low | 265 | 124 | 141 | 46.79 | ok |
| medium | T2_mid | 129 | 63 | 66 | 48.84 | ok |
| medium | T3_high | 700 | 345 | 355 | 49.29 | ok |
| high | T1_low | 165 | 77 | 88 | 46.67 | ok |
| high | T2_mid | 66 | 30 | 36 | 45.45 | ok |
| high | T3_high | 425 | 226 | 199 | 53.18 | ok |
| missing | missing | 291 | 169 | 122 | 58.08 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.