# Market-Adjusted Daily Candidate Report - 2026-10-27

Generated at: 2026-10-27 02:02:54

ML dataset source: `data/processed/ml_dataset_20261027.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261027.csv`

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

- Total rows: **964**
- positive_candidate: **770**
- risk_or_avoid_review: **172**
- watchlist_candidate: **19**
- volatile_watchlist: **3**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 071970 | HD현대마린엔진 | supply_contract | positive | success | market_data_missing | 150.00 | 0.00 | 150.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 382480 | 지아이텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 200230 | 텔콘RF제약 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 294630 | 서남 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 104460 | 디와이피엔에프 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 171090 | 선익시스템 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 036190 | 금화피에스시 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 060980 | HL홀딩스 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 002020 | 코오롱 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 028260 | 삼성물산 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 028260 | 삼성물산 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 049800 | 우진플라임 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 107590 | 미원홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 049800 | 우진플라임 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 020150 | 롯데에너지머티리얼즈 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 145270 | 케이탑리츠 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 003080 | SB성보 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 070960 | 모나용평 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 070960 | 모나용평 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 311390 | 네오크레마 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 288620 | 에스프리즘 | convertible_bond | negative | success | market_data_missing | 5.00 | 0.00 | 5.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | paid_in_capital_increase | negative | failure | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 247540 | 에코프로비엠 | convertible_bond | negative | failure | market_data_missing | -15.00 | 0.00 | -15.00 | N/A |
| 1970-01-01 | 229640 | LS에코에너지 | paid_in_capital_increase | negative | failure | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 229640 | LS에코에너지 | paid_in_capital_increase | negative | failure | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 229640 | LS에코에너지 | paid_in_capital_increase | negative | failure | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
