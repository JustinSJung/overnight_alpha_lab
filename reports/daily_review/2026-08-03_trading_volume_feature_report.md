# Trading Volume Feature Report - 2026-08-03

Generated at: 2026-08-03 23:23:53

Source ML dataset: `data/processed/ml_dataset_20260803.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **37**
- Rows with price file found: **37**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **37**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260803 | 031860 | 디에이치엑스컴퍼니 | investment_decision | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260803 | 031860 | 디에이치엑스컴퍼니 | investment_decision | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260803 | 031860 | 디에이치엑스컴퍼니 | investment_decision | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260803 | 031860 | 디에이치엑스컴퍼니 | investment_decision | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260803 | 347700 | 스피어 | supply_contract | positive | N/A | 1,175,514 | N/A | N/A | 2,085,805 | N/A |
| 20260803 | 001260 | 남광토건 | investment_decision | volatile | N/A | 2,675,021 | N/A | N/A | 1,880,510 | N/A |
| 20260803 | 255220 | SG | supply_contract | positive | N/A | 755,251 | N/A | N/A | 1,988,591 | N/A |
| 20260803 | 148250 | 알엔투테크놀로지 | lawsuit | negative | N/A | 65,695 | N/A | N/A | 87,992 | N/A |
| 20260803 | 148250 | 알엔투테크놀로지 | lawsuit | negative | N/A | 65,695 | N/A | N/A | 87,992 | N/A |
| 20260803 | 148250 | 알엔투테크놀로지 | lawsuit | negative | N/A | 65,695 | N/A | N/A | 87,992 | N/A |
| 20260803 | 148250 | 알엔투테크놀로지 | lawsuit | negative | N/A | 65,695 | N/A | N/A | 87,992 | N/A |
| 20260803 | 178320 | 서진시스템 | major_shareholder_change | volatile | N/A | 1,392,575 | N/A | N/A | 842,662 | N/A |
| 20260803 | 020150 | 롯데에너지머티리얼즈 | major_shareholder_change | volatile | N/A | 219,658 | N/A | N/A | 211,773 | N/A |
| 20260803 | 028100 | 동아지질 | supply_contract | positive | N/A | 32,451 | N/A | N/A | 24,027 | N/A |
| 20260803 | 033310 | 엠투엔 | major_shareholder_change | volatile | N/A | 25,027 | N/A | N/A | 44,041 | N/A |
| 20260803 | 027580 | 상보 | major_shareholder_change | volatile | N/A | 27,254 | N/A | N/A | 31,990 | N/A |
| 20260803 | 047920 | HLB제약 | paid_in_capital_increase | negative | N/A | 43,077 | N/A | N/A | 60,891 | N/A |
| 20260803 | 223220 | 로지스몬 | lawsuit | negative | N/A | 126 | N/A | N/A | 2,841 | N/A |
| 20260803 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 451,113 | N/A | N/A | 240,556 | N/A |
| 20260803 | 473980 | 노머스 | convertible_bond | negative | N/A | 72,455 | N/A | N/A | 22,173 | N/A |
| 20260803 | 473980 | 노머스 | convertible_bond | negative | N/A | 72,455 | N/A | N/A | 22,173 | N/A |
| 20260803 | 473980 | 노머스 | convertible_bond | negative | N/A | 72,455 | N/A | N/A | 22,173 | N/A |
| 20260803 | 473980 | 노머스 | convertible_bond | negative | N/A | 72,455 | N/A | N/A | 22,173 | N/A |
| 20260803 | 012630 | HDC | investment_decision | volatile | N/A | 26,213 | N/A | N/A | 45,350 | N/A |
| 20260803 | 294870 | IPARK현대산업개발 | investment_decision | volatile | N/A | 230,712 | N/A | N/A | 264,093 | N/A |
| 20260803 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | N/A | 234,625 | N/A | N/A | 265,640 | N/A |
| 20260803 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | N/A | 234,625 | N/A | N/A | 265,640 | N/A |
| 20260803 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | N/A | 234,625 | N/A | N/A | 265,640 | N/A |
| 20260803 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | N/A | 234,625 | N/A | N/A | 265,640 | N/A |
| 20260803 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | N/A | 234,625 | N/A | N/A | 265,640 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
