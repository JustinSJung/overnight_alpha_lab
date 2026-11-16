# Trading Volume Feature Report - 2026-11-16

Generated at: 2026-11-16 02:53:20

Source ML dataset: `data/processed/ml_dataset_20261116.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **865**
- Rows with price file found: **865**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **865**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261113 | 159910 | 에코글로우 | disclosure_violation | negative | N/A | 30,191 | N/A | N/A | 5,082 | N/A |
| 20261113 | 224060 | 더코디 | disclosure_violation | negative | N/A | 62,350 | N/A | N/A | 44,305 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | N/A | 4,909 | N/A | N/A | 9,031 | N/A |
| 20261113 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 36,473 | N/A | N/A | 16,809 | N/A |
| 20261113 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 36,473 | N/A | N/A | 16,809 | N/A |
| 20261113 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | N/A | 36,473 | N/A | N/A | 16,809 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
