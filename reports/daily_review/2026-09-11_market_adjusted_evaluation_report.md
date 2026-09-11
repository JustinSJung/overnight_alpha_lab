# Market-Adjusted Evaluation Report - 2026-09-11

Generated at: 2026-09-11 01:09:40

Source feature file: `data/processed/market_adjusted_features_20260911.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **244**
- market_data_missing: **244**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 317400 | 자이에스앤디 | volatile | failure | market_data_missing | 1.50% | N/A | N/A |
| 1970-01-01 | 11300 | 우성머티리얼스 | negative | failure | market_data_missing | 6.05% | N/A | N/A |
| 1970-01-01 | 11300 | 우성머티리얼스 | negative | failure | market_data_missing | 6.05% | N/A | N/A |
| 1970-01-01 | 11300 | 우성머티리얼스 | negative | failure | market_data_missing | 6.05% | N/A | N/A |
| 1970-01-01 | 9810 | MDS스피어 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |
| 1970-01-01 | 1390 | KG케미칼 | volatile | failure | market_data_missing | -0.67% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
