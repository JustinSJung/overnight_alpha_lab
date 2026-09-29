# Trading Volume Feature Report - 2026-09-29

Generated at: 2026-09-29 03:31:52

Source ML dataset: `data/processed/ml_dataset_20260929.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **598996**
- Rows with price file found: **598996**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **598996**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260928 | 402030 | 코난테크놀로지 | major_shareholder_change | volatile | N/A | 23,788 | N/A | N/A | 13,147 | N/A |
| 20260928 | 092040 | 아미코젠 | disclosure_violation | negative | N/A | 339,107 | N/A | N/A | 544,066 | N/A |
| 20260928 | 206400 | 베노티앤알 | major_shareholder_change | volatile | N/A | 25,466 | N/A | N/A | 13,269 | N/A |
| 20260928 | 222080 | SFA넥셀 | supply_contract | positive | N/A | 491,598 | N/A | N/A | 698,416 | N/A |
| 20260928 | 306620 | 지아이에스 | bond_with_warrant | negative | N/A | 245,444 | N/A | N/A | 137,629 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |
| 20260928 | 250030 | 진코스텍 | paid_in_capital_increase | negative | N/A | 20,172 | N/A | N/A | 3,335 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
