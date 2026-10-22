# Trading Volume Feature Report - 2026-10-22

Generated at: 2026-10-22 01:25:57

Source ML dataset: `data/processed/ml_dataset_20261022.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **21475**
- Rows with price file found: **21475**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **21475**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261021 | 011000 | 진원생명과학 | lawsuit | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 355390 | 크라우드웍스 | disclosure_violation | negative | N/A | 262,847 | N/A | N/A | 536,785 | N/A |
| 20261021 | 043100 | 알파AI | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 043100 | 알파AI | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 043100 | 알파AI | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 043100 | 알파AI | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 043100 | 알파AI | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 043100 | 알파AI | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 043100 | 알파AI | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 043100 | 알파AI | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 043100 | 알파AI | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 305090 | 마이크로디지탈 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261021 | 288980 | 모아데이타 | disclosure_violation | negative | N/A | 796,141 | N/A | N/A | 1,070,945 | N/A |
| 20261021 | 288980 | 모아데이타 | disclosure_violation | negative | N/A | 796,141 | N/A | N/A | 1,070,945 | N/A |
| 20261021 | 288980 | 모아데이타 | disclosure_violation | negative | N/A | 796,141 | N/A | N/A | 1,070,945 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
