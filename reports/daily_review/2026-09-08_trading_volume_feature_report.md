# Trading Volume Feature Report - 2026-09-08

Generated at: 2026-09-08 01:05:19

Source ML dataset: `data/processed/ml_dataset_20260908.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **44219**
- Rows with price file found: **44219**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **44219**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260907 | 294870 | IPARK현대산업개발 | disclosure_violation | negative | N/A | 119,962 | N/A | N/A | 154,164 | N/A |
| 20260907 | 294870 | IPARK현대산업개발 | disclosure_violation | negative | N/A | 119,962 | N/A | N/A | 154,164 | N/A |
| 20260907 | 294870 | IPARK현대산업개발 | disclosure_violation | negative | N/A | 119,962 | N/A | N/A | 154,164 | N/A |
| 20260907 | 294870 | IPARK현대산업개발 | disclosure_violation | negative | N/A | 119,962 | N/A | N/A | 154,164 | N/A |
| 20260907 | 012630 | HDC | disclosure_violation | negative | N/A | 44,827 | N/A | N/A | 50,279 | N/A |
| 20260907 | 083790 | CG인바이츠 | supply_contract | positive | N/A | 136,990 | N/A | N/A | 148,833 | N/A |
| 20260907 | 056090 | 시지메드텍 | spin_off | volatile | N/A | 909,266 | N/A | N/A | 294,498 | N/A |
| 20260907 | 206400 | 베노티앤알 | lawsuit | negative | N/A | 35,948 | N/A | N/A | 23,785 | N/A |
| 20260907 | 320000 | 한울반도체 | major_shareholder_change | volatile | N/A | 152,799 | N/A | N/A | 378,904 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |
| 20260907 | 001260 | 남광토건 | investment_decision | volatile | N/A | 42,966 | N/A | N/A | 683,711 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
