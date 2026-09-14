# Market-Adjusted Evaluation Report - 2026-09-14

Generated at: 2026-09-14 00:59:51

Source feature file: `data/processed/market_adjusted_features_20260914.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **179**
- market_data_missing: **179**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 2990 | 금호건설 | positive | failure | market_data_missing | -2.31% | N/A | N/A |
| 1970-01-01 | 256940 | 킵스파마 | volatile | failure | market_data_missing | 1.42% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | success | market_data_missing | -1.62% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | success | market_data_missing | -1.62% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | success | market_data_missing | -1.62% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | success | market_data_missing | -1.62% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | success | market_data_missing | -1.62% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | success | market_data_missing | -1.62% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | success | market_data_missing | -1.62% | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | success | market_data_missing | -1.62% | N/A | N/A |
| 1970-01-01 | 203400 | 에이비온 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | negative | failure | market_data_missing | 29.90% | N/A | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | failure | market_data_missing | 1.76% | N/A | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | failure | market_data_missing | 5.85% | N/A | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | failure | market_data_missing | 5.85% | N/A | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | failure | market_data_missing | 5.85% | N/A | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | failure | market_data_missing | 5.85% | N/A | N/A |
| 1970-01-01 | 119830 | 아이텍 | negative | failure | market_data_missing | 2.56% | N/A | N/A |
| 1970-01-01 | 119830 | 아이텍 | negative | failure | market_data_missing | 2.56% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
