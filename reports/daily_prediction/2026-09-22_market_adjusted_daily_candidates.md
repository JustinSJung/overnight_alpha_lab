# Market-Adjusted Daily Candidate Report - 2026-09-22

Generated at: 2026-09-22 02:09:04

ML dataset source: `data/processed/ml_dataset_20260922.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260922.csv`

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

- Total rows: **2575**
- risk_or_avoid_review: **2391**
- positive_candidate: **114**
- watchlist_candidate: **69**
- volatile_watchlist: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 010400 | 우진아이엔에스 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 032820 | 우리기술 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 032820 | 우리기술 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 032820 | 우리기술 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 032820 | 우리기술 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 206560 | 덱스터 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 277070 | 린드먼아시아 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 334970 | 프레스티지바이오로직스 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 090470 | 제이스로보틱스 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 028050 | 삼성E&A | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 028050 | 삼성E&A | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 032800 | 판타지오 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 032800 | 판타지오 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 042660 | 한화오션 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 032800 | 판타지오 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 045390 | 대아티아이 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 105840 | 우진 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 064350 | 현대로템 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 204840 | 지엘팜텍 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 127710 | 아시아경제 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 038500 | 삼표시멘트 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 000480 | 시알홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 011810 | STX | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 166090 | 하나머티리얼즈 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 340810 | 시선AI | convertible_bond | negative | success | market_data_missing | 5.00 | 0.00 | 5.00 | N/A |
| 1970-01-01 | 026150 | 특수건설 | convertible_bond | negative | success | market_data_missing | -5.00 | 0.00 | -5.00 | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | convertible_bond | negative | failure | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 121600 | 나노신소재 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 121600 | 나노신소재 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 121600 | 나노신소재 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 121600 | 나노신소재 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 121600 | 나노신소재 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 121600 | 나노신소재 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 121600 | 나노신소재 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 121600 | 나노신소재 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | convertible_bond | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | convertible_bond | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | convertible_bond | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | convertible_bond | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | convertible_bond | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | convertible_bond | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | convertible_bond | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | convertible_bond | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 049120 | 파인디앤씨 | convertible_bond | negative | failure | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
