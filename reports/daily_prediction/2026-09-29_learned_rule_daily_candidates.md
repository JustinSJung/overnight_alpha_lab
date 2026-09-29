# Learned-Rule Daily Candidate Report - 2026-09-29

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

- Total candidate rows: **1470**
- Rows with active learned-rule adjustment: **575**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 1214 |
| watchlist_candidate | 222 |
| general_review | 34 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 475230 | 엔알비 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 475230 | 엔알비 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 475230 | 엔알비 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 475230 | 엔알비 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 475230 | 엔알비 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 475230 | 엔알비 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 475230 | 엔알비 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 475230 | 엔알비 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 475230 | 엔알비 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 096770 | SK이노베이션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 621 | 28.18% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
