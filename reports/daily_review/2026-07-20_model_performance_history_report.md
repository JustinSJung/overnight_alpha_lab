# Model Performance History Report - 2026-07-20

Generated at: 2026-07-20 23:18:33

## Purpose

This report summarizes cumulative model, prediction, market-adjusted, and trading-volume performance history.

It is designed to track whether the project is accumulating enough evaluated cases to support better model training and recommendation logic.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary Metrics

- ML dataset rows: **1568**
- Error-note rows: **420**
- Market-adjusted evaluation rows: **377**
- Market-adjusted score rows: **377**
- Trading volume score rows: **8413**

- Prediction success: **0**
- Prediction failure: **0**
- Prediction pending: **420**
- Prediction evaluated: **0**
- Prediction success rate: **0.00%**

- Market-adjusted success: **0**
- Market-adjusted failure: **0**
- Market-driven weak success: **0**
- Market-adjusted pending: **377**

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

## Prediction Result Counts

| count |
|---|
| count    pending
count        420
Name: 0, dtype: object |

## Market-Adjusted Result Counts

| count |
|---|
| count    pending
count        377
Name: 0, dtype: object |

## Trading Volume Adjustment Counts

| count |
|---|
| count    neutral_volume_adjustment
count                         8413
Name: 0, dtype: object |

## Event-Type Performance Summary

| event_type | total | success | failure | pending | evaluated | success_rate |
|---|---|---|---|---|---|---|
| bonus_issue | 1 | 0 | 0 | 1 | 0 | 0.00% |
| convertible_bond | 68 | 0 | 0 | 68 | 0 | 0.00% |
| disclosure_violation | 19 | 0 | 0 | 19 | 0 | 0.00% |
| earnings_guidance | 2 | 0 | 0 | 2 | 0 | 0.00% |
| investment_decision | 34 | 0 | 0 | 34 | 0 | 0.00% |
| lawsuit | 41 | 0 | 0 | 41 | 0 | 0.00% |
| major_shareholder_change | 79 | 0 | 0 | 79 | 0 | 0.00% |
| merger | 23 | 0 | 0 | 23 | 0 | 0.00% |
| paid_in_capital_increase | 69 | 0 | 0 | 69 | 0 | 0.00% |
| spin_off | 2 | 0 | 0 | 2 | 0 | 0.00% |
| supply_contract | 82 | 0 | 0 | 82 | 0 | 0.00% |

## Automation History

| run_date | generated_at | raw_dart_rows | parsed_dart_rows | selected_event_rows | scored_event_rows | news_feature_rows | error_note_rows | ml_dataset_rows | pending_rows | success_rows | failure_rows | trainable_rows | baseline_model_report_exists | automation_status_report_exists | raw_dart_file | ml_dataset_file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-06-19 | N/A | 100 | 100 | 18 | 18 | 18 | 19 | 21 | 21 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260619.csv | data/processed/ml_dataset_20260619.csv |
| 2026-06-24 | N/A | 100 | 100 | 11 | 11 | 11 | 11 | 11 | 11 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260624.csv | data/processed/ml_dataset_20260624.csv |
| 2026-06-26 | N/A | 100 | 100 | 20 | 20 | 20 | 34 | 92 | 92 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260626.csv | data/processed/ml_dataset_20260626.csv |
| 2026-06-27 | N/A | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | False | True | nan | nan |
| 2026-06-29 | N/A | 100 | 100 | 19 | 19 | 19 | 43 | 109 | 109 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260629.csv | data/processed/ml_dataset_20260629.csv |
| 2026-06-30 | N/A | 100 | 100 | 2 | 2 | 2 | 3 | 5 | 5 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260630.csv | data/processed/ml_dataset_20260630.csv |
| 2026-07-01 | N/A | 100 | 100 | 3 | 3 | 3 | 4 | 6 | 6 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260701.csv | data/processed/ml_dataset_20260701.csv |
| 2026-07-02 | N/A | 100 | 100 | 15 | 15 | 15 | 36 | 106 | 106 | 0 | 0 | 0 | False | True | data/raw/dart_disclosures_20260701.csv | data/processed/ml_dataset_20260701.csv |
| 2026-07-03 | N/A | 100 | 100 | 2 | 2 | 2 | 5 | 5 | 5 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260703.csv | data/processed/ml_dataset_20260703.csv |
| 2026-07-06 | N/A | 100 | 100 | 23 | 23 | 23 | 31 | 87 | 87 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260706.csv | data/processed/ml_dataset_20260706.csv |
| 2026-07-07 | N/A | 100 | 100 | 18 | 18 | 18 | 36 | 148 | 148 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260707.csv | data/processed/ml_dataset_20260707.csv |
| 2026-07-09 | N/A | 100 | 100 | 24 | 24 | 24 | 50 | 162 | 162 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260709.csv | data/processed/ml_dataset_20260709.csv |
| 2026-07-13 | N/A | 100 | 100 | 19 | 19 | 19 | 50 | 752 | 752 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260713.csv | data/processed/ml_dataset_20260713.csv |
| 2026-07-15 | N/A | 100 | 100 | 24 | 24 | 24 | 69 | 87 | 87 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260715.csv | data/processed/ml_dataset_20260715.csv |
| 2026-07-16 | N/A | 100 | 100 | 12 | 12 | 12 | 18 | 18 | 18 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260716.csv | data/processed/ml_dataset_20260716.csv |
| 2026-07-20 | N/A | 100 | 100 | 18 | 18 | 18 | 39 | 39 | 39 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260720.csv | data/processed/ml_dataset_20260720.csv |

## Interpretation

- A high pending count means the system needs more next-trading-day price data before performance can be judged.
- A low evaluated count means the model should remain conservative.
- Market-adjusted success is more meaningful than simple absolute-return success.
- Trading-volume score adjustment is useful only when enough price and volume history is available.
- The main goal at this stage is data accumulation and evaluation structure, not live trading performance.

## Next Step

The next step is to prepare the final MVP summary and clean up the README after Day 30.
