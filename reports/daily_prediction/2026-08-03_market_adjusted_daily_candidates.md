# Market-Adjusted Daily Candidate Report - 2026-08-03

Generated at: 2026-08-03 23:23:53

ML dataset source: `data/processed/ml_dataset_20260803.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260803.csv`

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

- Total rows: **25**
- risk_or_avoid_review: **11**
- positive_candidate: **10**
- watchlist_candidate: **4**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 255220 | SG | supply_contract | positive | pending | pending | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 032580 | 피델릭스 | supply_contract | positive | pending | pending | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 028100 | 동아지질 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 001260 | 남광토건 | investment_decision | volatile | pending | pending | 101.00 | 0.00 | 101.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | pending | pending | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 033310 | 엠투엔 | major_shareholder_change | volatile | pending | pending | 61.00 | 0.00 | 61.00 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | investment_decision | volatile | pending | pending | 61.00 | 0.00 | 61.00 | N/A |
| 1970-01-01 | 012630 | HDC | investment_decision | volatile | pending | pending | 56.00 | 0.00 | 56.00 | N/A |
| 1970-01-01 | 403490 | 우듬지팜 | spin_off | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 027580 | 상보 | major_shareholder_change | volatile | pending | pending | 41.00 | 0.00 | 41.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 031860 | 디에이치엑스컴퍼니 | investment_decision | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 031860 | 디에이치엑스컴퍼니 | investment_decision | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 178320 | 서진시스템 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 020150 | 롯데에너지머티리얼즈 | major_shareholder_change | volatile | pending | pending | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 060230 | 제이케이시냅스 | convertible_bond | negative | pending | pending | 0.00 | 0.00 | 0.00 | N/A |
| 1970-01-01 | 473980 | 노머스 | convertible_bond | negative | pending | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 473980 | 노머스 | convertible_bond | negative | pending | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 047920 | HLB제약 | paid_in_capital_increase | negative | pending | pending | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 148250 | 알엔투테크놀로지 | lawsuit | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 148250 | 알엔투테크놀로지 | lawsuit | negative | pending | pending | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | pending | pending | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 227610 | 아우딘퓨쳐스 | convertible_bond | negative | pending | pending | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
