# Volume + Market-Adjusted Daily Candidate Report - 2026-07-27

Generated at: 2026-07-27 23:24:33

ML dataset source: `data/processed/ml_dataset_20260727.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260727.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260727.csv`

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

- Total rows: **903**
- watchlist_candidate: **730**
- strong_volume_market_adjusted_candidate: **162**
- risk_or_avoid_review: **5**
- positive_candidate: **3**
- volatile_watchlist: **3**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 282720 | 금양그린파워 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 475400 | 씨메스로보틱스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 86.00 | 0.00 | 0.00 | 86.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 86.00 | 0.00 | 0.00 | 86.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 86.00 | 0.00 | 0.00 | 86.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 86.00 | 0.00 | 0.00 | 86.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 86.00 | 0.00 | 0.00 | 86.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 86.00 | 0.00 | 0.00 | 86.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 86.00 | 0.00 | 0.00 | 86.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 86.00 | 0.00 | 0.00 | 86.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 86.00 | 0.00 | 0.00 | 86.00 | N/A | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 81.00 | 0.00 | 0.00 | 81.00 | N/A | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 81.00 | 0.00 | 0.00 | 81.00 | N/A | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 81.00 | 0.00 | 0.00 | 81.00 | N/A | N/A | N/A |
| 1970-01-01 | 059270 | 해성에어로보틱스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 76.00 | 0.00 | 0.00 | 76.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 66.00 | 0.00 | 0.00 | 66.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 66.00 | 0.00 | 0.00 | 66.00 | N/A | N/A | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 66.00 | 0.00 | 0.00 | 66.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 023760 | 한국캐피탈 | spin_off | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 001630 | 종근당홀딩스 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 131100 | 티엔엔터테인먼트 | spin_off | volatile | pending | pending | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | spin_off | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003100 | 선광 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 028260 | 삼성물산 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 028260 | 삼성물산 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 200230 | 텔콘RF제약 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 6.00 | 0.00 | 0.00 | 6.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 062970 | 한국첨단소재 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | 10.00 | 0.00 | 0.00 | 10.00 | N/A | N/A | N/A |
| 1970-01-01 | 337840 | 유엑스엔 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 065650 | 하이퍼코퍼레이션 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 290270 | 휴네시온 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | lawsuit | negative | pending | pending | insufficient_volume_baseline | -95.00 | 0.00 | 0.00 | -95.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
