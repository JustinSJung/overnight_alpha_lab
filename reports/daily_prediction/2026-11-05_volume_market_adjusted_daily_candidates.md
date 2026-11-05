# Volume + Market-Adjusted Daily Candidate Report - 2026-11-05

Generated at: 2026-11-05 03:22:30

ML dataset source: `data/processed/ml_dataset_20261105.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261105.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20261105.csv`

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

- Total rows: **70**
- risk_or_avoid_review: **31**
- positive_candidate: **19**
- strong_volume_market_adjusted_candidate: **15**
- watchlist_candidate: **4**
- volatile_watchlist: **1**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 017510 | 세명전기 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 254120 | 자비스 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 143210 | 핸즈코퍼레이션 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 041960 | 코미팜 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 017000 | 신원종합개발 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 451760 | 컨텍 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 007610 | 선도전기 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 277880 | 티에스아이 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 035890 | 서희건설 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 023350 | 한국종합기술 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 101680 | 한국정밀기계 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 017040 | 광명전기 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 010130 | 고려아연 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 81.00 | 0.00 | 0.00 | 81.00 | N/A | N/A | N/A |
| 1970-01-01 | 140410 | 메지온 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 66.00 | 0.00 | 0.00 | 66.00 | N/A | N/A | N/A |
| 1970-01-01 | 307180 | 아이엘 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 61.00 | 0.00 | 0.00 | 61.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 057050 | 현대홈쇼핑 | spin_off | volatile | nan | nan | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 057050 | 현대홈쇼핑 | spin_off | volatile | nan | nan | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 057050 | 현대홈쇼핑 | spin_off | volatile | nan | nan | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 057050 | 현대홈쇼핑 | spin_off | volatile | nan | nan | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 008930 | 한미사이언스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 005440 | 현대지에프홀딩스 | spin_off | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 180640 | 한진칼 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 180640 | 한진칼 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 180640 | 한진칼 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 180640 | 한진칼 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 180640 | 한진칼 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 180640 | 한진칼 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 306200 | 세아제강 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 180640 | 한진칼 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 326030 | 에스케이바이오팜 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 180640 | 한진칼 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 016610 | DB증권 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 004410 | 서울식품공업 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 066590 | 스모트로닉 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 015360 | INVENI | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 004080 | 신흥 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 005930 | 삼성전자 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | -4.00 | 0.00 | 0.00 | -4.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 177350 | 베셀 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 432430 | 와이랩 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 214270 | FSN | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 163730 | 핑거 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 013360 | 일성건설 | disclosure_violation | negative | nan | market_data_missing | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 321820 | 아티스트컴퍼니 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 277410 | 인산가 | bond_with_warrant | negative | nan | market_data_missing | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 468530 | 프로티나 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 241690 | 유니테크노 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 191600 | 블루탑 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 328130 | 루닛 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 468530 | 프로티나 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 042940 | 상지건설 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 072770 | 멤레이비티 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 159910 | 에코글로우 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -75.00 | 0.00 | 0.00 | -75.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -75.00 | 0.00 | 0.00 | -75.00 | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -75.00 | 0.00 | 0.00 | -75.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
