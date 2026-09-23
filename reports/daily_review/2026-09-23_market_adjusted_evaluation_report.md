# Market-Adjusted Evaluation Report - 2026-09-23

Generated at: 2026-09-23 02:02:20

Source feature file: `data/processed/market_adjusted_features_20260923.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **148**
- market_data_missing: **148**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 299660 | 셀리드 | negative | failure | market_data_missing | 6.93% | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | failure | market_data_missing | 6.93% | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | failure | market_data_missing | 6.93% | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | failure | market_data_missing | 6.93% | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | failure | market_data_missing | 6.93% | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | failure | market_data_missing | 6.93% | N/A | N/A |
| 1970-01-01 | 013700 | 까뮤이앤씨 | negative | success | market_data_missing | -2.58% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | success | market_data_missing | -1.37% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | success | market_data_missing | -1.37% | N/A | N/A |
| 1970-01-01 | 025560 | 미래산업 | positive | success | market_data_missing | 0.78% | N/A | N/A |
| 1970-01-01 | 011790 | SKC | volatile | failure | market_data_missing | 1.13% | N/A | N/A |
| 1970-01-01 | 011790 | SKC | volatile | failure | market_data_missing | 1.13% | N/A | N/A |
| 1970-01-01 | 011790 | SKC | volatile | failure | market_data_missing | 1.13% | N/A | N/A |
| 1970-01-01 | 011790 | SKC | volatile | failure | market_data_missing | 1.13% | N/A | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | failure | market_data_missing | 0.27% | N/A | N/A |
| 1970-01-01 | 457600 | 벡트 | volatile | failure | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 457600 | 벡트 | volatile | failure | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 457600 | 벡트 | volatile | failure | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 457600 | 벡트 | volatile | failure | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 024830 | 세원물산 | positive | success | market_data_missing | 0.72% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
