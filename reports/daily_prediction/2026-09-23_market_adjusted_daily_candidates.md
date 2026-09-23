# Market-Adjusted Daily Candidate Report - 2026-09-23

Generated at: 2026-09-23 02:02:21

ML dataset source: `data/processed/ml_dataset_20260923.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260923.csv`

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

- Total rows: **638**
- risk_or_avoid_review: **495**
- watchlist_candidate: **91**
- positive_candidate: **44**
- volatile_watchlist: **8**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 066980 | 한성크린텍 | supply_contract | positive | success | market_data_missing | 155.00 | 0.00 | 155.00 | N/A |
| 1970-01-01 | 003670 | 포스코퓨처엠 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 012630 | HDC | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 002460 | HS화성 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 137080 | 나래나노텍 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 148780 | 비큐AI | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 064400 | LG씨엔에스 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 017040 | 광명전기 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 025560 | 미래산업 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 003850 | 보령 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 007610 | 선도전기 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 007610 | 선도전기 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 038870 | 에코심플렉스 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 004440 | 삼일씨엔에스 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 070960 | 모나용평 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 070960 | 모나용평 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 290690 | 아리바이오홀딩스 | merger | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 290690 | 아리바이오홀딩스 | merger | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 013520 | 화승코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 480370 | 씨케이솔루션 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 480370 | 씨케이솔루션 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 290690 | 아리바이오홀딩스 | merger | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 002880 | 디와이에이 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 038620 | 위즈코프 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 119610 | 인터로조 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 181710 | NHN | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 181710 | NHN | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 003300 | 한일홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 119610 | 인터로조 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 033310 | 엠투엔 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 005830 | DB손해보험 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 005830 | DB손해보험 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 119610 | 인터로조 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 119610 | 인터로조 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 011790 | SKC | investment_decision | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 011790 | SKC | investment_decision | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 011790 | SKC | investment_decision | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 178320 | 서진시스템 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 011790 | SKC | investment_decision | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 008870 | 금비 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 008870 | 금비 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | -4.00 | 0.00 | -4.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 060900 | 에이전트AI | convertible_bond | negative | success | market_data_missing | 15.00 | 0.00 | 15.00 | N/A |
| 1970-01-01 | 474650 | 링크솔루션 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 086890 | 이수앱지스 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 357120 | 코람코라이프인프라리츠 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
