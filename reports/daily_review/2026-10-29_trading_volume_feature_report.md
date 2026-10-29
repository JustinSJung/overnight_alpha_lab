# Trading Volume Feature Report - 2026-10-29

Generated at: 2026-10-29 02:25:46

Source ML dataset: `data/processed/ml_dataset_20261029.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **736**
- Rows with price file found: **735**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **735**
- price_file_missing: **1**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261028 | 196170 | 알테오젠 | merger | volatile | N/A | 297,353 | N/A | N/A | 229,571 | N/A |
| 20261028 | 009190 | 대양금속 | disclosure_violation | negative | N/A | 1,875,671 | N/A | N/A | 1,752,141 | N/A |
| 20261028 | 002020 | 코오롱 | disclosure_violation | negative | N/A | 19,851 | N/A | N/A | 13,801 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |
| 20261028 | 299660 | 셀리드 | lawsuit | negative | N/A | 693,886 | N/A | N/A | 270,909 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
