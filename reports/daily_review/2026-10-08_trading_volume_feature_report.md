# Trading Volume Feature Report - 2026-10-08

Generated at: 2026-10-08 04:05:58

Source ML dataset: `data/processed/ml_dataset_20261008.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **222**
- Rows with price file found: **221**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **221**
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
| 20261007 | 007570 | 일양약품 | disclosure_violation | negative | N/A | 12,603 | N/A | N/A | 13,938 | N/A |
| 20261007 | 203400 | 에이비온 | disclosure_violation | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261007 | 035200 | 프럼파스트 | major_shareholder_change | volatile | N/A | 12,876 | N/A | N/A | 22,842 | N/A |
| 20261007 | 009190 | 대양금속 | major_shareholder_change | volatile | N/A | 266,522 | N/A | N/A | 421,133 | N/A |
| 20261007 | 008930 | 한미사이언스 | investment_decision | volatile | N/A | 818,252 | N/A | N/A | 270,110 | N/A |
| 20261007 | 288980 | 모아데이타 | convertible_bond | negative | N/A | 3,611,339 | N/A | N/A | 3,062,348 | N/A |
| 20261007 | 128940 | 한미약품 | investment_decision | volatile | N/A | 99,415 | N/A | N/A | 136,830 | N/A |
| 20261007 | 011000 | 진원생명과학 | convertible_bond | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |
| 20261007 | 224060 | 더코디 | paid_in_capital_increase | negative | N/A | 471,934 | N/A | N/A | 180,703 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
