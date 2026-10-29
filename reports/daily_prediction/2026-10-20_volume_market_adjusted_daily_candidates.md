# Volume + Market-Adjusted Daily Candidate Report - 2026-10-20

Generated at: 2026-10-20 01:45:23

ML dataset source: `data/processed/ml_dataset_20261020.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261020.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20261020.csv`

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

- Total rows: **84**
- strong_volume_market_adjusted_candidate: **40**
- risk_or_avoid_review: **21**
- positive_candidate: **12**
- watchlist_candidate: **9**
- volatile_watchlist: **2**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 010960 | 삼호개발 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 155.00 | 0.00 | 0.00 | 155.00 | N/A | N/A | N/A |
| 1970-01-01 | 005870 | 휴니드테크놀러지스 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 155.00 | 0.00 | 0.00 | 155.00 | N/A | N/A | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 025950 | 동신건설 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 141000 | 비아트론 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 010120 | 엘에스일렉트릭 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 032820 | 우리기술 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 028100 | 동아지질 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 420770 | 기가비스 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 025560 | 미래산업 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 028260 | 삼성물산 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 000300 | DH오토넥스 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 007680 | 대원 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 54.00 | 0.00 | 0.00 | 54.00 | N/A | N/A | N/A |
| 1970-01-01 | 290120 | DH오토리드 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 082270 | 젬백스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 005940 | NH투자증권 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 032620 | GC메디아이 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 006980 | 우성 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 033310 | 엠투엔 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 000720 | 현대건설 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 366030 | 나인앤컴퍼니 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 070960 | 모나용평 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 088790 | 진도 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 363280 | 티와이홀딩스 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 006340 | 대원전선 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 068290 | 삼성출판사 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 011930 | 신성이엔지 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 005610 | 삼립 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 012160 | 영흥 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 196170 | 알테오젠 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 6.00 | 0.00 | 0.00 | 6.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 065450 | 빅텍 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 440320 | 오픈놀 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -35.00 | 0.00 | 0.00 | -35.00 | N/A | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 060900 | 에이전트AI | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 091440 | 한울소재과학 | bond_with_warrant | negative | nan | market_data_missing | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 031990 | 대선조선 | lawsuit | negative | nan | nan | price_file_missing | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 302550 | 리메드 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 407400 | 꿈비 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 465770 | STX그린로지스 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 018500 | 동원모빌리티 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 123010 | MSDI | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 207490 | 에이펙스인텍 | disclosure_violation | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 377450 | 리파인 | disclosure_violation | negative | nan | market_data_missing | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 078020 | LS증권 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -75.00 | 0.00 | 0.00 | -75.00 | N/A | N/A | N/A |
| 1970-01-01 | 900100 | 파이온엑스 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -80.00 | 0.00 | 0.00 | -80.00 | N/A | N/A | N/A |
| 1970-01-01 | 247540 | 에코프로비엠 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -80.00 | 0.00 | 0.00 | -80.00 | N/A | N/A | N/A |
| 1970-01-01 | 320000 | 한울반도체 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -80.00 | 0.00 | 0.00 | -80.00 | N/A | N/A | N/A |
| 1970-01-01 | 059270 | 해성에어로보틱스 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -95.00 | 0.00 | 0.00 | -95.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
