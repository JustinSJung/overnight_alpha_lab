# Market-Adjusted Evaluation Report - 2026-09-22

Generated at: 2026-09-22 02:09:03

Source feature file: `data/processed/market_adjusted_features_20260922.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **301**
- market_data_missing: **301**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 002990 | 금호건설 | positive | failure | market_data_missing | -2.47% | N/A | N/A |
| 1970-01-01 | 002990 | 금호건설 | positive | failure | market_data_missing | -2.47% | N/A | N/A |
| 1970-01-01 | 002990 | 금호건설 | positive | failure | market_data_missing | -2.47% | N/A | N/A |
| 1970-01-01 | 002990 | 금호건설 | positive | failure | market_data_missing | -2.47% | N/A | N/A |
| 1970-01-01 | 002990 | 금호건설 | negative | success | market_data_missing | -2.47% | N/A | N/A |
| 1970-01-01 | 002990 | 금호건설 | negative | success | market_data_missing | -2.47% | N/A | N/A |
| 1970-01-01 | 002990 | 금호건설 | negative | success | market_data_missing | -2.47% | N/A | N/A |
| 1970-01-01 | 002990 | 금호건설 | negative | success | market_data_missing | -2.47% | N/A | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | negative | success | market_data_missing | -2.11% | N/A | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | negative | success | market_data_missing | -2.11% | N/A | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | negative | success | market_data_missing | -2.11% | N/A | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | negative | success | market_data_missing | -2.11% | N/A | N/A |
| 1970-01-01 | 127710 | 아시아경제 | volatile | success | market_data_missing | -2.67% | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | success | market_data_missing | -1.52% | N/A | N/A |
| 1970-01-01 | 148250 | 알엔투테크놀로지 | negative | success | market_data_missing | -0.49% | N/A | N/A |
| 1970-01-01 | 026150 | 특수건설 | negative | success | market_data_missing | -2.78% | N/A | N/A |
| 1970-01-01 | 377450 | 리파인 | negative | success | market_data_missing | -0.34% | N/A | N/A |
| 1970-01-01 | 377450 | 리파인 | negative | success | market_data_missing | -0.34% | N/A | N/A |
| 1970-01-01 | 377450 | 리파인 | negative | success | market_data_missing | -0.34% | N/A | N/A |
| 1970-01-01 | 122450 | KX | volatile | failure | market_data_missing | -0.38% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
