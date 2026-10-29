# Volume + Market-Adjusted Daily Candidate Report - 2026-10-29

Generated at: 2026-10-29 02:25:46

ML dataset source: `data/processed/ml_dataset_20261029.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261029.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20261029.csv`

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

- Total rows: **136**
- strong_volume_market_adjusted_candidate: **61**
- risk_or_avoid_review: **32**
- watchlist_candidate: **21**
- positive_candidate: **20**
- volatile_watchlist: **2**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 295310 | 에이치브이엠 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 155.00 | 0.00 | 0.00 | 155.00 | N/A | N/A | N/A |
| 1970-01-01 | 295310 | 에이치브이엠 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 155.00 | 0.00 | 0.00 | 155.00 | N/A | N/A | N/A |
| 1970-01-01 | 295310 | 에이치브이엠 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 155.00 | 0.00 | 0.00 | 155.00 | N/A | N/A | N/A |
| 1970-01-01 | 295310 | 에이치브이엠 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 155.00 | 0.00 | 0.00 | 155.00 | N/A | N/A | N/A |
| 1970-01-01 | 295310 | 에이치브이엠 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 155.00 | 0.00 | 0.00 | 155.00 | N/A | N/A | N/A |
| 1970-01-01 | 295310 | 에이치브이엠 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 155.00 | 0.00 | 0.00 | 155.00 | N/A | N/A | N/A |
| 1970-01-01 | 295310 | 에이치브이엠 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 155.00 | 0.00 | 0.00 | 155.00 | N/A | N/A | N/A |
| 1970-01-01 | 295310 | 에이치브이엠 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 155.00 | 0.00 | 0.00 | 155.00 | N/A | N/A | N/A |
| 1970-01-01 | 131760 | 파인텍 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 145.00 | 0.00 | 0.00 | 145.00 | N/A | N/A | N/A |
| 1970-01-01 | 420770 | 기가비스 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 014790 | HL D&I | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 001260 | 남광토건 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 001260 | 남광토건 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 060980 | HL홀딩스 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 017000 | 신원종합개발 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 032820 | 우리기술 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 032820 | 우리기술 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 097230 | HJ중공업 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 010400 | 우진아이엔에스 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 105630 | 한세실업 | earnings_guidance | neutral_positive | nan | market_data_missing | insufficient_volume_baseline | 108.00 | 0.00 | 0.00 | 108.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 012330 | 현대모비스 | spin_off | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 000300 | DH오토넥스 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 389470 | 인벤티지랩 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 034730 | SK | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 086790 | 하나금융지주 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 016610 | DB증권 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 061040 | 알에프텍 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 096770 | SK이노베이션 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 096770 | SK이노베이션 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 096770 | SK이노베이션 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 096770 | SK이노베이션 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 096770 | SK이노베이션 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 361610 | SK아이이테크놀로지 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 361610 | SK아이이테크놀로지 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 096770 | SK이노베이션 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 096770 | SK이노베이션 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 096770 | SK이노베이션 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 025000 | KPX케미칼 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 015360 | INVENI | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 068290 | 삼성출판사 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 005300 | 롯데칠성음료 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 019210 | 와이지-원 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 053690 | 한미글로벌 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 069540 | 빛과전자 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 299480 | 지앤이헬스케어 | disclosure_violation | negative | nan | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 159910 | 에코글로우 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 217320 | 썬테크 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 123010 | MSDI | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 002020 | 코오롱 | disclosure_violation | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 340360 | 다보링크 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 065060 | 지엔코 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -75.00 | 0.00 | 0.00 | -75.00 | N/A | N/A | N/A |
| 1970-01-01 | 424870 | 이뮨온시아 | disclosure_violation | negative | nan | market_data_missing | insufficient_volume_baseline | -75.00 | 0.00 | 0.00 | -75.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -75.00 | 0.00 | 0.00 | -75.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
