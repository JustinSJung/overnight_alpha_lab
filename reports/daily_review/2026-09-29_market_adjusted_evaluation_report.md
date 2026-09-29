# Market-Adjusted Evaluation Report - 2026-09-29

Generated at: 2026-09-29 03:31:38

Source feature file: `data/processed/market_adjusted_features_20260929.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **202**
- market_data_missing: **202**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 402030 | 코난테크놀로지 | volatile | success | market_data_missing | -3.44% | N/A | N/A |
| 1970-01-01 | 092040 | 아미코젠 | negative | success | market_data_missing | -3.42% | N/A | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | volatile | success | market_data_missing | 6.56% | N/A | N/A |
| 1970-01-01 | 222080 | SFA넥셀 | positive | failure | market_data_missing | -3.42% | N/A | N/A |
| 1970-01-01 | 306620 | 지아이에스 | negative | failure | market_data_missing | 3.72% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |
| 1970-01-01 | 250030 | 진코스텍 | negative | failure | market_data_missing | 14.60% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
