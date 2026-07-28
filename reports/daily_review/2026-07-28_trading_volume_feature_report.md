# Trading Volume Feature Report - 2026-07-28

Generated at: 2026-07-28 23:19:20

Source ML dataset: `data/processed/ml_dataset_20260728.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **61**
- Rows with price file found: **61**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **61**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260728 | 217730 | 강스템바이오텍 | investment_decision | volatile | N/A | 410,364 | N/A | N/A | 313,691 | N/A |
| 20260728 | 217730 | 강스템바이오텍 | investment_decision | volatile | N/A | 410,364 | N/A | N/A | 313,691 | N/A |
| 20260728 | 217730 | 강스템바이오텍 | investment_decision | volatile | N/A | 410,364 | N/A | N/A | 313,691 | N/A |
| 20260728 | 217730 | 강스템바이오텍 | investment_decision | volatile | N/A | 410,364 | N/A | N/A | 313,691 | N/A |
| 20260728 | 083640 | 인콘 | investment_decision | volatile | N/A | 234,249 | N/A | N/A | 177,573 | N/A |
| 20260728 | 060900 | 에이전트AI | paid_in_capital_increase | negative | N/A | 16,695 | N/A | N/A | 8,146 | N/A |
| 20260728 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 187,601 | N/A | N/A | 324,185 | N/A |
| 20260728 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 187,601 | N/A | N/A | 324,185 | N/A |
| 20260728 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 187,601 | N/A | N/A | 324,185 | N/A |
| 20260728 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 187,601 | N/A | N/A | 324,185 | N/A |
| 20260728 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 85,336 | N/A | N/A | 29,900 | N/A |
| 20260728 | 064350 | 현대로템 | investment_decision | volatile | N/A | 623,798 | N/A | N/A | 485,861 | N/A |
| 20260728 | 066410 | 버킷스튜디오 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260728 | 032800 | 판타지오 | paid_in_capital_increase | negative | N/A | 595,104 | N/A | N/A | 69,798 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |
| 20260728 | 210980 | SK디앤디 | paid_in_capital_increase | negative | N/A | 9,392 | N/A | N/A | 14,241 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
