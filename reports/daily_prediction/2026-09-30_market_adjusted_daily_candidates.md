# Market-Adjusted Daily Candidate Report - 2026-09-30

Generated at: 2026-09-30 02:55:23

ML dataset source: `data/processed/ml_dataset_20260930.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260930.csv`

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

- Total rows: **1015**
- positive_candidate: **672**
- risk_or_avoid_review: **317**
- watchlist_candidate: **24**
- volatile_watchlist: **2**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 003030 | 세아제강지주 | supply_contract | positive | success | market_data_missing | 165.00 | 0.00 | 165.00 | N/A |
| 1970-01-01 | 306200 | 세아제강 | supply_contract | positive | success | market_data_missing | 160.00 | 0.00 | 160.00 | N/A |
| 1970-01-01 | 032580 | 피델릭스 | supply_contract | positive | success | market_data_missing | 155.00 | 0.00 | 155.00 | N/A |
| 1970-01-01 | 017000 | 신원종합개발 | supply_contract | positive | failure | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 303360 | 프로티아 | bonus_issue | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 142210 | 유니트론텍 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 142210 | 유니트론텍 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 298040 | 효성중공업 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 298040 | 효성중공업 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 298040 | 효성중공업 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 418620 | E8 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 012030 | DB | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 012030 | DB | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 013520 | 화승코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 298000 | 효성화학 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 012030 | DB | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 298000 | 효성화학 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 298000 | 효성화학 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 298000 | 효성화학 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 244920 | 에이플러스에셋 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 016610 | DB증권 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 016610 | DB증권 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 016610 | DB증권 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 004970 | 신라교역 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 004970 | 신라교역 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 320000 | 한울반도체 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 369370 | 블리츠웨이엔터테인먼트 | convertible_bond | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 038880 | 아이에이 | paid_in_capital_increase | negative | failure | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 015590 | DKME | lawsuit | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
