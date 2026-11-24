# Trading Volume Feature Report - 2026-11-24

Generated at: 2026-11-24 06:54:24

Source ML dataset: `data/processed/ml_dataset_20261124.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **116931**
- Rows with price file found: **116931**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **116931**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261123 | 009830 | 한화솔루션 | merger | volatile | N/A | 2,545,856 | N/A | N/A | 2,558,167 | N/A |
| 20261123 | 009830 | 한화솔루션 | merger | volatile | N/A | 2,545,856 | N/A | N/A | 2,558,167 | N/A |
| 20261123 | 009830 | 한화솔루션 | merger | volatile | N/A | 2,545,856 | N/A | N/A | 2,558,167 | N/A |
| 20261123 | 009830 | 한화솔루션 | merger | volatile | N/A | 2,545,856 | N/A | N/A | 2,558,167 | N/A |
| 20261123 | 290560 | 파라택시스이더리움 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261123 | 276040 | 스코넥 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261123 | 320000 | 한울반도체 | major_shareholder_change | volatile | N/A | 34,221 | N/A | N/A | 29,921 | N/A |
| 20261123 | 0153R0 | 바로팜 | investment_decision | volatile | N/A | 18,507,340 | N/A | N/A | 2,771,561 | N/A |
| 20261123 | 006370 | 대구백화점 | lawsuit | negative | N/A | 29,575 | N/A | N/A | 33,547 | N/A |
| 20261123 | 262260 | 에이프로 | merger | volatile | N/A | 32,431 | N/A | N/A | 17,591 | N/A |
| 20261123 | 262260 | 에이프로 | merger | volatile | N/A | 32,431 | N/A | N/A | 17,591 | N/A |
| 20261123 | 262260 | 에이프로 | merger | volatile | N/A | 32,431 | N/A | N/A | 17,591 | N/A |
| 20261123 | 262260 | 에이프로 | merger | volatile | N/A | 32,431 | N/A | N/A | 17,591 | N/A |
| 20261123 | 033270 | 유나이티드 | investment_decision | volatile | N/A | 31,502 | N/A | N/A | 136,162 | N/A |
| 20261123 | 033270 | 유나이티드 | investment_decision | volatile | N/A | 31,502 | N/A | N/A | 136,162 | N/A |
| 20261123 | 033270 | 유나이티드 | investment_decision | volatile | N/A | 31,502 | N/A | N/A | 136,162 | N/A |
| 20261123 | 033270 | 유나이티드 | investment_decision | volatile | N/A | 31,502 | N/A | N/A | 136,162 | N/A |
| 20261123 | 0220W0 | 한화머시너리앤서비스홀딩스 | lawsuit | negative | N/A | 888,696 | N/A | N/A | 547,162 | N/A |
| 20261123 | 053210 | 케이티스카이라이프 | merger | volatile | N/A | 21,863 | N/A | N/A | 35,396 | N/A |
| 20261123 | 358570 | 지아이이노베이션 | investment_decision | volatile | N/A | 178,056 | N/A | N/A | 340,962 | N/A |
| 20261123 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 478,452 | N/A | N/A | 317,550 | N/A |
| 20261123 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 478,452 | N/A | N/A | 317,550 | N/A |
| 20261123 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 478,452 | N/A | N/A | 317,550 | N/A |
| 20261123 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 478,452 | N/A | N/A | 317,550 | N/A |
| 20261123 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 478,452 | N/A | N/A | 317,550 | N/A |
| 20261123 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 478,452 | N/A | N/A | 317,550 | N/A |
| 20261123 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 478,452 | N/A | N/A | 317,550 | N/A |
| 20261123 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 478,452 | N/A | N/A | 317,550 | N/A |
| 20261123 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 478,452 | N/A | N/A | 317,550 | N/A |
| 20261123 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | N/A | 478,452 | N/A | N/A | 317,550 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
