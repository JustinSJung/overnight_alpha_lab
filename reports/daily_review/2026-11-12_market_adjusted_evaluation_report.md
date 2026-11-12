# Market-Adjusted Evaluation Report - 2026-11-12

Generated at: 2026-11-12 03:54:55

Source feature file: `data/processed/market_adjusted_features_20261112.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **146**
- market_data_missing: **146**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 7540 | 샘표 | volatile | failure | market_data_missing | -1.62% | N/A | N/A |
| 1970-01-01 | 248170 | 샘표식품 | volatile | failure | market_data_missing | -1.28% | N/A | N/A |
| 1970-01-01 | 9190 | 대양금속 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 26910 | 광진실업 | volatile | success | market_data_missing | -2.01% | N/A | N/A |
| 1970-01-01 | 26910 | 광진실업 | volatile | success | market_data_missing | -2.01% | N/A | N/A |
| 1970-01-01 | 26910 | 광진실업 | volatile | success | market_data_missing | -2.01% | N/A | N/A |
| 1970-01-01 | 26910 | 광진실업 | volatile | success | market_data_missing | -2.01% | N/A | N/A |
| 1970-01-01 | 26910 | 광진실업 | volatile | success | market_data_missing | -2.01% | N/A | N/A |
| 1970-01-01 | 26910 | 광진실업 | volatile | success | market_data_missing | -2.01% | N/A | N/A |
| 1970-01-01 | 26910 | 광진실업 | volatile | success | market_data_missing | -2.01% | N/A | N/A |
| 1970-01-01 | 26910 | 광진실업 | volatile | success | market_data_missing | -2.01% | N/A | N/A |
| 1970-01-01 | 115440 | 우리넷 | negative | success | market_data_missing | -1.54% | N/A | N/A |
| 1970-01-01 | 4150 | 한솔홀딩스 | volatile | failure | market_data_missing | -0.83% | N/A | N/A |
| 1970-01-01 | 4150 | 한솔홀딩스 | volatile | failure | market_data_missing | -0.83% | N/A | N/A |
| 1970-01-01 | 213500 | 한솔제지 | volatile | failure | market_data_missing | -1.56% | N/A | N/A |
| 1970-01-01 | 213500 | 한솔제지 | volatile | failure | market_data_missing | -1.56% | N/A | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | negative | success | market_data_missing | -2.55% | N/A | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | negative | success | market_data_missing | -2.55% | N/A | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | negative | success | market_data_missing | -2.55% | N/A | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | negative | success | market_data_missing | -2.55% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
