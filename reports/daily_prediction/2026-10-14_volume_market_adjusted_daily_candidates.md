# Volume + Market-Adjusted Daily Candidate Report - 2026-10-14

Generated at: 2026-10-14 02:04:00

ML dataset source: `data/processed/ml_dataset_20261014.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261014.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20261014.csv`

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

- Total rows: **783**
- risk_or_avoid_review: **387**
- strong_volume_market_adjusted_candidate: **379**
- positive_candidate: **6**
- volatile_watchlist: **6**
- watchlist_candidate: **5**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 011560 | 세보엠이씨 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 145.00 | 0.00 | 0.00 | 145.00 | N/A | N/A | N/A |
| 1970-01-01 | 452450 | 피아이이 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 145.00 | 0.00 | 0.00 | 145.00 | N/A | N/A | N/A |
| 1970-01-01 | 950250 | 테라뷰 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 417200 | LS머트리얼즈 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 083930 | 아바코 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 001260 | 남광토건 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 032580 | 피델릭스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 010960 | 삼호개발 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 010120 | 엘에스일렉트릭 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 002020 | 코오롱 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 363280 | 티와이홀딩스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 009410 | 태영건설 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 103.00 | 0.00 | 0.00 | 103.00 | N/A | N/A | N/A |
| 1970-01-01 | 329180 | HD현대중공업 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 002780 | 진흥기업 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 119650 | KC코트렐 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 90.00 | 0.00 | 0.00 | 90.00 | N/A | N/A | N/A |
| 1970-01-01 | 084730 | 팅크웨어 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 85.00 | 0.00 | 0.00 | 85.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 418620 | E8 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 003580 | HLB글로벌 | merger | volatile | success | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 013520 | 화승코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 013520 | 화승코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 071950 | 코아스 | investment_decision | volatile | success | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 071950 | 코아스 | investment_decision | volatile | success | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 004970 | 신라교역 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 004970 | 신라교역 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 103140 | 풍산 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 089860 | 롯데렌탈 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 036530 | SNT홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 036530 | SNT홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 005930 | 삼성전자 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 005930 | 삼성전자 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 465770 | STX그린로지스 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -5.00 | 0.00 | 0.00 | -5.00 | N/A | N/A | N/A |
| 1970-01-01 | 011810 | STX | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 011810 | STX | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 011810 | STX | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 011810 | STX | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 011810 | STX | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 011810 | STX | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 011810 | STX | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 011810 | STX | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 011810 | STX | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 011810 | STX | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
