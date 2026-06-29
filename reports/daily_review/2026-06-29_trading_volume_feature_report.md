# Trading Volume Feature Report - 2026-06-29

Generated at: 2026-06-29 01:54:46

Source ML dataset: `data/processed/ml_dataset_20260629.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **29**
- Rows with price file found: **29**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **29**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260629 | 118000 | 메타케어 | paid_in_capital_increase | negative | N/A | 116,762 | N/A | N/A | 100,634 | N/A |
| 20260629 | 480370 | 씨케이솔루션 | supply_contract | positive | N/A | 235,971 | N/A | N/A | 147,437 | N/A |
| 20260629 | 068790 | DMS | supply_contract | positive | N/A | 173,999 | N/A | N/A | 179,485 | N/A |
| 20260629 | 011930 | 신성이엔지 | major_shareholder_change | volatile | N/A | 702,257 | N/A | N/A | 633,769 | N/A |
| 20260629 | 011930 | 신성이엔지 | major_shareholder_change | volatile | N/A | 702,257 | N/A | N/A | 633,769 | N/A |
| 20260629 | 011930 | 신성이엔지 | major_shareholder_change | volatile | N/A | 702,257 | N/A | N/A | 633,769 | N/A |
| 20260629 | 011930 | 신성이엔지 | major_shareholder_change | volatile | N/A | 702,257 | N/A | N/A | 633,769 | N/A |
| 20260629 | 011930 | 신성이엔지 | major_shareholder_change | volatile | N/A | 702,257 | N/A | N/A | 633,769 | N/A |
| 20260629 | 011930 | 신성이엔지 | major_shareholder_change | volatile | N/A | 702,257 | N/A | N/A | 633,769 | N/A |
| 20260629 | 011930 | 신성이엔지 | major_shareholder_change | volatile | N/A | 702,257 | N/A | N/A | 633,769 | N/A |
| 20260629 | 011930 | 신성이엔지 | major_shareholder_change | volatile | N/A | 702,257 | N/A | N/A | 633,769 | N/A |
| 20260629 | 011930 | 신성이엔지 | major_shareholder_change | volatile | N/A | 702,257 | N/A | N/A | 633,769 | N/A |
| 20260629 | 445090 | 에이직랜드 | supply_contract | positive | N/A | 125,078 | N/A | N/A | 397,360 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |
| 20260629 | 300080 | 플리토 | supply_contract | positive | N/A | 1,113,577 | N/A | N/A | 371,027 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
