# Market-Adjusted Daily Candidate Report - 2026-09-14

Generated at: 2026-09-14 00:59:51

ML dataset source: `data/processed/ml_dataset_20260914.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260914.csv`

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

- Total rows: **321**
- risk_or_avoid_review: **240**
- positive_candidate: **53**
- volatile_watchlist: **15**
- watchlist_candidate: **13**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 189300 | 인텔리안테크 | supply_contract | positive | success | market_data_missing | 175.00 | 0.00 | 175.00 | N/A |
| 1970-01-01 | 028050 | 삼성E&A | supply_contract | positive | failure | market_data_missing | 155.00 | 0.00 | 155.00 | N/A |
| 1970-01-01 | 012450 | 한화에어로스페이스 | supply_contract | positive | success | market_data_missing | 155.00 | 0.00 | 155.00 | N/A |
| 1970-01-01 | 383310 | 에코프로에이치엔 | supply_contract | positive | failure | market_data_missing | 145.00 | 0.00 | 145.00 | N/A |
| 1970-01-01 | 119850 | 지엔씨에너지 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 090430 | 아모레퍼시픽 | earnings_guidance | neutral_positive | success | market_data_missing | 138.00 | 0.00 | 138.00 | N/A |
| 1970-01-01 | 090430 | 아모레퍼시픽 | earnings_guidance | neutral_positive | success | market_data_missing | 138.00 | 0.00 | 138.00 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | supply_contract | positive | failure | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | supply_contract | positive | failure | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | supply_contract | positive | failure | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | supply_contract | positive | failure | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 070590 | 인티큐브 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | supply_contract | positive | failure | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 005960 | 동부건설 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 101680 | 한국정밀기계 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 101680 | 한국정밀기계 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 101680 | 한국정밀기계 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 071950 | 코아스 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 272210 | 한화시스템 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 391710 | 코닉오토메이션 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 006340 | 대원전선 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 006340 | 대원전선 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 001570 | 금양 | spin_off | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 006650 | 대한유화 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 068290 | 삼성출판사 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 023530 | 롯데쇼핑 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 023530 | 롯데쇼핑 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 004770 | 써니전자 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 025770 | 한국정보통신 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 025770 | 한국정보통신 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 259960 | 크래프톤 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 259960 | 크래프톤 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 259960 | 크래프톤 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 011090 | 에넥스 | investment_decision | volatile | success | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 011090 | 에넥스 | investment_decision | volatile | success | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 011090 | 에넥스 | investment_decision | volatile | success | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 011090 | 에넥스 | investment_decision | volatile | success | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 011090 | 에넥스 | investment_decision | volatile | success | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 011090 | 에넥스 | investment_decision | volatile | success | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 383800 | LX홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 383800 | LX홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 383800 | LX홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 383800 | LX홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 050090 | 비케이홀딩스 | paid_in_capital_increase | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 215570 | 크로넥스 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 064800 | 포니링크 | lawsuit | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 003620 | KG모빌리티 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 317770 | 엑스페릭스 | convertible_bond | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 317770 | 엑스페릭스 | convertible_bond | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 380540 | 옵티코어 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 317770 | 엑스페릭스 | convertible_bond | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 317770 | 엑스페릭스 | convertible_bond | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 900100 | 파이온엑스 | paid_in_capital_increase | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 340360 | 다보링크 | convertible_bond | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 079190 | 케스피온 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 001210 | 금호전기 | convertible_bond | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 001360 | 삼성제약 | paid_in_capital_increase | negative | failure | market_data_missing | -65.00 | 0.00 | -65.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
