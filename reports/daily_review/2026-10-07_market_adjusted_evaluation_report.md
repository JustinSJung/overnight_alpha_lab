# Market-Adjusted Evaluation Report - 2026-10-07

Generated at: 2026-10-07 02:53:49

Source feature file: `data/processed/market_adjusted_features_20261007.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **237**
- market_data_missing: **237**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -14.12% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -14.12% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -14.12% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -14.12% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -14.12% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -14.12% | N/A | N/A |
| 1970-01-01 | 145210 | 다이나믹디자인 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 145210 | 다이나믹디자인 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | negative | success | market_data_missing | -2.91% | N/A | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | negative | success | market_data_missing | -2.91% | N/A | N/A |
| 1970-01-01 | 101360 | 에코앤드림 | negative | success | market_data_missing | -0.45% | N/A | N/A |
| 1970-01-01 | 119830 | 아이텍 | negative | success | market_data_missing | -1.55% | N/A | N/A |
| 1970-01-01 | 031860 | 디에이치엑스컴퍼니 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 418620 | E8 | volatile | success | market_data_missing | 6.89% | N/A | N/A |
| 1970-01-01 | 070300 | 퀀텀레일 | negative | failure | market_data_missing | 16.97% | N/A | N/A |
| 1970-01-01 | 070300 | 퀀텀레일 | negative | failure | market_data_missing | 16.97% | N/A | N/A |
| 1970-01-01 | 070300 | 퀀텀레일 | negative | failure | market_data_missing | 16.97% | N/A | N/A |
| 1970-01-01 | 002720 | 국제약품 | volatile | success | market_data_missing | 27.30% | N/A | N/A |
| 1970-01-01 | 002720 | 국제약품 | volatile | success | market_data_missing | 27.30% | N/A | N/A |
| 1970-01-01 | 002720 | 국제약품 | volatile | success | market_data_missing | 27.30% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
