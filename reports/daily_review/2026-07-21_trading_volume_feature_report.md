# Trading Volume Feature Report - 2026-07-21

Generated at: 2026-07-21 05:32:29

Source ML dataset: `data/processed/ml_dataset_20260721.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **6**
- Rows with price file found: **6**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **6**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260721 | 127120 | 제이에스링크 | paid_in_capital_increase | negative | N/A | 91,701 | N/A | N/A | 224,358 | N/A |
| 20260721 | 215380 | 우정바이오 | merger | volatile | N/A | 97,244 | N/A | N/A | 187,152 | N/A |
| 20260721 | 009810 | 플레이그램 | paid_in_capital_increase | negative | N/A | 4,892 | N/A | N/A | 96,350 | N/A |
| 20260721 | 009810 | 플레이그램 | paid_in_capital_increase | negative | N/A | 4,892 | N/A | N/A | 96,350 | N/A |
| 20260721 | 009810 | 플레이그램 | paid_in_capital_increase | negative | N/A | 4,892 | N/A | N/A | 96,350 | N/A |
| 20260721 | 009810 | 플레이그램 | paid_in_capital_increase | negative | N/A | 4,892 | N/A | N/A | 96,350 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
