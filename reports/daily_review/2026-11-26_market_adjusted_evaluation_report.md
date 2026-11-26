# Market-Adjusted Evaluation Report - 2026-11-26

Generated at: 2026-11-26 04:59:06

Source feature file: `data/processed/market_adjusted_features_20261126.csv`

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
| 1970-01-01 | 18620 | 우진비앤지 | volatile | failure | market_data_missing | -1.87% | N/A | N/A |
| 1970-01-01 | 18620 | 우진비앤지 | volatile | failure | market_data_missing | -1.87% | N/A | N/A |
| 1970-01-01 | 95700 | 제넥신 | negative | failure | market_data_missing | 7.99% | N/A | N/A |
| 1970-01-01 | 71280 | 로체시스템즈 | positive | success | market_data_missing | 5.99% | N/A | N/A |
| 1970-01-01 | 42660 | 한화오션 | volatile | failure | market_data_missing | 1.52% | N/A | N/A |
| 1970-01-01 | 42660 | 한화오션 | volatile | failure | market_data_missing | 1.52% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |
| 1970-01-01 | 10170 | 대한광통신 | volatile | success | market_data_missing | 3.06% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
