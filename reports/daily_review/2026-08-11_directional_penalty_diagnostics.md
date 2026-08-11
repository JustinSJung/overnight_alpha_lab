# Directional Penalty Diagnostics - 2026-08-11

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **196**
- Overall success rate: **42.86%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 37 | 20 | 17 | 54.05 | ok |
| none | T2_mid | 29 | 14 | 15 | 48.28 | ok |
| none | T3_high | 12 | 9 | 3 | 75.0 | insufficient |
| low | T1_low | 2 | 1 | 1 | 50.0 | insufficient |
| low | T2_mid | 5 | 3 | 2 | 60.0 | insufficient |
| low | T3_high | 10 | 4 | 6 | 40.0 | insufficient |
| medium | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| medium | T2_mid | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T3_high | 7 | 3 | 4 | 42.86 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| high | T3_high | 5 | 3 | 2 | 60.0 | insufficient |
| missing | missing | 84 | 24 | 60 | 28.57 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 40 | 22 | 18 | 55.0 | ok |
| none | T2_mid | 35 | 17 | 18 | 48.57 | ok |
| none | T3_high | 32 | 17 | 15 | 53.12 | ok |
| low | T3_high | 2 | 2 | 0 | 100.0 | insufficient |
| medium | T2_mid | 2 | 1 | 1 | 50.0 | insufficient |
| high | T2_mid | 1 | 1 | 0 | 100.0 | insufficient |
| missing | missing | 84 | 24 | 60 | 28.57 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **1526**
- Overall success rate: **42.73%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 346 | 114 | 232 | 32.95 | ok |
| none | T2_mid | 400 | 153 | 247 | 38.25 | ok |
| none | T3_high | 278 | 114 | 164 | 41.01 | ok |
| low | T1_low | 10 | 3 | 7 | 30.0 | insufficient |
| low | T2_mid | 12 | 5 | 7 | 41.67 | insufficient |
| low | T3_high | 19 | 6 | 13 | 31.58 | insufficient |
| medium | T1_low | 5 | 2 | 3 | 40.0 | insufficient |
| medium | T2_mid | 9 | 2 | 7 | 22.22 | insufficient |
| medium | T3_high | 15 | 7 | 8 | 46.67 | insufficient |
| high | T1_low | 18 | 3 | 15 | 16.67 | insufficient |
| high | T2_mid | 21 | 8 | 13 | 38.1 | ok |
| high | T3_high | 109 | 69 | 40 | 63.3 | ok |
| missing | missing | 284 | 166 | 118 | 58.45 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 177 | 49 | 128 | 27.68 | ok |
| none | T2_mid | 254 | 91 | 163 | 35.83 | ok |
| none | T3_high | 153 | 57 | 96 | 37.25 | ok |
| low | T1_low | 86 | 28 | 58 | 32.56 | ok |
| low | T2_mid | 64 | 23 | 41 | 35.94 | ok |
| low | T3_high | 58 | 24 | 34 | 41.38 | ok |
| medium | T1_low | 77 | 31 | 46 | 40.26 | ok |
| medium | T2_mid | 82 | 35 | 47 | 42.68 | ok |
| medium | T3_high | 97 | 44 | 53 | 45.36 | ok |
| high | T1_low | 39 | 14 | 25 | 35.9 | ok |
| high | T2_mid | 42 | 19 | 23 | 45.24 | ok |
| high | T3_high | 113 | 71 | 42 | 62.83 | ok |
| missing | missing | 284 | 166 | 118 | 58.45 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.