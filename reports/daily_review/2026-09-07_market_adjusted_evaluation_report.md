# Market-Adjusted Evaluation Report - 2026-09-07

Generated at: 2026-09-07 00:27:24

Source feature file: `data/processed/market_adjusted_features_20260907.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **191**
- market_data_missing: **191**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 361610 | SK아이이테크놀로지 | volatile | failure | market_data_missing | -1.17% | N/A | N/A |
| 1970-01-01 | 096770 | SK이노베이션 | volatile | failure | market_data_missing | -1.45% | N/A | N/A |
| 1970-01-01 | 208640 | 썸에이지 | negative | failure | market_data_missing | 0.15% | N/A | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | success | market_data_missing | -0.38% | N/A | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | success | market_data_missing | -0.38% | N/A | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | success | market_data_missing | -0.38% | N/A | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | success | market_data_missing | -0.38% | N/A | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | success | market_data_missing | -0.38% | N/A | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | success | market_data_missing | -0.38% | N/A | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | success | market_data_missing | -0.38% | N/A | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | success | market_data_missing | -0.38% | N/A | N/A |
| 1970-01-01 | 092870 | 엑시콘 | positive | failure | market_data_missing | -4.75% | N/A | N/A |
| 1970-01-01 | 376270 | HEM파마 | positive | failure | market_data_missing | -1.42% | N/A | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 011090 | 에넥스 | negative | failure | market_data_missing | 3.68% | N/A | N/A |
| 1970-01-01 | 011090 | 에넥스 | negative | failure | market_data_missing | 3.68% | N/A | N/A |
| 1970-01-01 | 011090 | 에넥스 | negative | failure | market_data_missing | 3.68% | N/A | N/A |
| 1970-01-01 | 011090 | 에넥스 | negative | failure | market_data_missing | 3.68% | N/A | N/A |
| 1970-01-01 | 011090 | 에넥스 | negative | failure | market_data_missing | 3.68% | N/A | N/A |
| 1970-01-01 | 011090 | 에넥스 | negative | failure | market_data_missing | 3.68% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
