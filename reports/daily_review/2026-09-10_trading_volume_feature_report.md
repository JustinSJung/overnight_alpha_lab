# Trading Volume Feature Report - 2026-09-10

Generated at: 2026-09-10 00:54:31

Source ML dataset: `data/processed/ml_dataset_20260910.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **578**
- Rows with price file found: **577**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **577**
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
| 20260909 | 288980 | 모아데이타 | paid_in_capital_increase | negative | N/A | 471,563 | N/A | N/A | 370,151 | N/A |
| 20260909 | 035620 | 바른손이앤에이 | paid_in_capital_increase | negative | N/A | 144,382 | N/A | N/A | 74,230 | N/A |
| 20260909 | 006980 | 우성 | merger | volatile | N/A | 1,186 | N/A | N/A | 291 | N/A |
| 20260909 | 357880 | SKAI | paid_in_capital_increase | negative | N/A | 2,818,646 | N/A | N/A | 755,261 | N/A |
| 20260909 | 255220 | SG | supply_contract | positive | N/A | 864,086 | N/A | N/A | 521,896 | N/A |
| 20260909 | 226340 | 본느 | paid_in_capital_increase | negative | N/A | 15,447,542 | N/A | N/A | 11,919,472 | N/A |
| 20260909 | 294090 | 이오플로우 | convertible_bond | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260909 | 109740 | 디에스케이 | major_shareholder_change | volatile | N/A | 46,869 | N/A | N/A | 91,088 | N/A |
| 20260909 | 261780 | 아리바이오LAB | convertible_bond | negative | N/A | 244,655 | N/A | N/A | 218,374 | N/A |
| 20260909 | 261780 | 아리바이오LAB | convertible_bond | negative | N/A | 244,655 | N/A | N/A | 218,374 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |
| 20260909 | 310210 | 보로노이 | investment_decision | volatile | N/A | 139,151 | N/A | N/A | 110,033 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
