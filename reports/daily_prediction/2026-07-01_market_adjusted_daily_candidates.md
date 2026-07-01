# Market-Adjusted Daily Candidate Report - 2026-07-01

Generated at: 2026-07-01 00:05:44

ML dataset source: `data/processed/ml_dataset_20260701.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260701.csv`

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

- Total rows: **1**
- positive_candidate: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 028080 | 휴맥스홀딩스 | merger | volatile | pending | pending | 86.00 | 0.00 | 86.00 | N/A |

## Watchlist Candidates

No candidates in this section.

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

No candidates in this section.

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
