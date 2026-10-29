# Directional Penalty Diagnostics - 2026-10-27

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1934**
- Overall success rate: **41.05%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 555 | 248 | 307 | 44.68 | ok |
| none | T2_mid | 515 | 203 | 312 | 39.42 | ok |
| none | T3_high | 384 | 163 | 221 | 42.45 | ok |
| low | T1_low | 17 | 6 | 11 | 35.29 | insufficient |
| low | T2_mid | 69 | 29 | 40 | 42.03 | ok |
| low | T3_high | 87 | 35 | 52 | 40.23 | ok |
| medium | T1_low | 5 | 1 | 4 | 20.0 | insufficient |
| medium | T2_mid | 20 | 11 | 9 | 55.0 | ok |
| medium | T3_high | 83 | 35 | 48 | 42.17 | ok |
| high | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| high | T2_mid | 13 | 5 | 8 | 38.46 | insufficient |
| high | T3_high | 81 | 33 | 48 | 40.74 | ok |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 560 | 252 | 308 | 45.0 | ok |
| none | T2_mid | 588 | 233 | 355 | 39.63 | ok |
| none | T3_high | 571 | 237 | 334 | 41.51 | ok |
| low | T1_low | 11 | 2 | 9 | 18.18 | insufficient |
| low | T2_mid | 14 | 6 | 8 | 42.86 | insufficient |
| low | T3_high | 35 | 12 | 23 | 34.29 | ok |
| medium | T1_low | 6 | 0 | 6 | 0.0 | insufficient |
| medium | T2_mid | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T3_high | 21 | 11 | 10 | 52.38 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 8 | 6 | 2 | 75.0 | insufficient |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **14374**
- Overall success rate: **50.56%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4603 | 2173 | 2430 | 47.21 | ok |
| none | T2_mid | 4607 | 2375 | 2232 | 51.55 | ok |
| none | T3_high | 3545 | 1873 | 1672 | 52.83 | ok |
| low | T1_low | 33 | 9 | 24 | 27.27 | ok |
| low | T2_mid | 20 | 8 | 12 | 40.0 | ok |
| low | T3_high | 111 | 62 | 49 | 55.86 | ok |
| medium | T1_low | 14 | 7 | 7 | 50.0 | insufficient |
| medium | T2_mid | 16 | 6 | 10 | 37.5 | insufficient |
| medium | T3_high | 113 | 61 | 52 | 53.98 | ok |
| high | T1_low | 40 | 9 | 31 | 22.5 | ok |
| high | T2_mid | 17 | 10 | 7 | 58.82 | insufficient |
| high | T3_high | 953 | 498 | 455 | 52.26 | ok |
| missing | missing | 302 | 177 | 125 | 58.61 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 3771 | 1795 | 1976 | 47.6 | ok |
| none | T2_mid | 4074 | 2154 | 1920 | 52.87 | ok |
| none | T3_high | 2426 | 1298 | 1128 | 53.5 | ok |
| low | T1_low | 401 | 166 | 235 | 41.4 | ok |
| low | T2_mid | 277 | 119 | 158 | 42.96 | ok |
| low | T3_high | 692 | 353 | 339 | 51.01 | ok |
| medium | T1_low | 322 | 149 | 173 | 46.27 | ok |
| medium | T2_mid | 224 | 94 | 130 | 41.96 | ok |
| medium | T3_high | 1028 | 537 | 491 | 52.24 | ok |
| high | T1_low | 196 | 88 | 108 | 44.9 | ok |
| high | T2_mid | 85 | 32 | 53 | 37.65 | ok |
| high | T3_high | 576 | 306 | 270 | 53.12 | ok |
| missing | missing | 302 | 177 | 125 | 58.61 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.