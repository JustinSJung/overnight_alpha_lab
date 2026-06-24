# Trading Volume Feature Report - 2026-06-24

Generated at: 2026-06-24 22:40:49

Source ML dataset: `data/processed/ml_dataset_20260624.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **11**
- Rows with price file found: **11**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **11**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260624 | 043260 | 성호전자 | major_shareholder_change | volatile | N/A | 3,230,570 | N/A | N/A | 2,700,711 | N/A |
| 20260624 | 083790 | CG인바이츠 | disclosure_violation | negative | N/A | 415,350 | N/A | N/A | 344,903 | N/A |
| 20260624 | 061040 | 알에프텍 | merger | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260624 | 396470 | 워트 | supply_contract | positive | N/A | 315,472 | N/A | N/A | 1,885,793 | N/A |
| 20260624 | 452260 | 한화갤러리아 | investment_decision | volatile | N/A | 5,838,144 | N/A | N/A | 3,760,837 | N/A |
| 20260624 | 036620 | 감성코퍼레이션 | spin_off | volatile | N/A | 476,855 | N/A | N/A | 927,141 | N/A |
| 20260624 | 307870 | 비투엔 | major_shareholder_change | volatile | N/A | 583,433 | N/A | N/A | 344,859 | N/A |
| 20260624 | 097780 | 에코볼트 | merger | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260624 | 052710 | 아모텍 | paid_in_capital_increase | negative | N/A | 3,975,834 | N/A | N/A | 5,016,269 | N/A |
| 20260624 | 123690 | 한국화장품 | major_shareholder_change | volatile | N/A | 56,544 | N/A | N/A | 113,941 | N/A |
| 20260624 | 003350 | 한국화장품제조 | major_shareholder_change | volatile | N/A | 74,982 | N/A | N/A | 184,031 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
