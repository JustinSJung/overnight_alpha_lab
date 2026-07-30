# Volume + Market-Adjusted Daily Candidate Report - 2026-07-30

Generated at: 2026-07-30 06:16:23

ML dataset source: `data/processed/ml_dataset_20260730.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260730.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260730.csv`

## Purpose

This report applies both market-adjusted score adjustments and trading volume score adjustments to daily candidate scoring.

It is a v3 candidate report for comparison and does not replace the main recommender yet.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Score Formula

```text
base_recommendation_score_v3
+ market_adjusted_score_adjustment
+ trading_volume_score_adjustment
= final_volume_market_adjusted_score
```

## Summary

- Total rows: **67**
- risk_or_avoid_review: **65**
- strong_volume_market_adjusted_candidate: **2**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 330730 | 스톤브릿지벤처스 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 86.00 | 0.00 | 0.00 | 86.00 | N/A | N/A | N/A |
| 1970-01-01 | 475580 | 에이럭스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 80.00 | 0.00 | 0.00 | 80.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

No candidates in this section.

## Watchlist Candidates

No candidates in this section.

## Volatile Watchlist

No candidates in this section.

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 332290 | 누보 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -25.00 | 0.00 | 0.00 | -25.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 061970 | LB세미콘 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
