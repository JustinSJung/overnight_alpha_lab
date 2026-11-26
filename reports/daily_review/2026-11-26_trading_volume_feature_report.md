# Trading Volume Feature Report - 2026-11-26

Generated at: 2026-11-26 04:59:51

Source ML dataset: `data/processed/ml_dataset_20261126.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **3178635**
- Rows with price file found: **3178635**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **3178635**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261125 | 018620 | 우진비앤지 | major_shareholder_change | volatile | N/A | 32,756 | N/A | N/A | 26,635 | N/A |
| 20261125 | 018620 | 우진비앤지 | major_shareholder_change | volatile | N/A | 32,756 | N/A | N/A | 26,635 | N/A |
| 20261125 | 018620 | 우진비앤지 | major_shareholder_change | volatile | N/A | 32,756 | N/A | N/A | 26,635 | N/A |
| 20261125 | 018620 | 우진비앤지 | major_shareholder_change | volatile | N/A | 32,756 | N/A | N/A | 26,635 | N/A |
| 20261125 | 095700 | 제넥신 | disclosure_violation | negative | N/A | 115,134 | N/A | N/A | 193,483 | N/A |
| 20261125 | 071280 | 로체시스템즈 | supply_contract | positive | N/A | 290,007 | N/A | N/A | 142,026 | N/A |
| 20261125 | 042660 | 한화오션 | investment_decision | volatile | N/A | 1,340,655 | N/A | N/A | 1,780,286 | N/A |
| 20261125 | 042660 | 한화오션 | investment_decision | volatile | N/A | 1,340,655 | N/A | N/A | 1,780,286 | N/A |
| 20261125 | 042660 | 한화오션 | investment_decision | volatile | N/A | 1,340,655 | N/A | N/A | 1,780,286 | N/A |
| 20261125 | 042660 | 한화오션 | investment_decision | volatile | N/A | 1,340,655 | N/A | N/A | 1,780,286 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |
| 20261125 | 010170 | 대한광통신 | merger | volatile | N/A | 5,054,153 | N/A | N/A | 13,046,253 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
