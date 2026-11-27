# Market-Adjusted Evaluation Report - 2026-11-27

Generated at: 2026-11-27 05:31:52

Source feature file: `data/processed/market_adjusted_features_20261127.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **207**
- market_data_missing: **207**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 115180 | 큐리언트 | negative | failure | market_data_missing | 29.25% | N/A | N/A |
| 1970-01-01 | 212310 | 오건에코텍 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 212310 | 오건에코텍 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 212310 | 오건에코텍 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | success | market_data_missing | -1.30% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | success | market_data_missing | -1.30% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | success | market_data_missing | -1.30% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | success | market_data_missing | -1.30% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | success | market_data_missing | -1.30% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | success | market_data_missing | -1.30% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | success | market_data_missing | -1.30% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | success | market_data_missing | -1.30% | N/A | N/A |
| 1970-01-01 | 3470 | 유안타증권 | volatile | success | market_data_missing | 5.61% | N/A | N/A |
| 1970-01-01 | 3470 | 유안타증권 | volatile | success | market_data_missing | 5.61% | N/A | N/A |
| 1970-01-01 | 159910 | 에코글로우 | negative | success | market_data_missing | -3.94% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | positive | failure | market_data_missing | -8.81% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | positive | failure | market_data_missing | -8.81% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | positive | failure | market_data_missing | -8.81% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | positive | failure | market_data_missing | -8.81% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | positive | failure | market_data_missing | -8.81% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
