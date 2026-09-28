# Directional Penalty Diagnostics - 2026-09-28

Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score tertiles, split by candidate direction. This report is diagnostic only: it does not change score weights, penalty formulas, or candidate selection.

Cells with fewer than 20 evaluated cases are flagged `insufficient` and should be read conservatively rather than acted on.

## Buy-Type (매수형)

- Evaluated cases (all penalty/momentum buckets): **1194**
- Overall success rate: **42.46%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 334 | 155 | 179 | 46.41 | ok |
| none | T2_mid | 309 | 137 | 172 | 44.34 | ok |
| none | T3_high | 235 | 105 | 130 | 44.68 | ok |
| low | T1_low | 7 | 3 | 4 | 42.86 | insufficient |
| low | T2_mid | 29 | 12 | 17 | 41.38 | ok |
| low | T3_high | 50 | 19 | 31 | 38.0 | ok |
| medium | T1_low | 4 | 0 | 4 | 0.0 | insufficient |
| medium | T2_mid | 13 | 8 | 5 | 61.54 | insufficient |
| medium | T3_high | 48 | 21 | 27 | 43.75 | ok |
| high | T1_low | 1 | 1 | 0 | 100.0 | insufficient |
| high | T2_mid | 9 | 3 | 6 | 33.33 | insufficient |
| high | T3_high | 50 | 19 | 31 | 38.0 | ok |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 328 | 153 | 175 | 46.65 | ok |
| none | T2_mid | 339 | 153 | 186 | 45.13 | ok |
| none | T3_high | 340 | 143 | 197 | 42.06 | ok |
| low | T1_low | 13 | 3 | 10 | 23.08 | insufficient |
| low | T2_mid | 13 | 4 | 9 | 30.77 | insufficient |
| low | T3_high | 24 | 10 | 14 | 41.67 | ok |
| medium | T1_low | 3 | 1 | 2 | 33.33 | insufficient |
| medium | T2_mid | 7 | 3 | 4 | 42.86 | insufficient |
| medium | T3_high | 14 | 7 | 7 | 50.0 | insufficient |
| high | T1_low | 2 | 2 | 0 | 100.0 | insufficient |
| high | T2_mid | 1 | 0 | 1 | 0.0 | insufficient |
| high | T3_high | 5 | 4 | 1 | 80.0 | insufficient |
| missing | missing | 105 | 24 | 81 | 22.86 | ok |

## Avoid-Type (회피형)

- Evaluated cases (all penalty/momentum buckets): **6882**
- Overall success rate: **46.75%**

### overextension_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 2147 | 961 | 1186 | 44.76 | ok |
| none | T2_mid | 2136 | 982 | 1154 | 45.97 | ok |
| none | T3_high | 1410 | 658 | 752 | 46.67 | ok |
| low | T1_low | 23 | 3 | 20 | 13.04 | ok |
| low | T2_mid | 15 | 8 | 7 | 53.33 | insufficient |
| low | T3_high | 74 | 37 | 37 | 50.0 | ok |
| medium | T1_low | 13 | 5 | 8 | 38.46 | insufficient |
| medium | T2_mid | 11 | 6 | 5 | 54.55 | insufficient |
| medium | T3_high | 67 | 32 | 35 | 47.76 | ok |
| high | T1_low | 45 | 12 | 33 | 26.67 | ok |
| high | T2_mid | 13 | 8 | 5 | 61.54 | insufficient |
| high | T3_high | 618 | 324 | 294 | 52.43 | ok |
| missing | missing | 310 | 181 | 129 | 58.39 | ok |

### reversal_risk_penalty x base_momentum_score tertile

| penalty_bucket | momentum_tertile | evaluated_count | success_count | failure_count | success_rate | confidence_flag |
|---|---|---|---|---|---|---|
| none | T1_low | 1517 | 670 | 847 | 44.17 | ok |
| none | T2_mid | 1825 | 851 | 974 | 46.63 | ok |
| none | T3_high | 766 | 351 | 415 | 45.82 | ok |
| low | T1_low | 295 | 115 | 180 | 38.98 | ok |
| low | T2_mid | 158 | 62 | 96 | 39.24 | ok |
| low | T3_high | 365 | 173 | 192 | 47.4 | ok |
| medium | T1_low | 255 | 120 | 135 | 47.06 | ok |
| medium | T2_mid | 128 | 63 | 65 | 49.22 | ok |
| medium | T3_high | 644 | 318 | 326 | 49.38 | ok |
| high | T1_low | 161 | 76 | 85 | 47.2 | ok |
| high | T2_mid | 64 | 28 | 36 | 43.75 | ok |
| high | T3_high | 394 | 209 | 185 | 53.05 | ok |
| missing | missing | 310 | 181 | 129 | 58.39 | ok |

## Notes

- `momentum_tertile` is computed within each direction's evaluated subset (T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few distinct momentum values were available to split into tertiles.
- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells conservatively even when not flagged `insufficient`.
- This report does not feed back into scoring, penalty weights, or candidate selection.