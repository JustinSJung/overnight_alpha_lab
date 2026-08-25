# Trading Volume Feature Report - 2026-08-25

Generated at: 2026-08-25 22:50:25

Source ML dataset: `data/processed/ml_dataset_20260825.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **23**
- Rows with price file found: **23**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **23**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260825 | 270520 | 앱튼 | investment_decision | volatile | N/A | 300,572 | N/A | N/A | 273,279 | N/A |
| 20260825 | 000210 | DL | supply_contract | positive | N/A | 82,462 | N/A | N/A | 40,863 | N/A |
| 20260825 | 014970 | 삼륭물산 | disclosure_violation | negative | N/A | 329,024 | N/A | N/A | 126,775 | N/A |
| 20260825 | 375500 | DL이앤씨 | supply_contract | positive | N/A | 298,876 | N/A | N/A | 277,538 | N/A |
| 20260825 | 267250 | HD현대 | supply_contract | positive | N/A | 122,439 | N/A | N/A | 165,010 | N/A |
| 20260825 | 216400 | 인바이츠바이오코아 | disclosure_violation | negative | N/A | 112 | N/A | N/A | 12,258 | N/A |
| 20260825 | 216400 | 인바이츠바이오코아 | disclosure_violation | negative | N/A | 112 | N/A | N/A | 12,258 | N/A |
| 20260825 | 216400 | 인바이츠바이오코아 | disclosure_violation | negative | N/A | 112 | N/A | N/A | 12,258 | N/A |
| 20260825 | 216400 | 인바이츠바이오코아 | disclosure_violation | negative | N/A | 112 | N/A | N/A | 12,258 | N/A |
| 20260825 | 009540 | HD한국조선해양 | supply_contract | positive | N/A | 161,515 | N/A | N/A | 200,941 | N/A |
| 20260825 | 000950 | 전방 | major_shareholder_change | volatile | N/A | 592 | N/A | N/A | 1,251 | N/A |
| 20260825 | 000950 | 전방 | major_shareholder_change | volatile | N/A | 592 | N/A | N/A | 1,251 | N/A |
| 20260825 | 000950 | 전방 | major_shareholder_change | volatile | N/A | 592 | N/A | N/A | 1,251 | N/A |
| 20260825 | 000950 | 전방 | major_shareholder_change | volatile | N/A | 592 | N/A | N/A | 1,251 | N/A |
| 20260825 | 006260 | LS | major_shareholder_change | volatile | N/A | 107,606 | N/A | N/A | 147,308 | N/A |
| 20260825 | 006260 | LS | major_shareholder_change | volatile | N/A | 107,606 | N/A | N/A | 147,308 | N/A |
| 20260825 | 006260 | LS | major_shareholder_change | volatile | N/A | 107,606 | N/A | N/A | 147,308 | N/A |
| 20260825 | 006260 | LS | major_shareholder_change | volatile | N/A | 107,606 | N/A | N/A | 147,308 | N/A |
| 20260825 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 3,091,479 | N/A | N/A | 1,342,334 | N/A |
| 20260825 | 034730 | SK | merger | volatile | N/A | 155,413 | N/A | N/A | 289,456 | N/A |
| 20260825 | 034730 | SK | merger | volatile | N/A | 155,413 | N/A | N/A | 289,456 | N/A |
| 20260825 | 034730 | SK | merger | volatile | N/A | 155,413 | N/A | N/A | 289,456 | N/A |
| 20260825 | 034730 | SK | merger | volatile | N/A | 155,413 | N/A | N/A | 289,456 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
