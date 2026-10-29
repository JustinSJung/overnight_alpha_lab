# Market-Adjusted Evaluation Report - 2026-10-26

Generated at: 2026-10-26 00:56:11

Source feature file: `data/processed/market_adjusted_features_20261026.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **139**
- market_data_missing: **139**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | success | market_data_missing | -1.32% | N/A | N/A |
| 1970-01-01 | 010130 | 고려아연 | negative | failure | market_data_missing | 0.47% | N/A | N/A |
| 1970-01-01 | 010130 | 고려아연 | negative | failure | market_data_missing | 0.47% | N/A | N/A |
| 1970-01-01 | 005320 | 온타이드 | volatile | success | market_data_missing | -2.39% | N/A | N/A |
| 1970-01-01 | 005320 | 온타이드 | volatile | success | market_data_missing | -2.39% | N/A | N/A |
| 1970-01-01 | 005320 | 온타이드 | volatile | success | market_data_missing | -2.39% | N/A | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | positive | failure | market_data_missing | -1.30% | N/A | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | positive | failure | market_data_missing | -1.30% | N/A | N/A |
| 1970-01-01 | 040350 | 크레오에스지 | volatile | success | market_data_missing | -2.25% | N/A | N/A |
| 1970-01-01 | 030200 | 케이티 | negative | success | market_data_missing | -0.86% | N/A | N/A |
| 1970-01-01 | 030200 | 케이티 | negative | success | market_data_missing | -0.86% | N/A | N/A |
| 1970-01-01 | 018500 | 동원모빌리티 | negative | success | market_data_missing | -0.16% | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | failure | market_data_missing | 12.17% | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | failure | market_data_missing | 12.17% | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | failure | market_data_missing | 12.17% | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | failure | market_data_missing | 12.17% | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | failure | market_data_missing | 12.17% | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | failure | market_data_missing | 12.17% | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | failure | market_data_missing | 12.17% | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | failure | market_data_missing | 12.17% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
