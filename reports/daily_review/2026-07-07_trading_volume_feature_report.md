# Trading Volume Feature Report - 2026-07-07

Generated at: 2026-07-07 06:47:39

Source ML dataset: `data/processed/ml_dataset_20260707.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **150**
- Rows with price file found: **150**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **150**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260707 | 288980 | 모아데이타 | convertible_bond | negative | N/A | 565,046 | N/A | N/A | 261,325 | N/A |
| 20260707 | 019570 | 플루토스 | convertible_bond | negative | N/A | 674,738 | N/A | N/A | 315,958 | N/A |
| 20260707 | 013520 | 화승코퍼레이션 | major_shareholder_change | volatile | N/A | 112,650 | N/A | N/A | 134,864 | N/A |
| 20260707 | 013720 | 청보 | spin_off | volatile | N/A | 3,016,634 | N/A | N/A | 367,178 | N/A |
| 20260707 | 253450 | 스튜디오드래곤 | merger | volatile | N/A | 92,983 | N/A | N/A | 105,841 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 010140 | 삼성중공업 | major_shareholder_change | volatile | N/A | 4,092,220 | N/A | N/A | 5,590,102 | N/A |
| 20260707 | 101970 | 우양에이치씨 | supply_contract | positive | N/A | 24,501 | N/A | N/A | 11,758 | N/A |
| 20260707 | 068240 | 다원시스 | supply_contract | positive | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260707 | 000720 | 현대건설 | paid_in_capital_increase | negative | N/A | 834,619 | N/A | N/A | 633,184 | N/A |
| 20260707 | 047040 | 대우건설 | supply_contract | positive | N/A | 6,750,004 | N/A | N/A | 7,740,230 | N/A |
| 20260707 | 368970 | 오에스피 | paid_in_capital_increase | negative | N/A | 31,343 | N/A | N/A | 54,477 | N/A |
| 20260707 | 003070 | 코오롱글로벌 | major_shareholder_change | volatile | N/A | 24,866 | N/A | N/A | 16,837 | N/A |
| 20260707 | 187870 | 디바이스 | supply_contract | positive | N/A | 241,741 | N/A | N/A | 263,723 | N/A |
| 20260707 | 007980 | TP | major_shareholder_change | volatile | N/A | 297,591 | N/A | N/A | 238,402 | N/A |
| 20260707 | 007980 | TP | major_shareholder_change | volatile | N/A | 297,591 | N/A | N/A | 238,402 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
