# Learned-Rule Daily Candidate Report - 2026-09-10

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

- Total candidate rows: **112**
- Rows with active learned-rule adjustment: **112**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 48 |
| watchlist_candidate | 23 |
| risk_or_avoid_review | 23 |
| volatile_watchlist | 18 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 255220 | SG | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 137400 | 피엔티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 200710 | 에이디테크놀로지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 376270 | HEM파마 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 282720 | 금양그린파워 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 047040 | 대우건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 005960 | 동부건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 002460 | HS화성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 047040 | 대우건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 047040 | 대우건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 047040 | 대우건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 026150 | 특수건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 000720 | 현대건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 047040 | 대우건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 013700 | 까뮤이앤씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 064290 | 인텍플러스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 294870 | IPARK현대산업개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 012630 | HDC | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 007570 | 일양약품 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 047040 | 대우건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 047040 | 대우건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 047040 | 대우건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 340 | 26.47% |
| 310210 | 보로노이 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 95 | 62.11% |
| 351320 | 넥사다이내믹스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 95 | 62.11% |
| 351320 | 넥사다이내믹스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 95 | 62.11% |
| 348950 | 제이알글로벌리츠 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 95 | 62.11% |
| 042660 | 한화오션 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 95 | 62.11% |
| 351320 | 넥사다이내믹스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 95 | 62.11% |
| 351320 | 넥사다이내믹스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 95 | 62.11% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
