# Directional Penalty Diagnostics - 2026-11-20

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2740**
- Overall success rate: **42.19%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 817 | 351 | 466 | 42.96 | ok |
| none | T2_mid | 771 | 330 | 441 | 42.8 | ok |
| none | T3_high | 571 | 240 | 331 | 42.03 | ok |
| low | T1_low | 24 | 9 | 15 | 37.5 | ok |
| low | T2_mid | 85 | 33 | 52 | 38.82 | ok |
| low | T3_high | 127 | 56 | 71 | 44.09 | ok |
| medium | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T2_mid | 28 | 14 | 14 | 50.0 | ok |
| medium | T3_high | 108 | 46 | 62 | 42.59 | ok |
| high | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| high | T2_mid | 15 | 7 | 8 | 46.67 | insufficient |
| high | T3_high | 113 | 46 | 67 | 40.71 | ok |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 817 | 353 | 464 | 43.21 | ok |
| none | T2_mid | 853 | 364 | 489 | 42.67 | ok |
| none | T3_high | 827 | 344 | 483 | 41.6 | ok |
| low | T1_low | 23 | 8 | 15 | 34.78 | ok |
| low | T2_mid | 24 | 8 | 16 | 33.33 | ok |
| low | T3_high | 52 | 19 | 33 | 36.54 | ok |
| medium | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| medium | T2_mid | 17 | 8 | 9 | 47.06 | insufficient |
| medium | T3_high | 26 | 17 | 9 | 65.38 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 5 | 4 | 1 | 80.0 | insufficient |
| high | T3_high | 14 | 8 | 6 | 57.14 | insufficient |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **23018**
- Overall success rate: **50.54%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 7363 | 3584 | 3779 | 48.68 | ok |
| none | T2_mid | 7459 | 3743 | 3716 | 50.18 | ok |
| none | T3_high | 6252 | 3266 | 2986 | 52.24 | ok |
| low | T1_low | 75 | 32 | 43 | 42.67 | ok |
| low | T2_mid | 61 | 31 | 30 | 50.82 | ok |
| low | T3_high | 141 | 84 | 57 | 59.57 | ok |
| medium | T1_low | 30 | 17 | 13 | 56.67 | ok |
| medium | T2_mid | 39 | 16 | 23 | 41.03 | ok |
| medium | T3_high | 150 | 83 | 67 | 55.33 | ok |
| high | T1_low | 37 | 14 | 23 | 37.84 | ok |
| high | T2_mid | 55 | 22 | 33 | 40.0 | ok |
| high | T3_high | 1167 | 629 | 538 | 53.9 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 6066 | 2963 | 3103 | 48.85 | ok |
| none | T2_mid | 6363 | 3242 | 3121 | 50.95 | ok |
| none | T3_high | 4633 | 2436 | 2197 | 52.58 | ok |
| low | T1_low | 818 | 376 | 442 | 45.97 | ok |
| low | T2_mid | 519 | 240 | 279 | 46.24 | ok |
| low | T3_high | 982 | 502 | 480 | 51.12 | ok |
| medium | T1_low | 468 | 234 | 234 | 50.0 | ok |
| medium | T2_mid | 551 | 246 | 305 | 44.65 | ok |
| medium | T3_high | 1319 | 693 | 626 | 52.54 | ok |
| high | T1_low | 153 | 74 | 79 | 48.37 | ok |
| high | T2_mid | 181 | 84 | 97 | 46.41 | ok |
| high | T3_high | 776 | 431 | 345 | 55.54 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.