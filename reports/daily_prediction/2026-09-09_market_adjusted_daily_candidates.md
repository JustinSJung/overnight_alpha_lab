# Market-Adjusted Daily Candidate Report - 2026-09-09

Generated at: 2026-09-09 00:53:42

ML dataset source: `data/processed/ml_dataset_20260909.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260909.csv`

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

- Total rows: **499**
- risk_or_avoid_review: **382**
- positive_candidate: **105**
- watchlist_candidate: **12**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 010960 | 삼호개발 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 037370 | EG | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 076080 | 웰크론한텍 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 490470 | 세미파이브 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 011200 | HMM | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 002020 | 코오롱 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 002990 | 금호건설 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 002780 | 진흥기업 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 389260 | 대명에너지 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 011370 | 서한 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 203400 | 에이비온 | spin_off | volatile | failure | market_data_missing | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 096350 | 대창솔루션 | investment_decision | volatile | success | market_data_missing | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 096350 | 대창솔루션 | investment_decision | volatile | success | market_data_missing | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 226950 | 올릭스 | investment_decision | volatile | failure | market_data_missing | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 096350 | 대창솔루션 | investment_decision | volatile | success | market_data_missing | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | failure | market_data_missing | 66.00 | 0.00 | 66.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 047050 | 포스코인터내셔널 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 019210 | 와이지-원 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 019210 | 와이지-원 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 020120 | 키다리스튜디오 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 005930 | 삼성전자 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 021240 | 코웨이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 268280 | 미원에스씨 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 009620 | 삼보산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 009620 | 삼보산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 021240 | 코웨이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 009620 | 삼보산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 009620 | 삼보산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 148250 | 알엔투테크놀로지 | convertible_bond | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 079970 | 투비소프트 | lawsuit | negative | failure | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | failure | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | failure | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 317690 | 퀀타매트릭스 | convertible_bond | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | paid_in_capital_increase | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
