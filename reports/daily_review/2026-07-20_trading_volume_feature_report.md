# Trading Volume Feature Report - 2026-07-20

Generated at: 2026-07-20 08:43:31

Source ML dataset: `data/processed/ml_dataset_20260720.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **16414**
- Rows with price file found: **16414**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **16414**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260720 | 033310 | 엠투엔 | major_shareholder_change | volatile | N/A | 142,525 | N/A | N/A | 180,169 | N/A |
| 20260720 | 290720 | 푸드나무 | paid_in_capital_increase | negative | N/A | 480,361 | N/A | N/A | 97,501 | N/A |
| 20260720 | 389680 | 유디엠텍 | supply_contract | positive | N/A | 84,490 | N/A | N/A | 93,323 | N/A |
| 20260720 | 144510 | 지씨셀 | investment_decision | volatile | N/A | 42,753 | N/A | N/A | 65,761 | N/A |
| 20260720 | 078350 | 한양디지텍 | major_shareholder_change | volatile | N/A | 180,062 | N/A | N/A | 424,926 | N/A |
| 20260720 | 224060 | 더코디 | convertible_bond | negative | N/A | 56,315 | N/A | N/A | 21,296 | N/A |
| 20260720 | 055550 | 신한지주 | major_shareholder_change | volatile | N/A | 1,096,436 | N/A | N/A | 1,558,595 | N/A |
| 20260720 | 082270 | 젬백스 | major_shareholder_change | volatile | N/A | 291,427 | N/A | N/A | 239,142 | N/A |
| 20260720 | 033540 | 파라텍 | convertible_bond | negative | N/A | 418,589 | N/A | N/A | 347,603 | N/A |
| 20260720 | 112610 | 씨에스윈드 | major_shareholder_change | volatile | N/A | 570,600 | N/A | N/A | 637,278 | N/A |
| 20260720 | 112610 | 씨에스윈드 | major_shareholder_change | volatile | N/A | 570,600 | N/A | N/A | 637,278 | N/A |
| 20260720 | 112610 | 씨에스윈드 | major_shareholder_change | volatile | N/A | 570,600 | N/A | N/A | 637,278 | N/A |
| 20260720 | 112610 | 씨에스윈드 | major_shareholder_change | volatile | N/A | 570,600 | N/A | N/A | 637,278 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |
| 20260720 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 51,729 | N/A | N/A | 0 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
