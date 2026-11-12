# Learned-Rule Daily Candidate Report - 2026-11-12

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

- Total candidate rows: **434**
- Rows with active learned-rule adjustment: **427**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 186 |
| risk_or_avoid_review | 129 |
| watchlist_candidate | 107 |
| positive_candidate | 12 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 013120 | 동원개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 002990 | 금호건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 388050 | 지투파워 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 006360 | GS건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 064480 | 브리지텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 189860 | 서전기전 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 030530 | 원익홀딩스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 093370 | 후성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 093370 | 후성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 097230 | HJ중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 005960 | 동부건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1415 | 35.83% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |
| 036570 | NC | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -15.0 | 35.0 | watchlist_candidate | strong_negative_learning | 82 | 19.51% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
