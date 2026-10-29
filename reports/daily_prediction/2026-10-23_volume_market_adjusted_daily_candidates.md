# Volume + Market-Adjusted Daily Candidate Report - 2026-10-23

Generated at: 2026-10-23 01:25:39

ML dataset source: `data/processed/ml_dataset_20261023.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261023.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20261023.csv`

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

- Total rows: **85**
- risk_or_avoid_review: **33**
- strong_volume_market_adjusted_candidate: **31**
- positive_candidate: **12**
- watchlist_candidate: **6**
- volatile_watchlist: **3**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 000720 | 현대건설 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 143540 | 영우디에스피 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 071970 | HD현대마린엔진 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 028050 | 삼성E&A | earnings_guidance | neutral_positive | nan | market_data_missing | insufficient_volume_baseline | 113.00 | 0.00 | 0.00 | 113.00 | N/A | N/A | N/A |
| 1970-01-01 | 396470 | 워트 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 003380 | 하림지주 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 013580 | 계룡건설산업 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 119850 | 지엔씨에너지 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 122640 | 예스티 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 382900 | 범한퓨얼셀 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 012450 | 한화에어로스페이스 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 028670 | 팬오션 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 282880 | 코윈로보틱스 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 460470 | 아이빔테크놀로지 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 011560 | 세보엠이씨 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 90.00 | 0.00 | 0.00 | 90.00 | N/A | N/A | N/A |
| 1970-01-01 | 389140 | 포바이포 | supply_contract | positive | nan | market_data_missing | insufficient_volume_baseline | 90.00 | 0.00 | 0.00 | 90.00 | N/A | N/A | N/A |
| 1970-01-01 | 004990 | 롯데지주 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 81.00 | 0.00 | 0.00 | 81.00 | N/A | N/A | N/A |
| 1970-01-01 | 0099X0 | IBKS제25호스팩 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 76.00 | 0.00 | 0.00 | 76.00 | N/A | N/A | N/A |
| 1970-01-01 | 0099X0 | IBKS제25호스팩 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 76.00 | 0.00 | 0.00 | 76.00 | N/A | N/A | N/A |
| 1970-01-01 | 0099X0 | IBKS제25호스팩 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 76.00 | 0.00 | 0.00 | 76.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 006740 | 블루산업개발 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 068270 | 셀트리온 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 003030 | 세아제강지주 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 006370 | 대구백화점 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 131030 | 옵투스제약 | investment_decision | volatile | nan | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 051980 | 중앙첨단소재 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 008870 | 금비 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 229000 | 젠큐릭스 | merger | volatile | nan | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 011780 | 금호석유화학 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 088790 | 진도 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 004150 | 한솔홀딩스 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 129920 | 대성하이텍 | major_shareholder_change | volatile | nan | market_data_missing | insufficient_volume_baseline | 6.00 | 0.00 | 0.00 | 6.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 007120 | 미래아이앤지 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 335870 | 윙스풋 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 102280 | 쌍방울 | convertible_bond | negative | nan | nan | price_file_missing | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 332190 | 오션스바이오 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 002990 | 금호건설 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 000490 | 대동 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 083640 | 인콘 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 030610 | 교보증권 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 030610 | 교보증권 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 900100 | 파이온엑스 | convertible_bond | negative | nan | market_data_missing | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 373200 | 엑스플러스 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 373200 | 엑스플러스 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 083660 | CSA 코스믹 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 373200 | 엑스플러스 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 373200 | 엑스플러스 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 373200 | 엑스플러스 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 418250 | 시큐레터 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 373200 | 엑스플러스 | paid_in_capital_increase | negative | nan | market_data_missing | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
