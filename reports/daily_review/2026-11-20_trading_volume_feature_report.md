# Trading Volume Feature Report - 2026-11-20

Generated at: 2026-11-20 04:02:16

Source ML dataset: `data/processed/ml_dataset_20261120.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **22048**
- Rows with price file found: **22048**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **22048**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261119 | 028300 | HLB | merger | volatile | N/A | 381,124 | N/A | N/A | 417,960 | N/A |
| 20261119 | 424870 | 이뮨온시아 | disclosure_violation | negative | N/A | 199,598 | N/A | N/A | 285,714 | N/A |
| 20261119 | 900270 | 헝셩그룹 | disclosure_violation | negative | N/A | 21,754 | N/A | N/A | 13,228 | N/A |
| 20261119 | 290690 | 아리바이오홀딩스 | disclosure_violation | negative | N/A | 429,185 | N/A | N/A | 562,417 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |
| 20261119 | 078350 | 한양디지텍 | paid_in_capital_increase | negative | N/A | 588,670 | N/A | N/A | 445,794 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
