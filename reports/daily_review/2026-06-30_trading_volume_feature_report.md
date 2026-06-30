# Trading Volume Feature Report - 2026-06-30

Generated at: 2026-06-30 00:35:06

Source ML dataset: `data/processed/ml_dataset_20260630.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **17**
- Rows with price file found: **17**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **17**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 033500 | 동성화인텍 | supply_contract | positive | N/A | 236,349 | N/A | N/A | 249,630 | N/A |
| 20260630 | 009150 | 삼성전기 | supply_contract | positive | N/A | 1,639,739 | N/A | N/A | 1,954,960 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
