# Market-Adjusted Daily Candidate Report - 2026-07-21

Generated at: 2026-07-21 02:14:00

ML dataset source: `data/processed/ml_dataset_20260721.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260721.csv`

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

- Total rows: **10**
- positive_candidate: **6**
- watchlist_candidate: **3**
- risk_or_avoid_review: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 038680 | 에스넷 | supply_contract | positive | pending | pending | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 100840 | SNT에너지 | supply_contract | positive | pending | pending | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 036530 | SNT홀딩스 | supply_contract | positive | pending | pending | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 248070 | 솔루엠 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 248070 | 솔루엠 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 248070 | 솔루엠 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 084870 | 티비에이치글로벌 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 084870 | 티비에이치글로벌 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 134790 | 시디즈 | major_shareholder_change | volatile | pending | pending | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 004710 | 한솔테크닉스 | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
