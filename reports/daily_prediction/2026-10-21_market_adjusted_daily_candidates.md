# Market-Adjusted Daily Candidate Report - 2026-10-21

Generated at: 2026-10-21 01:15:44

ML dataset source: `data/processed/ml_dataset_20261021.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261021.csv`

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

- Total rows: **77**
- positive_candidate: **39**
- risk_or_avoid_review: **27**
- watchlist_candidate: **11**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 391710 | 코닉오토메이션 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 950130 | 엑세스바이오 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 277880 | 티에스아이 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 200710 | 에이디테크놀로지 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 187870 | 디바이스 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 122640 | 예스티 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 058970 | 엠로 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 002290 | 삼일기업공사 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 217330 | 싸이토젠 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 095910 | 에스에너지 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 329180 | HD현대중공업 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 010950 | S-Oil | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 117670 | 알파칩스 | bonus_issue | positive | success | market_data_missing | 85.00 | 0.00 | 85.00 | N/A |
| 1970-01-01 | 310210 | 보로노이 | investment_decision | volatile | success | market_data_missing | 66.00 | 0.00 | 66.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 003460 | 유화증권 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 143240 | 사람인 | investment_decision | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 013520 | 화승코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 090430 | 아모레퍼시픽 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 090430 | 아모레퍼시픽 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 090430 | 아모레퍼시픽 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 090430 | 아모레퍼시픽 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 090430 | 아모레퍼시픽 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 311060 | 엘에이티 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 431190 | 케이쓰리아이 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 002990 | 금호건설 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 017860 | DS단석 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 017860 | DS단석 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 002990 | 금호건설 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 002990 | 금호건설 | convertible_bond | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 060230 | 제이케이시냅스 | convertible_bond | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 017860 | DS단석 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 278470 | 에이피알 | disclosure_violation | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 001750 | 한양증권 | lawsuit | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 484810 | 티엑스알로보틱스 | convertible_bond | negative | failure | market_data_missing | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 006490 | 프리티 | paid_in_capital_increase | negative | failure | market_data_missing | -75.00 | 0.00 | -75.00 | N/A |
| 1970-01-01 | 148250 | 알엔투테크놀로지 | lawsuit | negative | success | market_data_missing | -75.00 | 0.00 | -75.00 | N/A |
| 1970-01-01 | 465770 | STX그린로지스 | convertible_bond | negative | failure | market_data_missing | -75.00 | 0.00 | -75.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | paid_in_capital_increase | negative | failure | market_data_missing | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | paid_in_capital_increase | negative | failure | market_data_missing | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | paid_in_capital_increase | negative | failure | market_data_missing | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | paid_in_capital_increase | negative | failure | market_data_missing | -80.00 | 0.00 | -80.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
