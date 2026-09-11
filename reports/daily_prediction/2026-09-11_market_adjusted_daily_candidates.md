# Market-Adjusted Daily Candidate Report - 2026-09-11

Generated at: 2026-09-11 01:09:41

ML dataset source: `data/processed/ml_dataset_20260911.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260911.csv`

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

- Total rows: **856**
- risk_or_avoid_review: **573**
- positive_candidate: **231**
- watchlist_candidate: **26**
- volatile_watchlist: **26**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 083650 | 비에이치아이 | supply_contract | positive | success | market_data_missing | 160.00 | 0.00 | 160.00 | N/A |
| 1970-01-01 | 023590 | 다우기술 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 032580 | 피델릭스 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 083790 | CG인바이츠 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 005880 | 대한해운 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 277880 | 티에스아이 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 006360 | GS건설 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 006360 | GS건설 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 006360 | GS건설 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 006360 | GS건설 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 041960 | 코미팜 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 043910 | 자연과환경 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 004870 | 티웨이홀딩스 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 004870 | 티웨이홀딩스 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 038290 | 마크로젠 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 007570 | 일양약품 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 432720 | 퀄리타스반도체 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 007570 | 일양약품 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 007570 | 일양약품 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 282330 | BGF리테일 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 282330 | BGF리테일 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 109070 | 주성코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 006800 | 미래에셋증권 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 006800 | 미래에셋증권 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 006800 | 미래에셋증권 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 006800 | 미래에셋증권 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 006800 | 미래에셋증권 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 006800 | 미래에셋증권 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 145270 | 케이탑리츠 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 006800 | 미래에셋증권 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 006800 | 미래에셋증권 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 001390 | KG케미칼 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 001390 | KG케미칼 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 001390 | KG케미칼 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 001390 | KG케미칼 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 001390 | KG케미칼 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 001390 | KG케미칼 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 001390 | KG케미칼 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 001390 | KG케미칼 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 001390 | KG케미칼 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 001390 | KG케미칼 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 001390 | KG케미칼 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 030210 | 다올투자증권 | lawsuit | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 307180 | 아이엘 | convertible_bond | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 307180 | 아이엘 | convertible_bond | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 290690 | 아리바이오홀딩스 | convertible_bond | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | paid_in_capital_increase | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
