# Market-Adjusted Evaluation Report - 2026-07-07

Generated at: 2026-07-07 06:47:38

Source feature file: `data/processed/market_adjusted_features_20260707.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **28**
- pending: **28**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 288980 | 모아데이타 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 19570 | 플루토스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 13520 | 화승코퍼레이션 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 13720 | 청보 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 253450 | 스튜디오드래곤 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 10140 | 삼성중공업 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 10140 | 삼성중공업 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 10140 | 삼성중공업 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 10140 | 삼성중공업 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 101970 | 우양에이치씨 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 68240 | 다원시스 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 720 | 현대건설 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 47040 | 대우건설 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 368970 | 오에스피 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 3070 | 코오롱글로벌 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 187870 | 디바이스 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 7980 | TP | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 7980 | TP | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 7980 | TP | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 7980 | TP | volatile | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
