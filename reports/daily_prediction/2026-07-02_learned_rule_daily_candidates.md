# Learned-Rule Daily Candidate Report - 2026-07-02

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

- Total candidate rows: **2134424**
- Rows with active learned-rule adjustment: **0**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 2097169 |
| risk_or_avoid_review | 20738 |
| positive_candidate | 16514 |
| watchlist_candidate | 3 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
