# Directional Penalty Diagnostics - 2026-11-24

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2808**
- Overall success rate: **40.81%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 832 | 341 | 491 | 40.99 | ok |
| none | T2_mid | 795 | 333 | 462 | 41.89 | ok |
| none | T3_high | 586 | 240 | 346 | 40.96 | ok |
| low | T1_low | 30 | 10 | 20 | 33.33 | ok |
| low | T2_mid | 88 | 33 | 55 | 37.5 | ok |
| low | T3_high | 128 | 55 | 73 | 42.97 | ok |
| medium | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T2_mid | 29 | 13 | 16 | 44.83 | ok |
| medium | T3_high | 109 | 45 | 64 | 41.28 | ok |
| high | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| high | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| high | T3_high | 115 | 44 | 71 | 38.26 | ok |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 839 | 344 | 495 | 41.0 | ok |
| none | T2_mid | 876 | 368 | 508 | 42.01 | ok |
| none | T3_high | 835 | 339 | 496 | 40.6 | ok |
| low | T1_low | 23 | 8 | 15 | 34.78 | ok |
| low | T2_mid | 25 | 7 | 18 | 28.0 | ok |
| low | T3_high | 59 | 20 | 39 | 33.9 | ok |
| medium | T1_low | 10 | 3 | 7 | 30.0 | insufficient |
| medium | T2_mid | 21 | 8 | 13 | 38.1 | ok |
| medium | T3_high | 28 | 16 | 12 | 57.14 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 5 | 4 | 1 | 80.0 | insufficient |
| high | T3_high | 16 | 9 | 7 | 56.25 | insufficient |
| missing | missing | 70 | 19 | 51 | 27.14 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **23912**
- Overall success rate: **52.47%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 7546 | 3909 | 3637 | 51.8 | ok |
| none | T2_mid | 7824 | 4087 | 3737 | 52.24 | ok |
| none | T3_high | 6588 | 3505 | 3083 | 53.2 | ok |
| low | T1_low | 71 | 32 | 39 | 45.07 | ok |
| low | T2_mid | 67 | 35 | 32 | 52.24 | ok |
| low | T3_high | 148 | 84 | 64 | 56.76 | ok |
| medium | T1_low | 32 | 16 | 16 | 50.0 | ok |
| medium | T2_mid | 39 | 18 | 21 | 46.15 | ok |
| medium | T3_high | 149 | 81 | 68 | 54.36 | ok |
| high | T1_low | 33 | 13 | 20 | 39.39 | ok |
| high | T2_mid | 57 | 23 | 34 | 40.35 | ok |
| high | T3_high | 1169 | 631 | 538 | 53.98 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 6215 | 3231 | 2984 | 51.99 | ok |
| none | T2_mid | 6677 | 3544 | 3133 | 53.08 | ok |
| none | T3_high | 4946 | 2646 | 2300 | 53.5 | ok |
| low | T1_low | 860 | 441 | 419 | 51.28 | ok |
| low | T2_mid | 534 | 254 | 280 | 47.57 | ok |
| low | T3_high | 1012 | 528 | 484 | 52.17 | ok |
| medium | T1_low | 456 | 228 | 228 | 50.0 | ok |
| medium | T2_mid | 571 | 275 | 296 | 48.16 | ok |
| medium | T3_high | 1318 | 698 | 620 | 52.96 | ok |
| high | T1_low | 151 | 70 | 81 | 46.36 | ok |
| high | T2_mid | 205 | 90 | 115 | 43.9 | ok |
| high | T3_high | 778 | 429 | 349 | 55.14 | ok |
| missing | missing | 189 | 112 | 77 | 59.26 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.