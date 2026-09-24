# Volume + Market-Adjusted Daily Candidate Report - 2026-09-24

Generated at: 2026-09-24 00:59:02

ML dataset source: `data/processed/ml_dataset_20260924.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260924.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260924.csv`

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

- Total rows: **82**
- risk_or_avoid_review: **49**
- strong_volume_market_adjusted_candidate: **15**
- watchlist_candidate: **9**
- positive_candidate: **8**
- volatile_watchlist: **1**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 101360 | 에코앤드림 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 150.00 | 0.00 | 0.00 | 150.00 | N/A | N/A | N/A |
| 1970-01-01 | 014790 | HL D&I | supply_contract | positive | nan | pending | insufficient_volume_baseline | 145.00 | 0.00 | 0.00 | 145.00 | N/A | N/A | N/A |
| 1970-01-01 | 272210 | 한화시스템 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 091590 | 남화토건 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 004440 | 삼일씨엔에스 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 326030 | 에스케이바이오팜 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 109860 | 동일금속 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 064350 | 현대로템 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 475400 | 씨메스로보틱스 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 90.00 | 0.00 | 0.00 | 90.00 | N/A | N/A | N/A |
| 1970-01-01 | 000720 | 현대건설 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 90.00 | 0.00 | 0.00 | 90.00 | N/A | N/A | N/A |
| 1970-01-01 | 060980 | HL홀딩스 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 90.00 | 0.00 | 0.00 | 90.00 | N/A | N/A | N/A |
| 1970-01-01 | 046390 | 삼화네트웍스 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 85.00 | 0.00 | 0.00 | 85.00 | N/A | N/A | N/A |
| 1970-01-01 | 083650 | 비에이치아이 | supply_contract | positive | nan | pending | insufficient_volume_baseline | 85.00 | 0.00 | 0.00 | 85.00 | N/A | N/A | N/A |
| 1970-01-01 | 068270 | 셀트리온 | investment_decision | volatile | nan | pending | insufficient_volume_baseline | 71.00 | 0.00 | 0.00 | 71.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 016740 | 두올 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 109670 | 씨싸이트 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 230360 | 에코마케팅 | spin_off | volatile | nan | nan | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 002810 | 삼영무역 | merger | volatile | nan | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 001360 | 삼성제약 | investment_decision | volatile | nan | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 377480 | 마음AI | investment_decision | volatile | nan | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 229000 | 젠큐릭스 | merger | volatile | nan | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 009160 | SIMPAC | investment_decision | volatile | nan | pending | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 251270 | 넷마블 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 002720 | 국제약품 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 007570 | 일양약품 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 259960 | 크래프톤 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 002790 | 아모레퍼시픽홀딩스 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 005250 | 녹십자홀딩스 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 090430 | 아모레퍼시픽 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 431190 | 케이쓰리아이 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 001210 | 금호전기 | major_shareholder_change | volatile | nan | pending | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 026150 | 특수건설 | convertible_bond | negative | nan | pending | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 003580 | HLB글로벌 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 117730 | 티로보틱스 | bond_with_warrant | negative | nan | pending | insufficient_volume_baseline | -35.00 | 0.00 | 0.00 | -35.00 | N/A | N/A | N/A |
| 1970-01-01 | 083640 | 인콘 | convertible_bond | negative | nan | pending | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 065650 | 하이퍼코퍼레이션 | convertible_bond | negative | nan | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 431190 | 케이쓰리아이 | convertible_bond | negative | nan | pending | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 039200 | 오스코텍 | lawsuit | negative | nan | pending | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 328130 | 루닛 | convertible_bond | negative | nan | pending | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 003060 | 에이프로젠바이오로직스 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | lawsuit | negative | nan | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 431190 | 케이쓰리아이 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 003060 | 에이프로젠바이오로직스 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 003060 | 에이프로젠바이오로직스 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 003060 | 에이프로젠바이오로직스 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 003060 | 에이프로젠바이오로직스 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 003060 | 에이프로젠바이오로직스 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 003060 | 에이프로젠바이오로직스 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 003060 | 에이프로젠바이오로직스 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 090710 | 휴림로봇 | paid_in_capital_increase | negative | nan | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
