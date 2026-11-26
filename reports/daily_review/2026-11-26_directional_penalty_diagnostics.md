# Directional Penalty Diagnostics - 2026-11-26

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2934**
- Overall success rate: **41.68%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 880 | 378 | 502 | 42.95 | ok |
| none | T2_mid | 833 | 348 | 485 | 41.78 | ok |
| none | T3_high | 610 | 253 | 357 | 41.48 | ok |
| low | T1_low | 30 | 10 | 20 | 33.33 | ok |
| low | T2_mid | 86 | 35 | 51 | 40.7 | ok |
| low | T3_high | 138 | 64 | 74 | 46.38 | ok |
| medium | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T2_mid | 30 | 13 | 17 | 43.33 | ok |
| medium | T3_high | 115 | 46 | 69 | 40.0 | ok |
| high | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| high | T2_mid | 16 | 8 | 8 | 50.0 | insufficient |
| high | T3_high | 115 | 44 | 71 | 38.26 | ok |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 886 | 382 | 504 | 43.12 | ok |
| none | T2_mid | 911 | 383 | 528 | 42.04 | ok |
| none | T3_high | 866 | 358 | 508 | 41.34 | ok |
| low | T1_low | 24 | 8 | 16 | 33.33 | ok |
| low | T2_mid | 28 | 8 | 20 | 28.57 | ok |
| low | T3_high | 68 | 24 | 44 | 35.29 | ok |
| medium | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| medium | T2_mid | 20 | 8 | 12 | 40.0 | ok |
| medium | T3_high | 28 | 16 | 12 | 57.14 | ok |
| high | T2_mid | 6 | 5 | 1 | 83.33 | insufficient |
| high | T3_high | 16 | 9 | 7 | 56.25 | insufficient |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **25602**
- Overall success rate: **51.9%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 8379 | 4279 | 4100 | 51.07 | ok |
| none | T2_mid | 8291 | 4285 | 4006 | 51.68 | ok |
| none | T3_high | 6934 | 3660 | 3274 | 52.78 | ok |
| low | T1_low | 72 | 32 | 40 | 44.44 | ok |
| low | T2_mid | 66 | 34 | 32 | 51.52 | ok |
| low | T3_high | 152 | 89 | 63 | 58.55 | ok |
| medium | T1_low | 32 | 16 | 16 | 50.0 | ok |
| medium | T2_mid | 42 | 19 | 23 | 45.24 | ok |
| medium | T3_high | 155 | 86 | 69 | 55.48 | ok |
| high | T1_low | 35 | 13 | 22 | 37.14 | ok |
| high | T2_mid | 59 | 23 | 36 | 38.98 | ok |
| high | T3_high | 1196 | 640 | 556 | 53.51 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 6873 | 3511 | 3362 | 51.08 | ok |
| none | T2_mid | 7028 | 3688 | 3340 | 52.48 | ok |
| none | T3_high | 5224 | 2785 | 2439 | 53.31 | ok |
| low | T1_low | 964 | 494 | 470 | 51.24 | ok |
| low | T2_mid | 577 | 272 | 305 | 47.14 | ok |
| low | T3_high | 1069 | 548 | 521 | 51.26 | ok |
| medium | T1_low | 524 | 267 | 257 | 50.95 | ok |
| medium | T2_mid | 635 | 304 | 331 | 47.87 | ok |
| medium | T3_high | 1364 | 722 | 642 | 52.93 | ok |
| high | T1_low | 157 | 68 | 89 | 43.31 | ok |
| high | T2_mid | 218 | 97 | 121 | 44.5 | ok |
| high | T3_high | 780 | 420 | 360 | 53.85 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.