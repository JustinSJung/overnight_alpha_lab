# Market-Adjusted Evaluation Report - 2026-08-13

Generated at: 2026-08-13 23:08:06

Source feature file: `data/processed/market_adjusted_features_20260813.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **26**
- pending: **26**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 215480 | 토박스코리아 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 215480 | 토박스코리아 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 407400 | 꿈비 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 107640 | 한중엔시에스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 9160 | SIMPAC | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 248070 | 솔루엠 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 248070 | 솔루엠 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 28050 | 삼성E&A | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 1340 | PKC | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 1340 | PKC | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
