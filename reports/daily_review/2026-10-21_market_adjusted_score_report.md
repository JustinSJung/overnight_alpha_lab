# Market-Adjusted Score Integration Report - 2026-10-21

Generated at: 2026-10-21 01:15:44

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261021.csv`

## Purpose

This report converts market-adjusted evaluation results into recommendation score adjustment signals.

The goal is to reward predictions that outperform the market and penalize results that only appear successful because of broader market movement.

## Score Rules

| Market-Adjusted Result | Score Adjustment |
|---|---:|
| market_adjusted_success | 15 |
| market_driven_weak_success | -5 |
| relative_success_but_absolute_loss | 5 |
| market_adjusted_failure | -15 |
| relative_failure_despite_absolute_gain | -10 |
| market_adjusted_volatility_success | 10 |
| market_driven_volatility | -5 |
| volatility_overestimated | -10 |
| market_data_missing | 0 |
| pending | 0 |
| unknown | 0 |

## Summary

- Total rows: **72**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **72**

## Market-Adjusted Result Counts

- market_data_missing: **72**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 278470 | 에이피알 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 095910 | 에스에너지 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 117670 | 알파칩스 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 310210 | 보로노이 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 002990 | 금호건설 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 002990 | 금호건설 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 002990 | 금호건설 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 001750 | 한양증권 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 097780 | 에코볼트 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 122640 | 예스티 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 484810 | 티엑스알로보틱스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 002290 | 삼일기업공사 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 025000 | KPX케미칼 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 025000 | KPX케미칼 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 025000 | KPX케미칼 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 028260 | 삼성물산 | volatile | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
