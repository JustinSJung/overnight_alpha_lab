# Market-Adjusted Evaluation Report - 2026-09-15

Generated at: 2026-09-15 01:44:42

Source feature file: `data/processed/market_adjusted_features_20260915.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **194**
- market_data_missing: **192**
- pending: **2**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 079190 | 케스피온 | volatile | success | market_data_missing | -9.50% | N/A | N/A |
| 1970-01-01 | 079190 | 케스피온 | volatile | success | market_data_missing | -9.50% | N/A | N/A |
| 1970-01-01 | 079190 | 케스피온 | volatile | success | market_data_missing | -9.50% | N/A | N/A |
| 1970-01-01 | 079190 | 케스피온 | volatile | success | market_data_missing | -9.50% | N/A | N/A |
| 1970-01-01 | 079190 | 케스피온 | volatile | success | market_data_missing | -9.50% | N/A | N/A |
| 1970-01-01 | 079190 | 케스피온 | volatile | success | market_data_missing | -9.50% | N/A | N/A |
| 1970-01-01 | 331920 | 셀레믹스 | negative | success | market_data_missing | -0.92% | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | failure | market_data_missing | 1.60% | N/A | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | negative | success | market_data_missing | -11.42% | N/A | N/A |
| 1970-01-01 | 002780 | 진흥기업 | positive | failure | market_data_missing | -1.58% | N/A | N/A |
| 1970-01-01 | 058110 | 멕아이씨에스 | negative | success | market_data_missing | -1.66% | N/A | N/A |
| 1970-01-01 | 058110 | 멕아이씨에스 | negative | success | market_data_missing | -1.66% | N/A | N/A |
| 1970-01-01 | 058110 | 멕아이씨에스 | negative | success | market_data_missing | -1.66% | N/A | N/A |
| 1970-01-01 | 058110 | 멕아이씨에스 | negative | success | market_data_missing | -1.66% | N/A | N/A |
| 1970-01-01 | 389020 | 자람테크놀로지 | positive | failure | market_data_missing | -4.27% | N/A | N/A |
| 1970-01-01 | 222080 | SFA넥셀 | positive | success | market_data_missing | 2.47% | N/A | N/A |
| 1970-01-01 | 027740 | 마니커 | volatile | failure | market_data_missing | -1.38% | N/A | N/A |
| 1970-01-01 | 027740 | 마니커 | volatile | failure | market_data_missing | -1.38% | N/A | N/A |
| 1970-01-01 | 027740 | 마니커 | volatile | failure | market_data_missing | -1.38% | N/A | N/A |
| 1970-01-01 | 038870 | 에코심플렉스 | positive | failure | market_data_missing | -2.61% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
