# Market-Adjusted Evaluation Report - 2026-10-05

Generated at: 2026-10-05 01:19:24

Source feature file: `data/processed/market_adjusted_features_20261005.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **120**
- pending: **120**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 235980 | 메드팩토 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 3060 | 에이프로젠바이오로직스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 3060 | 에이프로젠바이오로직스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 3060 | 에이프로젠바이오로직스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 1040 | CJ | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 1040 | CJ | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 97950 | CJ제일제당 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 5930 | 삼성전자 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 205100 | 엑셈 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 469480 | IBKS제24호스팩 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 469480 | IBKS제24호스팩 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 469480 | IBKS제24호스팩 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 66790 | 씨씨에스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 27040 | 서울전자통신 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 27040 | 서울전자통신 | negative | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
