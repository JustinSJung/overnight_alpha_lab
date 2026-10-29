# Trading Volume Feature Report - 2026-10-09

Generated at: 2026-10-09 02:45:38

Source ML dataset: `data/processed/ml_dataset_20261009.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **2926853**
- Rows with price file found: **2926853**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **2926853**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |
| 20261008 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | N/A | 929,961 | N/A | N/A | 177,844 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
