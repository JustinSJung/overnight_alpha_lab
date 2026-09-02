# Learned-Rule Daily Candidate Report - 2026-09-02

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

- Total candidate rows: **184**
- Rows with active learned-rule adjustment: **151**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 97 |
| risk_or_avoid_review | 48 |
| watchlist_candidate | 39 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 064290 | 인텍플러스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 368770 | 파이버프로 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 045660 | 에이텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 034020 | 두산에너빌리티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 034020 | 두산에너빌리티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 034020 | 두산에너빌리티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 034020 | 두산에너빌리티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 021320 | KCC건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 002990 | 금호건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 321370 | 센서뷰 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 066980 | 한성크린텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 005880 | 대한해운 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 493330 | 지에프아이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 383310 | 에코프로에이치엔 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 034020 | 두산에너빌리티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 034020 | 두산에너빌리티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 034020 | 두산에너빌리티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 012630 | HDC | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 034020 | 두산에너빌리티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 000100 | 유한양행 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 126720 | 수산인더스트리 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 126720 | 수산인더스트리 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 294870 | IPARK현대산업개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 097230 | HJ중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 331920 | 셀레믹스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 046390 | 삼화네트웍스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 464080 | 에스오에스랩 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |
| 028100 | 동아지질 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 216 | 17.13% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
