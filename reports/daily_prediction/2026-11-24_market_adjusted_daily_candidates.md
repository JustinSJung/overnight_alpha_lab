# Market-Adjusted Daily Candidate Report - 2026-11-24

Generated at: 2026-11-24 06:54:18

ML dataset source: `data/processed/ml_dataset_20261124.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261124.csv`

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

- Total rows: **825**
- risk_or_avoid_review: **592**
- positive_candidate: **162**
- volatile_watchlist: **64**
- watchlist_candidate: **7**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 420770 | 기가비스 | supply_contract | positive | failure | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 206400 | 아인스팩씨엔에스 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 206400 | 아인스팩씨엔에스 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 417860 | 오브젠 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 272210 | 한화시스템 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 047810 | 한국항공우주 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 475230 | 엔알비 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 003480 | 한진중공업홀딩스 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 015230 | 대창단조 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 015230 | 대창단조 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 021050 | 서원 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 015360 | INVENI | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 015360 | INVENI | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 015360 | INVENI | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 145270 | 케이탑리츠 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
