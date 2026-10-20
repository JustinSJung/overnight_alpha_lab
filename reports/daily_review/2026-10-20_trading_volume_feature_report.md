# Trading Volume Feature Report - 2026-10-20

Generated at: 2026-10-20 01:45:23

Source ML dataset: `data/processed/ml_dataset_20261020.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **200**
- Rows with price file found: **199**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **199**
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
| 20261019 | 059270 | 해성에어로보틱스 | lawsuit | negative | N/A | 66,395 | N/A | N/A | 36,182 | N/A |
| 20261019 | 302550 | 리메드 | convertible_bond | negative | N/A | 18,837 | N/A | N/A | 25,312 | N/A |
| 20261019 | 207490 | 에이펙스인텍 | disclosure_violation | negative | N/A | 10 | N/A | N/A | 0 | N/A |
| 20261019 | 032820 | 우리기술 | supply_contract | positive | N/A | 5,978,685 | N/A | N/A | 5,641,883 | N/A |
| 20261019 | 377450 | 리파인 | disclosure_violation | negative | N/A | 22,327 | N/A | N/A | 15,190 | N/A |
| 20261019 | 018500 | 동원모빌리티 | lawsuit | negative | N/A | 57,652 | N/A | N/A | 53,840 | N/A |
| 20261019 | 465770 | STX그린로지스 | convertible_bond | negative | N/A | 239,646 | N/A | N/A | 281,715 | N/A |
| 20261019 | 010960 | 삼호개발 | supply_contract | positive | N/A | 63,060 | N/A | N/A | 136,086 | N/A |
| 20261019 | 000210 | DL | investment_decision | volatile | N/A | 51,723 | N/A | N/A | 30,194 | N/A |
| 20261019 | 011300 | 우성머티리얼스 | convertible_bond | negative | N/A | 113,146 | N/A | N/A | 879,371 | N/A |
| 20261019 | 375500 | DL이앤씨 | investment_decision | volatile | N/A | 254,621 | N/A | N/A | 284,798 | N/A |
| 20261019 | 033310 | 엠투엔 | major_shareholder_change | volatile | N/A | 31,838 | N/A | N/A | 46,834 | N/A |
| 20261019 | 288980 | 모아데이타 | paid_in_capital_increase | negative | N/A | 1,346,128 | N/A | N/A | 796,141 | N/A |
| 20261019 | 363280 | 티와이홀딩스 | investment_decision | volatile | N/A | 15,902 | N/A | N/A | 18,101 | N/A |
| 20261019 | 069460 | 대호에이엘 | lawsuit | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261019 | 196170 | 알테오젠 | merger | volatile | N/A | 193,075 | N/A | N/A | 276,847 | N/A |
| 20261019 | 009410 | 태영건설 | investment_decision | volatile | N/A | 224,995 | N/A | N/A | 134,727 | N/A |
| 20261019 | 006980 | 우성 | merger | volatile | N/A | 1,298 | N/A | N/A | 2,605 | N/A |
| 20261019 | 009150 | 삼성전기 | supply_contract | positive | N/A | 589,885 | N/A | N/A | 908,255 | N/A |
| 20261019 | 078020 | LS증권 | lawsuit | negative | N/A | 45,499 | N/A | N/A | 59,677 | N/A |
| 20261019 | 900100 | 파이온엑스 | paid_in_capital_increase | negative | N/A | 183,584 | N/A | N/A | 241,101 | N/A |
| 20261019 | 060900 | 에이전트AI | convertible_bond | negative | N/A | 6,961 | N/A | N/A | 10,325 | N/A |
| 20261019 | 025950 | 동신건설 | supply_contract | positive | N/A | 15,192 | N/A | N/A | 10,443 | N/A |
| 20261019 | 000300 | DH오토넥스 | merger | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261019 | 214330 | 금호에이치티 | major_shareholder_change | volatile | N/A | 45,431 | N/A | N/A | 49,443 | N/A |
| 20261019 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | N/A | 142,167 | N/A | N/A | 114,728 | N/A |
| 20261019 | 028100 | 동아지질 | supply_contract | positive | N/A | 74,637 | N/A | N/A | 45,608 | N/A |
| 20261019 | 290120 | DH오토리드 | merger | volatile | N/A | 4,103 | N/A | N/A | 7,305 | N/A |
| 20261019 | 407400 | 꿈비 | convertible_bond | negative | N/A | 38,396 | N/A | N/A | 40,540 | N/A |
| 20261019 | 082270 | 젬백스 | major_shareholder_change | volatile | N/A | 132,494 | N/A | N/A | 88,292 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
