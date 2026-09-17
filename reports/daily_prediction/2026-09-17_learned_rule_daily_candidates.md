# Learned-Rule Daily Candidate Report - 2026-09-17

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

- Total candidate rows: **320**
- Rows with active learned-rule adjustment: **296**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 214 |
| general_review | 75 |
| watchlist_candidate | 18 |
| volatile_watchlist | 13 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 083650 | 비에이치아이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 296640 | 이노에이엑스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 267850 | 아시아나IDT | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 406820 | 뷰티스킨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 130660 | 한전산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 130660 | 한전산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 130660 | 한전산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 021320 | KCC건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 130660 | 한전산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 220100 | 퓨쳐켐 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 61 | 47.54% |
| 220100 | 퓨쳐켐 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 61 | 47.54% |
| 220100 | 퓨쳐켐 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 61 | 47.54% |
| 220100 | 퓨쳐켐 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 61 | 47.54% |
| 257370 | 피엔티엠에스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 220100 | 퓨쳐켐 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 61 | 47.54% |
| 220100 | 퓨쳐켐 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 61 | 47.54% |
| 455180 | 케이지에이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 490 | 28.57% |
| 011810 | STX | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |
| 011810 | STX | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |
| 011810 | STX | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |
| 011810 | STX | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |
| 011810 | STX | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |
| 011810 | STX | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |
| 011810 | STX | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |
| 011810 | STX | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |
| 226950 | 올릭스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |
| 011810 | STX | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |
| 011810 | STX | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |
| 011810 | STX | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 10.0 | 40.0 | volatile_watchlist | positive_learning | 157 | 65.61% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
