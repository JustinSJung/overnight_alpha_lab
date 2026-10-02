# Market-Adjusted Evaluation Report - 2026-10-02

Generated at: 2026-10-02 03:11:15

Source feature file: `data/processed/market_adjusted_features_20261002.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **168**
- market_data_missing: **168**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 007610 | 선도전기 | positive | failure | market_data_missing | -1.03% | N/A | N/A |
| 1970-01-01 | 028260 | 삼성물산 | negative | success | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 0126Z0 | 삼성에피스홀딩스 | volatile | failure | market_data_missing | 0.94% | N/A | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 066590 | 스모트로닉 | negative | failure | market_data_missing | 2.88% | N/A | N/A |
| 1970-01-01 | 207490 | 에이펙스인텍 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 181710 | NHN | volatile | failure | market_data_missing | 0.53% | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | volatile | success | market_data_missing | 6.74% | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | volatile | success | market_data_missing | 6.74% | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | volatile | success | market_data_missing | 6.74% | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | volatile | success | market_data_missing | 6.74% | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | volatile | success | market_data_missing | -4.21% | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | volatile | success | market_data_missing | -4.21% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
