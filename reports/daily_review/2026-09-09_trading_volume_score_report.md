# Trading Volume Score Integration Report - 2026-09-09

Generated at: 2026-09-09 00:53:47

Source trading volume feature file: `data/processed/trading_volume_features_20260909.csv`

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

- Total rows: **71059**
- Total volume adjustment score: **0.00**
- Average volume adjustment score: **0.00**

## Adjustment Label Counts

- neutral_volume_adjustment: **71059**

## Volume Reaction Counts

- insufficient_volume_baseline: **71059**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | volume_reaction_label | event_volume_ratio_20d | next_volume_ratio_20d | trading_volume_score_adjustment | trading_volume_adjustment_label |
|---|---|---|---|---|---|---|---|---|
| 20260908 | 203400 | 에이비온 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 005930 | 삼성전자 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 199730 | 바이오인프라 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 199730 | 바이오인프라 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 199730 | 바이오인프라 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 199730 | 바이오인프라 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 020120 | 키다리스튜디오 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 009320 | 아진전자부품 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 009320 | 아진전자부품 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 009320 | 아진전자부품 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 009320 | 아진전자부품 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 010960 | 삼호개발 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 027410 | BGF | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 027040 | 서울전자통신 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 027040 | 서울전자통신 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 027040 | 서울전자통신 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 027040 | 서울전자통신 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 288980 | 모아데이타 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 126600 | BGF에코머티리얼즈 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 247660 | 나노씨엠에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 247660 | 나노씨엠에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 247660 | 나노씨엠에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 247660 | 나노씨엠에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 247660 | 나노씨엠에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 247660 | 나노씨엠에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 247660 | 나노씨엠에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 247660 | 나노씨엠에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 247660 | 나노씨엠에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 247660 | 나노씨엠에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260908 | 247660 | 나노씨엠에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |

## Next Step

The next step is to connect trading volume score adjustment to the market-adjusted daily candidate report.
