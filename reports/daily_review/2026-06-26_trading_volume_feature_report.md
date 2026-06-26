# Trading Volume Feature Report - 2026-06-26

Generated at: 2026-06-26 16:11:02

Source ML dataset: `data/processed/ml_dataset_20260626.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **24**
- Rows with price file found: **24**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **24**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260626 | 221840 | 하이즈항공 | lawsuit | negative | N/A | 43,338 | N/A | N/A | 55,572 | N/A |
| 20260626 | 439580 | 블루엠텍 | bond_with_warrant | negative | N/A | 372,964 | N/A | N/A | 231,811 | N/A |
| 20260626 | 224060 | 더코디 | convertible_bond | negative | N/A | 27,884 | N/A | N/A | 27,873 | N/A |
| 20260626 | 014130 | 한익스프레스 | major_shareholder_change | volatile | N/A | 22,255 | N/A | N/A | 13,728 | N/A |
| 20260626 | 014130 | 한익스프레스 | major_shareholder_change | volatile | N/A | 22,255 | N/A | N/A | 13,728 | N/A |
| 20260626 | 014130 | 한익스프레스 | major_shareholder_change | volatile | N/A | 22,255 | N/A | N/A | 13,728 | N/A |
| 20260626 | 014130 | 한익스프레스 | major_shareholder_change | volatile | N/A | 22,255 | N/A | N/A | 13,728 | N/A |
| 20260626 | 082740 | 한화엔진 | supply_contract | positive | N/A | 1,869,454 | N/A | N/A | 1,066,043 | N/A |
| 20260626 | 259960 | 크래프톤 | major_shareholder_change | volatile | N/A | 139,718 | N/A | N/A | 154,742 | N/A |
| 20260626 | 259960 | 크래프톤 | major_shareholder_change | volatile | N/A | 139,718 | N/A | N/A | 154,742 | N/A |
| 20260626 | 259960 | 크래프톤 | major_shareholder_change | volatile | N/A | 139,718 | N/A | N/A | 154,742 | N/A |
| 20260626 | 259960 | 크래프톤 | major_shareholder_change | volatile | N/A | 139,718 | N/A | N/A | 154,742 | N/A |
| 20260626 | 259960 | 크래프톤 | major_shareholder_change | volatile | N/A | 139,718 | N/A | N/A | 154,742 | N/A |
| 20260626 | 259960 | 크래프톤 | major_shareholder_change | volatile | N/A | 139,718 | N/A | N/A | 154,742 | N/A |
| 20260626 | 259960 | 크래프톤 | major_shareholder_change | volatile | N/A | 139,718 | N/A | N/A | 154,742 | N/A |
| 20260626 | 259960 | 크래프톤 | major_shareholder_change | volatile | N/A | 139,718 | N/A | N/A | 154,742 | N/A |
| 20260626 | 259960 | 크래프톤 | major_shareholder_change | volatile | N/A | 139,718 | N/A | N/A | 154,742 | N/A |
| 20260626 | 066980 | 한성크린텍 | supply_contract | positive | N/A | 3,174,701 | N/A | N/A | 10,672,425 | N/A |
| 20260626 | 074610 | 이엔플러스 | convertible_bond | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260626 | 348080 | 큐라티스 | spin_off | volatile | N/A | 214,539 | N/A | N/A | 137,973 | N/A |
| 20260626 | 090350 | 노루페인트 | major_shareholder_change | volatile | N/A | 123,106 | N/A | N/A | 86,441 | N/A |
| 20260626 | 033250 | 체시스 | major_shareholder_change | volatile | N/A | 20,975 | N/A | N/A | 21,368 | N/A |
| 20260626 | 021240 | 코웨이 | major_shareholder_change | volatile | N/A | 189,586 | N/A | N/A | 246,327 | N/A |
| 20260626 | 229000 | 젠큐릭스 | merger | volatile | N/A | 7,899,645 | N/A | N/A | 5,899,432 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
