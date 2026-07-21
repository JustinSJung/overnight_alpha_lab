# Trading Volume Feature Report - 2026-07-21

Generated at: 2026-07-21 02:14:00

Source ML dataset: `data/processed/ml_dataset_20260721.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **18**
- Rows with price file found: **18**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **18**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260721 | 134790 | 시디즈 | major_shareholder_change | volatile | N/A | 2,650 | N/A | N/A | 2,796 | N/A |
| 20260721 | 038680 | 에스넷 | supply_contract | positive | N/A | 126,523 | N/A | N/A | 158,864 | N/A |
| 20260721 | 036530 | SNT홀딩스 | supply_contract | positive | N/A | 15,630 | N/A | N/A | 20,920 | N/A |
| 20260721 | 100840 | SNT에너지 | supply_contract | positive | N/A | 113,256 | N/A | N/A | 156,378 | N/A |
| 20260721 | 084870 | 티비에이치글로벌 | major_shareholder_change | volatile | N/A | 19,887 | N/A | N/A | 29,803 | N/A |
| 20260721 | 084870 | 티비에이치글로벌 | major_shareholder_change | volatile | N/A | 19,887 | N/A | N/A | 29,803 | N/A |
| 20260721 | 084870 | 티비에이치글로벌 | major_shareholder_change | volatile | N/A | 19,887 | N/A | N/A | 29,803 | N/A |
| 20260721 | 084870 | 티비에이치글로벌 | major_shareholder_change | volatile | N/A | 19,887 | N/A | N/A | 29,803 | N/A |
| 20260721 | 248070 | 솔루엠 | major_shareholder_change | volatile | N/A | 159,531 | N/A | N/A | 230,625 | N/A |
| 20260721 | 248070 | 솔루엠 | major_shareholder_change | volatile | N/A | 159,531 | N/A | N/A | 230,625 | N/A |
| 20260721 | 248070 | 솔루엠 | major_shareholder_change | volatile | N/A | 159,531 | N/A | N/A | 230,625 | N/A |
| 20260721 | 248070 | 솔루엠 | major_shareholder_change | volatile | N/A | 159,531 | N/A | N/A | 230,625 | N/A |
| 20260721 | 248070 | 솔루엠 | major_shareholder_change | volatile | N/A | 159,531 | N/A | N/A | 230,625 | N/A |
| 20260721 | 248070 | 솔루엠 | major_shareholder_change | volatile | N/A | 159,531 | N/A | N/A | 230,625 | N/A |
| 20260721 | 248070 | 솔루엠 | major_shareholder_change | volatile | N/A | 159,531 | N/A | N/A | 230,625 | N/A |
| 20260721 | 248070 | 솔루엠 | major_shareholder_change | volatile | N/A | 159,531 | N/A | N/A | 230,625 | N/A |
| 20260721 | 248070 | 솔루엠 | major_shareholder_change | volatile | N/A | 159,531 | N/A | N/A | 230,625 | N/A |
| 20260721 | 004710 | 한솔테크닉스 | paid_in_capital_increase | negative | N/A | 12,431,044 | N/A | N/A | 2,936,059 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
