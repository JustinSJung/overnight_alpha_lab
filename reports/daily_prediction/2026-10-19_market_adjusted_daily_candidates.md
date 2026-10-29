# Market-Adjusted Daily Candidate Report - 2026-10-19

Generated at: 2026-10-19 00:38:25

ML dataset source: `data/processed/ml_dataset_20261019.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261019.csv`

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

- Total rows: **1913**
- risk_or_avoid_review: **1690**
- watchlist_candidate: **172**
- positive_candidate: **38**
- volatile_watchlist: **13**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 215090 | 솔디펜스 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 215090 | 솔디펜스 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 215090 | 솔디펜스 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 215090 | 솔디펜스 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 222420 | 쎄노텍 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 348350 | 위드텍 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 089790 | 제이티 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 028100 | 동아지질 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 475230 | 엔알비 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 004800 | 효성 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 000640 | 동아제약 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 019660 | 글로본 | supply_contract | positive | success | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 189330 | 씨이랩 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 025560 | 미래산업 | supply_contract | positive | failure | market_data_missing | 85.00 | 0.00 | 85.00 | N/A |
| 1970-01-01 | 025560 | 미래산업 | supply_contract | positive | failure | market_data_missing | 85.00 | 0.00 | 85.00 | N/A |
| 1970-01-01 | 025560 | 미래산업 | supply_contract | positive | failure | market_data_missing | 85.00 | 0.00 | 85.00 | N/A |
| 1970-01-01 | 025560 | 미래산업 | supply_contract | positive | failure | market_data_missing | 85.00 | 0.00 | 85.00 | N/A |
| 1970-01-01 | 0203K0 | 송우인포텍 | supply_contract | positive | failure | market_data_missing | 75.00 | 0.00 | 75.00 | N/A |
| 1970-01-01 | 498390 | 한화플러스제5호스팩 | merger | volatile | failure | market_data_missing | 71.00 | 0.00 | 71.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 078930 | GS | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 246720 | 아스타 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 020000 | 한섬 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 020000 | 한섬 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 210980 | SK디앤디 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 210980 | SK디앤디 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 210980 | SK디앤디 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 020000 | 한섬 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004890 | 동일산업 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 065570 | 삼영이엔씨 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 006570 | 대림통상 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 006570 | 대림통상 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 006570 | 대림통상 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 006570 | 대림통상 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 290650 | 엘앤씨바이오 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 115180 | 큐리언트 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
