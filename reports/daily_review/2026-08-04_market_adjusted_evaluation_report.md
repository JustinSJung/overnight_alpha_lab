# Market-Adjusted Evaluation Report - 2026-08-04

Generated at: 2026-08-04 16:35:28

Source feature file: `data/processed/market_adjusted_features_20260804.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **55**
- pending: **55**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 11000 | 진원생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 11000 | 진원생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 11000 | 진원생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 11000 | 진원생명과학 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 31860 | 디에이치엑스컴퍼니 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 92040 | 아미코젠 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 92040 | 아미코젠 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 229640 | LS에코에너지 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 109740 | 디에스케이 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 109740 | 디에스케이 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 2990 | 금호건설 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 166090 | 하나머티리얼즈 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 166090 | 하나머티리얼즈 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 208640 | 썸에이지 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 208640 | 썸에이지 | negative | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
