# Market-Adjusted Daily Candidate Report - 2026-10-26

Generated at: 2026-10-26 00:56:12

ML dataset source: `data/processed/ml_dataset_20261026.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261026.csv`

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

- Total rows: **457**
- risk_or_avoid_review: **318**
- positive_candidate: **116**
- watchlist_candidate: **23**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 420770 | 기가비스 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 347000 | 센코 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 347000 | 센코 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 044450 | KSS해운 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 026150 | 특수건설 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 002290 | 삼일기업공사 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 010400 | 우진아이엔에스 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 014790 | HL D&I | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 028260 | 삼성물산 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 402490 | 그린리소스 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 056730 | CNT85 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 131220 | 대한과학 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 002020 | 코오롱 | supply_contract | positive | failure | market_data_missing | 85.00 | 0.00 | 85.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 078930 | GS | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 166090 | 하나머티리얼즈 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 078930 | GS | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 339770 | 교촌에프앤비 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 339770 | 교촌에프앤비 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 095570 | AJ네트웍스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 095570 | AJ네트웍스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 051780 | 큐로홀딩스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 051780 | 큐로홀딩스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 353200 | 대덕전자 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 353200 | 대덕전자 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 040350 | 크레오에스지 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 353200 | 대덕전자 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 020000 | 한섬 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 005320 | 온타이드 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 020000 | 한섬 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 005320 | 온타이드 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 020000 | 한섬 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 078020 | LS증권 | lawsuit | negative | success | market_data_missing | 0.00 | 0.00 | 0.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | convertible_bond | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 000040 | KR모터스 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 000040 | KR모터스 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 000040 | KR모터스 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 000040 | KR모터스 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | paid_in_capital_increase | negative | failure | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | paid_in_capital_increase | negative | failure | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 114810 | 한솔아이원스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
