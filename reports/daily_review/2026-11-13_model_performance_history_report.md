# Model Performance History Report - 2026-11-13

Generated at: 2026-11-13 04:20:48

## Purpose

This report summarizes cumulative model, prediction, market-adjusted, and trading-volume performance history.

It is designed to track whether the project is accumulating enough evaluated cases to support better model training and recommendation logic.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary Metrics

- ML dataset rows: **45818**
- Error-note rows: **12104**
- Market-adjusted evaluation rows: **11870**
- Market-adjusted score rows: **11870**
- Trading volume score rows: **7954390**

- Prediction success: **4537**
- Prediction failure: **5296**
- Prediction pending: **2271**
- Prediction evaluated: **9833**
- Prediction success rate: **46.14%**

- Market-adjusted success: **0**
- Market-adjusted failure: **0**
- Market-driven weak success: **0**
- Market-adjusted pending: **2037**

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
count       5296
Name: 0, dtype: object |
| count    success
count       4537
Name: 1, dtype: object |
| count    pending
count       2271
Name: 2, dtype: object |

## Market-Adjusted Result Counts

| count |
|---|
| count    market_data_missing
count                   9833
Name: 0, dtype: object |
| count    pending
count       2037
Name: 1, dtype: object |

## Trading Volume Adjustment Counts

| count |
|---|
| count    neutral_volume_adjustment
count                      7954390
Name: 0, dtype: object |

## Event-Type Performance Summary

| event_type | total | success | failure | pending | evaluated | success_rate |
|---|---|---|---|---|---|---|
| major_shareholder_change | 3111 | 935 | 1542 | 634 | 2477 | 37.75% |
| paid_in_capital_increase | 2891 | 1302 | 1068 | 521 | 2370 | 54.94% |
| supply_contract | 1768 | 530 | 912 | 326 | 1442 | 36.75% |
| convertible_bond | 1543 | 692 | 518 | 333 | 1210 | 57.19% |
| merger | 858 | 352 | 410 | 96 | 762 | 46.19% |
| lawsuit | 609 | 238 | 250 | 121 | 488 | 48.77% |
| investment_decision | 592 | 244 | 233 | 115 | 477 | 51.15% |
| disclosure_violation | 214 | 59 | 85 | 70 | 144 | 40.97% |
| bond_with_warrant | 154 | 62 | 80 | 12 | 142 | 43.66% |
| spin_off | 155 | 47 | 72 | 36 | 119 | 39.50% |
| bonus_issue | 119 | 56 | 60 | 3 | 116 | 48.28% |
| earnings_guidance | 90 | 20 | 66 | 4 | 86 | 23.26% |

## Automation History

| run_date | generated_at | raw_dart_rows | parsed_dart_rows | selected_event_rows | scored_event_rows | news_feature_rows | error_note_rows | ml_dataset_rows | pending_rows | success_rows | failure_rows | trainable_rows | baseline_model_report_exists | automation_status_report_exists | raw_dart_file | ml_dataset_file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
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
| 2026-11-03 | N/A | 498 | 498 | 82 | 82 | 82 | 197 | 551 | 0 | 256 | 295 | 551 | True | True | data/raw/dart_disclosures_20261102.csv | data/processed/ml_dataset_20261103.csv |
| 2026-11-04 | N/A | 518 | 518 | 56 | 56 | 56 | 126 | 213 | 0 | 57 | 156 | 213 | True | True | data/raw/dart_disclosures_20261103.csv | data/processed/ml_dataset_20261104.csv |
| 2026-11-05 | N/A | 527 | 527 | 54 | 54 | 54 | 135 | 70 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20261104.csv | data/processed/ml_dataset_20261105.csv |
| 2026-11-06 | N/A | 760 | 760 | 67 | 67 | 67 | 274 | 1062 | 0 | 610 | 452 | 1062 | True | True | data/raw/dart_disclosures_20261105.csv | data/processed/ml_dataset_20261106.csv |
| 2026-11-09 | N/A | 642 | 642 | 78 | 78 | 78 | 202 | 818 | 0 | 378 | 440 | 818 | True | True | data/raw/dart_disclosures_20261106.csv | data/processed/ml_dataset_20261109.csv |
| 2026-11-10 | N/A | 560 | 560 | 69 | 69 | 69 | 197 | 101 | 0 | 0 | 0 | 0 | True | True | data/raw/dart_disclosures_20261109.csv | data/processed/ml_dataset_20261110.csv |
| 2026-11-11 | N/A | 620 | 620 | 78 | 78 | 78 | 206 | 1290 | 0 | 972 | 318 | 1290 | True | True | data/raw/dart_disclosures_20261110.csv | data/processed/ml_dataset_20261111.csv |
| 2026-11-12 | N/A | 588 | 588 | 62 | 62 | 62 | 146 | 434 | 0 | 184 | 250 | 434 | True | True | data/raw/dart_disclosures_20261111.csv | data/processed/ml_dataset_20261112.csv |

## Interpretation

- A high pending count means the system needs more next-trading-day price data before performance can be judged.
- A low evaluated count means the model should remain conservative.
- Market-adjusted success is more meaningful than simple absolute-return success.
- Trading-volume score adjustment is useful only when enough price and volume history is available.
- The main goal at this stage is data accumulation and evaluation structure, not live trading performance.

## Next Step

The next step is to prepare the final MVP summary and clean up the README after Day 30.
