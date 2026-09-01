# Trading Volume Feature Report - 2026-09-01

Generated at: 2026-09-01 02:01:54

Source ML dataset: `data/processed/ml_dataset_20260901.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **90229**
- Rows with price file found: **90229**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **90229**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260831 | 153460 | 네이블 | supply_contract | positive | N/A | 2,508 | N/A | N/A | 3,991 | N/A |
| 20260831 | 121440 | 골프존홀딩스 | disclosure_violation | negative | N/A | 345,512 | N/A | N/A | 104,215 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 226330 | 신테카바이오 | paid_in_capital_increase | negative | N/A | 178,081 | N/A | N/A | 219,059 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |
| 20260831 | 340360 | 다보링크 | paid_in_capital_increase | negative | N/A | 435,158 | N/A | N/A | 199,109 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
