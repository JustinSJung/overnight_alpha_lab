# Trading Volume Feature Report - 2026-06-26

Generated at: 2026-06-26 07:57:05

Source ML dataset: `data/processed/ml_dataset_20260626.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **16493**
- Rows with price file found: **16493**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **16493**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260626 | 013580 | 계룡건설산업 | supply_contract | positive | N/A | 125,107 | N/A | N/A | 166,032 | N/A |
| 20260626 | 013580 | 계룡건설산업 | supply_contract | positive | N/A | 125,107 | N/A | N/A | 166,032 | N/A |
| 20260626 | 013580 | 계룡건설산업 | supply_contract | positive | N/A | 125,107 | N/A | N/A | 166,032 | N/A |
| 20260626 | 013580 | 계룡건설산업 | supply_contract | positive | N/A | 125,107 | N/A | N/A | 166,032 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
