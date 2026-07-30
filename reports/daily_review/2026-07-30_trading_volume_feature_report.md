# Trading Volume Feature Report - 2026-07-30

Generated at: 2026-07-30 02:43:25

Source ML dataset: `data/processed/ml_dataset_20260730.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **22**
- Rows with price file found: **22**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **22**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260730 | 107640 | 한중엔시에스 | merger | volatile | N/A | 83,123 | N/A | N/A | 69,184 | N/A |
| 20260730 | 007570 | 일양약품 | major_shareholder_change | volatile | N/A | 46,982 | N/A | N/A | 75,353 | N/A |
| 20260730 | 206400 | 베노티앤알 | supply_contract | positive | N/A | 41,300 | N/A | N/A | 28,775 | N/A |
| 20260730 | 080420 | 모다이노칩 | merger | volatile | N/A | 4,799 | N/A | N/A | 9,832 | N/A |
| 20260730 | 080420 | 모다이노칩 | merger | volatile | N/A | 4,799 | N/A | N/A | 9,832 | N/A |
| 20260730 | 080420 | 모다이노칩 | merger | volatile | N/A | 4,799 | N/A | N/A | 9,832 | N/A |
| 20260730 | 080420 | 모다이노칩 | merger | volatile | N/A | 4,799 | N/A | N/A | 9,832 | N/A |
| 20260730 | 080420 | 모다이노칩 | merger | volatile | N/A | 4,799 | N/A | N/A | 9,832 | N/A |
| 20260730 | 080420 | 모다이노칩 | merger | volatile | N/A | 4,799 | N/A | N/A | 9,832 | N/A |
| 20260730 | 080420 | 모다이노칩 | merger | volatile | N/A | 4,799 | N/A | N/A | 9,832 | N/A |
| 20260730 | 080420 | 모다이노칩 | merger | volatile | N/A | 4,799 | N/A | N/A | 9,832 | N/A |
| 20260730 | 080420 | 모다이노칩 | merger | volatile | N/A | 4,799 | N/A | N/A | 9,832 | N/A |
| 20260730 | 420770 | 기가비스 | supply_contract | positive | N/A | 149,883 | N/A | N/A | 115,873 | N/A |
| 20260730 | 025560 | 미래산업 | supply_contract | positive | N/A | 3,000,280 | N/A | N/A | 3,319,675 | N/A |
| 20260730 | 460940 | 피앤에스로보틱스 | supply_contract | positive | N/A | 81,340 | N/A | N/A | 57,712 | N/A |
| 20260730 | 011330 | 유니켐 | paid_in_capital_increase | negative | N/A | 66,768 | N/A | N/A | 154,796 | N/A |
| 20260730 | 402490 | 그린리소스 | paid_in_capital_increase | negative | N/A | 111,632 | N/A | N/A | 159,061 | N/A |
| 20260730 | 402490 | 그린리소스 | paid_in_capital_increase | negative | N/A | 111,632 | N/A | N/A | 159,061 | N/A |
| 20260730 | 402490 | 그린리소스 | paid_in_capital_increase | negative | N/A | 111,632 | N/A | N/A | 159,061 | N/A |
| 20260730 | 402490 | 그린리소스 | paid_in_capital_increase | negative | N/A | 111,632 | N/A | N/A | 159,061 | N/A |
| 20260730 | 104460 | 디와이피엔에프 | supply_contract | positive | N/A | 7,155 | N/A | N/A | 15,467 | N/A |
| 20260730 | 119850 | 지엔씨에너지 | supply_contract | positive | N/A | 190,803 | N/A | N/A | 813,362 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
