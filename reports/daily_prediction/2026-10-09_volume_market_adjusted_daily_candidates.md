# Volume + Market-Adjusted Daily Candidate Report - 2026-10-09

Generated at: 2026-10-09 02:47:33

ML dataset source: `data/processed/ml_dataset_20261009.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261009.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20261009.csv`

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

- Total rows: **2159**
- risk_or_avoid_review: **1928**
- volatile_watchlist: **144**
- strong_volume_market_adjusted_candidate: **44**
- positive_candidate: **27**
- watchlist_candidate: **16**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 147760 | 피엠티 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 145.00 | 0.00 | 0.00 | 145.00 | N/A | N/A | N/A |
| 1970-01-01 | 372170 | 윤성에프앤씨 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 003520 | 영진약품 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 046940 | 우원개발 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 101970 | 우양에이치씨 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 082740 | 한화엔진 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 007820 | 엠엑스로보틱스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 010400 | 우진아이엔에스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 010400 | 우진아이엔에스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 058730 | 다스코 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 399720 | 가온칩스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 440110 | 파두 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 440110 | 파두 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 440110 | 파두 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 043910 | 자연과환경 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 440110 | 파두 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 043910 | 자연과환경 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 440110 | 파두 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 047810 | 한국항공우주 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 348370 | 엔켐 | merger | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 348370 | 엔켐 | merger | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 348370 | 엔켐 | merger | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 066410 | 버킷스튜디오 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 064820 | 케이프 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 043340 | 에쎈테크 | spin_off | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | spin_off | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 226950 | 올릭스 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 185750 | 종근당 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 084870 | 티비에이치글로벌 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 185750 | 종근당 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 185750 | 종근당 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 185750 | 종근당 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 185750 | 종근당 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 084870 | 티비에이치글로벌 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 005610 | 삼립 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 005610 | 삼립 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 004770 | 써니전자 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 036570 | NC | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 026960 | 동서 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 026960 | 동서 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 026960 | 동서 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 003530 | 한화투자증권 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 065650 | 하이퍼코퍼레이션 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
