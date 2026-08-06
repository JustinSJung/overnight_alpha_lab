# Market-Adjusted Daily Candidate Report - 2026-08-06

Generated at: 2026-08-06 23:59:34

ML dataset source: `data/processed/ml_dataset_20260806.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260806.csv`

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

- Total rows: **25**
- positive_candidate: **14**
- risk_or_avoid_review: **8**
- watchlist_candidate: **2**
- volatile_watchlist: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 296640 | 이노에이엑스 | supply_contract | positive | pending | pending | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 488900 | 비츠로넥스텍 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 042370 | 비츠로테크 | supply_contract | positive | pending | pending | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 009190 | 대양금속 | investment_decision | volatile | pending | pending | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 009190 | 대양금속 | investment_decision | volatile | pending | pending | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 009190 | 대양금속 | investment_decision | volatile | pending | pending | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 009190 | 대양금속 | investment_decision | volatile | pending | pending | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | pending | pending | 61.00 | 0.00 | 61.00 | N/A |
| 1970-01-01 | 457600 | 벡트 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 009190 | 대양금속 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 009190 | 대양금속 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 457600 | 벡트 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 009190 | 대양금속 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 009190 | 대양금속 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | pending | pending | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | pending | pending | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 084180 | 수성웹툰 | major_shareholder_change | volatile | pending | pending | 16.00 | 0.00 | 16.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 376270 | HEM파마 | convertible_bond | negative | pending | pending | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 215570 | 크로넥스 | paid_in_capital_increase | negative | pending | pending | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 163730 | 핑거 | paid_in_capital_increase | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 079950 | 인베니아 | disclosure_violation | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 199800 | 툴젠 | paid_in_capital_increase | negative | pending | pending | -75.00 | 0.00 | -75.00 | N/A |
| 1970-01-01 | 064800 | 포니링크 | lawsuit | negative | pending | pending | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 115450 | HLB테라퓨틱스 | convertible_bond | negative | pending | pending | -80.00 | 0.00 | -80.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
