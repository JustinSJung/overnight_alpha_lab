# Market-Adjusted Daily Candidate Report - 2026-07-30

Generated at: 2026-07-30 05:53:45

ML dataset source: `data/processed/ml_dataset_20260730.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260730.csv`

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

- Total rows: **72**
- risk_or_avoid_review: **67**
- positive_candidate: **3**
- watchlist_candidate: **2**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 330730 | 스톤브릿지벤처스 | investment_decision | volatile | pending | pending | 91.00 | 0.00 | 91.00 | N/A |
| 1970-01-01 | 141000 | 비아트론 | supply_contract | positive | pending | pending | 85.00 | 0.00 | 85.00 | N/A |
| 1970-01-01 | 475580 | 에이럭스 | supply_contract | positive | pending | pending | 80.00 | 0.00 | 80.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 011330 | 유니켐 | major_shareholder_change | volatile | pending | pending | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 011330 | 유니켐 | major_shareholder_change | volatile | pending | pending | 31.00 | 0.00 | 31.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 332290 | 누보 | convertible_bond | negative | pending | pending | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 403550 | 쏘카 | paid_in_capital_increase | negative | pending | pending | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 403550 | 쏘카 | paid_in_capital_increase | negative | pending | pending | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
