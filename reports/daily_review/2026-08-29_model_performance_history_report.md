# Model Performance History Report - 2026-08-29

Generated at: 2026-08-29 23:19:02

## Purpose

This report summarizes cumulative model, prediction, market-adjusted, and trading-volume performance history.

It is designed to track whether the project is accumulating enough evaluated cases to support better model training and recommendation logic.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary Metrics

- ML dataset rows: **5790**
- Error-note rows: **1493**
- Market-adjusted evaluation rows: **1450**
- Market-adjusted score rows: **1450**
- Trading volume score rows: **184725**

- Prediction success: **0**
- Prediction failure: **0**
- Prediction pending: **1493**
- Prediction evaluated: **0**
- Prediction success rate: **0.00%**

- Market-adjusted success: **0**
- Market-adjusted failure: **0**
- Market-driven weak success: **0**
- Market-adjusted pending: **1450**

- Total market-adjusted score adjustment: **0.00**
- Average market-adjusted score adjustment: **0.00**
- Total trading-volume score adjustment: **0.00**
- Average trading-volume score adjustment: **0.00**

## Data Accumulation by File Date

| source_date | row_count |
|---|---|
| 2026-06-18 | 54 |
| 2026-06-19 | 21 |
| 2026-06-24 | 11 |
| 2026-06-26 | 92 |
| 2026-06-27 | 92 |
| 2026-07-03 | 5 |
| 2026-07-06 | 87 |
| 2026-07-07 | 148 |
| 2026-07-09 | 162 |
| 2026-07-13 | 752 |
| 2026-07-15 | 87 |
| 2026-07-16 | 18 |
| 2026-07-20 | 39 |
| 2026-07-21 | 30 |
| 2026-07-22 | 279 |
| 2026-07-23 | 151 |
| 2026-07-24 | 3 |
| 2026-07-27 | 903 |
| 2026-07-28 | 31 |
| 2026-07-29 | 24 |
| 2026-07-30 | 280 |
| 2026-08-03 | 25 |
| 2026-08-04 | 223 |
| 2026-08-05 | 11 |
| 2026-08-06 | 25 |
| 2026-08-07 | 3 |
| 2026-08-10 | 363 |
| 2026-08-11 | 53 |
| 2026-08-12 | 109 |
| 2026-08-13 | 112 |

## Prediction Result Counts

| count |
|---|
| count    pending
count       1493
Name: 0, dtype: object |

## Market-Adjusted Result Counts

| count |
|---|
| count    pending
count       1450
Name: 0, dtype: object |

## Trading Volume Adjustment Counts

| count |
|---|
| count    neutral_volume_adjustment
count                       184725
Name: 0, dtype: object |

## Event-Type Performance Summary

| event_type | total | success | failure | pending | evaluated | success_rate |
|---|---|---|---|---|---|---|
| bond_with_warrant | 10 | 0 | 0 | 10 | 0 | 0.00% |
| bonus_issue | 3 | 0 | 0 | 3 | 0 | 0.00% |
| convertible_bond | 247 | 0 | 0 | 247 | 0 | 0.00% |
| disclosure_violation | 48 | 0 | 0 | 48 | 0 | 0.00% |
| earnings_guidance | 4 | 0 | 0 | 4 | 0 | 0.00% |
| investment_decision | 92 | 0 | 0 | 92 | 0 | 0.00% |
| lawsuit | 91 | 0 | 0 | 91 | 0 | 0.00% |
| major_shareholder_change | 420 | 0 | 0 | 420 | 0 | 0.00% |
| merger | 61 | 0 | 0 | 61 | 0 | 0.00% |
| paid_in_capital_increase | 256 | 0 | 0 | 256 | 0 | 0.00% |
| spin_off | 18 | 0 | 0 | 18 | 0 | 0.00% |
| supply_contract | 243 | 0 | 0 | 243 | 0 | 0.00% |

## Automation History

| run_date | generated_at | raw_dart_rows | parsed_dart_rows | selected_event_rows | scored_event_rows | news_feature_rows | error_note_rows | ml_dataset_rows | pending_rows | success_rows | failure_rows | trainable_rows | baseline_model_report_exists | automation_status_report_exists | raw_dart_file | ml_dataset_file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-07-09 | N/A | 100 | 100 | 24 | 24 | 24 | 50 | 162 | 162 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260709.csv | data/processed/ml_dataset_20260709.csv |
| 2026-07-13 | N/A | 100 | 100 | 19 | 19 | 19 | 50 | 752 | 752 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260713.csv | data/processed/ml_dataset_20260713.csv |
| 2026-07-15 | N/A | 100 | 100 | 24 | 24 | 24 | 69 | 87 | 87 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260715.csv | data/processed/ml_dataset_20260715.csv |
| 2026-07-16 | N/A | 100 | 100 | 12 | 12 | 12 | 18 | 18 | 18 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260716.csv | data/processed/ml_dataset_20260716.csv |
| 2026-07-20 | N/A | 100 | 100 | 18 | 18 | 18 | 39 | 39 | 39 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260720.csv | data/processed/ml_dataset_20260720.csv |
| 2026-07-21 | N/A | 100 | 100 | 17 | 17 | 17 | 27 | 30 | 30 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260721.csv | data/processed/ml_dataset_20260721.csv |
| 2026-07-22 | N/A | 100 | 100 | 13 | 13 | 13 | 35 | 279 | 279 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260722.csv | data/processed/ml_dataset_20260722.csv |
| 2026-07-23 | N/A | 100 | 100 | 21 | 21 | 21 | 39 | 151 | 151 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260723.csv | data/processed/ml_dataset_20260723.csv |
| 2026-07-24 | N/A | 100 | 100 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260724.csv | data/processed/ml_dataset_20260724.csv |
| 2026-07-27 | N/A | 100 | 100 | 23 | 23 | 23 | 75 | 903 | 903 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260727.csv | data/processed/ml_dataset_20260727.csv |
| 2026-07-28 | N/A | 100 | 100 | 22 | 22 | 22 | 29 | 31 | 31 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260728.csv | data/processed/ml_dataset_20260728.csv |
| 2026-07-29 | N/A | 100 | 100 | 13 | 13 | 13 | 20 | 24 | 24 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260729.csv | data/processed/ml_dataset_20260729.csv |
| 2026-07-30 | N/A | 100 | 100 | 21 | 21 | 21 | 68 | 280 | 280 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260730.csv | data/processed/ml_dataset_20260730.csv |
| 2026-08-03 | N/A | 100 | 100 | 20 | 20 | 20 | 25 | 25 | 25 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260803.csv | data/processed/ml_dataset_20260803.csv |
| 2026-08-04 | N/A | 100 | 100 | 19 | 19 | 19 | 55 | 223 | 223 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260804.csv | data/processed/ml_dataset_20260804.csv |
| 2026-08-05 | N/A | 100 | 100 | 7 | 7 | 7 | 11 | 11 | 11 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260805.csv | data/processed/ml_dataset_20260805.csv |
| 2026-08-06 | N/A | 100 | 100 | 17 | 17 | 17 | 25 | 25 | 25 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260806.csv | data/processed/ml_dataset_20260806.csv |
| 2026-08-07 | N/A | 100 | 100 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260807.csv | data/processed/ml_dataset_20260807.csv |
| 2026-08-10 | N/A | 100 | 100 | 17 | 17 | 17 | 65 | 363 | 363 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260810.csv | data/processed/ml_dataset_20260810.csv |
| 2026-08-11 | N/A | 100 | 100 | 25 | 25 | 25 | 45 | 53 | 53 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260811.csv | data/processed/ml_dataset_20260811.csv |
| 2026-08-12 | N/A | 100 | 100 | 13 | 13 | 13 | 25 | 109 | 109 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260812.csv | data/processed/ml_dataset_20260812.csv |
| 2026-08-13 | N/A | 100 | 100 | 13 | 13 | 13 | 26 | 112 | 112 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260813.csv | data/processed/ml_dataset_20260813.csv |
| 2026-08-18 | N/A | 100 | 100 | 22 | 22 | 22 | 34 | 34 | 34 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260818.csv | data/processed/ml_dataset_20260818.csv |
| 2026-08-19 | N/A | 100 | 100 | 23 | 23 | 23 | 31 | 35 | 35 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260819.csv | data/processed/ml_dataset_20260819.csv |
| 2026-08-20 | N/A | 100 | 100 | 18 | 18 | 18 | 39 | 227 | 227 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260820.csv | data/processed/ml_dataset_20260820.csv |
| 2026-08-24 | N/A | 100 | 100 | 26 | 26 | 26 | 78 | 327 | 327 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260824.csv | data/processed/ml_dataset_20260824.csv |
| 2026-08-25 | N/A | 100 | 100 | 11 | 11 | 11 | 15 | 15 | 15 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260825.csv | data/processed/ml_dataset_20260825.csv |
| 2026-08-27 | N/A | 100 | 100 | 4 | 4 | 4 | 4 | 4 | 4 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260827.csv | data/processed/ml_dataset_20260827.csv |
| 2026-08-28 | N/A | 100 | 100 | 4 | 4 | 4 | 4 | 4 | 4 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260828.csv | data/processed/ml_dataset_20260828.csv |
| 2026-08-29 | N/A | 2145 | 2145 | 100 | 100 | 100 | 292 | 951 | 951 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260828.csv | data/processed/ml_dataset_20260829.csv |

## Interpretation

- A high pending count means the system needs more next-trading-day price data before performance can be judged.
- A low evaluated count means the model should remain conservative.
- Market-adjusted success is more meaningful than simple absolute-return success.
- Trading-volume score adjustment is useful only when enough price and volume history is available.
- The main goal at this stage is data accumulation and evaluation structure, not live trading performance.

## Next Step

The next step is to prepare the final MVP summary and clean up the README after Day 30.
