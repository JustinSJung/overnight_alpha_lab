# Trading Volume Feature Report - 2026-08-18

Generated at: 2026-08-18 22:47:58

Source ML dataset: `data/processed/ml_dataset_20260818.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **68**
- Rows with price file found: **68**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **68**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260818 | 033540 | 파라텍 | convertible_bond | negative | N/A | 41,611 | N/A | N/A | 25,696 | N/A |
| 20260818 | 0009K0 | 에임드바이오 | investment_decision | volatile | N/A | 130,955 | N/A | N/A | 159,171 | N/A |
| 20260818 | 418620 | E8 | paid_in_capital_increase | negative | N/A | 178,865 | N/A | N/A | 45,835 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 44,082 | N/A | N/A | 27,708 | N/A |
| 20260818 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 1,139,287 | N/A | N/A | 556,957 | N/A |
| 20260818 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 1,139,287 | N/A | N/A | 556,957 | N/A |
| 20260818 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 1,139,287 | N/A | N/A | 556,957 | N/A |
| 20260818 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 1,139,287 | N/A | N/A | 556,957 | N/A |
| 20260818 | 010960 | 삼호개발 | supply_contract | positive | N/A | 515,733 | N/A | N/A | 353,401 | N/A |
| 20260818 | 062970 | 한국첨단소재 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260818 | 062970 | 한국첨단소재 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260818 | 062970 | 한국첨단소재 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260818 | 062970 | 한국첨단소재 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260818 | 033310 | 엠투엔 | major_shareholder_change | volatile | N/A | 29,763 | N/A | N/A | 29,097 | N/A |
| 20260818 | 001740 | SK네트웍스 | major_shareholder_change | volatile | N/A | 1,437,093 | N/A | N/A | 1,122,283 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
