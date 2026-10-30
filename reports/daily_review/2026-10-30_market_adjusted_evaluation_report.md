# Market-Adjusted Evaluation Report - 2026-10-30

Generated at: 2026-10-30 02:28:15

Source feature file: `data/processed/market_adjusted_features_20261030.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **313**
- market_data_missing: **313**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 1470 | 삼부토건 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 72770 | 멤레이비티 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 72770 | 멤레이비티 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 72770 | 멤레이비티 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 88280 | 쏘닉스 | negative | success | market_data_missing | -6.61% | N/A | N/A |
| 1970-01-01 | 11000 | 진원생명과학 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 11000 | 진원생명과학 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 260870 | SK시그넷 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 260870 | SK시그넷 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 260870 | SK시그넷 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 445680 | 큐리옥스바이오시스템즈 | positive | failure | market_data_missing | -17.83% | N/A | N/A |
| 1970-01-01 | 246960 | SCL사이언스 | volatile | success | market_data_missing | -6.85% | N/A | N/A |
| 1970-01-01 | 90410 | 덕신이피씨 | positive | failure | market_data_missing | -2.78% | N/A | N/A |
| 1970-01-01 | 129260 | 인터지스 | volatile | failure | market_data_missing | -1.04% | N/A | N/A |
| 1970-01-01 | 129260 | 인터지스 | volatile | failure | market_data_missing | -1.04% | N/A | N/A |
| 1970-01-01 | 217320 | 썬테크 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 217320 | 썬테크 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 217320 | 썬테크 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 217320 | 썬테크 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 217320 | 썬테크 | negative | failure | market_data_missing | 0.00% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
