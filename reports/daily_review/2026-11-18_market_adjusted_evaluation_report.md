# Market-Adjusted Evaluation Report - 2026-11-18

Generated at: 2026-11-18 04:50:52

Source feature file: `data/processed/market_adjusted_features_20261118.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **115**
- market_data_missing: **115**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 331920 | 셀레믹스 | volatile | success | market_data_missing | -13.05% | N/A | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | volatile | success | market_data_missing | -4.84% | N/A | N/A |
| 1970-01-01 | 25560 | 미래산업 | positive | failure | market_data_missing | -9.25% | N/A | N/A |
| 1970-01-01 | 18620 | 우진비앤지 | negative | success | market_data_missing | -1.47% | N/A | N/A |
| 1970-01-01 | 18620 | 우진비앤지 | negative | success | market_data_missing | -1.47% | N/A | N/A |
| 1970-01-01 | 18620 | 우진비앤지 | negative | success | market_data_missing | -1.47% | N/A | N/A |
| 1970-01-01 | 18620 | 우진비앤지 | negative | success | market_data_missing | -1.47% | N/A | N/A |
| 1970-01-01 | 18620 | 우진비앤지 | negative | success | market_data_missing | -1.47% | N/A | N/A |
| 1970-01-01 | 18620 | 우진비앤지 | negative | success | market_data_missing | -1.47% | N/A | N/A |
| 1970-01-01 | 89140 | 넥스턴앤롤코리아 | negative | success | market_data_missing | -5.96% | N/A | N/A |
| 1970-01-01 | 89140 | 넥스턴앤롤코리아 | negative | success | market_data_missing | -5.96% | N/A | N/A |
| 1970-01-01 | 89140 | 넥스턴앤롤코리아 | negative | success | market_data_missing | -5.96% | N/A | N/A |
| 1970-01-01 | 89140 | 넥스턴앤롤코리아 | negative | success | market_data_missing | -5.96% | N/A | N/A |
| 1970-01-01 | 89140 | 넥스턴앤롤코리아 | negative | success | market_data_missing | -5.96% | N/A | N/A |
| 1970-01-01 | 89140 | 넥스턴앤롤코리아 | negative | success | market_data_missing | -5.96% | N/A | N/A |
| 1970-01-01 | 89140 | 넥스턴앤롤코리아 | negative | success | market_data_missing | -5.96% | N/A | N/A |
| 1970-01-01 | 89140 | 넥스턴앤롤코리아 | negative | success | market_data_missing | -5.96% | N/A | N/A |
| 1970-01-01 | 9970 | 영원무역홀딩스 | negative | success | market_data_missing | -4.16% | N/A | N/A |
| 1970-01-01 | 9970 | 영원무역홀딩스 | negative | success | market_data_missing | -4.16% | N/A | N/A |
| 1970-01-01 | 18620 | 우진비앤지 | negative | success | market_data_missing | -1.47% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
