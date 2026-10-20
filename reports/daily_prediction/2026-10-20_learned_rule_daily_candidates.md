# Learned-Rule Daily Candidate Report - 2026-10-20

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

- Total candidate rows: **84**
- Rows with active learned-rule adjustment: **65**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| watchlist_candidate | 44 |
| risk_or_avoid_review | 21 |
| general_review | 19 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 032820 | 우리기술 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 009150 | 삼성전기 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 005870 | 휴니드테크놀러지스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 126340 | 비나텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 234300 | 에스트래픽 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 234300 | 에스트래픽 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 234300 | 에스트래픽 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 234300 | 에스트래픽 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 234300 | 에스트래픽 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 126340 | 비나텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 187870 | 디바이스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 126340 | 비나텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 420770 | 기가비스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 025560 | 미래산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 234300 | 에스트래픽 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 234300 | 에스트래픽 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 234300 | 에스트래픽 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 028100 | 동아지질 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 025950 | 동신건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 141000 | 비아트론 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 010950 | S-Oil | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 010120 | 엘에스일렉트릭 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 006260 | LS | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 010950 | S-Oil | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 013360 | 일성건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 002990 | 금호건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 126340 | 비나텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 905 | 29.83% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
