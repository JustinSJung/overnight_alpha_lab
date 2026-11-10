# Market-Adjusted Daily Candidate Report - 2026-11-10

Generated at: 2026-11-10 05:37:09

ML dataset source: `data/processed/ml_dataset_20261110.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261110.csv`

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

- Total rows: **101**
- risk_or_avoid_review: **61**
- positive_candidate: **24**
- watchlist_candidate: **12**
- volatile_watchlist: **4**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 365330 | 에스와이스틸텍 | supply_contract | positive | nan | market_data_missing | 165.00 | 0.00 | 165.00 | N/A |
| 1970-01-01 | 064290 | 인텍플러스 | supply_contract | positive | nan | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 002460 | HS화성 | supply_contract | positive | nan | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 058730 | 다스코 | supply_contract | positive | nan | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 071970 | HD현대마린엔진 | supply_contract | positive | nan | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 171090 | 선익시스템 | supply_contract | positive | nan | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 083640 | 인콘 | supply_contract | positive | nan | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 013580 | 계룡건설산업 | supply_contract | positive | nan | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | nan | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 329180 | HD현대중공업 | supply_contract | positive | nan | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 006360 | GS건설 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 296640 | 이노에이엑스 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | investment_decision | volatile | nan | market_data_missing | 91.00 | 0.00 | 91.00 | N/A |
| 1970-01-01 | 005300 | 롯데칠성음료 | earnings_guidance | neutral_positive | nan | market_data_missing | 83.00 | 0.00 | 83.00 | N/A |
| 1970-01-01 | 000210 | DL | spin_off | volatile | nan | market_data_missing | 81.00 | 0.00 | 81.00 | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | supply_contract | positive | nan | market_data_missing | 80.00 | 0.00 | 80.00 | N/A |
| 1970-01-01 | 012630 | HDC | investment_decision | volatile | nan | market_data_missing | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 005940 | NH투자증권 | major_shareholder_change | volatile | nan | market_data_missing | 61.00 | 0.00 | 61.00 | N/A |
| 1970-01-01 | 950260 | 인제니아테라퓨틱스 | investment_decision | volatile | nan | market_data_missing | 56.00 | 0.00 | 56.00 | N/A |
| 1970-01-01 | 000590 | CS홀딩스 | major_shareholder_change | volatile | nan | market_data_missing | 46.00 | 0.00 | 46.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 000220 | 유유제약 | major_shareholder_change | volatile | nan | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 005830 | DB손해보험 | major_shareholder_change | volatile | nan | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 317240 | TS트릴리온 | spin_off | volatile | nan | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 005900 | 동양건설산업 | major_shareholder_change | volatile | nan | nan | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 090430 | 아모레퍼시픽 | major_shareholder_change | volatile | nan | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 100840 | SNT에너지 | major_shareholder_change | volatile | nan | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | nan | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 244920 | 에이플러스에셋 | major_shareholder_change | volatile | nan | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 006650 | 대한유화 | major_shareholder_change | volatile | nan | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | nan | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 376930 | 노을 | major_shareholder_change | volatile | nan | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 001450 | 현대해상 | major_shareholder_change | volatile | nan | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 268280 | 미원에스씨 | major_shareholder_change | volatile | nan | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | nan | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 005250 | 녹십자홀딩스 | major_shareholder_change | volatile | nan | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 033250 | 체시스 | investment_decision | volatile | nan | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 083640 | 인콘 | convertible_bond | negative | nan | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | nan | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 088280 | 쏘닉스 | convertible_bond | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 061040 | 알에프텍 | convertible_bond | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 290650 | 엘앤씨바이오 | convertible_bond | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 104040 | 디에스엠 | convertible_bond | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 104040 | 디에스엠 | convertible_bond | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 104040 | 디에스엠 | convertible_bond | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 104040 | 디에스엠 | convertible_bond | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 104040 | 디에스엠 | convertible_bond | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 010130 | 고려아연 | lawsuit | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | paid_in_capital_increase | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 060900 | 에이전트AI | convertible_bond | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 104040 | 디에스엠 | convertible_bond | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 104040 | 디에스엠 | convertible_bond | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 104040 | 디에스엠 | convertible_bond | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | nan | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | nan | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
