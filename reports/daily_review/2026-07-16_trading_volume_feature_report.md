# Trading Volume Feature Report - 2026-07-16

Generated at: 2026-07-16 23:14:06

Source ML dataset: `data/processed/ml_dataset_20260716.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **36**
- Rows with price file found: **36**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **36**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260716 | 009320 | 아진전자부품 | major_shareholder_change | volatile | N/A | 86,334 | N/A | N/A | 191,160 | N/A |
| 20260716 | 080010 | 이상네트웍스 | disclosure_violation | negative | N/A | 3,262 | N/A | N/A | 4,724 | N/A |
| 20260716 | 340810 | 시선AI | paid_in_capital_increase | negative | N/A | 144,008 | N/A | N/A | 69,437 | N/A |
| 20260716 | 011000 | 진원생명과학 | investment_decision | volatile | N/A | 1,446,276 | N/A | N/A | 1,407,021 | N/A |
| 20260716 | 011000 | 진원생명과학 | investment_decision | volatile | N/A | 1,446,276 | N/A | N/A | 1,407,021 | N/A |
| 20260716 | 011000 | 진원생명과학 | investment_decision | volatile | N/A | 1,446,276 | N/A | N/A | 1,407,021 | N/A |
| 20260716 | 011000 | 진원생명과학 | investment_decision | volatile | N/A | 1,446,276 | N/A | N/A | 1,407,021 | N/A |
| 20260716 | 097230 | HJ중공업 | supply_contract | positive | N/A | 795,594 | N/A | N/A | 1,205,533 | N/A |
| 20260716 | 042940 | 상지건설 | paid_in_capital_increase | negative | N/A | 3,279,398 | N/A | N/A | 521,134 | N/A |
| 20260716 | 066790 | 씨씨에스 | lawsuit | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260716 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 75,388 | N/A | N/A | 45,367 | N/A |
| 20260716 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 75,388 | N/A | N/A | 45,367 | N/A |
| 20260716 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 75,388 | N/A | N/A | 45,367 | N/A |
| 20260716 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 75,388 | N/A | N/A | 45,367 | N/A |
| 20260716 | 054940 | 엑사이엔씨 | spin_off | volatile | N/A | 267,095 | N/A | N/A | 292,244 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |
| 20260716 | 320000 | 한울반도체 | paid_in_capital_increase | negative | N/A | 52,710 | N/A | N/A | 63,142 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
