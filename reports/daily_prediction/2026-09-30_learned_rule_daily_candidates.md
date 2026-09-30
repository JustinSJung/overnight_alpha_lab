# Learned-Rule Daily Candidate Report - 2026-09-30

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

- Total candidate rows: **1015**
- Rows with active learned-rule adjustment: **998**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 559 |
| risk_or_avoid_review | 317 |
| positive_candidate | 96 |
| watchlist_candidate | 43 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |
| 303360 | 프로티아 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 5.0 | 65.0 | positive_candidate | mild_positive_learning | 74 | 55.41% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
