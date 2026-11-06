# Learned-Rule Daily Candidate Report - 2026-11-06

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

- Total candidate rows: **1062**
- Rows with active learned-rule adjustment: **1009**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 506 |
| general_review | 489 |
| watchlist_candidate | 67 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 112610 | 씨에스윈드 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 112610 | 씨에스윈드 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 006360 | GS건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 002990 | 금호건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 002990 | 금호건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 002990 | 금호건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 002990 | 금호건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 004800 | 효성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 004800 | 효성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 130660 | 한전산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 004800 | 효성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 376290 | 씨유테크 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 004800 | 효성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 004800 | 효성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 004800 | 효성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 004800 | 효성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 011930 | 신성이엔지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 008970 | KBI동양철관 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 008970 | KBI동양철관 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 002780 | 진흥기업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 099520 | DGI | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 294870 | IPARK현대산업개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 012630 | HDC | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 004800 | 효성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 012630 | HDC | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 033500 | 동성화인텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 297890 | HB솔루션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1310 | 33.36% |
| 035720 | 카카오 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 691 | 45.44% |
| 035720 | 카카오 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 691 | 45.44% |
| 035720 | 카카오 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 691 | 45.44% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
