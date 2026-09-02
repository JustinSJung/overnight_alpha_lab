# Market-Adjusted Daily Candidate Report - 2026-09-02

Generated at: 2026-09-02 00:49:26

ML dataset source: `data/processed/ml_dataset_20260902.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260902.csv`

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

- Total rows: **184**
- risk_or_avoid_review: **101**
- positive_candidate: **65**
- watchlist_candidate: **17**
- volatile_watchlist: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 009150 | 삼성전기 | supply_contract | positive | nan | market_data_missing | 175.00 | 0.00 | 175.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | supply_contract | positive | nan | market_data_missing | 160.00 | 0.00 | 160.00 | N/A |
| 1970-01-01 | 005880 | 대한해운 | supply_contract | positive | nan | market_data_missing | 155.00 | 0.00 | 155.00 | N/A |
| 1970-01-01 | 493330 | 지에프아이 | supply_contract | positive | nan | market_data_missing | 145.00 | 0.00 | 145.00 | N/A |
| 1970-01-01 | 383310 | 에코프로에이치엔 | supply_contract | positive | nan | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 368770 | 파이버프로 | supply_contract | positive | nan | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 331920 | 셀레믹스 | supply_contract | positive | nan | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 000100 | 유한양행 | supply_contract | positive | nan | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 418420 | 라온텍 | supply_contract | positive | nan | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 012210 | 삼미금속 | supply_contract | positive | nan | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 045660 | 에이텍 | supply_contract | positive | nan | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 013700 | 까뮤이앤씨 | supply_contract | positive | nan | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | nan | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 042660 | 한화오션 | supply_contract | positive | nan | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | supply_contract | positive | nan | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 464080 | 에스오에스랩 | supply_contract | positive | nan | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 382150 | 온코크로스 | investment_decision | volatile | nan | market_data_missing | 106.00 | 0.00 | 106.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 046390 | 삼화네트웍스 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 002990 | 금호건설 | supply_contract | positive | nan | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 268280 | 미원에스씨 | major_shareholder_change | volatile | nan | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 001740 | SK네트웍스 | major_shareholder_change | volatile | nan | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 017670 | SK텔레콤 | major_shareholder_change | volatile | nan | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 004770 | 써니전자 | major_shareholder_change | volatile | nan | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 023530 | 롯데쇼핑 | major_shareholder_change | volatile | nan | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 027740 | 마니커 | major_shareholder_change | volatile | nan | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | major_shareholder_change | volatile | nan | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 008930 | 한미사이언스 | major_shareholder_change | volatile | nan | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 090080 | 평화산업 | major_shareholder_change | volatile | nan | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | major_shareholder_change | volatile | nan | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 073640 | 테라사이언스 | merger | volatile | nan | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 007280 | 한국특강 | major_shareholder_change | volatile | nan | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 060900 | 에이전트AI | major_shareholder_change | volatile | nan | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 069730 | DSR제강 | major_shareholder_change | volatile | nan | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 177830 | 파버나인 | major_shareholder_change | volatile | nan | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 026960 | 동서 | major_shareholder_change | volatile | nan | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 015360 | INVENI | major_shareholder_change | volatile | nan | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 083470 | 이엠앤아이 | major_shareholder_change | volatile | nan | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 030210 | 다올투자증권 | lawsuit | negative | nan | market_data_missing | 0.00 | 0.00 | 0.00 | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | convertible_bond | negative | nan | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 003920 | 남양유업 | lawsuit | negative | nan | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 003920 | 남양유업 | lawsuit | negative | nan | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 003920 | 남양유업 | lawsuit | negative | nan | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 003920 | 남양유업 | lawsuit | negative | nan | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 003920 | 남양유업 | lawsuit | negative | nan | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 340810 | 시선AI | convertible_bond | negative | nan | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 003920 | 남양유업 | lawsuit | negative | nan | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 003920 | 남양유업 | lawsuit | negative | nan | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 003920 | 남양유업 | lawsuit | negative | nan | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | nan | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | nan | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 032680 | 소프트센 | convertible_bond | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 095190 | 신화프리텍 | convertible_bond | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | bond_with_warrant | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | convertible_bond | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 226340 | 본느 | paid_in_capital_increase | negative | nan | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
