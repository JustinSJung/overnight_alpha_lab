# Market-Adjusted Evaluation Report - 2026-07-23

Generated at: 2026-07-23 23:15:37

Source feature file: `data/processed/market_adjusted_features_20260723.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **39**
- pending: **39**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 39200 | 오스코텍 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 39200 | 오스코텍 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 39200 | 오스코텍 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 39200 | 오스코텍 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 39200 | 오스코텍 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 39200 | 오스코텍 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 39200 | 오스코텍 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 39200 | 오스코텍 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 25560 | 미래산업 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 28080 | 휴맥스홀딩스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 89140 | 넥스턴앤롤코리아 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 71950 | 코아스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 1260 | 남광토건 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 1420 | 태원물산 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 5940 | NH투자증권 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 309930 | 조이웍스앤코 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 309930 | 조이웍스앤코 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 309930 | 조이웍스앤코 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 309930 | 조이웍스앤코 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 45390 | 대아티아이 | positive | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
