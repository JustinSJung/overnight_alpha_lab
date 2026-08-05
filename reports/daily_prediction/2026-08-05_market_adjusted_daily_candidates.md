# Market-Adjusted Daily Candidate Report - 2026-08-05

Generated at: 2026-08-05 23:20:48

ML dataset source: `data/processed/ml_dataset_20260805.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260805.csv`

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

- Total rows: **11**
- positive_candidate: **5**
- watchlist_candidate: **5**
- risk_or_avoid_review: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 001260 | 남광토건 | supply_contract | positive | pending | pending | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 011810 | STX | investment_decision | volatile | pending | pending | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 252500 | 세화피앤씨 | spin_off | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 252500 | 세화피앤씨 | spin_off | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 004990 | 롯데지주 | major_shareholder_change | volatile | pending | pending | 41.00 | 0.00 | 41.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 276040 | 스코넥 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 276040 | 스코넥 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 276040 | 스코넥 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 000950 | 전방 | major_shareholder_change | volatile | pending | pending | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 000950 | 전방 | major_shareholder_change | volatile | pending | pending | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 380540 | 옵티코어 | convertible_bond | negative | pending | pending | -35.00 | 0.00 | -35.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
