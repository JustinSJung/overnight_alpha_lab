# Directional Penalty Diagnostics - 2026-09-25

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1145**
- Overall success rate: **41.57%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 318 | 144 | 174 | 45.28 | ok |
| none | T2_mid | 298 | 130 | 168 | 43.62 | ok |
| none | T3_high | 220 | 96 | 124 | 43.64 | ok |
| low | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| low | T2_mid | 29 | 12 | 17 | 41.38 | ok |
| low | T3_high | 49 | 19 | 30 | 38.78 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 11 | 7 | 4 | 63.64 | insufficient |
| medium | T3_high | 45 | 18 | 27 | 40.0 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 9 | 3 | 6 | 33.33 | insufficient |
| high | T3_high | 49 | 19 | 30 | 38.78 | ok |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 315 | 145 | 170 | 46.03 | ok |
| none | T2_mid | 327 | 145 | 182 | 44.34 | ok |
| none | T3_high | 320 | 131 | 189 | 40.94 | ok |
| low | T1_low | 13 | 3 | 10 | 23.08 | insufficient |
| low | T2_mid | 13 | 4 | 9 | 30.77 | insufficient |
| low | T3_high | 24 | 10 | 14 | 41.67 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T3_high | 14 | 7 | 7 | 50.0 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 5 | 4 | 1 | 80.0 | insufficient |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **6590**
- Overall success rate: **47.19%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2054 | 913 | 1141 | 44.45 | ok |
| none | T2_mid | 2041 | 956 | 1085 | 46.84 | ok |
| none | T3_high | 1329 | 633 | 696 | 47.63 | ok |
| low | T1_low | 23 | 3 | 20 | 13.04 | ok |
| low | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| low | T3_high | 71 | 36 | 35 | 50.7 | ok |
| medium | T1_low | 13 | 5 | 8 | 38.46 | insufficient |
| medium | T2_mid | 11 | 6 | 5 | 54.55 | insufficient |
| medium | T3_high | 64 | 32 | 32 | 50.0 | ok |
| high | T1_low | 42 | 11 | 31 | 26.19 | ok |
| high | T2_mid | 15 | 9 | 6 | 60.0 | insufficient |
| high | T3_high | 602 | 317 | 285 | 52.66 | ok |
| missing | missing | 310 | 181 | 129 | 58.39 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1445 | 635 | 810 | 43.94 | ok |
| none | T2_mid | 1734 | 827 | 907 | 47.69 | ok |
| none | T3_high | 705 | 330 | 375 | 46.81 | ok |
| low | T1_low | 289 | 113 | 176 | 39.1 | ok |
| low | T2_mid | 158 | 63 | 95 | 39.87 | ok |
| low | T3_high | 350 | 169 | 181 | 48.29 | ok |
| medium | T1_low | 242 | 110 | 132 | 45.45 | ok |
| medium | T2_mid | 125 | 60 | 65 | 48.0 | ok |
| medium | T3_high | 625 | 311 | 314 | 49.76 | ok |
| high | T1_low | 156 | 74 | 82 | 47.44 | ok |
| high | T2_mid | 65 | 29 | 36 | 44.62 | ok |
| high | T3_high | 386 | 208 | 178 | 53.89 | ok |
| missing | missing | 310 | 181 | 129 | 58.39 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.