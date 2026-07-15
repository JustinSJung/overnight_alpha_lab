# Market-Adjusted Daily Candidate Report - 2026-07-15

Generated at: 2026-07-15 00:22:37

ML dataset source: `data/processed/ml_dataset_20260715.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260715.csv`

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

- Total rows: **5**
- positive_candidate: **3**
- risk_or_avoid_review: **2**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 119850 | 지엔씨에너지 | supply_contract | positive | pending | pending | 155.00 | 0.00 | 155.00 | N/A |
| 1970-01-01 | 042660 | 한화오션 | supply_contract | positive | pending | pending | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 011930 | 신성이엔지 | supply_contract | positive | pending | pending | 100.00 | 0.00 | 100.00 | N/A |

## Watchlist Candidates

No candidates in this section.

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 000660 | SK하이닉스 | paid_in_capital_increase | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 000660 | SK하이닉스 | paid_in_capital_increase | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
