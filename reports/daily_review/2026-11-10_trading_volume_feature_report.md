# Trading Volume Feature Report - 2026-11-10

Generated at: 2026-11-10 05:37:09

Source ML dataset: `data/processed/ml_dataset_20261110.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **567**
- Rows with price file found: **566**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **566**
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
| 20261109 | 088280 | 쏘닉스 | convertible_bond | negative | N/A | 85,854 | N/A | N/A | 94,467 | N/A |
| 20261109 | 070300 | 퀀텀레일 | convertible_bond | negative | N/A | 1,368,808 | N/A | N/A | 2,471,792 | N/A |
| 20261109 | 950260 | 인제니아테라퓨틱스 | investment_decision | volatile | N/A | 296,710 | N/A | N/A | 497,447 | N/A |
| 20261109 | 060260 | 뉴보텍 | disclosure_violation | negative | N/A | 92,905 | N/A | N/A | 1,453,459 | N/A |
| 20261109 | 376930 | 노을 | major_shareholder_change | volatile | N/A | 53,347 | N/A | N/A | 21,260 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |
| 20261109 | 033250 | 체시스 | paid_in_capital_increase | negative | N/A | 19,133 | N/A | N/A | 17,242 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
