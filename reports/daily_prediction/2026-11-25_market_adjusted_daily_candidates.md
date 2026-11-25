# Market-Adjusted Daily Candidate Report - 2026-11-25

Generated at: 2026-11-25 05:30:52

ML dataset source: `data/processed/ml_dataset_20261125.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261125.csv`

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

- Total rows: **468**
- risk_or_avoid_review: **407**
- positive_candidate: **45**
- watchlist_candidate: **12**
- volatile_watchlist: **4**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 122640 | 예스티 | supply_contract | positive | failure | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 253590 | 네오셈 | supply_contract | positive | failure | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 086390 | 유니테스트 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 007820 | 엠엑스로보틱스 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 038870 | 에코심플렉스 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 010960 | 삼호개발 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 028050 | 삼성E&A | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | success | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | success | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | success | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 013580 | 계룡건설산업 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | success | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 456040 | OCI | investment_decision | volatile | failure | market_data_missing | 91.00 | 0.00 | 91.00 | N/A |
| 1970-01-01 | 052690 | 한전기술 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 126720 | 수산인더스트리 | supply_contract | positive | failure | market_data_missing | 80.00 | 0.00 | 80.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 267270 | HD건설기계 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 267270 | HD건설기계 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 021050 | 서원 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 033270 | 유나이티드 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 033270 | 유나이티드 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 347770 | 핌스 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 019210 | 와이지-원 | major_shareholder_change | volatile | failure | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
