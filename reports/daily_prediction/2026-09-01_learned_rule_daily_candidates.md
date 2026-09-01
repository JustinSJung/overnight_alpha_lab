# Learned-Rule Daily Candidate Report - 2026-09-01

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

- Total candidate rows: **945**
- Rows with active learned-rule adjustment: **926**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 430 |
| watchlist_candidate | 367 |
| general_review | 148 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 173 | 19.65% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
