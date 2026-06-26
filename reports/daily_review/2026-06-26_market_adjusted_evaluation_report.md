# Market-Adjusted Evaluation Report - 2026-06-26

Generated at: 2026-06-26 08:30:33

Source feature file: `data/processed/market_adjusted_features_20260626.csv`

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
| 1970-01-01 | 7460 | 에이프로젠 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 85660 | 차바이오텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 85660 | 차바이오텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 85660 | 차바이오텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 211270 | AP위성 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 12510 | 더존비즈온 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 243070 | 휴온스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 243070 | 휴온스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 54930 | 유신 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 13700 | 까뮤이앤씨 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 9730 | 이렘 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 445090 | 에이직랜드 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 13580 | 계룡건설산업 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 13580 | 계룡건설산업 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
