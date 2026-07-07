# Model Performance History Report - 2026-07-07

Generated at: 2026-07-07 23:19:49

## Purpose

This report summarizes cumulative model, prediction, market-adjusted, and trading-volume performance history.

It is designed to track whether the project is accumulating enough evaluated cases to support better model training and recommendation logic.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary Metrics

- ML dataset rows: **510**
- Error-note rows: **194**
- Market-adjusted evaluation rows: **151**
- Market-adjusted score rows: **151**
- Trading volume score rows: **20688**

- Prediction success: **0**
- Prediction failure: **0**
- Prediction pending: **194**
- Prediction evaluated: **0**
- Prediction success rate: **0.00%**

- Market-adjusted success: **0**
- Market-adjusted failure: **0**
- Market-driven weak success: **0**
- Market-adjusted pending: **151**

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

## Prediction Result Counts

| count |
|---|
| count    pending
count        194
Name: 0, dtype: object |

## Market-Adjusted Result Counts

| count |
|---|
| count    pending
count        151
Name: 0, dtype: object |

## Trading Volume Adjustment Counts

| count |
|---|
| count    neutral_volume_adjustment
count                        20688
Name: 0, dtype: object |

## Event-Type Performance Summary

| event_type | total | success | failure | pending | evaluated | success_rate |
|---|---|---|---|---|---|---|
| convertible_bond | 18 | 0 | 0 | 18 | 0 | 0.00% |
| disclosure_violation | 6 | 0 | 0 | 6 | 0 | 0.00% |
| earnings_guidance | 2 | 0 | 0 | 2 | 0 | 0.00% |
| investment_decision | 16 | 0 | 0 | 16 | 0 | 0.00% |
| lawsuit | 14 | 0 | 0 | 14 | 0 | 0.00% |
| major_shareholder_change | 45 | 0 | 0 | 45 | 0 | 0.00% |
| merger | 8 | 0 | 0 | 8 | 0 | 0.00% |
| paid_in_capital_increase | 23 | 0 | 0 | 23 | 0 | 0.00% |
| spin_off | 1 | 0 | 0 | 1 | 0 | 0.00% |
| supply_contract | 61 | 0 | 0 | 61 | 0 | 0.00% |

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
| 2026-07-07 | N/A | 100 | 100 | 15 | 15 | 15 | 28 | 28 | 28 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260707.csv | data/processed/ml_dataset_20260707.csv |

## Interpretation

- A high pending count means the system needs more next-trading-day price data before performance can be judged.
- A low evaluated count means the model should remain conservative.
- Market-adjusted success is more meaningful than simple absolute-return success.
- Trading-volume score adjustment is useful only when enough price and volume history is available.
- The main goal at this stage is data accumulation and evaluation structure, not live trading performance.

## Next Step

The next step is to prepare the final MVP summary and clean up the README after Day 30.
