# Volume + Market-Adjusted Daily Candidate Report - 2026-11-27

Generated at: 2026-11-27 05:32:03

ML dataset source: `data/processed/ml_dataset_20261127.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261127.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20261127.csv`

## Purpose

This report applies both market-adjusted score adjustments and trading volume score adjustments to daily candidate scoring.

It is a v3 candidate report for comparison and does not replace the main recommender yet.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Score Formula

```text
base_recommendation_score_v3
+ market_adjusted_score_adjustment
+ trading_volume_score_adjustment
= final_volume_market_adjusted_score
```

## Summary

- Total rows: **723**
- risk_or_avoid_review: **571**
- strong_volume_market_adjusted_candidate: **109**
- positive_candidate: **20**
- watchlist_candidate: **13**
- volatile_watchlist: **10**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 046940 | 우원개발 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 165.00 | 0.00 | 0.00 | 165.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 090080 | 평화산업 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 004990 | 롯데지주 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 090080 | 평화산업 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 004990 | 롯데지주 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 090080 | 평화산업 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 021240 | 코웨이 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 021240 | 코웨이 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 000590 | CS홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 021050 | 서원 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 000590 | CS홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 003200 | 일신방직 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 331920 | 셀레믹스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 331920 | 셀레믹스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 331920 | 셀레믹스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 331920 | 셀레믹스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 331920 | 셀레믹스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 331920 | 셀레믹스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 331920 | 셀레믹스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 331920 | 셀레믹스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 331920 | 셀레믹스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 008870 | 금비 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 008870 | 금비 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 033270 | 유나이티드 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 033270 | 유나이티드 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 362990 | 드림인사이트 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
