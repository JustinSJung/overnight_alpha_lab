# Trading Volume Feature Report - 2026-09-07

Generated at: 2026-09-07 00:27:27

Source ML dataset: `data/processed/ml_dataset_20260907.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **22414**
- Rows with price file found: **22414**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **22414**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260904 | 361610 | SK아이이테크놀로지 | merger | volatile | N/A | 168,089 | N/A | N/A | 111,215 | N/A |
| 20260904 | 096770 | SK이노베이션 | merger | volatile | N/A | 795,636 | N/A | N/A | 758,130 | N/A |
| 20260904 | 208640 | 썸에이지 | disclosure_violation | negative | N/A | 818,998 | N/A | N/A | 444,725 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |
| 20260904 | 322780 | 코퍼스코리아 | convertible_bond | negative | N/A | 54,714 | N/A | N/A | 26,153 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
