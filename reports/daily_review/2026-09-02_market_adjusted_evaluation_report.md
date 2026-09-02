# Market-Adjusted Evaluation Report - 2026-09-02

Generated at: 2026-09-02 00:49:25

Source feature file: `data/processed/market_adjusted_features_20260902.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **361**
- market_data_missing: **360**
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
| 1970-01-01 | 64290 | 인텍플러스 | positive | failure | market_data_missing | -2.04% | N/A | N/A |
| 1970-01-01 | 66430 | 아이로보틱스 | negative | success | market_data_missing | -2.11% | N/A | N/A |
| 1970-01-01 | 368770 | 파이버프로 | positive | failure | market_data_missing | -1.50% | N/A | N/A |
| 1970-01-01 | 45660 | 에이텍 | positive | success | market_data_missing | 0.65% | N/A | N/A |
| 1970-01-01 | 34020 | 두산에너빌리티 | positive | failure | market_data_missing | -2.70% | N/A | N/A |
| 1970-01-01 | 34020 | 두산에너빌리티 | positive | failure | market_data_missing | -2.70% | N/A | N/A |
| 1970-01-01 | 34020 | 두산에너빌리티 | positive | failure | market_data_missing | -2.70% | N/A | N/A |
| 1970-01-01 | 34020 | 두산에너빌리티 | positive | failure | market_data_missing | -2.70% | N/A | N/A |
| 1970-01-01 | 90080 | 평화산업 | volatile | failure | market_data_missing | -0.41% | N/A | N/A |
| 1970-01-01 | 90080 | 평화산업 | volatile | failure | market_data_missing | -0.41% | N/A | N/A |
| 1970-01-01 | 90080 | 평화산업 | volatile | failure | market_data_missing | -0.41% | N/A | N/A |
| 1970-01-01 | 21320 | KCC건설 | positive | failure | market_data_missing | -1.08% | N/A | N/A |
| 1970-01-01 | 2990 | 금호건설 | positive | failure | market_data_missing | -1.70% | N/A | N/A |
| 1970-01-01 | 92790 | 넥스틸 | volatile | failure | market_data_missing | -0.78% | N/A | N/A |
| 1970-01-01 | 3920 | 남양유업 | negative | success | market_data_missing | -0.90% | N/A | N/A |
| 1970-01-01 | 3920 | 남양유업 | negative | success | market_data_missing | -0.90% | N/A | N/A |
| 1970-01-01 | 3920 | 남양유업 | negative | success | market_data_missing | -0.90% | N/A | N/A |
| 1970-01-01 | 3920 | 남양유업 | negative | success | market_data_missing | -0.90% | N/A | N/A |
| 1970-01-01 | 27410 | BGF | volatile | failure | market_data_missing | -0.76% | N/A | N/A |
| 1970-01-01 | 26960 | 동서 | volatile | failure | market_data_missing | -0.78% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
