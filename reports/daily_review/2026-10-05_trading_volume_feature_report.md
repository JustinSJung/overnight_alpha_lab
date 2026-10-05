# Trading Volume Feature Report - 2026-10-05

Generated at: 2026-10-05 01:19:26

Source ML dataset: `data/processed/ml_dataset_20261005.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **9556**
- Rows with price file found: **9556**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **9556**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261002 | 235980 | 메드팩토 | investment_decision | volatile | N/A | 53,259 | N/A | N/A | 55,173 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 355390 | 크라우드웍스 | paid_in_capital_increase | negative | N/A | 170,662 | N/A | N/A | 297,875 | N/A |
| 20261002 | 003060 | 에이프로젠바이오로직스 | major_shareholder_change | volatile | N/A | 787,223 | N/A | N/A | 468,312 | N/A |
| 20261002 | 003060 | 에이프로젠바이오로직스 | major_shareholder_change | volatile | N/A | 787,223 | N/A | N/A | 468,312 | N/A |
| 20261002 | 003060 | 에이프로젠바이오로직스 | major_shareholder_change | volatile | N/A | 787,223 | N/A | N/A | 468,312 | N/A |
| 20261002 | 003060 | 에이프로젠바이오로직스 | major_shareholder_change | volatile | N/A | 787,223 | N/A | N/A | 468,312 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
