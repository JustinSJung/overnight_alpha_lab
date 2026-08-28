# Trading Volume Feature Report - 2026-08-28

Generated at: 2026-08-28 06:12:12

Source ML dataset: `data/processed/ml_dataset_20260828.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **4**
- Rows with price file found: **4**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **4**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260828 | 178780 | 일월지엠엘 | paid_in_capital_increase | negative | N/A | 23,374 | N/A | N/A | 4,492 | N/A |
| 20260828 | 028100 | 동아지질 | supply_contract | positive | N/A | 59,408 | N/A | N/A | 40,841 | N/A |
| 20260828 | 088390 | 이녹스 | supply_contract | positive | N/A | 28,445 | N/A | N/A | 16,435 | N/A |
| 20260828 | 123750 | 알톤 | supply_contract | positive | N/A | 74,905 | N/A | N/A | 32,471 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
