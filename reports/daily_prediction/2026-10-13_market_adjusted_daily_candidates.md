# Market-Adjusted Daily Candidate Report - 2026-10-13

Generated at: 2026-10-13 03:54:00

ML dataset source: `data/processed/ml_dataset_20261013.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261013.csv`

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

- Total rows: **441**
- risk_or_avoid_review: **282**
- positive_candidate: **141**
- watchlist_candidate: **10**
- volatile_watchlist: **8**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 215090 | 솔디펜스 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | supply_contract | positive | failure | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 274400 | 이노시뮬레이션 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 448710 | 코츠테크놀로지 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 212710 | 아이에스티이 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 019660 | 글로본 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 950250 | 테라뷰 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 004960 | 한신공영 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 178320 | 서진시스템 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 475150 | SK이터닉스 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 064290 | 인텍플러스 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 178320 | 서진시스템 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 178320 | 서진시스템 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 199480 | 뱅크웨어글로벌 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 178320 | 서진시스템 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 475150 | SK이터닉스 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 096770 | SK이노베이션 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 291810 | 핀텔 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 300080 | 플리토 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 105330 | 케이엔더블유 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 017040 | 광명전기 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 005320 | 온타이드 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 005320 | 온타이드 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 005320 | 온타이드 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 070960 | 모나용평 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 070960 | 모나용평 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 070960 | 모나용평 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 070960 | 모나용평 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 402030 | 코난테크놀로지 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 001570 | 금양 | spin_off | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 226950 | 올릭스 | investment_decision | volatile | success | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 006340 | 대원전선 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 006340 | 대원전선 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 006340 | 대원전선 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 006340 | 대원전선 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 210120 | 빅텐츠 | investment_decision | volatile | failure | market_data_missing | -19.00 | 0.00 | -19.00 | N/A |
| 1970-01-01 | 210120 | 빅텐츠 | investment_decision | volatile | failure | market_data_missing | -19.00 | 0.00 | -19.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 351320 | 넥사다이내믹스 | disclosure_violation | negative | failure | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | disclosure_violation | negative | failure | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 465770 | STX그린로지스 | convertible_bond | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 123010 | MSDI | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 484810 | 티엑스알로보틱스 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 123010 | MSDI | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 006490 | 프리티 | convertible_bond | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 006490 | 프리티 | convertible_bond | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 006490 | 프리티 | convertible_bond | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 006490 | 프리티 | convertible_bond | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | lawsuit | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 290650 | 엘앤씨바이오 | paid_in_capital_increase | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 290650 | 엘앤씨바이오 | paid_in_capital_increase | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 290650 | 엘앤씨바이오 | paid_in_capital_increase | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 290650 | 엘앤씨바이오 | paid_in_capital_increase | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | lawsuit | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | lawsuit | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | lawsuit | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 290650 | 엘앤씨바이오 | paid_in_capital_increase | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 002020 | 코오롱 | disclosure_violation | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
