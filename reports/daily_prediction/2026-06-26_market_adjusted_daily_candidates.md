# Market-Adjusted Daily Candidate Report - 2026-06-26

Generated at: 2026-06-26 16:39:46

ML dataset source: `data/processed/ml_dataset_20260626.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260626.csv`

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

- Total rows: **19**
- risk_or_avoid_review: **9**
- positive_candidate: **7**
- watchlist_candidate: **3**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 282720 | 금양그린파워 | supply_contract | positive | nan | pending | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 258610 | 케일럼 | supply_contract | positive | nan | pending | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 005960 | 동부건설 | supply_contract | positive | nan | pending | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 277880 | 티에스아이 | supply_contract | positive | nan | pending | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 476830 | 알지노믹스 | bonus_issue | positive | nan | pending | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | supply_contract | positive | nan | pending | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | nan | pending | 56.00 | 0.00 | 56.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 214150 | 클래시스 | major_shareholder_change | volatile | nan | pending | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 214150 | 클래시스 | major_shareholder_change | volatile | nan | pending | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 214150 | 클래시스 | major_shareholder_change | volatile | nan | pending | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | nan | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | nan | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | paid_in_capital_increase | negative | nan | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 138360 | 앤로보틱스 | paid_in_capital_increase | negative | nan | pending | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | convertible_bond | negative | nan | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 003450 | 케이비증권 | paid_in_capital_increase | negative | nan | nan | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 361610 | SK아이이테크놀로지 | paid_in_capital_increase | negative | nan | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 105560 | KB금융 | paid_in_capital_increase | negative | nan | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | nan | pending | -80.00 | 0.00 | -80.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
