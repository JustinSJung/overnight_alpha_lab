# Trading Volume Score Integration Report - 2026-10-20

Generated at: 2026-10-20 01:45:23

Source trading volume feature file: `data/processed/trading_volume_features_20261020.csv`

## Purpose

This report converts trading volume reaction labels into recommendation score adjustment signals.

The goal is to reward positive events with strong volume confirmation and penalize negative events with strong volume confirmation.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Score Logic

- Positive event + strong volume spike: positive adjustment
- Positive event + weak volume: conservative negative adjustment
- Negative event + strong volume spike: negative risk adjustment
- Volatile event + strong volume spike: volatility confirmation adjustment

## Summary

- Total rows: **200**
- Total volume adjustment score: **0.00**
- Average volume adjustment score: **0.00**

## Adjustment Label Counts

- neutral_volume_adjustment: **200**

## Volume Reaction Counts

- insufficient_volume_baseline: **199**
- price_file_missing: **1**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | volume_reaction_label | event_volume_ratio_20d | next_volume_ratio_20d | trading_volume_score_adjustment | trading_volume_adjustment_label |
|---|---|---|---|---|---|---|---|---|
| 20261019 | 059270 | 해성에어로보틱스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 302550 | 리메드 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 207490 | 에이펙스인텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 032820 | 우리기술 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 377450 | 리파인 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 018500 | 동원모빌리티 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 465770 | STX그린로지스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 010960 | 삼호개발 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 000210 | DL | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 011300 | 우성머티리얼스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 375500 | DL이앤씨 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 033310 | 엠투엔 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 288980 | 모아데이타 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 363280 | 티와이홀딩스 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 069460 | 대호에이엘 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 196170 | 알테오젠 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 009410 | 태영건설 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 006980 | 우성 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 009150 | 삼성전기 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 078020 | LS증권 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 900100 | 파이온엑스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 060900 | 에이전트AI | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 025950 | 동신건설 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 000300 | DH오토넥스 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 214330 | 금호에이치티 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 142760 | 모아라이프플러스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 028100 | 동아지질 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 290120 | DH오토리드 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 407400 | 꿈비 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261019 | 082270 | 젬백스 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |

## Next Step

The next step is to connect trading volume score adjustment to the market-adjusted daily candidate report.
