# Directional Penalty Diagnostics - 2026-11-19

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2704**
- Overall success rate: **41.16%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 797 | 334 | 463 | 41.91 | ok |
| none | T2_mid | 752 | 314 | 438 | 41.76 | ok |
| none | T3_high | 577 | 235 | 342 | 40.73 | ok |
| low | T1_low | 24 | 9 | 15 | 37.5 | ok |
| low | T2_mid | 83 | 31 | 52 | 37.35 | ok |
| low | T3_high | 128 | 54 | 74 | 42.19 | ok |
| medium | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T2_mid | 29 | 15 | 14 | 51.72 | ok |
| medium | T3_high | 110 | 46 | 64 | 41.82 | ok |
| high | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| high | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| high | T3_high | 108 | 43 | 65 | 39.81 | ok |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 799 | 338 | 461 | 42.3 | ok |
| none | T2_mid | 834 | 349 | 485 | 41.85 | ok |
| none | T3_high | 827 | 335 | 492 | 40.51 | ok |
| low | T1_low | 22 | 7 | 15 | 31.82 | ok |
| low | T2_mid | 23 | 7 | 16 | 30.43 | ok |
| low | T3_high | 56 | 19 | 37 | 33.93 | ok |
| medium | T1_low | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T2_mid | 17 | 8 | 9 | 47.06 | insufficient |
| medium | T3_high | 26 | 16 | 10 | 61.54 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 5 | 4 | 1 | 80.0 | insufficient |
| high | T3_high | 14 | 8 | 6 | 57.14 | insufficient |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **22625**
- Overall success rate: **51.02%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 7152 | 3531 | 3621 | 49.37 | ok |
| none | T2_mid | 7370 | 3740 | 3630 | 50.75 | ok |
| none | T3_high | 6153 | 3228 | 2925 | 52.46 | ok |
| low | T1_low | 77 | 32 | 45 | 41.56 | ok |
| low | T2_mid | 57 | 30 | 27 | 52.63 | ok |
| low | T3_high | 144 | 82 | 62 | 56.94 | ok |
| medium | T1_low | 31 | 17 | 14 | 54.84 | ok |
| medium | T2_mid | 39 | 16 | 23 | 41.03 | ok |
| medium | T3_high | 153 | 85 | 68 | 55.56 | ok |
| high | T1_low | 41 | 16 | 25 | 39.02 | ok |
| high | T2_mid | 57 | 23 | 34 | 40.35 | ok |
| high | T3_high | 1162 | 632 | 530 | 54.39 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5894 | 2924 | 2970 | 49.61 | ok |
| none | T2_mid | 6286 | 3249 | 3037 | 51.69 | ok |
| none | T3_high | 4526 | 2396 | 2130 | 52.94 | ok |
| low | T1_low | 790 | 369 | 421 | 46.71 | ok |
| low | T2_mid | 507 | 231 | 276 | 45.56 | ok |
| low | T3_high | 985 | 508 | 477 | 51.57 | ok |
| medium | T1_low | 461 | 229 | 232 | 49.67 | ok |
| medium | T2_mid | 538 | 244 | 294 | 45.35 | ok |
| medium | T3_high | 1334 | 698 | 636 | 52.32 | ok |
| high | T1_low | 156 | 74 | 82 | 47.44 | ok |
| high | T2_mid | 192 | 85 | 107 | 44.27 | ok |
| high | T3_high | 767 | 425 | 342 | 55.41 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.