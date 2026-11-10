# Directional Penalty Diagnostics - 2026-11-10

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2192**
- Overall success rate: **41.29%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 607 | 257 | 350 | 42.34 | ok |
| none | T2_mid | 606 | 249 | 357 | 41.09 | ok |
| none | T3_high | 463 | 199 | 264 | 42.98 | ok |
| low | T1_low | 16 | 5 | 11 | 31.25 | insufficient |
| low | T2_mid | 73 | 30 | 43 | 41.1 | ok |
| low | T3_high | 95 | 42 | 53 | 44.21 | ok |
| medium | T1_low | 4 | 2 | 2 | 50.0 | insufficient |
| medium | T2_mid | 25 | 12 | 13 | 48.0 | ok |
| medium | T3_high | 89 | 37 | 52 | 41.57 | ok |
| high | T1_low | 3 | 2 | 1 | 66.67 | insufficient |
| high | T2_mid | 13 | 7 | 6 | 53.85 | insufficient |
| high | T3_high | 95 | 39 | 56 | 41.05 | ok |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 607 | 261 | 346 | 43.0 | ok |
| none | T2_mid | 684 | 282 | 402 | 41.23 | ok |
| none | T3_high | 666 | 282 | 384 | 42.34 | ok |
| low | T1_low | 13 | 2 | 11 | 15.38 | insufficient |
| low | T2_mid | 15 | 6 | 9 | 40.0 | insufficient |
| low | T3_high | 41 | 13 | 28 | 31.71 | ok |
| medium | T1_low | 8 | 1 | 7 | 12.5 | insufficient |
| medium | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| medium | T3_high | 24 | 14 | 10 | 58.33 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 11 | 8 | 3 | 72.73 | insufficient |
| missing | missing | 103 | 24 | 79 | 23.3 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **18647**
- Overall success rate: **52.0%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5740 | 3028 | 2712 | 52.75 | ok |
| none | T2_mid | 6105 | 3111 | 2994 | 50.96 | ok |
| none | T3_high | 5098 | 2658 | 2440 | 52.14 | ok |
| low | T1_low | 41 | 14 | 27 | 34.15 | ok |
| low | T2_mid | 40 | 19 | 21 | 47.5 | ok |
| low | T3_high | 127 | 72 | 55 | 56.69 | ok |
| medium | T1_low | 13 | 7 | 6 | 53.85 | insufficient |
| medium | T2_mid | 21 | 7 | 14 | 33.33 | ok |
| medium | T3_high | 125 | 67 | 58 | 53.6 | ok |
| high | T1_low | 39 | 10 | 29 | 25.64 | ok |
| high | T2_mid | 21 | 10 | 11 | 47.62 | ok |
| high | T3_high | 978 | 521 | 457 | 53.27 | ok |
| missing | missing | 299 | 173 | 126 | 57.86 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 4660 | 2469 | 2191 | 52.98 | ok |
| none | T2_mid | 5369 | 2788 | 2581 | 51.93 | ok |
| none | T3_high | 3710 | 1945 | 1765 | 52.43 | ok |
| low | T1_low | 582 | 294 | 288 | 50.52 | ok |
| low | T2_mid | 391 | 184 | 207 | 47.06 | ok |
| low | T3_high | 820 | 421 | 399 | 51.34 | ok |
| medium | T1_low | 413 | 211 | 202 | 51.09 | ok |
| medium | T2_mid | 326 | 143 | 183 | 43.87 | ok |
| medium | T3_high | 1171 | 612 | 559 | 52.26 | ok |
| high | T1_low | 178 | 85 | 93 | 47.75 | ok |
| high | T2_mid | 101 | 32 | 69 | 31.68 | ok |
| high | T3_high | 627 | 340 | 287 | 54.23 | ok |
| missing | missing | 299 | 173 | 126 | 57.86 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.