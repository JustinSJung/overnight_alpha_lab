# Volume + Market-Adjusted Daily Candidate Report - 2026-07-20

Generated at: 2026-07-20 14:08:03

ML dataset source: `data/processed/ml_dataset_20260720.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260720.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260720.csv`

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

- Total rows: **39**
- risk_or_avoid_review: **24**
- strong_volume_market_adjusted_candidate: **12**
- positive_candidate: **2**
- watchlist_candidate: **1**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 389680 | 유디엠텍 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 431190 | 케이쓰리아이 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 144510 | 지씨셀 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 81.00 | 0.00 | 0.00 | 81.00 | N/A | N/A | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 80.00 | 0.00 | 0.00 | 80.00 | N/A | N/A | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 80.00 | 0.00 | 0.00 | 80.00 | N/A | N/A | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 80.00 | 0.00 | 0.00 | 80.00 | N/A | N/A | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 80.00 | 0.00 | 0.00 | 80.00 | N/A | N/A | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | merger | volatile | pending | pending | insufficient_volume_baseline | 71.00 | 0.00 | 0.00 | 71.00 | N/A | N/A | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | merger | volatile | pending | pending | insufficient_volume_baseline | 71.00 | 0.00 | 0.00 | 71.00 | N/A | N/A | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | merger | volatile | pending | pending | insufficient_volume_baseline | 71.00 | 0.00 | 0.00 | 71.00 | N/A | N/A | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | merger | volatile | pending | pending | insufficient_volume_baseline | 71.00 | 0.00 | 0.00 | 71.00 | N/A | N/A | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | merger | volatile | pending | pending | insufficient_volume_baseline | 71.00 | 0.00 | 0.00 | 71.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 078350 | 한양디지텍 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 033310 | 엠투엔 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 055550 | 신한지주 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

No candidates in this section.

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -15.00 | 0.00 | 0.00 | -15.00 | N/A | N/A | N/A |
| 1970-01-01 | 018700 | 졸스 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -35.00 | 0.00 | 0.00 | -35.00 | N/A | N/A | N/A |
| 1970-01-01 | 018700 | 졸스 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -35.00 | 0.00 | 0.00 | -35.00 | N/A | N/A | N/A |
| 1970-01-01 | 018700 | 졸스 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -35.00 | 0.00 | 0.00 | -35.00 | N/A | N/A | N/A |
| 1970-01-01 | 018700 | 졸스 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -35.00 | 0.00 | 0.00 | -35.00 | N/A | N/A | N/A |
| 1970-01-01 | 018700 | 졸스 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 018700 | 졸스 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 018700 | 졸스 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 018700 | 졸스 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 087260 | 모바일어플라이언스 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 087260 | 모바일어플라이언스 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 087260 | 모바일어플라이언스 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 005710 | 대원산업 | lawsuit | negative | pending | pending | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 290720 | 푸드나무 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 052770 | 아이톡시 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 052770 | 아이톡시 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 052770 | 아이톡시 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
