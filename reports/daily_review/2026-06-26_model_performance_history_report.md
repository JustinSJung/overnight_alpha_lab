# Model Performance History Report - 2026-06-26

Generated at: 2026-06-26 08:30:36

## Purpose

This report summarizes cumulative model, prediction, market-adjusted, and trading-volume performance history.

It is designed to track whether the project is accumulating enough evaluated cases to support better model training and recommendation logic.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary Metrics

- ML dataset rows: **84**
- Error-note rows: **28**
- Market-adjusted evaluation rows: **28**
- Market-adjusted score rows: **28**
- Trading volume score rows: **4128**

- Prediction success: **0**
- Prediction failure: **0**
- Prediction pending: **28**
- Prediction evaluated: **0**
- Prediction success rate: **0.00%**

- Market-adjusted success: **0**
- Market-adjusted failure: **0**
- Market-driven weak success: **0**
- Market-adjusted pending: **28**

- Total market-adjusted score adjustment: **0.00**
- Average market-adjusted score adjustment: **0.00**
- Total trading-volume score adjustment: **0.00**
- Average trading-volume score adjustment: **0.00**

## Data Accumulation by File Date

| source_date | row_count |
|---|---|
| 2026-06-26 | 84 |

## Prediction Result Counts

| count |
|---|
| count    pending
count         28
Name: 0, dtype: object |

## Market-Adjusted Result Counts

| count |
|---|
| count    pending
count         28
Name: 0, dtype: object |

## Trading Volume Adjustment Counts

| count |
|---|
| count    neutral_volume_adjustment
count                         4128
Name: 0, dtype: object |

## Event-Type Performance Summary

| event_type | total | success | failure | pending | evaluated | success_rate |
|---|---|---|---|---|---|---|
| bond_with_warrant | 1 | 0 | 0 | 1 | 0 | 0.00% |
| convertible_bond | 11 | 0 | 0 | 11 | 0 | 0.00% |
| investment_decision | 2 | 0 | 0 | 2 | 0 | 0.00% |
| major_shareholder_change | 3 | 0 | 0 | 3 | 0 | 0.00% |
| merger | 2 | 0 | 0 | 2 | 0 | 0.00% |
| paid_in_capital_increase | 3 | 0 | 0 | 3 | 0 | 0.00% |
| supply_contract | 6 | 0 | 0 | 6 | 0 | 0.00% |

## Automation History

| run_date | generated_at | raw_dart_rows | parsed_dart_rows | selected_event_rows | scored_event_rows | news_feature_rows | error_note_rows | ml_dataset_rows | pending_rows | success_rows | failure_rows | trainable_rows | baseline_model_report_exists | automation_status_report_exists | raw_dart_file | ml_dataset_file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-06-19 | N/A | 100 | 100 | 18 | 18 | 18 | 19 | 21 | 21 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260619.csv | data/processed/ml_dataset_20260619.csv |
| 2026-06-24 | N/A | 100 | 100 | 11 | 11 | 11 | 11 | 11 | 11 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260624.csv | data/processed/ml_dataset_20260624.csv |
| 2026-06-26 | N/A | 100 | 100 | 14 | 14 | 14 | 35 | 153 | 153 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260626.csv | data/processed/ml_dataset_20260626.csv |

## Interpretation

- A high pending count means the system needs more next-trading-day price data before performance can be judged.
- A low evaluated count means the model should remain conservative.
- Market-adjusted success is more meaningful than simple absolute-return success.
- Trading-volume score adjustment is useful only when enough price and volume history is available.
- The main goal at this stage is data accumulation and evaluation structure, not live trading performance.

## Next Step

The next step is to prepare the final MVP summary and clean up the README after Day 30.
