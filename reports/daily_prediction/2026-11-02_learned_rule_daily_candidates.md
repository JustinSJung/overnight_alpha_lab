# Learned-Rule Daily Candidate Report - 2026-11-02

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

- Total candidate rows: **254**
- Rows with active learned-rule adjustment: **146**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| watchlist_candidate | 169 |
| general_review | 51 |
| risk_or_avoid_review | 34 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 236810 | 엔비티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 045300 | 성우테크론 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 054220 | 비츠로시스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 065420 | 에스아이리소스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 114190 | 강원에너지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 420770 | 기가비스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 028100 | 동아지질 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 028100 | 동아지질 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 114190 | 강원에너지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 056730 | CNT85 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 056730 | CNT85 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 418620 | E8 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 056730 | CNT85 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 056730 | CNT85 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 056730 | CNT85 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 056730 | CNT85 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 056730 | CNT85 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 003070 | 코오롱글로벌 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 323350 | 다원넥스뷰 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 002020 | 코오롱 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 295310 | 에이치브이엠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 475150 | SK이터닉스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 006120 | SK디스커버리 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 056730 | CNT85 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 383310 | 에코프로에이치엔 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 025560 | 미래산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 112610 | 씨에스윈드 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 002780 | 진흥기업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |
| 053690 | 한미글로벌 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1211 | 33.61% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
