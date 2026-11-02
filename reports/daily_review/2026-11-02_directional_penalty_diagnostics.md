# Directional Penalty Diagnostics - 2026-11-02

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1843**
- Overall success rate: **40.86%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 502 | 220 | 282 | 43.82 | ok |
| none | T2_mid | 513 | 200 | 313 | 38.99 | ok |
| none | T3_high | 371 | 166 | 205 | 44.74 | ok |
| low | T1_low | 16 | 5 | 11 | 31.25 | insufficient |
| low | T2_mid | 64 | 24 | 40 | 37.5 | ok |
| low | T3_high | 83 | 33 | 50 | 39.76 | ok |
| medium | T1_low | 4 | 1 | 3 | 25.0 | insufficient |
| medium | T2_mid | 18 | 10 | 8 | 55.56 | insufficient |
| medium | T3_high | 79 | 31 | 48 | 39.24 | ok |
| high | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| high | T2_mid | 12 | 5 | 7 | 41.67 | insufficient |
| high | T3_high | 80 | 33 | 47 | 41.25 | ok |
| missing | missing | 99 | 24 | 75 | 24.24 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 507 | 223 | 284 | 43.98 | ok |
| none | T2_mid | 583 | 227 | 356 | 38.94 | ok |
| none | T3_high | 553 | 238 | 315 | 43.04 | ok |
| low | T1_low | 9 | 2 | 7 | 22.22 | insufficient |
| low | T2_mid | 12 | 6 | 6 | 50.0 | insufficient |
| low | T3_high | 32 | 8 | 24 | 25.0 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 9 | 5 | 4 | 55.56 | insufficient |
| medium | T3_high | 20 | 11 | 9 | 55.0 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 1 | 2 | 33.33 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 99 | 24 | 75 | 24.24 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **14476**
- Overall success rate: **49.9%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4590 | 2149 | 2441 | 46.82 | ok |
| none | T2_mid | 4695 | 2360 | 2335 | 50.27 | ok |
| none | T3_high | 3623 | 1897 | 1726 | 52.36 | ok |
| low | T1_low | 34 | 10 | 24 | 29.41 | ok |
| low | T2_mid | 26 | 7 | 19 | 26.92 | ok |
| low | T3_high | 108 | 58 | 50 | 53.7 | ok |
| medium | T1_low | 12 | 5 | 7 | 41.67 | insufficient |
| medium | T2_mid | 20 | 6 | 14 | 30.0 | ok |
| medium | T3_high | 113 | 60 | 53 | 53.1 | ok |
| high | T1_low | 34 | 11 | 23 | 32.35 | ok |
| high | T2_mid | 17 | 8 | 9 | 47.06 | insufficient |
| high | T3_high | 920 | 487 | 433 | 52.93 | ok |
| missing | missing | 284 | 165 | 119 | 58.1 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3826 | 1804 | 2022 | 47.15 | ok |
| none | T2_mid | 4173 | 2144 | 2029 | 51.38 | ok |
| none | T3_high | 2532 | 1339 | 1193 | 52.88 | ok |
| low | T1_low | 365 | 142 | 223 | 38.9 | ok |
| low | T2_mid | 283 | 117 | 166 | 41.34 | ok |
| low | T3_high | 691 | 340 | 351 | 49.2 | ok |
| medium | T1_low | 303 | 142 | 161 | 46.86 | ok |
| medium | T2_mid | 228 | 92 | 136 | 40.35 | ok |
| medium | T3_high | 994 | 529 | 465 | 53.22 | ok |
| high | T1_low | 176 | 87 | 89 | 49.43 | ok |
| high | T2_mid | 74 | 28 | 46 | 37.84 | ok |
| high | T3_high | 547 | 294 | 253 | 53.75 | ok |
| missing | missing | 284 | 165 | 119 | 58.1 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.