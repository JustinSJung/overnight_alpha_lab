# Learned-Rule Daily Candidate Report - 2026-11-04

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

- Total candidate rows: **213**
- Rows with active learned-rule adjustment: **200**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 158 |
| risk_or_avoid_review | 29 |
| watchlist_candidate | 26 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 375500 | DL이앤씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 375500 | DL이앤씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 000210 | DL | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 005960 | 동부건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 440110 | 파두 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 013360 | 일성건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 475040 | 스트라드비젼 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 000210 | DL | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 020180 | 대신정보통신 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 171090 | 선익시스템 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 066970 | 엘앤에프 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 207940 | 삼성바이오로직스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 066970 | 엘앤에프 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1271 | 34.23% |
| 381970 | KG모빌리티플랫폼 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 400 | 49.00% |
| 381970 | KG모빌리티플랫폼 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 400 | 49.00% |
| 381970 | KG모빌리티플랫폼 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 400 | 49.00% |
| 381970 | KG모빌리티플랫폼 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 400 | 49.00% |
| 381970 | KG모빌리티플랫폼 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 400 | 49.00% |
| 381970 | KG모빌리티플랫폼 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 400 | 49.00% |
| 016380 | KG스틸 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 663 | 46.91% |
| 016380 | KG스틸 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 663 | 46.91% |
| 016380 | KG스틸 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 663 | 46.91% |
| 016380 | KG스틸 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 663 | 46.91% |
| 034120 | SBS | spin_off | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 86 | 51.16% |
| 0126Z0 | 삼성에피스홀딩스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 400 | 49.00% |
| 487720 | 키움제10호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 663 | 46.91% |
| 019210 | 와이지-원 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2006 | 39.13% |
| 084680 | 이월드 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2006 | 39.13% |
| 019210 | 와이지-원 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2006 | 39.13% |
| 248070 | 솔루엠 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2006 | 39.13% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
