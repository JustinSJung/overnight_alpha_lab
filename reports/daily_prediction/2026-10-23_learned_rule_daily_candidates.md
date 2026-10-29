# Learned-Rule Daily Candidate Report - 2026-10-23

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

- Total candidate rows: **85**
- Rows with active learned-rule adjustment: **71**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 33 |
| general_review | 30 |
| watchlist_candidate | 22 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 028050 | 삼성E&A | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | 11.25 | 61.25 | watchlist_candidate | strong_positive_learning | 11 | 81.82% |
| 396470 | 워트 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 012450 | 한화에어로스페이스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 122640 | 예스티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 011560 | 세보엠이씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 013580 | 계룡건설산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 071970 | HD현대마린엔진 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 389140 | 포바이포 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 028670 | 팬오션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 382900 | 범한퓨얼셀 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 143540 | 영우디에스피 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 000720 | 현대건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 282880 | 코윈로보틱스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 119850 | 지엔씨에너지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 003380 | 하림지주 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 460470 | 아이빔테크놀로지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 988 | 30.57% |
| 068270 | 셀트리온 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 306 | 51.96% |
| 131030 | 옵투스제약 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 306 | 51.96% |
| 006370 | 대구백화점 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 306 | 51.96% |
| 004990 | 롯데지주 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 306 | 51.96% |
| 078130 | 에스엠국일 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 306 | 51.96% |
| 019170 | 신풍제약 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 306 | 51.96% |
| 0099X0 | IBKS제25호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 352 | 19.89% |
| 0099X0 | IBKS제25호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 352 | 19.89% |
| 0099X0 | IBKS제25호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 352 | 19.89% |
| 109070 | 주성코퍼레이션 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 352 | 19.89% |
| 078130 | 에스엠국일 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 352 | 19.89% |
| 0099X0 | IBKS제25호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 352 | 19.89% |
| 0099X0 | IBKS제25호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 352 | 19.89% |
| 0099X0 | IBKS제25호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 352 | 19.89% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
