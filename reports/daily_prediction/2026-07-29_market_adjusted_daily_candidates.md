# Market-Adjusted Daily Candidate Report - 2026-07-29

Generated at: 2026-07-29 23:18:03

ML dataset source: `data/processed/ml_dataset_20260729.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260729.csv`

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

- Total rows: **24**
- risk_or_avoid_review: **10**
- positive_candidate: **8**
- volatile_watchlist: **6**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 054220 | 비츠로시스 | supply_contract | positive | pending | pending | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 010780 | 아이에스동서 | supply_contract | positive | pending | pending | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 001260 | 남광토건 | supply_contract | positive | pending | pending | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | pending | pending | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | 75.00 | 0.00 | 75.00 | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | 75.00 | 0.00 | 75.00 | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | 75.00 | 0.00 | 75.00 | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | 75.00 | 0.00 | 75.00 | N/A |

## Watchlist Candidates

No candidates in this section.

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 066790 | 씨씨에스 | major_shareholder_change | volatile | pending | pending | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | pending | pending | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | major_shareholder_change | volatile | pending | pending | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | major_shareholder_change | volatile | pending | pending | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | major_shareholder_change | volatile | pending | pending | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | major_shareholder_change | volatile | pending | pending | 1.00 | 0.00 | 1.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 115530 | 씨엔플러스 | convertible_bond | negative | pending | pending | 0.00 | 0.00 | 0.00 | N/A |
| 1970-01-01 | 115530 | 씨엔플러스 | convertible_bond | negative | pending | pending | 0.00 | 0.00 | 0.00 | N/A |
| 1970-01-01 | 115530 | 씨엔플러스 | convertible_bond | negative | pending | pending | 0.00 | 0.00 | 0.00 | N/A |
| 1970-01-01 | 115530 | 씨엔플러스 | convertible_bond | negative | pending | pending | 0.00 | 0.00 | 0.00 | N/A |
| 1970-01-01 | 017810 | 풀무원 | paid_in_capital_increase | negative | pending | pending | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 017810 | 풀무원 | paid_in_capital_increase | negative | pending | pending | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 340360 | 다보링크 | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 340360 | 다보링크 | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 121440 | 골프존홀딩스 | disclosure_violation | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
