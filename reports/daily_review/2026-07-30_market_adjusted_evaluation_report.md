# Market-Adjusted Evaluation Report - 2026-07-30

Generated at: 2026-07-30 23:22:05

Source feature file: `data/processed/market_adjusted_features_20260730.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **68**
- pending: **68**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 660 | SK하이닉스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 12630 | HDC | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 12630 | HDC | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 58450 | 한주에이알티 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 58450 | 한주에이알티 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 378800 | 샤페론 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
