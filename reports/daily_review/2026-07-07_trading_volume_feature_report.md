# Trading Volume Feature Report - 2026-07-07

Generated at: 2026-07-07 23:19:47

Source ML dataset: `data/processed/ml_dataset_20260707.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **8228**
- Rows with price file found: **8228**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **8228**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260707 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 565,046 | N/A | N/A | 261,325 | N/A |
| 20260707 | 216080 | 제테마 | convertible_bond | negative | N/A | 185,352 | N/A | N/A | 113,843 | N/A |
| 20260707 | 380540 | 옵티코어 | supply_contract | positive | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260707 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | N/A | 242,944 | N/A | N/A | 162,375 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |
| 20260707 | 263800 | 데이타솔루션 | supply_contract | positive | N/A | 171,823 | N/A | N/A | 89,511 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
