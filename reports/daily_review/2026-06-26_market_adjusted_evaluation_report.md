# Market-Adjusted Evaluation Report - 2026-06-26

Generated at: 2026-06-26 16:11:01

Source feature file: `data/processed/market_adjusted_features_20260626.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **16**
- pending: **16**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 221840 | 하이즈항공 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 14130 | 한익스프레스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 14130 | 한익스프레스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 82740 | 한화엔진 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 259960 | 크래프톤 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 259960 | 크래프톤 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 259960 | 크래프톤 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 66980 | 한성크린텍 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 74610 | 이엔플러스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 348080 | 큐라티스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 90350 | 노루페인트 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 21240 | 코웨이 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 229000 | 젠큐릭스 | volatile | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
