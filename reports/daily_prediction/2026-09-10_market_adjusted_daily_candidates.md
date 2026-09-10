# Market-Adjusted Daily Candidate Report - 2026-09-10

Generated at: 2026-09-10 00:54:30

ML dataset source: `data/processed/ml_dataset_20260910.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260910.csv`

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

- Total rows: **112**
- positive_candidate: **63**
- risk_or_avoid_review: **38**
- watchlist_candidate: **8**
- volatile_watchlist: **3**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 064290 | 인텍플러스 | supply_contract | positive | nan | market_data_missing | 145.00 | 0.00 | 145.00 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | supply_contract | positive | nan | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 010960 | 삼호개발 | supply_contract | positive | nan | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | supply_contract | positive | nan | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 200710 | 에이디테크놀로지 | supply_contract | positive | nan | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 007570 | 일양약품 | supply_contract | positive | nan | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 137400 | 피엔티 | supply_contract | positive | nan | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 012630 | HDC | supply_contract | positive | nan | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 005960 | 동부건설 | supply_contract | positive | nan | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 376270 | HEM파마 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 002460 | HS화성 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 026150 | 특수건설 | supply_contract | positive | nan | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 268280 | 미원에스씨 | major_shareholder_change | volatile | nan | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 033310 | 엠투엔 | major_shareholder_change | volatile | nan | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 016380 | KG스틸 | major_shareholder_change | volatile | nan | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 348950 | 제이알글로벌리츠 | investment_decision | volatile | nan | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 014530 | 극동유화 | major_shareholder_change | volatile | nan | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 228670 | 레이 | major_shareholder_change | volatile | nan | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 069730 | DSR제강 | major_shareholder_change | volatile | nan | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 090430 | 아모레퍼시픽 | major_shareholder_change | volatile | nan | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 002790 | 아모레퍼시픽홀딩스 | major_shareholder_change | volatile | nan | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 006570 | 대림통상 | major_shareholder_change | volatile | nan | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 044380 | 주연테크 | major_shareholder_change | volatile | nan | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 083640 | 인콘 | convertible_bond | negative | nan | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | convertible_bond | negative | nan | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 226590 | 엠디바이스 | convertible_bond | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 031990 | 대선조선 | lawsuit | negative | nan | nan | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 226340 | 본느 | paid_in_capital_increase | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | nan | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | convertible_bond | negative | nan | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 009730 | 이렘 | paid_in_capital_increase | negative | nan | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 196300 | HLB펩 | convertible_bond | negative | nan | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | convertible_bond | negative | nan | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | nan | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | nan | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
