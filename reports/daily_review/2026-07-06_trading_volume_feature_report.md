# Trading Volume Feature Report - 2026-07-06

Generated at: 2026-07-06 23:35:34

Source ML dataset: `data/processed/ml_dataset_20260706.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **4123**
- Rows with price file found: **4123**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **4123**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260706 | 003490 | 대한항공 | merger | volatile | N/A | 1,684,972 | N/A | N/A | 1,827,147 | N/A |
| 20260706 | 020560 | 아시아나항공 | merger | volatile | N/A | 156,741 | N/A | N/A | 57,789 | N/A |
| 20260706 | 088790 | 진도 | lawsuit | negative | N/A | 33,602 | N/A | N/A | 34,300 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260706 | 001470 | 삼부토건 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
