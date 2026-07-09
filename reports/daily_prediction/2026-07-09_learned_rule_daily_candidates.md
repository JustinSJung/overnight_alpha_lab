# Learned-Rule Daily Candidate Report - 2026-07-09

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

- Total candidate rows: **2097243**
- Rows with active learned-rule adjustment: **0**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 2097233 |
| positive_candidate | 5 |
| risk_or_avoid_review | 5 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 329180 | HD현대중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 009540 | HD한국조선해양 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 003070 | 코오롱글로벌 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 302430 | 이노메트리 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 002020 | 코오롱 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000760 | 이화산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
