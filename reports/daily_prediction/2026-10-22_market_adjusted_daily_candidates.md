# Market-Adjusted Daily Candidate Report - 2026-10-22

Generated at: 2026-10-22 01:25:55

ML dataset source: `data/processed/ml_dataset_20261022.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261022.csv`

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

- Total rows: **467**
- positive_candidate: **293**
- risk_or_avoid_review: **158**
- volatile_watchlist: **10**
- watchlist_candidate: **6**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 013580 | 계룡건설산업 | supply_contract | positive | success | market_data_missing | 150.00 | 0.00 | 150.00 | N/A |
| 1970-01-01 | 013580 | 계룡건설산업 | supply_contract | positive | success | market_data_missing | 150.00 | 0.00 | 150.00 | N/A |
| 1970-01-01 | 025560 | 미래산업 | supply_contract | positive | success | market_data_missing | 145.00 | 0.00 | 145.00 | N/A |
| 1970-01-01 | 396470 | 워트 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 207940 | 삼성바이오로직스 | earnings_guidance | neutral_positive | failure | market_data_missing | 38.00 | 0.00 | 38.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | earnings_guidance | neutral_positive | failure | market_data_missing | 38.00 | 0.00 | 38.00 | N/A |
| 1970-01-01 | 002100 | 경농 | merger | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 177830 | 파버나인 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 177830 | 파버나인 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 457190 | 이수스페셜티케미컬 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 015360 | INVENI | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 055550 | 신한지주 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 055550 | 신한지주 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 055550 | 신한지주 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 015360 | INVENI | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 340360 | 다보링크 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 340360 | 다보링크 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 340360 | 다보링크 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 340360 | 다보링크 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 105560 | KB금융 | major_shareholder_change | volatile | failure | market_data_missing | -9.00 | 0.00 | -9.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | success | market_data_missing | -15.00 | 0.00 | -15.00 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 417010 | 나노팀 | convertible_bond | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 066430 | 아이로보틱스 | lawsuit | negative | failure | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 043100 | 알파AI | disclosure_violation | negative | failure | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 043100 | 알파AI | disclosure_violation | negative | failure | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 357880 | SKAI | convertible_bond | negative | failure | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 043100 | 알파AI | disclosure_violation | negative | failure | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 357880 | SKAI | convertible_bond | negative | failure | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 357880 | SKAI | convertible_bond | negative | failure | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | disclosure_violation | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 397810 | 애드포러스 | convertible_bond | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | convertible_bond | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 061040 | 알에프텍 | convertible_bond | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 061040 | 알에프텍 | convertible_bond | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 061040 | 알에프텍 | convertible_bond | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
