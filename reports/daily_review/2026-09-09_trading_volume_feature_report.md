# Trading Volume Feature Report - 2026-09-09

Generated at: 2026-09-09 00:53:45

Source ML dataset: `data/processed/ml_dataset_20260909.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **71059**
- Rows with price file found: **71059**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **71059**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260908 | 203400 | 에이비온 | spin_off | volatile | N/A | 1,158,766 | N/A | N/A | 8,846,447 | N/A |
| 20260908 | 005930 | 삼성전자 | major_shareholder_change | volatile | N/A | 16,327,805 | N/A | N/A | 23,310,969 | N/A |
| 20260908 | 199730 | 바이오인프라 | merger | volatile | N/A | 72,342 | N/A | N/A | 43,220 | N/A |
| 20260908 | 199730 | 바이오인프라 | merger | volatile | N/A | 72,342 | N/A | N/A | 43,220 | N/A |
| 20260908 | 199730 | 바이오인프라 | merger | volatile | N/A | 72,342 | N/A | N/A | 43,220 | N/A |
| 20260908 | 199730 | 바이오인프라 | merger | volatile | N/A | 72,342 | N/A | N/A | 43,220 | N/A |
| 20260908 | 020120 | 키다리스튜디오 | major_shareholder_change | volatile | N/A | 127,769 | N/A | N/A | 438,738 | N/A |
| 20260908 | 009320 | 아진전자부품 | major_shareholder_change | volatile | N/A | 226,192 | N/A | N/A | 147,289 | N/A |
| 20260908 | 009320 | 아진전자부품 | major_shareholder_change | volatile | N/A | 226,192 | N/A | N/A | 147,289 | N/A |
| 20260908 | 009320 | 아진전자부품 | major_shareholder_change | volatile | N/A | 226,192 | N/A | N/A | 147,289 | N/A |
| 20260908 | 009320 | 아진전자부품 | major_shareholder_change | volatile | N/A | 226,192 | N/A | N/A | 147,289 | N/A |
| 20260908 | 010960 | 삼호개발 | supply_contract | positive | N/A | 136,583 | N/A | N/A | 745,135 | N/A |
| 20260908 | 027410 | BGF | merger | volatile | N/A | 154,221 | N/A | N/A | 70,713 | N/A |
| 20260908 | 027040 | 서울전자통신 | paid_in_capital_increase | negative | N/A | 448,563 | N/A | N/A | 203,311 | N/A |
| 20260908 | 027040 | 서울전자통신 | paid_in_capital_increase | negative | N/A | 448,563 | N/A | N/A | 203,311 | N/A |
| 20260908 | 027040 | 서울전자통신 | paid_in_capital_increase | negative | N/A | 448,563 | N/A | N/A | 203,311 | N/A |
| 20260908 | 027040 | 서울전자통신 | paid_in_capital_increase | negative | N/A | 448,563 | N/A | N/A | 203,311 | N/A |
| 20260908 | 288980 | 모아데이타 | convertible_bond | negative | N/A | 237,756 | N/A | N/A | 471,563 | N/A |
| 20260908 | 126600 | BGF에코머티리얼즈 | merger | volatile | N/A | 49,366 | N/A | N/A | 40,529 | N/A |
| 20260908 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | N/A | 64,497 | N/A | N/A | 58,268 | N/A |
| 20260908 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | N/A | 64,497 | N/A | N/A | 58,268 | N/A |
| 20260908 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | N/A | 64,497 | N/A | N/A | 58,268 | N/A |
| 20260908 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | N/A | 64,497 | N/A | N/A | 58,268 | N/A |
| 20260908 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | N/A | 64,497 | N/A | N/A | 58,268 | N/A |
| 20260908 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | N/A | 64,497 | N/A | N/A | 58,268 | N/A |
| 20260908 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | N/A | 64,497 | N/A | N/A | 58,268 | N/A |
| 20260908 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | N/A | 64,497 | N/A | N/A | 58,268 | N/A |
| 20260908 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | N/A | 64,497 | N/A | N/A | 58,268 | N/A |
| 20260908 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | N/A | 64,497 | N/A | N/A | 58,268 | N/A |
| 20260908 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | N/A | 64,497 | N/A | N/A | 58,268 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
