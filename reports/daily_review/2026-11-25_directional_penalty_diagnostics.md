# Directional Penalty Diagnostics - 2026-11-25

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2891**
- Overall success rate: **41.34%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 857 | 366 | 491 | 42.71 | ok |
| none | T2_mid | 814 | 338 | 476 | 41.52 | ok |
| none | T3_high | 612 | 250 | 362 | 40.85 | ok |
| low | T1_low | 30 | 10 | 20 | 33.33 | ok |
| low | T2_mid | 88 | 34 | 54 | 38.64 | ok |
| low | T3_high | 136 | 60 | 76 | 44.12 | ok |
| medium | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T2_mid | 29 | 14 | 15 | 48.28 | ok |
| medium | T3_high | 115 | 47 | 68 | 40.87 | ok |
| high | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| high | T2_mid | 16 | 8 | 8 | 50.0 | insufficient |
| high | T3_high | 113 | 44 | 69 | 38.94 | ok |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 863 | 369 | 494 | 42.76 | ok |
| none | T2_mid | 893 | 374 | 519 | 41.88 | ok |
| none | T3_high | 869 | 354 | 515 | 40.74 | ok |
| low | T1_low | 23 | 8 | 15 | 34.78 | ok |
| low | T2_mid | 28 | 8 | 20 | 28.57 | ok |
| low | T3_high | 64 | 23 | 41 | 35.94 | ok |
| medium | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| medium | T2_mid | 21 | 8 | 13 | 38.1 | ok |
| medium | T3_high | 28 | 16 | 12 | 57.14 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 5 | 4 | 1 | 80.0 | insufficient |
| high | T3_high | 15 | 8 | 7 | 53.33 | insufficient |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **24961**
- Overall success rate: **51.42%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 8070 | 4013 | 4057 | 49.73 | ok |
| none | T2_mid | 8069 | 4150 | 3919 | 51.43 | ok |
| none | T3_high | 6824 | 3593 | 3231 | 52.65 | ok |
| low | T1_low | 72 | 34 | 38 | 47.22 | ok |
| low | T2_mid | 68 | 36 | 32 | 52.94 | ok |
| low | T3_high | 157 | 91 | 66 | 57.96 | ok |
| medium | T1_low | 33 | 16 | 17 | 48.48 | ok |
| medium | T2_mid | 43 | 20 | 23 | 46.51 | ok |
| medium | T3_high | 155 | 89 | 66 | 57.42 | ok |
| high | T1_low | 35 | 14 | 21 | 40.0 | ok |
| high | T2_mid | 61 | 24 | 37 | 39.34 | ok |
| high | T3_high | 1185 | 642 | 543 | 54.18 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 6624 | 3310 | 3314 | 49.97 | ok |
| none | T2_mid | 6851 | 3583 | 3268 | 52.3 | ok |
| none | T3_high | 5081 | 2704 | 2377 | 53.22 | ok |
| low | T1_low | 928 | 452 | 476 | 48.71 | ok |
| low | T2_mid | 561 | 263 | 298 | 46.88 | ok |
| low | T3_high | 1053 | 541 | 512 | 51.38 | ok |
| medium | T1_low | 498 | 243 | 255 | 48.8 | ok |
| medium | T2_mid | 613 | 288 | 325 | 46.98 | ok |
| medium | T3_high | 1376 | 723 | 653 | 52.54 | ok |
| high | T1_low | 160 | 72 | 88 | 45.0 | ok |
| high | T2_mid | 216 | 96 | 120 | 44.44 | ok |
| high | T3_high | 811 | 447 | 364 | 55.12 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.