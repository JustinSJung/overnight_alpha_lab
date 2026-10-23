# Trading Volume Feature Report - 2026-10-23

Generated at: 2026-10-23 01:25:38

Source ML dataset: `data/processed/ml_dataset_20261023.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **265**
- Rows with price file found: **264**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **264**
- price_file_missing: **1**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261022 | 006370 | 대구백화점 | investment_decision | volatile | N/A | 88,756 | N/A | N/A | 44,287 | N/A |
| 20261022 | 011560 | 세보엠이씨 | supply_contract | positive | N/A | 43,847 | N/A | N/A | 38,561 | N/A |
| 20261022 | 396470 | 워트 | supply_contract | positive | N/A | 40,213 | N/A | N/A | 77,049 | N/A |
| 20261022 | 000490 | 대동 | convertible_bond | negative | N/A | 110,307 | N/A | N/A | 73,674 | N/A |
| 20261022 | 002990 | 금호건설 | convertible_bond | negative | N/A | 839,324 | N/A | N/A | 1,140,219 | N/A |
| 20261022 | 030610 | 교보증권 | paid_in_capital_increase | negative | N/A | 20,154 | N/A | N/A | 13,289 | N/A |
| 20261022 | 030610 | 교보증권 | paid_in_capital_increase | negative | N/A | 20,154 | N/A | N/A | 13,289 | N/A |
| 20261022 | 030610 | 교보증권 | paid_in_capital_increase | negative | N/A | 20,154 | N/A | N/A | 13,289 | N/A |
| 20261022 | 030610 | 교보증권 | paid_in_capital_increase | negative | N/A | 20,154 | N/A | N/A | 13,289 | N/A |
| 20261022 | 317770 | 엑스페릭스 | paid_in_capital_increase | negative | N/A | 121,207 | N/A | N/A | 120,609 | N/A |
| 20261022 | 066790 | 씨씨에스 | lawsuit | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261022 | 288980 | 모아데이타 | paid_in_capital_increase | negative | N/A | 1,070,945 | N/A | N/A | 1,688,484 | N/A |
| 20261022 | 078130 | 에스엠국일 | investment_decision | volatile | N/A | 95,653 | N/A | N/A | 77,418 | N/A |
| 20261022 | 078130 | 에스엠국일 | investment_decision | volatile | N/A | 95,653 | N/A | N/A | 77,418 | N/A |
| 20261022 | 294090 | 이오플로우 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261022 | 051980 | 중앙첨단소재 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261022 | 115160 | 휴맥스 | merger | volatile | N/A | 5,295 | N/A | N/A | 3,114 | N/A |
| 20261022 | 115160 | 휴맥스 | merger | volatile | N/A | 5,295 | N/A | N/A | 3,114 | N/A |
| 20261022 | 115160 | 휴맥스 | convertible_bond | negative | N/A | 5,295 | N/A | N/A | 3,114 | N/A |
| 20261022 | 115160 | 휴맥스 | convertible_bond | negative | N/A | 5,295 | N/A | N/A | 3,114 | N/A |
| 20261022 | 083660 | CSA 코스믹 | paid_in_capital_increase | negative | N/A | 19,415 | N/A | N/A | 77,666 | N/A |
| 20261022 | 0117P0 | 피스피스스튜디오 | merger | volatile | N/A | 54,946 | N/A | N/A | 66,962 | N/A |
| 20261022 | 033530 | SJG세종 | paid_in_capital_increase | negative | N/A | 52,729 | N/A | N/A | 22,306 | N/A |
| 20261022 | 004990 | 롯데지주 | investment_decision | volatile | N/A | 81,386 | N/A | N/A | 83,864 | N/A |
| 20261022 | 332190 | 오션스바이오 | paid_in_capital_increase | negative | N/A | 3 | N/A | N/A | 5 | N/A |
| 20261022 | 109070 | 주성코퍼레이션 | merger | volatile | N/A | 0 | N/A | N/A | 70,909 | N/A |
| 20261022 | 109070 | 주성코퍼레이션 | merger | volatile | N/A | 0 | N/A | N/A | 70,909 | N/A |
| 20261022 | 109070 | 주성코퍼레이션 | merger | volatile | N/A | 0 | N/A | N/A | 70,909 | N/A |
| 20261022 | 109070 | 주성코퍼레이션 | merger | volatile | N/A | 0 | N/A | N/A | 70,909 | N/A |
| 20261022 | 122640 | 예스티 | supply_contract | positive | N/A | 280,589 | N/A | N/A | 218,808 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
