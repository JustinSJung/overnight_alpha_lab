# Trading Volume Feature Report - 2026-06-26

Generated at: 2026-06-26 16:39:46

Source ML dataset: `data/processed/ml_dataset_20260626.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **31**
- Rows with price file found: **30**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **30**
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
| 20260626 | 361610 | SK아이이테크놀로지 | paid_in_capital_increase | negative | N/A | 294,939 | N/A | N/A | 340,406 | N/A |
| 20260626 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | N/A | 3,045,375 | N/A | N/A | 1,187,751 | N/A |
| 20260626 | 476830 | 알지노믹스 | bonus_issue | positive | N/A | 429,701 | N/A | N/A | 233,729 | N/A |
| 20260626 | 005960 | 동부건설 | supply_contract | positive | N/A | 129,046 | N/A | N/A | 123,309 | N/A |
| 20260626 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260626 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260626 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260626 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260626 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260626 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260626 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260626 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260626 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260626 | 138360 | 앤로보틱스 | paid_in_capital_increase | negative | N/A | 1,453,137 | N/A | N/A | 1,182,134 | N/A |
| 20260626 | 214150 | 클래시스 | major_shareholder_change | volatile | N/A | 215,047 | N/A | N/A | 404,393 | N/A |
| 20260626 | 214150 | 클래시스 | major_shareholder_change | volatile | N/A | 215,047 | N/A | N/A | 404,393 | N/A |
| 20260626 | 214150 | 클래시스 | major_shareholder_change | volatile | N/A | 215,047 | N/A | N/A | 404,393 | N/A |
| 20260626 | 214150 | 클래시스 | major_shareholder_change | volatile | N/A | 215,047 | N/A | N/A | 404,393 | N/A |
| 20260626 | 214150 | 클래시스 | major_shareholder_change | volatile | N/A | 215,047 | N/A | N/A | 404,393 | N/A |
| 20260626 | 214150 | 클래시스 | major_shareholder_change | volatile | N/A | 215,047 | N/A | N/A | 404,393 | N/A |
| 20260626 | 214150 | 클래시스 | major_shareholder_change | volatile | N/A | 215,047 | N/A | N/A | 404,393 | N/A |
| 20260626 | 214150 | 클래시스 | major_shareholder_change | volatile | N/A | 215,047 | N/A | N/A | 404,393 | N/A |
| 20260626 | 214150 | 클래시스 | major_shareholder_change | volatile | N/A | 215,047 | N/A | N/A | 404,393 | N/A |
| 20260626 | 258610 | 케일럼 | supply_contract | positive | N/A | 40,608 | N/A | N/A | 54,012 | N/A |
| 20260626 | 277880 | 티에스아이 | supply_contract | positive | N/A | 149,633 | N/A | N/A | 110,499 | N/A |
| 20260626 | 003450 | 케이비증권 | paid_in_capital_increase | negative | N/A | N/A | N/A | N/A | N/A | N/A |
| 20260626 | 003470 | 유안타증권 | major_shareholder_change | volatile | N/A | 1,267,942 | N/A | N/A | 1,658,188 | N/A |
| 20260626 | 186230 | 그린플러스 | supply_contract | positive | N/A | 31,911 | N/A | N/A | 65,996 | N/A |
| 20260626 | 282720 | 금양그린파워 | supply_contract | positive | N/A | 165,865 | N/A | N/A | 119,315 | N/A |
| 20260626 | 105560 | KB금융 | paid_in_capital_increase | negative | N/A | 1,180,209 | N/A | N/A | 1,497,632 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
