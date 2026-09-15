# Learned-Rule Daily Candidate Report - 2026-09-15

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

- Total candidate rows: **106**
- Rows with active learned-rule adjustment: **84**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 53 |
| watchlist_candidate | 27 |
| general_review | 14 |
| volatile_watchlist | 12 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 038870 | 에코심플렉스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 002780 | 진흥기업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 222080 | SFA넥셀 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 389020 | 자람테크놀로지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 004800 | 효성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 045390 | 대아티아이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 206400 | 베노티앤알 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 005960 | 동부건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 298040 | 효성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 067080 | 대화제약 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 046970 | 우리로 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 469750 | 아이비젼웍스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 326030 | 에스케이바이오팜 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 011560 | 세보엠이씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 336260 | 두산퓨얼셀 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 115530 | 씨엔플러스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 052400 | 코나아이 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 54 | 51.85% |
| 010140 | 삼성중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 052400 | 코나아이 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 54 | 51.85% |
| 052400 | 코나아이 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 54 | 51.85% |
| 052400 | 코나아이 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 54 | 51.85% |
| 052400 | 코나아이 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 54 | 51.85% |
| 052400 | 코나아이 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 54 | 51.85% |
| 000720 | 현대건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 052400 | 코나아이 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 54 | 51.85% |
| 052400 | 코나아이 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 54 | 51.85% |
| 000720 | 현대건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 445 | 27.87% |
| 424870 | 이뮨온시아 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 117 | 64.96% |
| 424870 | 이뮨온시아 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 117 | 64.96% |
| 424870 | 이뮨온시아 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 117 | 64.96% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
