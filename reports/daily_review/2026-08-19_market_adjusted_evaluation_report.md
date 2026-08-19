# Market-Adjusted Evaluation Report - 2026-08-19

Generated at: 2026-08-19 22:48:37

Source feature file: `data/processed/market_adjusted_features_20260819.csv`

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
| 1970-01-01 | 322780 | 코퍼스코리아 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 352940 | 인바이오 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 2020 | 코오롱 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 3070 | 코오롱글로벌 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 33530 | SJG세종 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 33530 | SJG세종 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 73190 | 듀오백 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 73190 | 듀오백 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 73190 | 듀오백 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 73190 | 듀오백 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 389680 | 유디엠텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 290270 | 휴네시온 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 148250 | 알엔투테크놀로지 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 3470 | 유안타증권 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 28260 | 삼성물산 | positive | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
