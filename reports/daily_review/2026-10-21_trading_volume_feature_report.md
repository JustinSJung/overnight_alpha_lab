# Trading Volume Feature Report - 2026-10-21

Generated at: 2026-10-21 01:15:45

Source ML dataset: `data/processed/ml_dataset_20261021.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **207**
- Rows with price file found: **207**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **207**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261020 | 278470 | 에이피알 | disclosure_violation | negative | N/A | 134,043 | N/A | N/A | 202,998 | N/A |
| 20261020 | 095910 | 에스에너지 | supply_contract | positive | N/A | 206,177 | N/A | N/A | 246,164 | N/A |
| 20261020 | 117670 | 알파칩스 | bonus_issue | positive | N/A | 484,666 | N/A | N/A | 139,614 | N/A |
| 20261020 | 310210 | 보로노이 | investment_decision | volatile | N/A | 147,103 | N/A | N/A | 102,352 | N/A |
| 20261020 | 002990 | 금호건설 | convertible_bond | negative | N/A | 2,498,881 | N/A | N/A | 1,895,575 | N/A |
| 20261020 | 002990 | 금호건설 | convertible_bond | negative | N/A | 2,498,881 | N/A | N/A | 1,895,575 | N/A |
| 20261020 | 002990 | 금호건설 | convertible_bond | negative | N/A | 2,498,881 | N/A | N/A | 1,895,575 | N/A |
| 20261020 | 002990 | 금호건설 | convertible_bond | negative | N/A | 2,498,881 | N/A | N/A | 1,895,575 | N/A |
| 20261020 | 002990 | 금호건설 | convertible_bond | negative | N/A | 2,498,881 | N/A | N/A | 1,895,575 | N/A |
| 20261020 | 002990 | 금호건설 | convertible_bond | negative | N/A | 2,498,881 | N/A | N/A | 1,895,575 | N/A |
| 20261020 | 002990 | 금호건설 | convertible_bond | negative | N/A | 2,498,881 | N/A | N/A | 1,895,575 | N/A |
| 20261020 | 002990 | 금호건설 | convertible_bond | negative | N/A | 2,498,881 | N/A | N/A | 1,895,575 | N/A |
| 20261020 | 002990 | 금호건설 | convertible_bond | negative | N/A | 2,498,881 | N/A | N/A | 1,895,575 | N/A |
| 20261020 | 101000 | KS인더스트리 | paid_in_capital_increase | negative | N/A | 276,075 | N/A | N/A | 146,976 | N/A |
| 20261020 | 069640 | 한세엠케이 | major_shareholder_change | volatile | N/A | 6,559 | N/A | N/A | 35,965 | N/A |
| 20261020 | 069640 | 한세엠케이 | major_shareholder_change | volatile | N/A | 6,559 | N/A | N/A | 35,965 | N/A |
| 20261020 | 069640 | 한세엠케이 | major_shareholder_change | volatile | N/A | 6,559 | N/A | N/A | 35,965 | N/A |
| 20261020 | 069640 | 한세엠케이 | major_shareholder_change | volatile | N/A | 6,559 | N/A | N/A | 35,965 | N/A |
| 20261020 | 069640 | 한세엠케이 | major_shareholder_change | volatile | N/A | 6,559 | N/A | N/A | 35,965 | N/A |
| 20261020 | 069640 | 한세엠케이 | major_shareholder_change | volatile | N/A | 6,559 | N/A | N/A | 35,965 | N/A |
| 20261020 | 069640 | 한세엠케이 | major_shareholder_change | volatile | N/A | 6,559 | N/A | N/A | 35,965 | N/A |
| 20261020 | 069640 | 한세엠케이 | major_shareholder_change | volatile | N/A | 6,559 | N/A | N/A | 35,965 | N/A |
| 20261020 | 069640 | 한세엠케이 | major_shareholder_change | volatile | N/A | 6,559 | N/A | N/A | 35,965 | N/A |
| 20261020 | 001750 | 한양증권 | lawsuit | negative | N/A | 8,766 | N/A | N/A | 9,180 | N/A |
| 20261020 | 097780 | 에코볼트 | spin_off | volatile | N/A | 2,298 | N/A | N/A | 1,808 | N/A |
| 20261020 | 122640 | 예스티 | supply_contract | positive | N/A | 899,250 | N/A | N/A | 382,025 | N/A |
| 20261020 | 484810 | 티엑스알로보틱스 | convertible_bond | negative | N/A | 89,633 | N/A | N/A | 89,269 | N/A |
| 20261020 | 002290 | 삼일기업공사 | supply_contract | positive | N/A | 15,817 | N/A | N/A | 7,457 | N/A |
| 20261020 | 025000 | KPX케미칼 | major_shareholder_change | volatile | N/A | 2,479 | N/A | N/A | 4,187 | N/A |
| 20261020 | 025000 | KPX케미칼 | major_shareholder_change | volatile | N/A | 2,479 | N/A | N/A | 4,187 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
