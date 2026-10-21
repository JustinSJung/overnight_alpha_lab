# Market-Adjusted Evaluation Report - 2026-10-21

Generated at: 2026-10-21 01:15:44

Source feature file: `data/processed/market_adjusted_features_20261021.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **72**
- market_data_missing: **72**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 278470 | 에이피알 | negative | failure | market_data_missing | 3.61% | N/A | N/A |
| 1970-01-01 | 95910 | 에스에너지 | positive | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 117670 | 알파칩스 | positive | success | market_data_missing | 1.84% | N/A | N/A |
| 1970-01-01 | 310210 | 보로노이 | volatile | success | market_data_missing | 8.27% | N/A | N/A |
| 1970-01-01 | 2990 | 금호건설 | negative | failure | market_data_missing | 3.99% | N/A | N/A |
| 1970-01-01 | 2990 | 금호건설 | negative | failure | market_data_missing | 3.99% | N/A | N/A |
| 1970-01-01 | 2990 | 금호건설 | negative | failure | market_data_missing | 3.99% | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | negative | failure | market_data_missing | 4.73% | N/A | N/A |
| 1970-01-01 | 69640 | 한세엠케이 | volatile | failure | market_data_missing | 0.14% | N/A | N/A |
| 1970-01-01 | 69640 | 한세엠케이 | volatile | failure | market_data_missing | 0.14% | N/A | N/A |
| 1970-01-01 | 69640 | 한세엠케이 | volatile | failure | market_data_missing | 0.14% | N/A | N/A |
| 1970-01-01 | 1750 | 한양증권 | negative | success | market_data_missing | -0.53% | N/A | N/A |
| 1970-01-01 | 97780 | 에코볼트 | volatile | failure | market_data_missing | -1.17% | N/A | N/A |
| 1970-01-01 | 122640 | 예스티 | positive | success | market_data_missing | 13.95% | N/A | N/A |
| 1970-01-01 | 484810 | 티엑스알로보틱스 | negative | failure | market_data_missing | 2.23% | N/A | N/A |
| 1970-01-01 | 2290 | 삼일기업공사 | positive | success | market_data_missing | 0.31% | N/A | N/A |
| 1970-01-01 | 25000 | KPX케미칼 | volatile | success | market_data_missing | -2.94% | N/A | N/A |
| 1970-01-01 | 25000 | KPX케미칼 | volatile | success | market_data_missing | -2.94% | N/A | N/A |
| 1970-01-01 | 25000 | KPX케미칼 | volatile | success | market_data_missing | -2.94% | N/A | N/A |
| 1970-01-01 | 28260 | 삼성물산 | volatile | success | market_data_missing | 5.88% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
