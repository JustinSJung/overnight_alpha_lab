# Directional Penalty Diagnostics - 2026-11-11

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2252**
- Overall success rate: **41.92%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 639 | 282 | 357 | 44.13 | ok |
| none | T2_mid | 621 | 260 | 361 | 41.87 | ok |
| none | T3_high | 474 | 202 | 272 | 42.62 | ok |
| low | T1_low | 17 | 6 | 11 | 35.29 | insufficient |
| low | T2_mid | 72 | 29 | 43 | 40.28 | ok |
| low | T3_high | 98 | 41 | 57 | 41.84 | ok |
| medium | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T2_mid | 25 | 13 | 12 | 52.0 | ok |
| medium | T3_high | 92 | 38 | 54 | 41.3 | ok |
| high | T1_low | 3 | 2 | 1 | 66.67 | insufficient |
| high | T2_mid | 11 | 6 | 5 | 54.55 | insufficient |
| high | T3_high | 93 | 39 | 54 | 41.94 | ok |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 638 | 286 | 352 | 44.83 | ok |
| none | T2_mid | 696 | 293 | 403 | 42.1 | ok |
| none | T3_high | 681 | 285 | 396 | 41.85 | ok |
| low | T1_low | 13 | 2 | 11 | 15.38 | insufficient |
| low | T2_mid | 16 | 6 | 10 | 37.5 | insufficient |
| low | T3_high | 42 | 14 | 28 | 33.33 | ok |
| medium | T1_low | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| medium | T3_high | 22 | 14 | 8 | 63.64 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 2 | 1 | 1 | 50.0 | insufficient |
| high | T3_high | 12 | 7 | 5 | 58.33 | insufficient |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **19372**
- Overall success rate: **50.88%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 6106 | 3054 | 3052 | 50.02 | ok |
| none | T2_mid | 6336 | 3166 | 3170 | 49.97 | ok |
| none | T3_high | 5236 | 2730 | 2506 | 52.14 | ok |
| low | T1_low | 40 | 14 | 26 | 35.0 | ok |
| low | T2_mid | 42 | 19 | 23 | 45.24 | ok |
| low | T3_high | 126 | 69 | 57 | 54.76 | ok |
| medium | T1_low | 12 | 7 | 5 | 58.33 | insufficient |
| medium | T2_mid | 22 | 7 | 15 | 31.82 | ok |
| medium | T3_high | 128 | 74 | 54 | 57.81 | ok |
| high | T1_low | 37 | 10 | 27 | 27.03 | ok |
| high | T2_mid | 27 | 13 | 14 | 48.15 | ok |
| high | T3_high | 966 | 522 | 444 | 54.04 | ok |
| missing | missing | 294 | 172 | 122 | 58.5 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4988 | 2508 | 2480 | 50.28 | ok |
| none | T2_mid | 5515 | 2809 | 2706 | 50.93 | ok |
| none | T3_high | 3832 | 2014 | 1818 | 52.56 | ok |
| low | T1_low | 622 | 297 | 325 | 47.75 | ok |
| low | T2_mid | 421 | 188 | 233 | 44.66 | ok |
| low | T3_high | 844 | 434 | 410 | 51.42 | ok |
| medium | T1_low | 412 | 196 | 216 | 47.57 | ok |
| medium | T2_mid | 376 | 162 | 214 | 43.09 | ok |
| medium | T3_high | 1158 | 611 | 547 | 52.76 | ok |
| high | T1_low | 173 | 84 | 89 | 48.55 | ok |
| high | T2_mid | 115 | 46 | 69 | 40.0 | ok |
| high | T3_high | 622 | 336 | 286 | 54.02 | ok |
| missing | missing | 294 | 172 | 122 | 58.5 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.