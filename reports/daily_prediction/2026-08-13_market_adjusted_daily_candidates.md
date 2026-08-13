# Market-Adjusted Daily Candidate Report - 2026-08-13

Generated at: 2026-08-13 23:08:07

ML dataset source: `data/processed/ml_dataset_20260813.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260813.csv`

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

- Total rows: **112**
- risk_or_avoid_review: **107**
- positive_candidate: **3**
- volatile_watchlist: **2**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 028050 | 삼성E&A | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 071050 | 한국금융지주 | investment_decision | volatile | pending | pending | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 009160 | SIMPAC | investment_decision | volatile | pending | pending | 66.00 | 0.00 | 66.00 | N/A |

## Watchlist Candidates

No candidates in this section.

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 001340 | PKC | major_shareholder_change | volatile | pending | pending | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 001340 | PKC | major_shareholder_change | volatile | pending | pending | 16.00 | 0.00 | 16.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 107640 | 한중엔시에스 | convertible_bond | negative | pending | pending | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 407400 | 꿈비 | lawsuit | negative | pending | pending | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
