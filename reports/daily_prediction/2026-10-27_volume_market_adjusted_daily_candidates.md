# Volume + Market-Adjusted Daily Candidate Report - 2026-10-27

Generated at: 2026-10-27 02:03:08

ML dataset source: `data/processed/ml_dataset_20261027.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261027.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20261027.csv`

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

- Total rows: **964**
- strong_volume_market_adjusted_candidate: **757**
- risk_or_avoid_review: **172**
- watchlist_candidate: **17**
- positive_candidate: **15**
- volatile_watchlist: **3**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 071970 | HD현대마린엔진 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 150.00 | 0.00 | 0.00 | 150.00 | N/A | N/A | N/A |
| 1970-01-01 | 013360 | 일성건설 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 382480 | 지아이텍 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 200230 | 텔콘RF제약 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 294630 | 서남 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 104460 | 디와이피엔에프 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 171090 | 선익시스템 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 036190 | 금화피에스시 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 060980 | HL홀딩스 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 002020 | 코오롱 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 308170 | 씨티알모빌리티 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 308170 | 씨티알모빌리티 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 003380 | 하림지주 | spin_off | volatile | failure | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 217730 | 강스템바이오텍 | investment_decision | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 000180 | 성창기업지주 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 083640 | 인콘 | investment_decision | volatile | failure | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 000180 | 성창기업지주 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 003460 | 유화증권 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 012280 | 영화금속 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 105560 | KB금융 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 105560 | KB금융 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 012280 | 영화금속 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 012280 | 영화금속 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 028260 | 삼성물산 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 028260 | 삼성물산 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 049800 | 우진플라임 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 107590 | 미원홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 049800 | 우진플라임 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 020150 | 롯데에너지머티리얼즈 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 145270 | 케이탑리츠 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 003080 | SB성보 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 070960 | 모나용평 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 070960 | 모나용평 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 311390 | 네오크레마 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 288620 | 에스프리즘 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | 5.00 | 0.00 | 0.00 | 5.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 247540 | 에코프로비엠 | convertible_bond | negative | failure | market_data_missing | insufficient_volume_baseline | -15.00 | 0.00 | 0.00 | -15.00 | N/A | N/A | N/A |
| 1970-01-01 | 229640 | LS에코에너지 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 229640 | LS에코에너지 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 229640 | LS에코에너지 | paid_in_capital_increase | negative | failure | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
