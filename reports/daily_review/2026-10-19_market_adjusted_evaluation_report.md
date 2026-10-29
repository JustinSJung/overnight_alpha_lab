# Market-Adjusted Evaluation Report - 2026-10-19

Generated at: 2026-10-19 00:38:25

Source feature file: `data/processed/market_adjusted_features_20261019.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **227**
- market_data_missing: **227**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 148780 | 비큐AI | volatile | failure | market_data_missing | -1.43% | N/A | N/A |
| 1970-01-01 | 083660 | CSA 코스믹 | negative | failure | market_data_missing | 16.51% | N/A | N/A |
| 1970-01-01 | 083660 | CSA 코스믹 | negative | failure | market_data_missing | 16.51% | N/A | N/A |
| 1970-01-01 | 083660 | CSA 코스믹 | negative | failure | market_data_missing | 16.51% | N/A | N/A |
| 1970-01-01 | 083660 | CSA 코스믹 | negative | failure | market_data_missing | 16.51% | N/A | N/A |
| 1970-01-01 | 083660 | CSA 코스믹 | negative | failure | market_data_missing | 16.51% | N/A | N/A |
| 1970-01-01 | 083660 | CSA 코스믹 | negative | failure | market_data_missing | 16.51% | N/A | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 060260 | 뉴보텍 | negative | success | market_data_missing | -5.59% | N/A | N/A |
| 1970-01-01 | 060260 | 뉴보텍 | negative | success | market_data_missing | -5.59% | N/A | N/A |
| 1970-01-01 | 060260 | 뉴보텍 | negative | success | market_data_missing | -5.59% | N/A | N/A |
| 1970-01-01 | 060260 | 뉴보텍 | negative | success | market_data_missing | -5.59% | N/A | N/A |
| 1970-01-01 | 060260 | 뉴보텍 | negative | success | market_data_missing | -5.59% | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | success | market_data_missing | -0.52% | N/A | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 002240 | 고려제강 | volatile | failure | market_data_missing | -1.61% | N/A | N/A |
| 1970-01-01 | 002240 | 고려제강 | volatile | failure | market_data_missing | -1.61% | N/A | N/A |
| 1970-01-01 | 002240 | 고려제강 | volatile | failure | market_data_missing | -1.61% | N/A | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 065570 | 삼영이엔씨 | negative | failure | market_data_missing | 0.00% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
