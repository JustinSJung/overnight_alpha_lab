# Model Performance History Report - 2026-11-03

Generated at: 2026-11-03 04:09:32

## Purpose

This report summarizes cumulative model, prediction, market-adjusted, and trading-volume performance history.

It is designed to track whether the project is accumulating enough evaluated cases to support better model training and recommendation logic.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary Metrics

- ML dataset rows: **37066**
- Error-note rows: **10471**
- Market-adjusted evaluation rows: **10237**
- Market-adjusted score rows: **10237**
- Trading volume score rows: **40277**

- Prediction success: **3884**
- Prediction failure: **4321**
- Prediction pending: **2266**
- Prediction evaluated: **8205**
- Prediction success rate: **47.34%**

- Market-adjusted success: **0**
- Market-adjusted failure: **0**
- Market-driven weak success: **0**
- Market-adjusted pending: **2032**

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
| count    failure
count       4321
Name: 0, dtype: object |
| count    success
count       3884
Name: 1, dtype: object |
| count    pending
count       2266
Name: 2, dtype: object |

## Market-Adjusted Result Counts

| count |
|---|
| count    market_data_missing
count                   8205
Name: 0, dtype: object |
| count    pending
count       2032
Name: 1, dtype: object |

## Trading Volume Adjustment Counts

| count |
|---|
| count    neutral_volume_adjustment
count                        40277
Name: 0, dtype: object |

## Event-Type Performance Summary

| event_type | total | success | failure | pending | evaluated | success_rate |
|---|---|---|---|---|---|---|
| paid_in_capital_increase | 2555 | 1166 | 868 | 521 | 2034 | 57.33% |
| major_shareholder_change | 2584 | 770 | 1181 | 633 | 1951 | 39.47% |
| supply_contract | 1584 | 433 | 825 | 326 | 1258 | 34.42% |
| convertible_bond | 1350 | 585 | 432 | 333 | 1017 | 57.52% |
| merger | 754 | 311 | 347 | 96 | 658 | 47.26% |
| investment_decision | 508 | 196 | 197 | 115 | 393 | 49.87% |
| lawsuit | 504 | 215 | 168 | 121 | 383 | 56.14% |
| bond_with_warrant | 145 | 53 | 80 | 12 | 133 | 39.85% |
| disclosure_violation | 202 | 53 | 79 | 70 | 132 | 40.15% |
| bonus_issue | 105 | 42 | 60 | 3 | 102 | 41.18% |
| spin_off | 117 | 44 | 41 | 32 | 85 | 51.76% |
| earnings_guidance | 63 | 16 | 43 | 4 | 59 | 27.12% |

## Automation History

| run_date | generated_at | raw_dart_rows | parsed_dart_rows | selected_event_rows | scored_event_rows | news_feature_rows | error_note_rows | ml_dataset_rows | pending_rows | success_rows | failure_rows | trainable_rows | baseline_model_report_exists | automation_status_report_exists | raw_dart_file | ml_dataset_file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-11 | N/A | 651 | 651 | 73 | 73 | 73 | 244 | 856 | 0 | 309 | 547 | 856 | True | True | data/raw/dart_disclosures_20260910.csv | data/processed/ml_dataset_20260911.csv |
| 2026-09-14 | N/A | 656 | 656 | 80 | 80 | 80 | 179 | 321 | 0 | 102 | 219 | 321 | True | True | data/raw/dart_disclosures_20260911.csv | data/processed/ml_dataset_20260914.csv |
| 2026-09-15 | N/A | 506 | 506 | 78 | 78 | 78 | 194 | 106 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260914.csv | data/processed/ml_dataset_20260915.csv |
| 2026-09-16 | N/A | 561 | 561 | 88 | 88 | 88 | 367 | 1362 | 0 | 1003 | 359 | 1362 | True | True | data/raw/dart_disclosures_20260915.csv | data/processed/ml_dataset_20260916.csv |
| 2026-09-17 | N/A | 626 | 626 | 59 | 59 | 59 | 212 | 320 | 0 | 84 | 236 | 320 | True | True | data/raw/dart_disclosures_20260916.csv | data/processed/ml_dataset_20260917.csv |
| 2026-09-21 | N/A | 695 | 695 | 82 | 82 | 82 | 208 | 1120 | 0 | 88 | 1032 | 1120 | True | True | data/raw/dart_disclosures_20260918.csv | data/processed/ml_dataset_20260921.csv |
| 2026-09-22 | N/A | 508 | 508 | 79 | 79 | 79 | 301 | 2575 | 0 | 275 | 2300 | 2575 | True | True | data/raw/dart_disclosures_20260921.csv | data/processed/ml_dataset_20260922.csv |
| 2026-09-23 | N/A | 531 | 531 | 81 | 81 | 81 | 148 | 638 | 0 | 108 | 530 | 638 | True | True | data/raw/dart_disclosures_20260922.csv | data/processed/ml_dataset_20260923.csv |
| 2026-09-24 | N/A | 683 | 683 | 62 | 62 | 62 | 184 | 82 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260923.csv | data/processed/ml_dataset_20260924.csv |
| 2026-09-29 | N/A | 523 | 523 | 73 | 73 | 73 | 202 | 1470 | 0 | 913 | 557 | 1470 | True | True | data/raw/dart_disclosures_20260928.csv | data/processed/ml_dataset_20260929.csv |
| 2026-09-30 | N/A | 837 | 837 | 92 | 92 | 92 | 206 | 1015 | 0 | 423 | 592 | 1015 | True | True | data/raw/dart_disclosures_20260929.csv | data/processed/ml_dataset_20260930.csv |
| 2026-10-02 | N/A | 647 | 647 | 66 | 66 | 66 | 168 | 486 | 0 | 382 | 104 | 486 | True | True | data/raw/dart_disclosures_20261001.csv | data/processed/ml_dataset_20261002.csv |
| 2026-10-05 | N/A | 771 | 771 | 61 | 61 | 61 | 120 | 204 | 204 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20261002.csv | data/processed/ml_dataset_20261005.csv |
| 2026-10-07 | N/A | 538 | 538 | 80 | 80 | 80 | 237 | 952 | 0 | 205 | 747 | 952 | True | True | data/raw/dart_disclosures_20261006.csv | data/processed/ml_dataset_20261007.csv |
| 2026-10-08 | N/A | 717 | 717 | 58 | 58 | 58 | 134 | 76 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20261007.csv | data/processed/ml_dataset_20261008.csv |
| 2026-10-09 | N/A | 991 | 991 | 75 | 75 | 75 | 267 | 2159 | 2159 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20261008.csv | data/processed/ml_dataset_20261009.csv |
| 2026-10-13 | N/A | 559 | 559 | 74 | 74 | 74 | 189 | 441 | 0 | 312 | 129 | 441 | True | True | data/raw/dart_disclosures_20261012.csv | data/processed/ml_dataset_20261013.csv |
| 2026-10-14 | N/A | 456 | 456 | 66 | 66 | 66 | 192 | 783 | 0 | 54 | 729 | 783 | True | True | data/raw/dart_disclosures_20261013.csv | data/processed/ml_dataset_20261014.csv |
| 2026-10-15 | N/A | 578 | 578 | 65 | 65 | 65 | 138 | 100 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20261014.csv | data/processed/ml_dataset_20261015.csv |
| 2026-10-16 | N/A | 568 | 568 | 83 | 83 | 83 | 243 | 577 | 0 | 106 | 471 | 577 | True | True | data/raw/dart_disclosures_20261015.csv | data/processed/ml_dataset_20261016.csv |
| 2026-10-19 | N/A | 646 | 646 | 62 | 62 | 62 | 227 | 1913 | 0 | 1580 | 333 | 1913 | True | True | data/raw/dart_disclosures_20261016.csv | data/processed/ml_dataset_20261019.csv |
| 2026-10-20 | N/A | 483 | 483 | 71 | 71 | 71 | 140 | 84 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20261019.csv | data/processed/ml_dataset_20261020.csv |
| 2026-10-21 | N/A | 545 | 545 | 46 | 46 | 46 | 72 | 77 | 0 | 31 | 46 | 77 | True | True | data/raw/dart_disclosures_20261020.csv | data/processed/ml_dataset_20261021.csv |
| 2026-10-22 | N/A | 523 | 523 | 76 | 76 | 76 | 169 | 467 | 0 | 110 | 357 | 467 | True | True | data/raw/dart_disclosures_20261021.csv | data/processed/ml_dataset_20261022.csv |
| 2026-10-23 | N/A | 570 | 570 | 63 | 63 | 63 | 144 | 85 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20261022.csv | data/processed/ml_dataset_20261023.csv |
| 2026-10-26 | N/A | 570 | 570 | 57 | 57 | 57 | 139 | 457 | 0 | 237 | 220 | 457 | True | True | data/raw/dart_disclosures_20261023.csv | data/processed/ml_dataset_20261026.csv |
| 2026-10-27 | N/A | 526 | 526 | 79 | 79 | 79 | 234 | 964 | 0 | 509 | 455 | 964 | True | True | data/raw/dart_disclosures_20261026.csv | data/processed/ml_dataset_20261027.csv |
| 2026-10-29 | N/A | 665 | 665 | 79 | 79 | 79 | 385 | 136 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20261028.csv | data/processed/ml_dataset_20261029.csv |
| 2026-10-30 | N/A | 854 | 854 | 87 | 87 | 87 | 313 | 2799 | 0 | 2308 | 491 | 2799 | True | True | data/raw/dart_disclosures_20261029.csv | data/processed/ml_dataset_20261030.csv |
| 2026-11-02 | N/A | 1061 | 1061 | 134 | 134 | 134 | 452 | 254 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20261030.csv | data/processed/ml_dataset_20261102.csv |

## Interpretation

- A high pending count means the system needs more next-trading-day price data before performance can be judged.
- A low evaluated count means the model should remain conservative.
- Market-adjusted success is more meaningful than simple absolute-return success.
- Trading-volume score adjustment is useful only when enough price and volume history is available.
- The main goal at this stage is data accumulation and evaluation structure, not live trading performance.

## Next Step

The next step is to prepare the final MVP summary and clean up the README after Day 30.
