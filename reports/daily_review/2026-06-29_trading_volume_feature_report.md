# Trading Volume Feature Report - 2026-06-29

Generated at: 2026-06-29 14:39:36

Source ML dataset: `data/processed/ml_dataset_20260629.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **4713**
- Rows with price file found: **4713**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **4713**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260629 | 068240 | 다원시스 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260629 | 109740 | 디에스케이 | major_shareholder_change | volatile | N/A | 117,407 | N/A | N/A | 39,601 | N/A |
| 20260629 | 109740 | 디에스케이 | major_shareholder_change | volatile | N/A | 117,407 | N/A | N/A | 39,601 | N/A |
| 20260629 | 109740 | 디에스케이 | major_shareholder_change | volatile | N/A | 117,407 | N/A | N/A | 39,601 | N/A |
| 20260629 | 109740 | 디에스케이 | major_shareholder_change | volatile | N/A | 117,407 | N/A | N/A | 39,601 | N/A |
| 20260629 | 247540 | 에코프로비엠 | lawsuit | negative | N/A | 662,016 | N/A | N/A | 867,237 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |
| 20260629 | 083660 | CSA 코스믹 | spin_off | volatile | N/A | 726,438 | N/A | N/A | 489,368 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
