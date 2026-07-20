# Market-Adjusted Daily Candidate Report - 2026-07-20

Generated at: 2026-07-20 21:24:59

ML dataset source: `data/processed/ml_dataset_20260720.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260720.csv`

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

- Total rows: **39**
- risk_or_avoid_review: **24**
- positive_candidate: **14**
- watchlist_candidate: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 389680 | 유디엠텍 | supply_contract | positive | pending | pending | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 431190 | 케이쓰리아이 | supply_contract | positive | pending | pending | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 144510 | 지씨셀 | investment_decision | volatile | pending | pending | 81.00 | 0.00 | 81.00 | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | supply_contract | positive | pending | pending | 75.00 | 0.00 | 75.00 | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | supply_contract | positive | pending | pending | 75.00 | 0.00 | 75.00 | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | supply_contract | positive | pending | pending | 75.00 | 0.00 | 75.00 | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | supply_contract | positive | pending | pending | 75.00 | 0.00 | 75.00 | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | merger | volatile | pending | pending | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | merger | volatile | pending | pending | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | merger | volatile | pending | pending | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | merger | volatile | pending | pending | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | merger | volatile | pending | pending | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 033310 | 엠투엔 | major_shareholder_change | volatile | pending | pending | 56.00 | 0.00 | 56.00 | N/A |
| 1970-01-01 | 078350 | 한양디지텍 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 055550 | 신한지주 | major_shareholder_change | volatile | pending | pending | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | pending | pending | -15.00 | 0.00 | -15.00 | N/A |
| 1970-01-01 | 005710 | 대원산업 | lawsuit | negative | pending | pending | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 018700 | 졸스 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 018700 | 졸스 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 018700 | 졸스 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 018700 | 졸스 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 087260 | 모바일어플라이언스 | disclosure_violation | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 087260 | 모바일어플라이언스 | disclosure_violation | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 290720 | 푸드나무 | paid_in_capital_increase | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 087260 | 모바일어플라이언스 | disclosure_violation | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 052770 | 아이톡시 | disclosure_violation | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 052770 | 아이톡시 | disclosure_violation | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 052770 | 아이톡시 | disclosure_violation | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 018700 | 졸스 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 018700 | 졸스 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 018700 | 졸스 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 018700 | 졸스 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 255220 | SG | paid_in_capital_increase | negative | pending | pending | -75.00 | 0.00 | -75.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
