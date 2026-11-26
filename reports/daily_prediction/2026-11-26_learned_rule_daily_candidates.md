# Learned-Rule Daily Candidate Report - 2026-11-26

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

- Total candidate rows: **2861**
- Rows with active learned-rule adjustment: **237**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| watchlist_candidate | 2621 |
| risk_or_avoid_review | 109 |
| positive_candidate | 82 |
| general_review | 49 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 077970 | STX엔진 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 119850 | 지엔씨에너지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 119850 | 지엔씨에너지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 003070 | 코오롱글로벌 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 178320 | 서진시스템 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 002020 | 코오롱 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 012320 | 경동인베스트 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 253590 | 네오셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 475040 | 스트라드비젼 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 000720 | 현대건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 000720 | 현대건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |
| 013580 | 계룡건설산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -5.0 | 65.0 | positive_candidate | mild_negative_learning | 1704 | 36.27% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
