# Trading Volume Feature Report - 2026-09-02

Generated at: 2026-09-02 00:49:27

Source ML dataset: `data/processed/ml_dataset_20260902.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **1858**
- Rows with price file found: **1857**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **1857**
- price_file_missing: **1**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260901 | 064290 | 인텍플러스 | supply_contract | positive | N/A | 159,126 | N/A | N/A | 249,069 | N/A |
| 20260901 | 066430 | 아이로보틱스 | lawsuit | negative | N/A | 4,358,411 | N/A | N/A | 1,550,693 | N/A |
| 20260901 | 368770 | 파이버프로 | supply_contract | positive | N/A | 81,292 | N/A | N/A | 124,189 | N/A |
| 20260901 | 045660 | 에이텍 | supply_contract | positive | N/A | 9,540 | N/A | N/A | 11,951 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |
| 20260901 | 034020 | 두산에너빌리티 | supply_contract | positive | N/A | 1,762,521 | N/A | N/A | 2,577,175 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
