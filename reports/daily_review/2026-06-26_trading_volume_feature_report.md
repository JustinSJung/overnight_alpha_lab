# Trading Volume Feature Report - 2026-06-26

Generated at: 2026-06-26 08:30:35

Source ML dataset: `data/processed/ml_dataset_20260626.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **4128**
- Rows with price file found: **4128**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **4128**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260626 | 007460 | 에이프로젠 | investment_decision | volatile | N/A | 298,121 | N/A | N/A | 385,226 | N/A |
| 20260626 | 085660 | 차바이오텍 | paid_in_capital_increase | negative | N/A | 407,411 | N/A | N/A | 357,153 | N/A |
| 20260626 | 085660 | 차바이오텍 | paid_in_capital_increase | negative | N/A | 407,411 | N/A | N/A | 357,153 | N/A |
| 20260626 | 085660 | 차바이오텍 | paid_in_capital_increase | negative | N/A | 407,411 | N/A | N/A | 357,153 | N/A |
| 20260626 | 085660 | 차바이오텍 | paid_in_capital_increase | negative | N/A | 407,411 | N/A | N/A | 357,153 | N/A |
| 20260626 | 085660 | 차바이오텍 | paid_in_capital_increase | negative | N/A | 407,411 | N/A | N/A | 357,153 | N/A |
| 20260626 | 085660 | 차바이오텍 | paid_in_capital_increase | negative | N/A | 407,411 | N/A | N/A | 357,153 | N/A |
| 20260626 | 085660 | 차바이오텍 | paid_in_capital_increase | negative | N/A | 407,411 | N/A | N/A | 357,153 | N/A |
| 20260626 | 085660 | 차바이오텍 | paid_in_capital_increase | negative | N/A | 407,411 | N/A | N/A | 357,153 | N/A |
| 20260626 | 085660 | 차바이오텍 | paid_in_capital_increase | negative | N/A | 407,411 | N/A | N/A | 357,153 | N/A |
| 20260626 | 211270 | AP위성 | convertible_bond | negative | N/A | 593,684 | N/A | N/A | 337,846 | N/A |
| 20260626 | 012510 | 더존비즈온 | major_shareholder_change | volatile | N/A | 6,454 | N/A | N/A | 6,750 | N/A |
| 20260626 | 243070 | 휴온스 | merger | volatile | N/A | 72,311 | N/A | N/A | 48,262 | N/A |
| 20260626 | 243070 | 휴온스 | merger | volatile | N/A | 72,311 | N/A | N/A | 48,262 | N/A |
| 20260626 | 243070 | 휴온스 | merger | volatile | N/A | 72,311 | N/A | N/A | 48,262 | N/A |
| 20260626 | 243070 | 휴온스 | merger | volatile | N/A | 72,311 | N/A | N/A | 48,262 | N/A |
| 20260626 | 054930 | 유신 | supply_contract | positive | N/A | 25,120 | N/A | N/A | 21,356 | N/A |
| 20260626 | 299660 | 셀리드 | investment_decision | volatile | N/A | 1,065,638 | N/A | N/A | 596,859 | N/A |
| 20260626 | 013700 | 까뮤이앤씨 | supply_contract | positive | N/A | 123,667 | N/A | N/A | 112,523 | N/A |
| 20260626 | 009730 | 이렘 | convertible_bond | negative | N/A | 1,316,342 | N/A | N/A | 1,642,508 | N/A |
| 20260626 | 445090 | 에이직랜드 | supply_contract | positive | N/A | 187,479 | N/A | N/A | 239,724 | N/A |
| 20260626 | 043260 | 성호전자 | bond_with_warrant | negative | N/A | 2,700,711 | N/A | N/A | 2,116,021 | N/A |
| 20260626 | 013580 | 계룡건설산업 | supply_contract | positive | N/A | 125,107 | N/A | N/A | 166,032 | N/A |
| 20260626 | 013580 | 계룡건설산업 | supply_contract | positive | N/A | 125,107 | N/A | N/A | 166,032 | N/A |
| 20260626 | 013580 | 계룡건설산업 | supply_contract | positive | N/A | 125,107 | N/A | N/A | 166,032 | N/A |
| 20260626 | 013580 | 계룡건설산업 | supply_contract | positive | N/A | 125,107 | N/A | N/A | 166,032 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |
| 20260626 | 179530 | 애드바이오텍 | convertible_bond | negative | N/A | 98,071 | N/A | N/A | 112,102 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
