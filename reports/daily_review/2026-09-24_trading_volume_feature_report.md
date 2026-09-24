# Trading Volume Feature Report - 2026-09-24

Generated at: 2026-09-24 00:59:02

Source ML dataset: `data/processed/ml_dataset_20260924.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **262**
- Rows with price file found: **262**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **262**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260923 | 431190 | 케이쓰리아이 | paid_in_capital_increase | negative | N/A | 9,621 | N/A | N/A | 7,426 | N/A |
| 20260923 | 431190 | 케이쓰리아이 | paid_in_capital_increase | negative | N/A | 9,621 | N/A | N/A | 7,426 | N/A |
| 20260923 | 431190 | 케이쓰리아이 | paid_in_capital_increase | negative | N/A | 9,621 | N/A | N/A | 7,426 | N/A |
| 20260923 | 431190 | 케이쓰리아이 | convertible_bond | negative | N/A | 9,621 | N/A | N/A | 7,426 | N/A |
| 20260923 | 431190 | 케이쓰리아이 | convertible_bond | negative | N/A | 9,621 | N/A | N/A | 7,426 | N/A |
| 20260923 | 431190 | 케이쓰리아이 | convertible_bond | negative | N/A | 9,621 | N/A | N/A | 7,426 | N/A |
| 20260923 | 084110 | 휴온스글로벌 | disclosure_violation | negative | N/A | 25,368 | N/A | N/A | 30,580 | N/A |
| 20260923 | 243070 | 휴온스 | disclosure_violation | negative | N/A | 47,410 | N/A | N/A | 11,526 | N/A |
| 20260923 | 083650 | 비에이치아이 | supply_contract | positive | N/A | 752,632 | N/A | N/A | 595,544 | N/A |
| 20260923 | 230360 | 에코마케팅 | spin_off | volatile | N/A | 29,368 | N/A | N/A | 26,121 | N/A |
| 20260923 | 079940 | 가비아 | lawsuit | negative | N/A | 22,632 | N/A | N/A | 12,540 | N/A |
| 20260923 | 079940 | 가비아 | lawsuit | negative | N/A | 22,632 | N/A | N/A | 12,540 | N/A |
| 20260923 | 109670 | 씨싸이트 | major_shareholder_change | volatile | N/A | 4,586 | N/A | N/A | 18,330 | N/A |
| 20260923 | 079940 | 가비아 | major_shareholder_change | volatile | N/A | 22,632 | N/A | N/A | 12,540 | N/A |
| 20260923 | 079940 | 가비아 | major_shareholder_change | volatile | N/A | 22,632 | N/A | N/A | 12,540 | N/A |
| 20260923 | 001360 | 삼성제약 | investment_decision | volatile | N/A | 184,306 | N/A | N/A | 256,858 | N/A |
| 20260923 | 005250 | 녹십자홀딩스 | major_shareholder_change | volatile | N/A | 117,199 | N/A | N/A | 63,832 | N/A |
| 20260923 | 288980 | 모아데이타 | convertible_bond | negative | N/A | 16,998,463 | N/A | N/A | 14,449,978 | N/A |
| 20260923 | 377460 | 큐에이드 | lawsuit | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260923 | 004440 | 삼일씨엔에스 | supply_contract | positive | N/A | 30,334 | N/A | N/A | 16,496 | N/A |
| 20260923 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | N/A | 714,540 | N/A | N/A | 687,820 | N/A |
| 20260923 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | N/A | 714,540 | N/A | N/A | 687,820 | N/A |
| 20260923 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | N/A | 714,540 | N/A | N/A | 687,820 | N/A |
| 20260923 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | N/A | 714,540 | N/A | N/A | 687,820 | N/A |
| 20260923 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | N/A | 714,540 | N/A | N/A | 687,820 | N/A |
| 20260923 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | N/A | 714,540 | N/A | N/A | 687,820 | N/A |
| 20260923 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | N/A | 714,540 | N/A | N/A | 687,820 | N/A |
| 20260923 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | N/A | 714,540 | N/A | N/A | 687,820 | N/A |
| 20260923 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | N/A | 714,540 | N/A | N/A | 687,820 | N/A |
| 20260923 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | N/A | 714,540 | N/A | N/A | 687,820 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
