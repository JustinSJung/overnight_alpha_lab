# Trading Volume Feature Report - 2026-07-21

Generated at: 2026-07-21 23:15:37

Source ML dataset: `data/processed/ml_dataset_20260721.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **88**
- Rows with price file found: **88**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **88**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260721 | 066790 | 씨씨에스 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260721 | 348950 | 제이알글로벌리츠 | investment_decision | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260721 | 397030 | 에이프릴바이오 | investment_decision | volatile | N/A | 358,046 | N/A | N/A | 472,067 | N/A |
| 20260721 | 006220 | 제주은행 | disclosure_violation | negative | N/A | 645,374 | N/A | N/A | 4,531,342 | N/A |
| 20260721 | 066430 | 아이로보틱스 | lawsuit | negative | N/A | 1,661,636 | N/A | N/A | 1,045,186 | N/A |
| 20260721 | 106240 | 파인테크닉스 | convertible_bond | negative | N/A | 67,748 | N/A | N/A | 117,455 | N/A |
| 20260721 | 276730 | 한울앤제주 | convertible_bond | negative | N/A | 107,225 | N/A | N/A | 35,043 | N/A |
| 20260721 | 276730 | 한울앤제주 | convertible_bond | negative | N/A | 107,225 | N/A | N/A | 35,043 | N/A |
| 20260721 | 276730 | 한울앤제주 | convertible_bond | negative | N/A | 107,225 | N/A | N/A | 35,043 | N/A |
| 20260721 | 276730 | 한울앤제주 | convertible_bond | negative | N/A | 107,225 | N/A | N/A | 35,043 | N/A |
| 20260721 | 053580 | 웹케시 | supply_contract | positive | N/A | 39,715 | N/A | N/A | 77,651 | N/A |
| 20260721 | 071950 | 코아스 | paid_in_capital_increase | negative | N/A | 105,341 | N/A | N/A | 63,347 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |
| 20260721 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 139,176 | N/A | N/A | 73,236 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
