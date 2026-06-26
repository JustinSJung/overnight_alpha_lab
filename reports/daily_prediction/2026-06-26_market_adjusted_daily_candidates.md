# Market-Adjusted Daily Candidate Report - 2026-06-26

Generated at: 2026-06-26 16:24:22

ML dataset source: `data/processed/ml_dataset_20260626.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260626.csv`

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

- Total rows: **19**
- risk_or_avoid_review: **11**
- positive_candidate: **5**
- watchlist_candidate: **3**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 082740 | 한화엔진 | supply_contract | positive | pending | pending | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 011810 | STX | investment_decision | volatile | pending | pending | 61.00 | 0.00 | 61.00 | N/A |
| 1970-01-01 | 011810 | STX | investment_decision | volatile | pending | pending | 61.00 | 0.00 | 61.00 | N/A |
| 1970-01-01 | 011810 | STX | investment_decision | volatile | pending | pending | 61.00 | 0.00 | 61.00 | N/A |
| 1970-01-01 | 011810 | STX | investment_decision | volatile | pending | pending | 61.00 | 0.00 | 61.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 014130 | 한익스프레스 | major_shareholder_change | volatile | pending | pending | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 014130 | 한익스프레스 | major_shareholder_change | volatile | pending | pending | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 014130 | 한익스프레스 | major_shareholder_change | volatile | pending | pending | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 221840 | 하이즈항공 | lawsuit | negative | pending | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | convertible_bond | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | convertible_bond | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | convertible_bond | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | convertible_bond | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | convertible_bond | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | convertible_bond | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | convertible_bond | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 224060 | 더코디 | convertible_bond | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | convertible_bond | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | bond_with_warrant | negative | pending | pending | -50.00 | 0.00 | -50.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
