# Volume + Market-Adjusted Daily Candidate Report - 2026-11-24

Generated at: 2026-11-24 06:54:29

ML dataset source: `data/processed/ml_dataset_20261124.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261124.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20261124.csv`

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

- Total rows: **825**
- risk_or_avoid_review: **592**
- strong_volume_market_adjusted_candidate: **136**
- volatile_watchlist: **64**
- positive_candidate: **26**
- watchlist_candidate: **7**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 420770 | 기가비스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 206400 | 아인스팩씨엔에스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 206400 | 아인스팩씨엔에스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 417860 | 오브젠 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 272210 | 한화시스템 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 047810 | 한국항공우주 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 475230 | 엔알비 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 003480 | 한진중공업홀딩스 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 006360 | GS건설 | investment_decision | volatile | failure | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 006360 | GS건설 | investment_decision | volatile | failure | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 0153R0 | 바로팜 | investment_decision | volatile | failure | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 006360 | GS건설 | investment_decision | volatile | failure | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 006360 | GS건설 | investment_decision | volatile | failure | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 329180 | HD현대중공업 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 329180 | HD현대중공업 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 329180 | HD현대중공업 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 004960 | 한신공영 | investment_decision | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 329180 | HD현대중공업 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 053210 | 케이티스카이라이프 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 006880 | 신송홀딩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 006880 | 신송홀딩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 006880 | 신송홀딩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 013580 | 계룡건설산업 | investment_decision | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 006880 | 신송홀딩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 320000 | 한울반도체 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 028260 | 삼성물산 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 262260 | 에이프로 | merger | volatile | success | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 262260 | 에이프로 | merger | volatile | success | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 015230 | 대창단조 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 015230 | 대창단조 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 021050 | 서원 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 015360 | INVENI | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 015360 | INVENI | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 015360 | INVENI | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 145270 | 케이탑리츠 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | success | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
