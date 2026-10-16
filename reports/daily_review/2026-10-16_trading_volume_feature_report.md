# Trading Volume Feature Report - 2026-10-16

Generated at: 2026-10-16 00:50:10

Source ML dataset: `data/processed/ml_dataset_20261016.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **53173**
- Rows with price file found: **53173**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **53173**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261015 | 019570 | GMI벤처 | major_shareholder_change | volatile | N/A | 13,544 | N/A | N/A | 12,912 | N/A |
| 20261015 | 019570 | GMI벤처 | major_shareholder_change | volatile | N/A | 13,544 | N/A | N/A | 12,912 | N/A |
| 20261015 | 019570 | GMI벤처 | major_shareholder_change | volatile | N/A | 13,544 | N/A | N/A | 12,912 | N/A |
| 20261015 | 019570 | GMI벤처 | major_shareholder_change | volatile | N/A | 13,544 | N/A | N/A | 12,912 | N/A |
| 20261015 | 033310 | 엠투엔 | major_shareholder_change | volatile | N/A | 35,092 | N/A | N/A | 29,441 | N/A |
| 20261015 | 031860 | 디에이치엑스컴퍼니 | lawsuit | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261015 | 336570 | 원텍 | disclosure_violation | negative | N/A | 371,770 | N/A | N/A | 276,169 | N/A |
| 20261015 | 336570 | 원텍 | disclosure_violation | negative | N/A | 371,770 | N/A | N/A | 276,169 | N/A |
| 20261015 | 336570 | 원텍 | disclosure_violation | negative | N/A | 371,770 | N/A | N/A | 276,169 | N/A |
| 20261015 | 336570 | 원텍 | disclosure_violation | negative | N/A | 371,770 | N/A | N/A | 276,169 | N/A |
| 20261015 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | N/A | 389,682 | N/A | N/A | 146,407 | N/A |
| 20261015 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | N/A | 389,682 | N/A | N/A | 146,407 | N/A |
| 20261015 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | N/A | 389,682 | N/A | N/A | 146,407 | N/A |
| 20261015 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | N/A | 389,682 | N/A | N/A | 146,407 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |
| 20261015 | 288980 | 모아데이타 | major_shareholder_change | volatile | N/A | 8,857,587 | N/A | N/A | 1,223,100 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
