# Trading Volume Feature Report - 2026-08-11

Generated at: 2026-08-11 23:08:32

Source ML dataset: `data/processed/ml_dataset_20260811.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **283**
- Rows with price file found: **283**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **283**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260811 | 006060 | 화승인더스트리 | investment_decision | volatile | N/A | 62,777 | N/A | N/A | 67,966 | N/A |
| 20260811 | 348370 | 엔켐 | major_shareholder_change | volatile | N/A | 147,152 | N/A | N/A | 191,137 | N/A |
| 20260811 | 006370 | 대구백화점 | investment_decision | volatile | N/A | 1,060,895 | N/A | N/A | 283,852 | N/A |
| 20260811 | 006370 | 대구백화점 | investment_decision | volatile | N/A | 1,060,895 | N/A | N/A | 283,852 | N/A |
| 20260811 | 006370 | 대구백화점 | investment_decision | volatile | N/A | 1,060,895 | N/A | N/A | 283,852 | N/A |
| 20260811 | 006370 | 대구백화점 | investment_decision | volatile | N/A | 1,060,895 | N/A | N/A | 283,852 | N/A |
| 20260811 | 263750 | 펄어비스 | earnings_guidance | neutral_positive | N/A | 234,533 | N/A | N/A | 265,038 | N/A |
| 20260811 | 263750 | 펄어비스 | earnings_guidance | neutral_positive | N/A | 234,533 | N/A | N/A | 265,038 | N/A |
| 20260811 | 263750 | 펄어비스 | earnings_guidance | neutral_positive | N/A | 234,533 | N/A | N/A | 265,038 | N/A |
| 20260811 | 263750 | 펄어비스 | earnings_guidance | neutral_positive | N/A | 234,533 | N/A | N/A | 265,038 | N/A |
| 20260811 | 068240 | 다원시스 | supply_contract | positive | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260811 | 065420 | 에스아이리소스 | lawsuit | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260811 | 378800 | 샤페론 | convertible_bond | negative | N/A | 825,717 | N/A | N/A | 709,898 | N/A |
| 20260811 | 089860 | 롯데렌탈 | investment_decision | volatile | N/A | 109,455 | N/A | N/A | 95,006 | N/A |
| 20260811 | 089860 | 롯데렌탈 | investment_decision | volatile | N/A | 109,455 | N/A | N/A | 95,006 | N/A |
| 20260811 | 089860 | 롯데렌탈 | investment_decision | volatile | N/A | 109,455 | N/A | N/A | 95,006 | N/A |
| 20260811 | 089860 | 롯데렌탈 | investment_decision | volatile | N/A | 109,455 | N/A | N/A | 95,006 | N/A |
| 20260811 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | N/A | 2,415,144 | N/A | N/A | 1,547,137 | N/A |
| 20260811 | 033270 | 유나이티드 | major_shareholder_change | volatile | N/A | 32,172 | N/A | N/A | 55,365 | N/A |
| 20260811 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 192,074 | N/A | N/A | 290,597 | N/A |
| 20260811 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 192,074 | N/A | N/A | 290,597 | N/A |
| 20260811 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 192,074 | N/A | N/A | 290,597 | N/A |
| 20260811 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 192,074 | N/A | N/A | 290,597 | N/A |
| 20260811 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 192,074 | N/A | N/A | 290,597 | N/A |
| 20260811 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 192,074 | N/A | N/A | 290,597 | N/A |
| 20260811 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 192,074 | N/A | N/A | 290,597 | N/A |
| 20260811 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 192,074 | N/A | N/A | 290,597 | N/A |
| 20260811 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 192,074 | N/A | N/A | 290,597 | N/A |
| 20260811 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 192,074 | N/A | N/A | 290,597 | N/A |
| 20260811 | 060230 | 제이케이시냅스 | convertible_bond | negative | N/A | 192,074 | N/A | N/A | 290,597 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
