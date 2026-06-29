# Market-Adjusted Daily Candidate Report - 2026-06-29

Generated at: 2026-06-29 01:54:45

ML dataset source: `data/processed/ml_dataset_20260629.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260629.csv`

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
- positive_candidate: **7**
- volatile_watchlist: **3**
- risk_or_avoid_review: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 068790 | DMS | supply_contract | positive | pending | pending | 150.00 | 0.00 | 150.00 | N/A |
| 1970-01-01 | 445090 | 에이직랜드 | supply_contract | positive | pending | pending | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 300080 | 플리토 | supply_contract | positive | pending | pending | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 300080 | 플리토 | supply_contract | positive | pending | pending | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 300080 | 플리토 | supply_contract | positive | pending | pending | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 300080 | 플리토 | supply_contract | positive | pending | pending | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 480370 | 씨케이솔루션 | supply_contract | positive | pending | pending | 85.00 | 0.00 | 85.00 | N/A |

## Watchlist Candidates

No candidates in this section.

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 011930 | 신성이엔지 | major_shareholder_change | volatile | pending | pending | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 011930 | 신성이엔지 | major_shareholder_change | volatile | pending | pending | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 011930 | 신성이엔지 | major_shareholder_change | volatile | pending | pending | 16.00 | 0.00 | 16.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 118000 | 메타케어 | paid_in_capital_increase | negative | pending | pending | -55.00 | 0.00 | -55.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
