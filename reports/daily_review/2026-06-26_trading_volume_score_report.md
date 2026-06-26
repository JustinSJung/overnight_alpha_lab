# Trading Volume Score Integration Report - 2026-06-26

Generated at: 2026-06-26 08:30:35

Source trading volume feature file: `data/processed/trading_volume_features_20260626.csv`

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

- Total rows: **4128**
- Total volume adjustment score: **0.00**
- Average volume adjustment score: **0.00**

## Adjustment Label Counts

- neutral_volume_adjustment: **4128**

## Volume Reaction Counts

- insufficient_volume_baseline: **4128**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | volume_reaction_label | event_volume_ratio_20d | next_volume_ratio_20d | trading_volume_score_adjustment | trading_volume_adjustment_label |
|---|---|---|---|---|---|---|---|---|
| 20260626 | 007460 | 에이프로젠 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 085660 | 차바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 085660 | 차바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 085660 | 차바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 085660 | 차바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 085660 | 차바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 085660 | 차바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 085660 | 차바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 085660 | 차바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 085660 | 차바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 211270 | AP위성 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 012510 | 더존비즈온 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 243070 | 휴온스 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 243070 | 휴온스 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 243070 | 휴온스 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 243070 | 휴온스 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 054930 | 유신 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 299660 | 셀리드 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 013700 | 까뮤이앤씨 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 009730 | 이렘 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 445090 | 에이직랜드 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 043260 | 성호전자 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 013580 | 계룡건설산업 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 013580 | 계룡건설산업 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 013580 | 계룡건설산업 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 013580 | 계룡건설산업 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 179530 | 애드바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 179530 | 애드바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 179530 | 애드바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260626 | 179530 | 애드바이오텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |

## Next Step

The next step is to connect trading volume score adjustment to the market-adjusted daily candidate report.
