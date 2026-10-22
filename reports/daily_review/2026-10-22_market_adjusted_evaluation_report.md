# Market-Adjusted Evaluation Report - 2026-10-22

Generated at: 2026-10-22 01:25:54

Source feature file: `data/processed/market_adjusted_features_20261022.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **169**
- market_data_missing: **169**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 11000 | 진원생명과학 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | failure | market_data_missing | 0.88% | N/A | N/A |
| 1970-01-01 | 43100 | 알파AI | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 43100 | 알파AI | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 43100 | 알파AI | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 305090 | 마이크로디지탈 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 305090 | 마이크로디지탈 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 305090 | 마이크로디지탈 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 305090 | 마이크로디지탈 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 84110 | 휴온스글로벌 | negative | failure | market_data_missing | 0.70% | N/A | N/A |
| 1970-01-01 | 243070 | 휴온스 | negative | success | market_data_missing | -0.50% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | failure | market_data_missing | 0.20% | N/A | N/A |
| 1970-01-01 | 38060 | 루멘스바이오스 | negative | success | market_data_missing | -1.51% | N/A | N/A |
| 1970-01-01 | 38060 | 루멘스바이오스 | negative | success | market_data_missing | -1.51% | N/A | N/A |
| 1970-01-01 | 38060 | 루멘스바이오스 | negative | success | market_data_missing | -1.51% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | success | market_data_missing | -2.01% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | success | market_data_missing | -2.01% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | success | market_data_missing | -2.01% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
