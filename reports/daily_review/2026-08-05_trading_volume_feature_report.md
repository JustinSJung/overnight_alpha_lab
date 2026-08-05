# Trading Volume Feature Report - 2026-08-05

Generated at: 2026-08-05 23:20:49

Source ML dataset: `data/processed/ml_dataset_20260805.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **21**
- Rows with price file found: **21**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **21**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260805 | 252500 | 세화피앤씨 | spin_off | volatile | N/A | 36,821 | N/A | N/A | 24,095 | N/A |
| 20260805 | 252500 | 세화피앤씨 | spin_off | volatile | N/A | 36,821 | N/A | N/A | 24,095 | N/A |
| 20260805 | 252500 | 세화피앤씨 | spin_off | volatile | N/A | 36,821 | N/A | N/A | 24,095 | N/A |
| 20260805 | 252500 | 세화피앤씨 | spin_off | volatile | N/A | 36,821 | N/A | N/A | 24,095 | N/A |
| 20260805 | 380540 | 옵티코어 | convertible_bond | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260805 | 276040 | 스코넥 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260805 | 276040 | 스코넥 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260805 | 276040 | 스코넥 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260805 | 276040 | 스코넥 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260805 | 276040 | 스코넥 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260805 | 276040 | 스코넥 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260805 | 276040 | 스코넥 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260805 | 276040 | 스코넥 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260805 | 276040 | 스코넥 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260805 | 000950 | 전방 | major_shareholder_change | volatile | N/A | 4,279 | N/A | N/A | 2,935 | N/A |
| 20260805 | 000950 | 전방 | major_shareholder_change | volatile | N/A | 4,279 | N/A | N/A | 2,935 | N/A |
| 20260805 | 000950 | 전방 | major_shareholder_change | volatile | N/A | 4,279 | N/A | N/A | 2,935 | N/A |
| 20260805 | 000950 | 전방 | major_shareholder_change | volatile | N/A | 4,279 | N/A | N/A | 2,935 | N/A |
| 20260805 | 001260 | 남광토건 | supply_contract | positive | N/A | 2,675,021 | N/A | N/A | 1,880,510 | N/A |
| 20260805 | 004990 | 롯데지주 | major_shareholder_change | volatile | N/A | 105,024 | N/A | N/A | 173,730 | N/A |
| 20260805 | 011810 | STX | investment_decision | volatile | N/A | 0 | N/A | N/A | 0 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
