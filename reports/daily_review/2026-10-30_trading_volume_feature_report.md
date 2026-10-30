# Trading Volume Feature Report - 2026-10-30

Generated at: 2026-10-30 02:29:12

Source ML dataset: `data/processed/ml_dataset_20261030.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **3964593**
- Rows with price file found: **3964593**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **3964593**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261029 | 001470 | 삼부토건 | investment_decision | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261029 | 072770 | 멤레이비티 | convertible_bond | negative | N/A | 150,771 | N/A | N/A | 180,225 | N/A |
| 20261029 | 072770 | 멤레이비티 | convertible_bond | negative | N/A | 150,771 | N/A | N/A | 180,225 | N/A |
| 20261029 | 072770 | 멤레이비티 | convertible_bond | negative | N/A | 150,771 | N/A | N/A | 180,225 | N/A |
| 20261029 | 072770 | 멤레이비티 | convertible_bond | negative | N/A | 150,771 | N/A | N/A | 180,225 | N/A |
| 20261029 | 072770 | 멤레이비티 | convertible_bond | negative | N/A | 150,771 | N/A | N/A | 180,225 | N/A |
| 20261029 | 072770 | 멤레이비티 | convertible_bond | negative | N/A | 150,771 | N/A | N/A | 180,225 | N/A |
| 20261029 | 072770 | 멤레이비티 | convertible_bond | negative | N/A | 150,771 | N/A | N/A | 180,225 | N/A |
| 20261029 | 072770 | 멤레이비티 | convertible_bond | negative | N/A | 150,771 | N/A | N/A | 180,225 | N/A |
| 20261029 | 072770 | 멤레이비티 | convertible_bond | negative | N/A | 150,771 | N/A | N/A | 180,225 | N/A |
| 20261029 | 088280 | 쏘닉스 | convertible_bond | negative | N/A | 62,621 | N/A | N/A | 65,296 | N/A |
| 20261029 | 011000 | 진원생명과학 | convertible_bond | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261029 | 011000 | 진원생명과학 | convertible_bond | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261029 | 011000 | 진원생명과학 | convertible_bond | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261029 | 011000 | 진원생명과학 | convertible_bond | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261029 | 260870 | SK시그넷 | major_shareholder_change | volatile | N/A | 1,844 | N/A | N/A | 3,837 | N/A |
| 20261029 | 260870 | SK시그넷 | major_shareholder_change | volatile | N/A | 1,844 | N/A | N/A | 3,837 | N/A |
| 20261029 | 260870 | SK시그넷 | major_shareholder_change | volatile | N/A | 1,844 | N/A | N/A | 3,837 | N/A |
| 20261029 | 260870 | SK시그넷 | major_shareholder_change | volatile | N/A | 1,844 | N/A | N/A | 3,837 | N/A |
| 20261029 | 260870 | SK시그넷 | major_shareholder_change | volatile | N/A | 1,844 | N/A | N/A | 3,837 | N/A |
| 20261029 | 260870 | SK시그넷 | major_shareholder_change | volatile | N/A | 1,844 | N/A | N/A | 3,837 | N/A |
| 20261029 | 260870 | SK시그넷 | major_shareholder_change | volatile | N/A | 1,844 | N/A | N/A | 3,837 | N/A |
| 20261029 | 260870 | SK시그넷 | major_shareholder_change | volatile | N/A | 1,844 | N/A | N/A | 3,837 | N/A |
| 20261029 | 260870 | SK시그넷 | major_shareholder_change | volatile | N/A | 1,844 | N/A | N/A | 3,837 | N/A |
| 20261029 | 445680 | 큐리옥스바이오시스템즈 | supply_contract | positive | N/A | 123,294 | N/A | N/A | 77,649 | N/A |
| 20261029 | 246960 | SCL사이언스 | merger | volatile | N/A | 253,621 | N/A | N/A | 97,261 | N/A |
| 20261029 | 090410 | 덕신이피씨 | supply_contract | positive | N/A | 28,355 | N/A | N/A | 12,019 | N/A |
| 20261029 | 129260 | 인터지스 | major_shareholder_change | volatile | N/A | 9,677 | N/A | N/A | 11,822 | N/A |
| 20261029 | 129260 | 인터지스 | major_shareholder_change | volatile | N/A | 9,677 | N/A | N/A | 11,822 | N/A |
| 20261029 | 129260 | 인터지스 | major_shareholder_change | volatile | N/A | 9,677 | N/A | N/A | 11,822 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
