# Market-Adjusted Daily Candidate Report - 2026-10-16

Generated at: 2026-10-16 00:50:07

ML dataset source: `data/processed/ml_dataset_20261016.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261016.csv`

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

- Total rows: **577**
- positive_candidate: **302**
- risk_or_avoid_review: **206**
- volatile_watchlist: **35**
- watchlist_candidate: **34**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 064400 | LG씨엔에스 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 064400 | LG씨엔에스 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 001440 | 대한전선 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 064400 | LG씨엔에스 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 295310 | 에이치브이엠 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 141000 | 비아트론 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 052690 | 한전기술 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 378340 | 필에너지 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 216080 | 제테마 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 216080 | 제테마 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 046970 | 우리로 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 216080 | 제테마 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 440110 | 파두 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 021320 | KCC건설 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 216080 | 제테마 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 212710 | 아이에스티이 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 475150 | SK이터닉스 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 123860 | 아나패스 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 123860 | 아나패스 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 008930 | 한미사이언스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 145270 | 케이탑리츠 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | spin_off | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 033310 | 엠투엔 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 004830 | 덕성 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 009320 | 아진전자부품 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 008870 | 금비 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 008870 | 금비 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 009320 | 아진전자부품 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 035150 | 백산 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 009320 | 아진전자부품 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 004830 | 덕성 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 035150 | 백산 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | bond_with_warrant | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | convertible_bond | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 429270 | 시지트로닉스 | paid_in_capital_increase | negative | failure | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 340360 | 다보링크 | convertible_bond | negative | failure | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 340360 | 다보링크 | convertible_bond | negative | failure | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 258050 | 테크트랜스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | convertible_bond | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | convertible_bond | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 336570 | 원텍 | disclosure_violation | negative | failure | market_data_missing | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 336570 | 원텍 | disclosure_violation | negative | failure | market_data_missing | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 247540 | 에코프로비엠 | paid_in_capital_increase | negative | failure | market_data_missing | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | paid_in_capital_increase | negative | failure | market_data_missing | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | paid_in_capital_increase | negative | failure | market_data_missing | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 009620 | 삼보산업 | paid_in_capital_increase | negative | success | market_data_missing | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 210980 | SK디앤디 | paid_in_capital_increase | negative | failure | market_data_missing | -75.00 | 0.00 | -75.00 | N/A |
| 1970-01-01 | 210980 | SK디앤디 | paid_in_capital_increase | negative | failure | market_data_missing | -75.00 | 0.00 | -75.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | bond_with_warrant | negative | failure | market_data_missing | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | bond_with_warrant | negative | failure | market_data_missing | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | bond_with_warrant | negative | failure | market_data_missing | -80.00 | 0.00 | -80.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
