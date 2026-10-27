# Market-Adjusted Evaluation Report - 2026-10-27

Generated at: 2026-10-27 02:02:54

Source feature file: `data/processed/market_adjusted_features_20261027.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **234**
- market_data_missing: **234**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 186230 | 그린플러스 | volatile | success | market_data_missing | -5.05% | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | success | market_data_missing | -5.05% | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | success | market_data_missing | -5.05% | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | success | market_data_missing | -5.05% | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | success | market_data_missing | -5.05% | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | success | market_data_missing | -5.05% | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | success | market_data_missing | -5.05% | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | success | market_data_missing | -5.05% | N/A | N/A |
| 1970-01-01 | 217730 | 강스템바이오텍 | volatile | failure | market_data_missing | -0.41% | N/A | N/A |
| 1970-01-01 | 90150 | 아이윈 | volatile | failure | market_data_missing | 1.97% | N/A | N/A |
| 1970-01-01 | 90150 | 아이윈 | volatile | failure | market_data_missing | 1.97% | N/A | N/A |
| 1970-01-01 | 60900 | 에이전트AI | negative | failure | market_data_missing | 5.19% | N/A | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | positive | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | positive | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 95700 | 제넥신 | negative | failure | market_data_missing | 0.64% | N/A | N/A |
| 1970-01-01 | 95700 | 제넥신 | negative | failure | market_data_missing | 0.64% | N/A | N/A |
| 1970-01-01 | 95700 | 제넥신 | negative | failure | market_data_missing | 0.64% | N/A | N/A |
| 1970-01-01 | 95700 | 제넥신 | negative | failure | market_data_missing | 0.64% | N/A | N/A |
| 1970-01-01 | 95700 | 제넥신 | negative | failure | market_data_missing | 0.64% | N/A | N/A |
| 1970-01-01 | 95700 | 제넥신 | negative | failure | market_data_missing | 0.64% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
