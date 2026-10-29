# Learned-Rule Daily Candidate Report - 2026-10-08

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

- Total candidate rows: **76**
- Rows with active learned-rule adjustment: **52**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 35 |
| watchlist_candidate | 27 |
| general_review | 14 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 117670 | 알파칩스 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 90 | 45.56% |
| 117670 | 알파칩스 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 90 | 45.56% |
| 117670 | 알파칩스 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 90 | 45.56% |
| 460930 | 현대힘스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 025950 | 동신건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 007610 | 선도전기 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 044380 | 주연테크 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 247660 | 나노씨엠에스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 037350 | 성도이엔지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 450520 | 인스웨이브 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 117670 | 알파칩스 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 90 | 45.56% |
| 372170 | 윤성에프앤씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 212710 | 아이에스티이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 117670 | 알파칩스 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 90 | 45.56% |
| 117670 | 알파칩스 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 90 | 45.56% |
| 117670 | 알파칩스 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 90 | 45.56% |
| 117670 | 알파칩스 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 90 | 45.56% |
| 097230 | HJ중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 002460 | HS화성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 267270 | HD건설기계 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 065450 | 빅텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 724 | 29.01% |
| 210120 | 빅텐츠 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 251 | 52.19% |
| 128940 | 한미약품 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 251 | 52.19% |
| 008930 | 한미사이언스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 251 | 52.19% |
| 290560 | 파라택시스이더리움 | spin_off | volatile | 30.0 | 0.0 | 0.0 | -10.0 | 20.0 | general_review | negative_learning | 55 | 32.73% |
| 498390 | 한화플러스제5호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 264 | 19.70% |
| 084680 | 이월드 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1182 | 34.01% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
