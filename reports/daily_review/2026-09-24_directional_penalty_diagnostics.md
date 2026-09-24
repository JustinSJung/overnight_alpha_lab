# Directional Penalty Diagnostics - 2026-09-24

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1119**
- Overall success rate: **42.18%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 311 | 141 | 170 | 45.34 | ok |
| none | T2_mid | 292 | 130 | 162 | 44.52 | ok |
| none | T3_high | 219 | 96 | 123 | 43.84 | ok |
| low | T1_low | 6 | 3 | 3 | 50.0 | insufficient |
| low | T2_mid | 28 | 11 | 17 | 39.29 | ok |
| low | T3_high | 49 | 19 | 30 | 38.78 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 10 | 7 | 3 | 70.0 | insufficient |
| medium | T3_high | 42 | 18 | 24 | 42.86 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 9 | 3 | 6 | 33.33 | insufficient |
| high | T3_high | 46 | 19 | 27 | 41.3 | ok |
| missing | missing | 102 | 24 | 78 | 23.53 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 308 | 142 | 166 | 46.1 | ok |
| none | T2_mid | 319 | 144 | 175 | 45.14 | ok |
| none | T3_high | 314 | 131 | 183 | 41.72 | ok |
| low | T1_low | 12 | 3 | 9 | 25.0 | insufficient |
| low | T2_mid | 13 | 4 | 9 | 30.77 | insufficient |
| low | T3_high | 24 | 10 | 14 | 41.67 | ok |
| medium | T1_low | 2 | 0 | 2 | 0.0 | insufficient |
| medium | T2_mid | 6 | 3 | 3 | 50.0 | insufficient |
| medium | T3_high | 13 | 7 | 6 | 53.85 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 5 | 4 | 1 | 80.0 | insufficient |
| missing | missing | 102 | 24 | 78 | 23.53 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **6412**
- Overall success rate: **47.29%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1987 | 888 | 1099 | 44.69 | ok |
| none | T2_mid | 1999 | 942 | 1057 | 47.12 | ok |
| none | T3_high | 1300 | 615 | 685 | 47.31 | ok |
| low | T1_low | 21 | 3 | 18 | 14.29 | ok |
| low | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| low | T3_high | 69 | 36 | 33 | 52.17 | ok |
| medium | T1_low | 9 | 2 | 7 | 22.22 | insufficient |
| medium | T2_mid | 11 | 6 | 5 | 54.55 | insufficient |
| medium | T3_high | 61 | 31 | 30 | 50.82 | ok |
| high | T1_low | 39 | 10 | 29 | 25.64 | ok |
| high | T2_mid | 15 | 9 | 6 | 60.0 | insufficient |
| high | T3_high | 588 | 309 | 279 | 52.55 | ok |
| missing | missing | 298 | 173 | 125 | 58.05 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1406 | 624 | 782 | 44.38 | ok |
| none | T2_mid | 1707 | 821 | 886 | 48.1 | ok |
| none | T3_high | 694 | 322 | 372 | 46.4 | ok |
| low | T1_low | 275 | 110 | 165 | 40.0 | ok |
| low | T2_mid | 151 | 60 | 91 | 39.74 | ok |
| low | T3_high | 344 | 165 | 179 | 47.97 | ok |
| medium | T1_low | 224 | 98 | 126 | 43.75 | ok |
| medium | T2_mid | 119 | 57 | 62 | 47.9 | ok |
| medium | T3_high | 606 | 302 | 304 | 49.83 | ok |
| high | T1_low | 151 | 71 | 80 | 47.02 | ok |
| high | T2_mid | 63 | 27 | 36 | 42.86 | ok |
| high | T3_high | 374 | 202 | 172 | 54.01 | ok |
| missing | missing | 298 | 173 | 125 | 58.05 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.