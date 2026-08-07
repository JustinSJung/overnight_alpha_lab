# Trading Volume Feature Report - 2026-08-07

Generated at: 2026-08-07 01:37:12

Source ML dataset: `data/processed/ml_dataset_20260807.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **3**
- Rows with price file found: **3**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **3**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260807 | 250060 | 모비스 | supply_contract | positive | N/A | 681,204 | N/A | N/A | 361,508 | N/A |
| 20260807 | 006360 | GS건설 | supply_contract | positive | N/A | 2,400,166 | N/A | N/A | 2,303,030 | N/A |
| 20260807 | 005690 | 파미셀 | supply_contract | positive | N/A | 691,664 | N/A | N/A | 559,511 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
