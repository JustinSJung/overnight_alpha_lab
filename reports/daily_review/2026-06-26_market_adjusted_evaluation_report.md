# Market-Adjusted Evaluation Report - 2026-06-26

Generated at: 2026-06-26 16:39:46

Source feature file: `data/processed/market_adjusted_features_20260626.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **21**
- pending: **21**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 361610 | SK아이이테크놀로지 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 187660 | 페니트리움바이오 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 476830 | 알지노믹스 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 5960 | 동부건설 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 6740 | 블루산업개발 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 6740 | 블루산업개발 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 6740 | 블루산업개발 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 138360 | 앤로보틱스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 214150 | 클래시스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 214150 | 클래시스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 214150 | 클래시스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 258610 | 케일럼 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 277880 | 티에스아이 | positive | pending | pending | N/A | N/A | N/A |
| nan | 3450 | 케이비증권 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 3470 | 유안타증권 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 186230 | 그린플러스 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 105560 | KB금융 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | negative | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
