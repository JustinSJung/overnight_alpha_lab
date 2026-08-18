# Volume + Market-Adjusted Daily Candidate Report - 2026-08-18

Generated at: 2026-08-18 22:47:59

ML dataset source: `data/processed/ml_dataset_20260818.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260818.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260818.csv`

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

- Total rows: **34**
- risk_or_avoid_review: **20**
- strong_volume_market_adjusted_candidate: **7**
- positive_candidate: **5**
- watchlist_candidate: **2**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 010960 | 삼호개발 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 009410 | 태영건설 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 363280 | 티와이홀딩스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 90.00 | 0.00 | 0.00 | 90.00 | N/A | N/A | N/A |
| 1970-01-01 | 095270 | 웨이브일렉트로 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 85.00 | 0.00 | 0.00 | 85.00 | N/A | N/A | N/A |
| 1970-01-01 | 0009K0 | 에임드바이오 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 76.00 | 0.00 | 0.00 | 76.00 | N/A | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 61.00 | 0.00 | 0.00 | 61.00 | N/A | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 61.00 | 0.00 | 0.00 | 61.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 950220 | 네오이뮨텍 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 001740 | SK네트웍스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 001740 | SK네트웍스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 033310 | 엠투엔 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 196450 | 코아시아씨엠 | spin_off | volatile | pending | pending | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 000950 | 전방 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 000950 | 전방 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

No candidates in this section.

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 033540 | 파라텍 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 294090 | 이오플로우 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 062970 | 한국첨단소재 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 062970 | 한국첨단소재 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 089230 | THE E&M | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -75.00 | 0.00 | 0.00 | -75.00 | N/A | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -75.00 | 0.00 | 0.00 | -75.00 | N/A | N/A | N/A |
| 1970-01-01 | 038880 | 아이에이 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -80.00 | 0.00 | 0.00 | -80.00 | N/A | N/A | N/A |
| 1970-01-01 | 038880 | 아이에이 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -80.00 | 0.00 | 0.00 | -80.00 | N/A | N/A | N/A |
| 1970-01-01 | 038880 | 아이에이 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -80.00 | 0.00 | 0.00 | -80.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
