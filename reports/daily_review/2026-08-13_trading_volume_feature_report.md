# Trading Volume Feature Report - 2026-08-13

Generated at: 2026-08-13 23:08:08

Source ML dataset: `data/processed/ml_dataset_20260813.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **9248**
- Rows with price file found: **9248**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **9248**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 215480 | 토박스코리아 | lawsuit | negative | N/A | 36,418 | N/A | N/A | 32,171 | N/A |
| 20260813 | 407400 | 꿈비 | lawsuit | negative | N/A | 66,536 | N/A | N/A | 17,309 | N/A |
| 20260813 | 107640 | 한중엔시에스 | convertible_bond | negative | N/A | 76,560 | N/A | N/A | 148,168 | N/A |
| 20260813 | 009160 | SIMPAC | investment_decision | volatile | N/A | 199,493 | N/A | N/A | 177,896 | N/A |
| 20260813 | 248070 | 솔루엠 | paid_in_capital_increase | negative | N/A | 237,891 | N/A | N/A | 68,571 | N/A |
| 20260813 | 248070 | 솔루엠 | paid_in_capital_increase | negative | N/A | 237,891 | N/A | N/A | 68,571 | N/A |
| 20260813 | 248070 | 솔루엠 | paid_in_capital_increase | negative | N/A | 237,891 | N/A | N/A | 68,571 | N/A |
| 20260813 | 248070 | 솔루엠 | paid_in_capital_increase | negative | N/A | 237,891 | N/A | N/A | 68,571 | N/A |
| 20260813 | 028050 | 삼성E&A | supply_contract | positive | N/A | 2,548,936 | N/A | N/A | 1,486,703 | N/A |
| 20260813 | 001340 | PKC | major_shareholder_change | volatile | N/A | 304,626 | N/A | N/A | 176,784 | N/A |
| 20260813 | 001340 | PKC | major_shareholder_change | volatile | N/A | 304,626 | N/A | N/A | 176,784 | N/A |
| 20260813 | 001340 | PKC | major_shareholder_change | volatile | N/A | 304,626 | N/A | N/A | 176,784 | N/A |
| 20260813 | 001340 | PKC | major_shareholder_change | volatile | N/A | 304,626 | N/A | N/A | 176,784 | N/A |
| 20260813 | 043260 | 성호전자 | convertible_bond | negative | N/A | 1,292,444 | N/A | N/A | 1,765,653 | N/A |
| 20260813 | 043260 | 성호전자 | convertible_bond | negative | N/A | 1,292,444 | N/A | N/A | 1,765,653 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
