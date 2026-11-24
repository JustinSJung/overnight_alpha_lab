# Learned-Rule Daily Candidate Report - 2026-11-24

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

- Total candidate rows: **825**
- Rows with active learned-rule adjustment: **703**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 591 |
| general_review | 102 |
| watchlist_candidate | 101 |
| positive_candidate | 31 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 475230 | 엔알비 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 006260 | LS | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 009540 | HD한국조선해양 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 009540 | HD한국조선해양 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 009540 | HD한국조선해양 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 006260 | LS | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 003480 | 한진중공업홀딩스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 065570 | 삼영이엔씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 420770 | 기가비스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 065570 | 삼영이엔씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 047810 | 한국항공우주 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 065570 | 삼영이엔씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 065570 | 삼영이엔씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 272210 | 한화시스템 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 206400 | 아인스팩씨엔에스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 006260 | LS | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 006260 | LS | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 206400 | 아인스팩씨엔에스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 047040 | 대우건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 000720 | 현대건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |
| 417860 | 오브젠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1660 | 35.54% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
