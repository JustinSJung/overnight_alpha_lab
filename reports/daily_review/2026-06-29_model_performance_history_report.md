# Model Performance History Report - 2026-06-29

Generated at: 2026-06-29 14:39:38

## Purpose

This report summarizes cumulative model, prediction, market-adjusted, and trading-volume performance history.

It is designed to track whether the project is accumulating enough evaluated cases to support better model training and recommendation logic.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary Metrics

- ML dataset rows: **379**
- Error-note rows: **165**
- Market-adjusted evaluation rows: **122**
- Market-adjusted score rows: **122**
- Trading volume score rows: **13037**

- Prediction success: **0**
- Prediction failure: **0**
- Prediction pending: **165**
- Prediction evaluated: **0**
- Prediction success rate: **0.00%**

- Market-adjusted success: **0**
- Market-adjusted failure: **0**
- Market-driven weak success: **0**
- Market-adjusted pending: **122**

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
| 2026-06-29 | 109 |

## Prediction Result Counts

| count |
|---|
| count    pending
count        165
Name: 0, dtype: object |

## Market-Adjusted Result Counts

| count |
|---|
| count    pending
count        122
Name: 0, dtype: object |

## Trading Volume Adjustment Counts

| count |
|---|
| count    neutral_volume_adjustment
count                        13037
Name: 0, dtype: object |

## Event-Type Performance Summary

| event_type | total | success | failure | pending | evaluated | success_rate |
|---|---|---|---|---|---|---|
| convertible_bond | 14 | 0 | 0 | 14 | 0 | 0.00% |
| disclosure_violation | 10 | 0 | 0 | 10 | 0 | 0.00% |
| investment_decision | 16 | 0 | 0 | 16 | 0 | 0.00% |
| lawsuit | 11 | 0 | 0 | 11 | 0 | 0.00% |
| major_shareholder_change | 20 | 0 | 0 | 20 | 0 | 0.00% |
| merger | 6 | 0 | 0 | 6 | 0 | 0.00% |
| paid_in_capital_increase | 33 | 0 | 0 | 33 | 0 | 0.00% |
| spin_off | 9 | 0 | 0 | 9 | 0 | 0.00% |
| supply_contract | 46 | 0 | 0 | 46 | 0 | 0.00% |

## Automation History

| run_date | generated_at | raw_dart_rows | parsed_dart_rows | selected_event_rows | scored_event_rows | news_feature_rows | error_note_rows | ml_dataset_rows | pending_rows | success_rows | failure_rows | trainable_rows | baseline_model_report_exists | automation_status_report_exists | raw_dart_file | ml_dataset_file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-06-19 | N/A | 100 | 100 | 18 | 18 | 18 | 19 | 21 | 21 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260619.csv | data/processed/ml_dataset_20260619.csv |
| 2026-06-24 | N/A | 100 | 100 | 11 | 11 | 11 | 11 | 11 | 11 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260624.csv | data/processed/ml_dataset_20260624.csv |
| 2026-06-26 | N/A | 100 | 100 | 20 | 20 | 20 | 34 | 92 | 92 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260626.csv | data/processed/ml_dataset_20260626.csv |
| 2026-06-27 | N/A | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | False | True | nan | nan |
| 2026-06-29 | N/A | 100 | 100 | 6 | 6 | 6 | 9 | 11 | 11 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260629.csv | data/processed/ml_dataset_20260629.csv |

## Interpretation

- A high pending count means the system needs more next-trading-day price data before performance can be judged.
- A low evaluated count means the model should remain conservative.
- Market-adjusted success is more meaningful than simple absolute-return success.
- Trading-volume score adjustment is useful only when enough price and volume history is available.
- The main goal at this stage is data accumulation and evaluation structure, not live trading performance.

## Next Step

The next step is to prepare the final MVP summary and clean up the README after Day 30.
