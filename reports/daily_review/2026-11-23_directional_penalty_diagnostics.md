# Directional Penalty Diagnostics - 2026-11-23

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2727**
- Overall success rate: **41.55%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 810 | 343 | 467 | 42.35 | ok |
| none | T2_mid | 777 | 328 | 449 | 42.21 | ok |
| none | T3_high | 565 | 231 | 334 | 40.88 | ok |
| low | T1_low | 26 | 9 | 17 | 34.62 | ok |
| low | T2_mid | 81 | 30 | 51 | 37.04 | ok |
| low | T3_high | 128 | 56 | 72 | 43.75 | ok |
| medium | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T2_mid | 28 | 14 | 14 | 50.0 | ok |
| medium | T3_high | 107 | 46 | 61 | 42.99 | ok |
| high | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| high | T2_mid | 14 | 8 | 6 | 57.14 | insufficient |
| high | T3_high | 110 | 44 | 66 | 40.0 | ok |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 811 | 345 | 466 | 42.54 | ok |
| none | T2_mid | 850 | 360 | 490 | 42.35 | ok |
| none | T3_high | 809 | 330 | 479 | 40.79 | ok |
| low | T1_low | 24 | 8 | 16 | 33.33 | ok |
| low | T2_mid | 26 | 8 | 18 | 30.77 | ok |
| low | T3_high | 60 | 22 | 38 | 36.67 | ok |
| medium | T1_low | 11 | 3 | 8 | 27.27 | insufficient |
| medium | T2_mid | 19 | 8 | 11 | 42.11 | insufficient |
| medium | T3_high | 26 | 16 | 10 | 61.54 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 5 | 4 | 1 | 80.0 | insufficient |
| high | T3_high | 15 | 9 | 6 | 60.0 | insufficient |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **23485**
- Overall success rate: **51.64%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 7513 | 3803 | 3710 | 50.62 | ok |
| none | T2_mid | 7628 | 3913 | 3715 | 51.3 | ok |
| none | T3_high | 6381 | 3361 | 3020 | 52.67 | ok |
| low | T1_low | 75 | 32 | 43 | 42.67 | ok |
| low | T2_mid | 62 | 32 | 30 | 51.61 | ok |
| low | T3_high | 148 | 85 | 63 | 57.43 | ok |
| medium | T1_low | 31 | 17 | 14 | 54.84 | ok |
| medium | T2_mid | 38 | 16 | 22 | 42.11 | ok |
| medium | T3_high | 156 | 89 | 67 | 57.05 | ok |
| high | T1_low | 33 | 12 | 21 | 36.36 | ok |
| high | T2_mid | 61 | 24 | 37 | 39.34 | ok |
| high | T3_high | 1170 | 631 | 539 | 53.93 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 6203 | 3150 | 3053 | 50.78 | ok |
| none | T2_mid | 6487 | 3378 | 3109 | 52.07 | ok |
| none | T3_high | 4758 | 2529 | 2229 | 53.15 | ok |
| low | T1_low | 826 | 403 | 423 | 48.79 | ok |
| low | T2_mid | 529 | 247 | 282 | 46.69 | ok |
| low | T3_high | 994 | 520 | 474 | 52.31 | ok |
| medium | T1_low | 480 | 245 | 235 | 51.04 | ok |
| medium | T2_mid | 569 | 271 | 298 | 47.63 | ok |
| medium | T3_high | 1346 | 697 | 649 | 51.78 | ok |
| high | T1_low | 143 | 66 | 77 | 46.15 | ok |
| high | T2_mid | 204 | 89 | 115 | 43.63 | ok |
| high | T3_high | 757 | 420 | 337 | 55.48 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.