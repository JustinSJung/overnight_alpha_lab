# Market-Adjusted Daily Candidate Report - 2026-09-29

Generated at: 2026-09-29 03:31:39

ML dataset source: `data/processed/ml_dataset_20260929.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260929.csv`

## Purpose

This report applies market-adjusted score adjustments to daily candidate scoring.

It is a safer v2 report and does not replace the existing daily stock recommender yet.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Score Formula

```text
base_recommendation_score_v2
+ market_adjusted_score_adjustment
= final_market_adjusted_score
```

## Summary

- Total rows: **1470**
- risk_or_avoid_review: **1214**
- positive_candidate: **240**
- watchlist_candidate: **15**
- volatile_watchlist: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 950250 | 테라뷰 | supply_contract | positive | success | market_data_missing | 150.00 | 0.00 | 150.00 | N/A |
| 1970-01-01 | 327260 | RF머트리얼즈 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 066980 | 한성크린텍 | supply_contract | positive | failure | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 003380 | 하림지주 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 109670 | 씨싸이트 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 109670 | 씨싸이트 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 109670 | 씨싸이트 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 102460 | 이연제약 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 102460 | 이연제약 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 102460 | 이연제약 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 102460 | 이연제약 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 402030 | 코난테크놀로지 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 102460 | 이연제약 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 102460 | 이연제약 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 092600 | 앤씨앤 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 145270 | 케이탑리츠 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 092600 | 앤씨앤 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 092600 | 앤씨앤 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 092600 | 앤씨앤 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 206400 | 베노티앤알 | major_shareholder_change | volatile | success | market_data_missing | -4.00 | 0.00 | -4.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 054220 | 비츠로시스 | convertible_bond | negative | success | market_data_missing | -15.00 | 0.00 | -15.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 082210 | 옵트론텍 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
