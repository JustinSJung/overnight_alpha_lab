# Market-Adjusted Daily Candidate Report - 2026-11-12

Generated at: 2026-11-12 03:54:56

ML dataset source: `data/processed/ml_dataset_20261112.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261112.csv`

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

- Total rows: **434**
- risk_or_avoid_review: **214**
- positive_candidate: **121**
- watchlist_candidate: **97**
- volatile_watchlist: **2**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 013120 | 동원개발 | supply_contract | positive | failure | market_data_missing | 155.00 | 0.00 | 155.00 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 064480 | 브리지텍 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 002990 | 금호건설 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 388050 | 지투파워 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 006360 | GS건설 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 030530 | 원익홀딩스 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 005960 | 동부건설 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 189860 | 서전기전 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 093370 | 후성 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 093370 | 후성 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 046890 | 서울반도체 | earnings_guidance | neutral_positive | failure | market_data_missing | 78.00 | 0.00 | 78.00 | N/A |
| 1970-01-01 | 046890 | 서울반도체 | earnings_guidance | neutral_positive | failure | market_data_missing | 78.00 | 0.00 | 78.00 | N/A |
| 1970-01-01 | 081660 | 미스토홀딩스 | earnings_guidance | neutral_positive | failure | market_data_missing | 73.00 | 0.00 | 73.00 | N/A |
| 1970-01-01 | 081660 | 미스토홀딩스 | earnings_guidance | neutral_positive | failure | market_data_missing | 73.00 | 0.00 | 73.00 | N/A |
| 1970-01-01 | 081660 | 미스토홀딩스 | earnings_guidance | neutral_positive | failure | market_data_missing | 73.00 | 0.00 | 73.00 | N/A |
| 1970-01-01 | 081660 | 미스토홀딩스 | earnings_guidance | neutral_positive | failure | market_data_missing | 73.00 | 0.00 | 73.00 | N/A |
| 1970-01-01 | 453450 | 그리드위즈 | merger | volatile | success | market_data_missing | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 036570 | NC | earnings_guidance | neutral_positive | failure | market_data_missing | 63.00 | 0.00 | 63.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 009190 | 대양금속 | investment_decision | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 336260 | 두산퓨얼셀 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | bond_with_warrant | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 086520 | 에코프로 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | convertible_bond | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | convertible_bond | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | convertible_bond | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
