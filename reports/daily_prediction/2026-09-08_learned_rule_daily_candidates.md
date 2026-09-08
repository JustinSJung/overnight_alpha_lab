# Learned-Rule Daily Candidate Report - 2026-09-08

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

- Total candidate rows: **441**
- Rows with active learned-rule adjustment: **441**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 266 |
| risk_or_avoid_review | 156 |
| watchlist_candidate | 19 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 067080 | 대화제약 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 001260 | 남광토건 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 001260 | 남광토건 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 459510 | 나우로보틱스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 046940 | 우원개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 217190 | 제너셈 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 001260 | 남광토건 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 001260 | 남광토건 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 001260 | 남광토건 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 083790 | CG인바이츠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 126340 | 비나텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 040910 | 아이씨디 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 002780 | 진흥기업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 000210 | DL | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 375500 | DL이앤씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 112610 | 씨에스윈드 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 112610 | 씨에스윈드 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 045100 | 한양이엔지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 001260 | 남광토건 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 303 | 24.42% |
| 056090 | 시지메드텍 | spin_off | volatile | 30.0 | 0.0 | 0.0 | -3.75 | 26.25 | general_review | mild_negative_learning | 12 | 41.67% |
| 310210 | 보로노이 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 59 | 44.07% |
| 068270 | 셀트리온 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 59 | 44.07% |
| 068270 | 셀트리온 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 59 | 44.07% |
| 068270 | 셀트리온 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 59 | 44.07% |
| 068270 | 셀트리온 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 59 | 44.07% |
| 068270 | 셀트리온 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 59 | 44.07% |
| 001260 | 남광토건 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 59 | 44.07% |
| 001260 | 남광토건 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 59 | 44.07% |
| 001260 | 남광토건 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 59 | 44.07% |
| 001260 | 남광토건 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 59 | 44.07% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
