# Directional Penalty Diagnostics - 2026-11-12

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **2338**
- Overall success rate: **42.17%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 664 | 298 | 366 | 44.88 | ok |
| none | T2_mid | 637 | 272 | 365 | 42.7 | ok |
| none | T3_high | 495 | 207 | 288 | 41.82 | ok |
| low | T1_low | 18 | 7 | 11 | 38.89 | insufficient |
| low | T2_mid | 71 | 29 | 42 | 40.85 | ok |
| low | T3_high | 105 | 44 | 61 | 41.9 | ok |
| medium | T1_low | 6 | 2 | 4 | 33.33 | insufficient |
| medium | T2_mid | 27 | 13 | 14 | 48.15 | ok |
| medium | T3_high | 95 | 41 | 54 | 43.16 | ok |
| high | T1_low | 3 | 2 | 1 | 66.67 | insufficient |
| high | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| high | T3_high | 97 | 39 | 58 | 40.21 | ok |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 666 | 303 | 363 | 45.5 | ok |
| none | T2_mid | 713 | 306 | 407 | 42.92 | ok |
| none | T3_high | 714 | 296 | 418 | 41.46 | ok |
| low | T1_low | 13 | 2 | 11 | 15.38 | insufficient |
| low | T2_mid | 19 | 6 | 13 | 31.58 | insufficient |
| low | T3_high | 43 | 15 | 28 | 34.88 | ok |
| medium | T1_low | 10 | 2 | 8 | 20.0 | insufficient |
| medium | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| medium | T3_high | 23 | 13 | 10 | 56.52 | ok |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 3 | 2 | 1 | 66.67 | insufficient |
| high | T3_high | 12 | 7 | 5 | 58.33 | insufficient |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **20096**
- Overall success rate: **49.64%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 6468 | 3088 | 3380 | 47.74 | ok |
| none | T2_mid | 6488 | 3185 | 3303 | 49.09 | ok |
| none | T3_high | 5369 | 2773 | 2596 | 51.65 | ok |
| low | T1_low | 44 | 14 | 30 | 31.82 | ok |
| low | T2_mid | 45 | 21 | 24 | 46.67 | ok |
| low | T3_high | 127 | 72 | 55 | 56.69 | ok |
| medium | T1_low | 17 | 9 | 8 | 52.94 | insufficient |
| medium | T2_mid | 23 | 5 | 18 | 21.74 | ok |
| medium | T3_high | 132 | 72 | 60 | 54.55 | ok |
| high | T1_low | 33 | 8 | 25 | 24.24 | ok |
| high | T2_mid | 31 | 14 | 17 | 45.16 | ok |
| high | T3_high | 1018 | 540 | 478 | 53.05 | ok |
| missing | missing | 301 | 175 | 126 | 58.14 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 5291 | 2542 | 2749 | 48.04 | ok |
| none | T2_mid | 5629 | 2819 | 2810 | 50.08 | ok |
| none | T3_high | 3949 | 2065 | 1884 | 52.29 | ok |
| low | T1_low | 671 | 294 | 377 | 43.82 | ok |
| low | T2_mid | 408 | 184 | 224 | 45.1 | ok |
| low | T3_high | 853 | 430 | 423 | 50.41 | ok |
| medium | T1_low | 429 | 203 | 226 | 47.32 | ok |
| medium | T2_mid | 415 | 174 | 241 | 41.93 | ok |
| medium | T3_high | 1194 | 611 | 583 | 51.17 | ok |
| high | T1_low | 171 | 80 | 91 | 46.78 | ok |
| high | T2_mid | 135 | 48 | 87 | 35.56 | ok |
| high | T3_high | 650 | 351 | 299 | 54.0 | ok |
| missing | missing | 301 | 175 | 126 | 58.14 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.