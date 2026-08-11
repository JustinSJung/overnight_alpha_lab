# Market-Adjusted Daily Candidate Report - 2026-08-11

Generated at: 2026-08-11 23:08:32

ML dataset source: `data/processed/ml_dataset_20260811.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260811.csv`

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

- Total rows: **53**
- positive_candidate: **40**
- risk_or_avoid_review: **9**
- watchlist_candidate: **2**
- volatile_watchlist: **2**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 199150 | 데이터스트림즈 | supply_contract | positive | pending | pending | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 002020 | 코오롱 | supply_contract | positive | pending | pending | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 002020 | 코오롱 | supply_contract | positive | pending | pending | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 002020 | 코오롱 | supply_contract | positive | pending | pending | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 068240 | 다원시스 | supply_contract | positive | pending | pending | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | pending | pending | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 000210 | DL | supply_contract | positive | pending | pending | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 006060 | 화승인더스트리 | investment_decision | volatile | pending | pending | 86.00 | 0.00 | 86.00 | N/A |
| 1970-01-01 | 375500 | DL이앤씨 | supply_contract | positive | pending | pending | 80.00 | 0.00 | 80.00 | N/A |
| 1970-01-01 | 089860 | 롯데렌탈 | investment_decision | volatile | pending | pending | 76.00 | 0.00 | 76.00 | N/A |
| 1970-01-01 | 089860 | 롯데렌탈 | investment_decision | volatile | pending | pending | 76.00 | 0.00 | 76.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 033270 | 유나이티드 | major_shareholder_change | volatile | pending | pending | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 019680 | 대교 | major_shareholder_change | volatile | pending | pending | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 228670 | 레이 | major_shareholder_change | volatile | pending | pending | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 348370 | 엔켐 | major_shareholder_change | volatile | pending | pending | 6.00 | 0.00 | 6.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 065420 | 에스아이리소스 | lawsuit | negative | pending | pending | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 378800 | 샤페론 | convertible_bond | negative | pending | pending | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 043260 | 성호전자 | bond_with_warrant | negative | pending | pending | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 060230 | 제이케이시냅스 | convertible_bond | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 060230 | 제이케이시냅스 | convertible_bond | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 187660 | 페니트리움바이오 | paid_in_capital_increase | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 060230 | 제이케이시냅스 | convertible_bond | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 060230 | 제이케이시냅스 | convertible_bond | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 340810 | 시선AI | convertible_bond | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
