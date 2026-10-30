# Model Performance History Report - 2026-10-30

Generated at: 2026-10-30 02:32:18

## Purpose

This report summarizes cumulative model, prediction, market-adjusted, and trading-volume performance history.

It is designed to track whether the project is accumulating enough evaluated cases to support better model training and recommendation logic.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary Metrics

- ML dataset rows: **36261**
- Error-note rows: **9822**
- Market-adjusted evaluation rows: **9588**
- Market-adjusted score rows: **9588**
- Trading volume score rows: **3972821**

- Prediction success: **3489**
- Prediction failure: **4068**
- Prediction pending: **2265**
- Prediction evaluated: **7557**
- Prediction success rate: **46.17%**

- Market-adjusted success: **0**
- Market-adjusted failure: **0**
- Market-driven weak success: **0**
- Market-adjusted pending: **2031**

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
count       4068
Name: 0, dtype: object |
| count    success
count       3489
Name: 1, dtype: object |
| count    pending
count       2265
Name: 2, dtype: object |

## Market-Adjusted Result Counts

| count |
|---|
| count    market_data_missing
count                   7557
Name: 0, dtype: object |
| count    pending
count       2031
Name: 1, dtype: object |

## Trading Volume Adjustment Counts

| count |
|---|
| count    neutral_volume_adjustment
count                      3972821
Name: 0, dtype: object |

## Event-Type Performance Summary

| event_type | total | success | failure | pending | evaluated | success_rate |
|---|---|---|---|---|---|---|
| paid_in_capital_increase | 2482 | 1137 | 825 | 520 | 1962 | 57.95% |
| major_shareholder_change | 2427 | 682 | 1112 | 633 | 1794 | 38.02% |
| supply_contract | 1465 | 360 | 779 | 326 | 1139 | 31.61% |
| convertible_bond | 1303 | 557 | 413 | 333 | 970 | 57.42% |
| merger | 591 | 166 | 329 | 96 | 495 | 33.54% |
| lawsuit | 497 | 211 | 165 | 121 | 376 | 56.12% |
| investment_decision | 439 | 171 | 153 | 115 | 324 | 52.78% |
| bond_with_warrant | 145 | 53 | 80 | 12 | 133 | 39.85% |
| disclosure_violation | 189 | 51 | 68 | 70 | 119 | 42.86% |
| bonus_issue | 105 | 42 | 60 | 3 | 102 | 41.18% |
| spin_off | 117 | 44 | 41 | 32 | 85 | 51.76% |
| earnings_guidance | 62 | 15 | 43 | 4 | 58 | 25.86% |

## Automation History

| run_date | generated_at | raw_dart_rows | parsed_dart_rows | selected_event_rows | scored_event_rows | news_feature_rows | error_note_rows | ml_dataset_rows | pending_rows | success_rows | failure_rows | trainable_rows | baseline_model_report_exists | automation_status_report_exists | raw_dart_file | ml_dataset_file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-09 | N/A | 508 | 508 | 53 | 53 | 53 | 135 | 499 | 0 | 145 | 354 | 499 | True | True | data/raw/dart_disclosures_20260908.csv | data/processed/ml_dataset_20260909.csv |
| 2026-09-10 | N/A | 525 | 525 | 68 | 68 | 68 | 228 | 112 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260909.csv | data/processed/ml_dataset_20260910.csv |
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

## Interpretation

- A high pending count means the system needs more next-trading-day price data before performance can be judged.
- A low evaluated count means the model should remain conservative.
- Market-adjusted success is more meaningful than simple absolute-return success.
- Trading-volume score adjustment is useful only when enough price and volume history is available.
- The main goal at this stage is data accumulation and evaluation structure, not live trading performance.

## Next Step

The next step is to prepare the final MVP summary and clean up the README after Day 30.
