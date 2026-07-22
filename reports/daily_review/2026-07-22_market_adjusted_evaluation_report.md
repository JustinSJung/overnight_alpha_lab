# Market-Adjusted Evaluation Report - 2026-07-22

Generated at: 2026-07-22 23:18:48

Source feature file: `data/processed/market_adjusted_features_20260722.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **35**
- pending: **35**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 005960 | 동부건설 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 002990 | 금호건설 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 114450 | 그린생명과학 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 0009K0 | 에임드바이오 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 009420 | 한올바이오파마 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 203650 | 드림시큐리티 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
