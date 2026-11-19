# Learned-Rule Daily Candidate Report - 2026-11-19

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

- Total candidate rows: **255**
- Rows with active learned-rule adjustment: **243**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| positive_candidate | 156 |
| general_review | 55 |
| risk_or_avoid_review | 35 |
| watchlist_candidate | 9 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 083650 | 비에이치아이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 361390 | 제노코 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 282880 | 코윈로보틱스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1564 | 36.38% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
