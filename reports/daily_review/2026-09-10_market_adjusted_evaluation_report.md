# Market-Adjusted Evaluation Report - 2026-09-10

Generated at: 2026-09-10 00:54:29

Source feature file: `data/processed/market_adjusted_features_20260910.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **228**
- market_data_missing: **227**
- pending: **1**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 288980 | 모아데이타 | negative | success | market_data_missing | -4.49% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | success | market_data_missing | -4.49% | N/A | N/A |
| 1970-01-01 | 35620 | 바른손이앤에이 | negative | failure | market_data_missing | 3.90% | N/A | N/A |
| 1970-01-01 | 6980 | 우성 | volatile | success | market_data_missing | -2.02% | N/A | N/A |
| 1970-01-01 | 357880 | SKAI | negative | success | market_data_missing | -2.41% | N/A | N/A |
| 1970-01-01 | 255220 | SG | positive | failure | market_data_missing | -0.25% | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | negative | failure | market_data_missing | 1.00% | N/A | N/A |
| 1970-01-01 | 294090 | 이오플로우 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 294090 | 이오플로우 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 109740 | 디에스케이 | volatile | failure | market_data_missing | -1.62% | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | negative | failure | market_data_missing | 2.89% | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | negative | failure | market_data_missing | 2.89% | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | negative | failure | market_data_missing | 2.89% | N/A | N/A |
| 1970-01-01 | 261780 | 아리바이오LAB | negative | failure | market_data_missing | 2.89% | N/A | N/A |
| 1970-01-01 | 310210 | 보로노이 | volatile | success | market_data_missing | -3.03% | N/A | N/A |
| 1970-01-01 | 310210 | 보로노이 | volatile | success | market_data_missing | -3.03% | N/A | N/A |
| 1970-01-01 | 310210 | 보로노이 | volatile | success | market_data_missing | -3.03% | N/A | N/A |
| 1970-01-01 | 310210 | 보로노이 | volatile | success | market_data_missing | -3.03% | N/A | N/A |
| 1970-01-01 | 310210 | 보로노이 | volatile | success | market_data_missing | -3.03% | N/A | N/A |
| 1970-01-01 | 310210 | 보로노이 | volatile | success | market_data_missing | -3.03% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
