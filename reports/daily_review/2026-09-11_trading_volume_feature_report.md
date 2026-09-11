# Trading Volume Feature Report - 2026-09-11

Generated at: 2026-09-11 01:09:46

Source ML dataset: `data/processed/ml_dataset_20260911.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **136670**
- Rows with price file found: **136670**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **136670**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260910 | 317400 | 자이에스앤디 | investment_decision | volatile | N/A | 1,791,797 | N/A | N/A | 2,602,173 | N/A |
| 20260910 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 138,452 | N/A | N/A | 195,757 | N/A |
| 20260910 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 138,452 | N/A | N/A | 195,757 | N/A |
| 20260910 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 138,452 | N/A | N/A | 195,757 | N/A |
| 20260910 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 138,452 | N/A | N/A | 195,757 | N/A |
| 20260910 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 138,452 | N/A | N/A | 195,757 | N/A |
| 20260910 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 138,452 | N/A | N/A | 195,757 | N/A |
| 20260910 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 138,452 | N/A | N/A | 195,757 | N/A |
| 20260910 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 138,452 | N/A | N/A | 195,757 | N/A |
| 20260910 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 138,452 | N/A | N/A | 195,757 | N/A |
| 20260910 | 009810 | MDS스피어 | convertible_bond | negative | N/A | 7,087 | N/A | N/A | 11,062 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |
| 20260910 | 001390 | KG케미칼 | major_shareholder_change | volatile | N/A | 1,104,147 | N/A | N/A | 288,631 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
