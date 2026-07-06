# Market-Adjusted Evaluation Report - 2026-07-06

Generated at: 2026-07-06 23:35:33

Source feature file: `data/processed/market_adjusted_features_20260706.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **31**
- pending: **31**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 003490 | 대한항공 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 020560 | 아시아나항공 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 088790 | 진도 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 023440 | 제이스코홀딩스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 004990 | 롯데지주 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 049950 | 미래컴퍼니 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 321370 | 센서뷰 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 236810 | 엔비티 | neutral_positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 236810 | 엔비티 | neutral_positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 025980 | 아난티 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 018260 | 삼성에스디에스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
