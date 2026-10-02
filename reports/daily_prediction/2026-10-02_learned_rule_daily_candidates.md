# Learned-Rule Daily Candidate Report - 2026-10-02

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

- Total candidate rows: **486**
- Rows with active learned-rule adjustment: **466**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 291 |
| general_review | 170 |
| watchlist_candidate | 25 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 480370 | 씨케이솔루션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 034020 | 두산에너빌리티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 003160 | 디아이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 034020 | 두산에너빌리티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 005880 | 대한해운 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 010780 | 아이에스동서 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 010400 | 우진아이엔에스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 000250 | 삼천당제약 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 002990 | 금호건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 023150 | MH에탄올 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 76 | 53.95% |
| 023150 | MH에탄올 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | neutral_learning | 76 | 53.95% |
| 010120 | 엘에스일렉트릭 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 490470 | 세미파이브 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 386380 | 스카이랩스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 006260 | LS | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 373220 | LG에너지솔루션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 348340 | 뉴로메카 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 406820 | 뷰티스킨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 007610 | 선도전기 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 214430 | 아이쓰리시스템 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 399720 | 가온칩스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 028670 | 팬오션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 432720 | 퀄리타스반도체 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 674 | 29.82% |
| 0126Z0 | 삼성에피스홀딩스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 240 | 51.25% |
| 358570 | 지아이이노베이션 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 240 | 51.25% |
| 393970 | 대진첨단소재 | merger | volatile | 30.0 | 0.0 | 0.0 | -10.0 | 20.0 | general_review | negative_learning | 186 | 26.88% |
| 393970 | 대진첨단소재 | merger | volatile | 30.0 | 0.0 | 0.0 | -10.0 | 20.0 | general_review | negative_learning | 186 | 26.88% |
| 393970 | 대진첨단소재 | merger | volatile | 30.0 | 0.0 | 0.0 | -10.0 | 20.0 | general_review | negative_learning | 186 | 26.88% |
| 393970 | 대진첨단소재 | merger | volatile | 30.0 | 0.0 | 0.0 | -10.0 | 20.0 | general_review | negative_learning | 186 | 26.88% |
| 393970 | 대진첨단소재 | merger | volatile | 30.0 | 0.0 | 0.0 | -10.0 | 20.0 | general_review | negative_learning | 186 | 26.88% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
