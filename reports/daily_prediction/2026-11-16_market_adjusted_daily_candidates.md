# Market-Adjusted Daily Candidate Report - 2026-11-16

Generated at: 2026-11-16 02:53:19

ML dataset source: `data/processed/ml_dataset_20261116.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261116.csv`

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

- Total rows: **131**
- risk_or_avoid_review: **55**
- positive_candidate: **34**
- watchlist_candidate: **29**
- volatile_watchlist: **13**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 419080 | 엔젯 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 049080 | 기가레인 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 288180 | 케이피항공산업 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 254120 | 자비스 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 282880 | 코윈로보틱스 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 321820 | 아티스트컴퍼니 | supply_contract | positive | success | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 321820 | 아티스트컴퍼니 | supply_contract | positive | success | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 282880 | 코윈로보틱스 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 383930 | 디티앤씨알오 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 375500 | DL이앤씨 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 383930 | 디티앤씨알오 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 180060 | 탑선 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 180060 | 탑선 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 375500 | DL이앤씨 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 180060 | 탑선 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 180060 | 탑선 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 000210 | DL | supply_contract | positive | failure | market_data_missing | 80.00 | 0.00 | 80.00 | N/A |
| 1970-01-01 | 006120 | SK디스커버리 | investment_decision | volatile | success | market_data_missing | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 006120 | SK디스커버리 | investment_decision | volatile | success | market_data_missing | 71.00 | 0.00 | 71.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 015230 | 대창단조 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 015230 | 대창단조 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 015230 | 대창단조 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 087260 | 모바일어플라이언스 | investment_decision | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 023960 | 에쓰씨엔지니어링 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 023960 | 에쓰씨엔지니어링 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 017800 | 현대엘리베이터 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 017800 | 현대엘리베이터 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 017800 | 현대엘리베이터 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 004830 | 덕성 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 017800 | 현대엘리베이터 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 087260 | 모바일어플라이언스 | investment_decision | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 023960 | 에쓰씨엔지니어링 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 017800 | 현대엘리베이터 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 087260 | 모바일어플라이언스 | investment_decision | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 087260 | 모바일어플라이언스 | investment_decision | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 087260 | 모바일어플라이언스 | investment_decision | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 004410 | 서울식품공업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 317530 | 에피소드컴퍼니 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 055550 | 신한지주 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 055550 | 신한지주 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 055550 | 신한지주 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 032790 | 엠젠솔루션 | convertible_bond | negative | success | market_data_missing | -5.00 | 0.00 | -5.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | convertible_bond | negative | success | market_data_missing | -5.00 | 0.00 | -5.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | convertible_bond | negative | success | market_data_missing | -5.00 | 0.00 | -5.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | convertible_bond | negative | success | market_data_missing | -5.00 | 0.00 | -5.00 | N/A |
| 1970-01-01 | 182360 | 큐브엔터 | convertible_bond | negative | failure | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 182360 | 큐브엔터 | convertible_bond | negative | failure | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 058730 | 다스코 | bond_with_warrant | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 304360 | 에스바이오메딕스 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 001210 | 금호전기 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 340810 | 시선AI | convertible_bond | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | convertible_bond | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | convertible_bond | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | convertible_bond | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | convertible_bond | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | bond_with_warrant | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | bond_with_warrant | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | bond_with_warrant | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
