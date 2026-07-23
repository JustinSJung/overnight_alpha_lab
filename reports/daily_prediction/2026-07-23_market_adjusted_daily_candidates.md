# Market-Adjusted Daily Candidate Report - 2026-07-23

Generated at: 2026-07-23 00:17:22

ML dataset source: `data/processed/ml_dataset_20260723.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260723.csv`

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

- Total rows: **2**
- positive_candidate: **1**
- risk_or_avoid_review: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 009150 | 삼성전기 | supply_contract | positive | pending | pending | 110.00 | 0.00 | 110.00 | N/A |

## Watchlist Candidates

No candidates in this section.

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 183490 | 엔지켐생명과학 | lawsuit | negative | pending | pending | -50.00 | 0.00 | -50.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
