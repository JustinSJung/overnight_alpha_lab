# Market-Adjusted Daily Candidate Report - 2026-07-16

Generated at: 2026-07-16 23:14:06

ML dataset source: `data/processed/ml_dataset_20260716.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260716.csv`

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

- Total rows: **18**
- risk_or_avoid_review: **10**
- positive_candidate: **7**
- watchlist_candidate: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 097230 | HJ중공업 | supply_contract | positive | pending | pending | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 002810 | 삼영무역 | merger | volatile | pending | pending | 56.00 | 0.00 | 56.00 | N/A |
| 1970-01-01 | 002810 | 삼영무역 | merger | volatile | pending | pending | 56.00 | 0.00 | 56.00 | N/A |
| 1970-01-01 | 009320 | 아진전자부품 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 054940 | 엑사이엔씨 | spin_off | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | investment_decision | volatile | pending | pending | 41.00 | 0.00 | 41.00 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | investment_decision | volatile | pending | pending | 41.00 | 0.00 | 41.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | pending | pending | 31.00 | 0.00 | 31.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 320000 | 한울반도체 | paid_in_capital_increase | negative | pending | pending | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 320000 | 한울반도체 | paid_in_capital_increase | negative | pending | pending | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 320000 | 한울반도체 | paid_in_capital_increase | negative | pending | pending | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 320000 | 한울반도체 | paid_in_capital_increase | negative | pending | pending | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | pending | pending | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | pending | pending | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 042940 | 상지건설 | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 340810 | 시선AI | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 080010 | 이상네트웍스 | disclosure_violation | negative | pending | pending | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | lawsuit | negative | pending | pending | -90.00 | 0.00 | -90.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
