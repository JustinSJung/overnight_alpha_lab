# Trading Volume Feature Report - 2026-11-18

Generated at: 2026-11-18 04:50:55

Source ML dataset: `data/processed/ml_dataset_20261118.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **13369**
- Rows with price file found: **13369**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **13369**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261117 | 331920 | 셀레믹스 | major_shareholder_change | volatile | N/A | 16,658 | N/A | N/A | 27,595 | N/A |
| 20261117 | 355390 | 크라우드웍스 | major_shareholder_change | volatile | N/A | 76,606 | N/A | N/A | 95,252 | N/A |
| 20261117 | 025560 | 미래산업 | supply_contract | positive | N/A | 184,195 | N/A | N/A | 189,095 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |
| 20261117 | 018620 | 우진비앤지 | convertible_bond | negative | N/A | 5,277 | N/A | N/A | 3,799 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
