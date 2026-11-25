# Learned-Rule Daily Candidate Report - 2026-11-25

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

- Total candidate rows: **468**
- Rows with active learned-rule adjustment: **449**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 333 |
| general_review | 100 |
| positive_candidate | 20 |
| watchlist_candidate | 15 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 013580 | 계룡건설산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 126720 | 수산인더스트리 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 052690 | 한전기술 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 028050 | 삼성E&A | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 086390 | 유니테스트 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 097230 | HJ중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 097230 | HJ중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 097230 | HJ중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 097230 | HJ중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 122640 | 예스티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 013360 | 일성건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 038870 | 에코심플렉스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 166480 | 코아스템켐온 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 007820 | 엠엑스로보틱스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1678 | 35.64% |
| 097230 | HJ중공업 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 547 | 51.01% |
| 078130 | 에스엠국일 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 826 | 46.25% |
| 482680 | 미래에셋비전스팩7호 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 826 | 46.25% |
| 097230 | HJ중공업 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 547 | 51.01% |
| 097230 | HJ중공업 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 547 | 51.01% |
| 097230 | HJ중공업 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 547 | 51.01% |
| 361610 | SK아이이테크놀로지 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 826 | 46.25% |
| 361610 | SK아이이테크놀로지 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 826 | 46.25% |
| 456040 | OCI | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 547 | 51.01% |
| 096770 | SK이노베이션 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 826 | 46.25% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
