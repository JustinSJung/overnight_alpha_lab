# Learned-Rule Daily Candidate Report - 2026-09-25

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

- Total candidate rows: **82**
- Rows with active learned-rule adjustment: **69**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 49 |
| watchlist_candidate | 18 |
| general_review | 15 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 004440 | 삼일씨엔에스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 083650 | 비에이치아이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 046390 | 삼화네트웍스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 000720 | 현대건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 060980 | HL홀딩스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 326030 | 에스케이바이오팜 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 101360 | 에코앤드림 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 475400 | 씨메스로보틱스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 064350 | 현대로템 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 272210 | 한화시스템 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 109860 | 동일금속 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 014790 | HL D&I | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 091590 | 남화토건 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 580 | 28.79% |
| 001360 | 삼성제약 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 216 | 50.46% |
| 009160 | SIMPAC | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 216 | 50.46% |
| 377480 | 마음AI | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 216 | 50.46% |
| 068270 | 셀트리온 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 216 | 50.46% |
| 230360 | 에코마케팅 | spin_off | volatile | 30.0 | 0.0 | 0.0 | -10.0 | 20.0 | general_review | negative_learning | 48 | 31.25% |
| 002810 | 삼영무역 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 117 | 21.37% |
| 229000 | 젠큐릭스 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 117 | 21.37% |
| 002720 | 국제약품 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1015 | 33.30% |
| 251270 | 넷마블 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1015 | 33.30% |
| 431190 | 케이쓰리아이 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1015 | 33.30% |
| 259960 | 크래프톤 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1015 | 33.30% |
| 007570 | 일양약품 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1015 | 33.30% |
| 002790 | 아모레퍼시픽홀딩스 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1015 | 33.30% |
| 090430 | 아모레퍼시픽 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1015 | 33.30% |
| 001210 | 금호전기 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1015 | 33.30% |
| 005250 | 녹십자홀딩스 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1015 | 33.30% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
