# Trading Volume Feature Report - 2026-11-11

Generated at: 2026-11-11 06:02:51

Source ML dataset: `data/processed/ml_dataset_20261111.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **570688**
- Rows with price file found: **570688**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **570688**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261110 | 065420 | 에스아이리소스 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 010960 | 삼호개발 | supply_contract | positive | N/A | 200,390 | N/A | N/A | 144,343 | N/A |
| 20261110 | 247540 | 에코프로비엠 | paid_in_capital_increase | negative | N/A | 560,088 | N/A | N/A | 569,576 | N/A |
| 20261110 | 247540 | 에코프로비엠 | paid_in_capital_increase | negative | N/A | 560,088 | N/A | N/A | 569,576 | N/A |
| 20261110 | 247540 | 에코프로비엠 | paid_in_capital_increase | negative | N/A | 560,088 | N/A | N/A | 569,576 | N/A |
| 20261110 | 247540 | 에코프로비엠 | paid_in_capital_increase | negative | N/A | 560,088 | N/A | N/A | 569,576 | N/A |
| 20261110 | 307180 | 아이엘 | convertible_bond | negative | N/A | 310,413 | N/A | N/A | 397,129 | N/A |
| 20261110 | 066790 | 씨씨에스 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261110 | 300080 | 플리토 | supply_contract | positive | N/A | 81,337 | N/A | N/A | 38,914 | N/A |
| 20261110 | 300080 | 플리토 | supply_contract | positive | N/A | 81,337 | N/A | N/A | 38,914 | N/A |
| 20261110 | 300080 | 플리토 | supply_contract | positive | N/A | 81,337 | N/A | N/A | 38,914 | N/A |
| 20261110 | 300080 | 플리토 | supply_contract | positive | N/A | 81,337 | N/A | N/A | 38,914 | N/A |
| 20261110 | 005880 | 대한해운 | major_shareholder_change | volatile | N/A | 2,880,044 | N/A | N/A | 1,510,735 | N/A |
| 20261110 | 005880 | 대한해운 | major_shareholder_change | volatile | N/A | 2,880,044 | N/A | N/A | 1,510,735 | N/A |
| 20261110 | 005880 | 대한해운 | major_shareholder_change | volatile | N/A | 2,880,044 | N/A | N/A | 1,510,735 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
