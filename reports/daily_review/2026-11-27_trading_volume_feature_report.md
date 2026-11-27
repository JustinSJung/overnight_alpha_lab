# Trading Volume Feature Report - 2026-11-27

Generated at: 2026-11-27 05:31:58

Source ML dataset: `data/processed/ml_dataset_20261127.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **104363**
- Rows with price file found: **104363**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **104363**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261126 | 115180 | 큐리언트 | paid_in_capital_increase | negative | N/A | 150,500 | N/A | N/A | 98,263 | N/A |
| 20261126 | 212310 | 오건에코텍 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261126 | 212310 | 오건에코텍 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261126 | 212310 | 오건에코텍 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261126 | 212310 | 오건에코텍 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261126 | 212310 | 오건에코텍 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261126 | 212310 | 오건에코텍 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261126 | 212310 | 오건에코텍 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261126 | 212310 | 오건에코텍 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261126 | 212310 | 오건에코텍 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |
| 20261126 | 192410 | 오늘이엔엠 | lawsuit | negative | N/A | 37,253 | N/A | N/A | 34,036 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
