# Market-Adjusted Evaluation Report - 2026-07-01

Generated at: 2026-07-01 01:01:07

Source feature file: `data/processed/market_adjusted_features_20260701.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **4**
- pending: **4**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 468760 | 유진스팩10호 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 14790 | HL D&I | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 28050 | 삼성E&A | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 28050 | 삼성E&A | positive | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
