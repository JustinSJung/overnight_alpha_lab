# Trading Volume Feature Report - 2026-08-06

Generated at: 2026-08-06 23:59:35

Source ML dataset: `data/processed/ml_dataset_20260806.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **85**
- Rows with price file found: **85**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **85**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260806 | 042370 | 비츠로테크 | supply_contract | positive | N/A | 265,873 | N/A | N/A | 185,124 | N/A |
| 20260806 | 163730 | 핑거 | paid_in_capital_increase | negative | N/A | 69,628 | N/A | N/A | 89,236 | N/A |
| 20260806 | 064800 | 포니링크 | lawsuit | negative | N/A | 43,767 | N/A | N/A | 27,673 | N/A |
| 20260806 | 457600 | 벡트 | major_shareholder_change | volatile | N/A | 248,554 | N/A | N/A | 916,459 | N/A |
| 20260806 | 457600 | 벡트 | major_shareholder_change | volatile | N/A | 248,554 | N/A | N/A | 916,459 | N/A |
| 20260806 | 457600 | 벡트 | major_shareholder_change | volatile | N/A | 248,554 | N/A | N/A | 916,459 | N/A |
| 20260806 | 457600 | 벡트 | major_shareholder_change | volatile | N/A | 248,554 | N/A | N/A | 916,459 | N/A |
| 20260806 | 488900 | 비츠로넥스텍 | supply_contract | positive | N/A | 87,839 | N/A | N/A | 77,992 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |
| 20260806 | 009190 | 대양금속 | investment_decision | volatile | N/A | 1,037,547 | N/A | N/A | 937,900 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
