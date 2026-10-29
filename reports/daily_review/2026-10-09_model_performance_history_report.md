# Model Performance History Report - 2026-10-09

Generated at: 2026-10-09 02:47:48

## Purpose

This report summarizes cumulative model, prediction, market-adjusted, and trading-volume performance history.

It is designed to track whether the project is accumulating enough evaluated cases to support better model training and recommendation logic.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary Metrics

- ML dataset rows: **27378**
- Error-note rows: **7237**
- Market-adjusted evaluation rows: **7003**
- Market-adjusted score rows: **7003**
- Trading volume score rows: **2935081**

- Prediction success: **2190**
- Prediction failure: **2787**
- Prediction pending: **2260**
- Prediction evaluated: **4977**
- Prediction success rate: **44.00%**

- Market-adjusted success: **0**
- Market-adjusted failure: **0**
- Market-driven weak success: **0**
- Market-adjusted pending: **2026**

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
count       2787
Name: 0, dtype: object |
| count    pending
count       2260
Name: 1, dtype: object |
| count    success
count       2190
Name: 2, dtype: object |

## Market-Adjusted Result Counts

| count |
|---|
| count    market_data_missing
count                   4977
Name: 0, dtype: object |
| count    pending
count       2026
Name: 1, dtype: object |

## Trading Volume Adjustment Counts

| count |
|---|
| count    neutral_volume_adjustment
count                      2935081
Name: 0, dtype: object |

## Event-Type Performance Summary

| event_type | total | success | failure | pending | evaluated | success_rate |
|---|---|---|---|---|---|---|
| paid_in_capital_increase | 1903 | 813 | 572 | 518 | 1385 | 58.70% |
| major_shareholder_change | 1815 | 402 | 780 | 633 | 1182 | 34.01% |
| supply_contract | 1050 | 210 | 514 | 326 | 724 | 29.01% |
| convertible_bond | 965 | 336 | 297 | 332 | 633 | 53.08% |
| merger | 359 | 52 | 212 | 95 | 264 | 19.70% |
| investment_decision | 366 | 131 | 120 | 115 | 251 | 52.19% |
| lawsuit | 369 | 141 | 108 | 120 | 249 | 56.63% |
| bonus_issue | 93 | 41 | 49 | 3 | 90 | 45.56% |
| disclosure_violation | 147 | 38 | 39 | 70 | 77 | 49.35% |
| bond_with_warrant | 77 | 6 | 59 | 12 | 65 | 9.23% |
| spin_off | 87 | 18 | 37 | 32 | 55 | 32.73% |
| earnings_guidance | 6 | 2 | 0 | 4 | 2 | 100.00% |

## Automation History

| run_date | generated_at | raw_dart_rows | parsed_dart_rows | selected_event_rows | scored_event_rows | news_feature_rows | error_note_rows | ml_dataset_rows | pending_rows | success_rows | failure_rows | trainable_rows | baseline_model_report_exists | automation_status_report_exists | raw_dart_file | ml_dataset_file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-20 | N/A | 100 | 100 | 18 | 18 | 18 | 39 | 227 | 227 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260820.csv | data/processed/ml_dataset_20260820.csv |
| 2026-08-24 | N/A | 100 | 100 | 26 | 26 | 26 | 78 | 327 | 327 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260824.csv | data/processed/ml_dataset_20260824.csv |
| 2026-08-25 | N/A | 100 | 100 | 11 | 11 | 11 | 15 | 15 | 15 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260825.csv | data/processed/ml_dataset_20260825.csv |
| 2026-08-27 | N/A | 100 | 100 | 4 | 4 | 4 | 4 | 4 | 4 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260827.csv | data/processed/ml_dataset_20260827.csv |
| 2026-08-28 | N/A | 100 | 100 | 4 | 4 | 4 | 4 | 4 | 4 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260828.csv | data/processed/ml_dataset_20260828.csv |
| 2026-08-29 | N/A | 2145 | 2145 | 100 | 100 | 100 | 292 | 951 | 951 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260828.csv | data/processed/ml_dataset_20260829.csv |
| 2026-08-31 | N/A | 2145 | 2145 | 100 | 100 | 100 | 292 | 951 | 0 | 142 | 809 | 951 | True | True | data/raw/dart_disclosures_20260828.csv | data/processed/ml_dataset_20260831.csv |
| 2026-09-01 | N/A | 1728 | 1728 | 115 | 115 | 115 | 303 | 945 | 0 | 523 | 422 | 945 | True | True | data/raw/dart_disclosures_20260831.csv | data/processed/ml_dataset_20260901.csv |
| 2026-09-02 | N/A | 530 | 530 | 105 | 105 | 105 | 361 | 184 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20260901.csv | data/processed/ml_dataset_20260902.csv |
| 2026-09-03 | N/A | 450 | 450 | 60 | 60 | 60 | 250 | 2275 | 0 | 2003 | 272 | 2275 | True | True | data/raw/dart_disclosures_20260902.csv | data/processed/ml_dataset_20260903.csv |
| 2026-09-04 | N/A | 461 | 461 | 68 | 68 | 68 | 275 | 1547 | 0 | 1172 | 375 | 1547 | True | True | data/raw/dart_disclosures_20260903.csv | data/processed/ml_dataset_20260904.csv |
| 2026-09-07 | N/A | 637 | 637 | 77 | 77 | 77 | 191 | 446 | 0 | 156 | 290 | 446 | True | True | data/raw/dart_disclosures_20260904.csv | data/processed/ml_dataset_20260907.csv |
| 2026-09-08 | N/A | 454 | 454 | 63 | 63 | 63 | 147 | 441 | 0 | 302 | 139 | 441 | True | True | data/raw/dart_disclosures_20260907.csv | data/processed/ml_dataset_20260908.csv |
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

## Interpretation

- A high pending count means the system needs more next-trading-day price data before performance can be judged.
- A low evaluated count means the model should remain conservative.
- Market-adjusted success is more meaningful than simple absolute-return success.
- Trading-volume score adjustment is useful only when enough price and volume history is available.
- The main goal at this stage is data accumulation and evaluation structure, not live trading performance.

## Next Step

The next step is to prepare the final MVP summary and clean up the README after Day 30.
