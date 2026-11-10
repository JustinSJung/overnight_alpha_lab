# Learned-Rule Daily Candidate Report - 2026-11-10

## Purpose

This report applies learned event-rule score adjustments to the daily candidate scoring formula.

The current v4 score formula is:

```text
base_event_score
+ market_adjusted_score_adjustment
+ trading_volume_score_adjustment
+ learned_event_score_adjustment
= final_learned_rule_score
```

This report is for research and portfolio demonstration purposes only. It is not investment advice.

## Summary

- Total candidate rows: **101**
- Rows with active learned-rule adjustment: **87**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 50 |
| risk_or_avoid_review | 31 |
| positive_candidate | 13 |
| watchlist_candidate | 7 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 006360 | GS건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 064290 | 인텍플러스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 058730 | 다스코 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 282720 | 금양그린파워 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 296640 | 이노에이엑스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 002460 | HS화성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 071970 | HD현대마린엔진 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 013580 | 계룡건설산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 365330 | 에스와이스틸텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 171090 | 선익시스템 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 009540 | HD한국조선해양 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 083640 | 인콘 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 329180 | HD현대중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1380 | 35.07% |
| 005300 | 롯데칠성음료 | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -10.0 | 40.0 | watchlist_candidate | negative_learning | 62 | 25.81% |
| 033250 | 체시스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 451 | 52.77% |
| 001260 | 남광토건 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 451 | 52.77% |
| 950260 | 인제니아테라퓨틱스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 451 | 52.77% |
| 294870 | IPARK현대산업개발 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 451 | 52.77% |
| 028260 | 삼성물산 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 451 | 52.77% |
| 012630 | HDC | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 451 | 52.77% |
| 000210 | DL | spin_off | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 116 | 37.93% |
| 232830 | 아이티센피엔에스 | merger | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 702 | 44.87% |
| 317240 | TS트릴리온 | spin_off | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 116 | 37.93% |
| 100840 | SNT에너지 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2223 | 39.81% |
| 003470 | 유안타증권 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2223 | 39.81% |
| 261780 | 아리바이오LAB | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2223 | 39.81% |
| 000590 | CS홀딩스 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2223 | 39.81% |
| 005940 | NH투자증권 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2223 | 39.81% |
| 090430 | 아모레퍼시픽 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2223 | 39.81% |
| 268280 | 미원에스씨 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2223 | 39.81% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
