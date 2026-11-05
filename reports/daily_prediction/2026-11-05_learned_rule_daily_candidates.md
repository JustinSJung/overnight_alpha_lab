# Learned-Rule Daily Candidate Report - 2026-11-05

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

- Total candidate rows: **70**
- Rows with active learned-rule adjustment: **53**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 31 |
| watchlist_candidate | 21 |
| risk_or_avoid_review | 18 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 017510 | 세명전기 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 041960 | 코미팜 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 023350 | 한국종합기술 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 254120 | 자비스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 277880 | 티에스아이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 143210 | 핸즈코퍼레이션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 007610 | 선도전기 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 017040 | 광명전기 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 451760 | 컨텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 017000 | 신원종합개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 035890 | 서희건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 101680 | 한국정밀기계 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1283 | 34.06% |
| 005440 | 현대지에프홀딩스 | spin_off | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 88 | 50.00% |
| 326030 | 에스케이바이오팜 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 408 | 50.00% |
| 307180 | 아이엘 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 664 | 46.99% |
| 057050 | 현대홈쇼핑 | spin_off | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 88 | 50.00% |
| 057050 | 현대홈쇼핑 | spin_off | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 88 | 50.00% |
| 057050 | 현대홈쇼핑 | spin_off | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 88 | 50.00% |
| 010130 | 고려아연 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 408 | 50.00% |
| 057050 | 현대홈쇼핑 | spin_off | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 88 | 50.00% |
| 140410 | 메지온 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 408 | 50.00% |
| 180640 | 한진칼 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2036 | 39.10% |
| 066590 | 스모트로닉 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2036 | 39.10% |
| 180640 | 한진칼 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2036 | 39.10% |
| 180640 | 한진칼 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2036 | 39.10% |
| 180640 | 한진칼 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2036 | 39.10% |
| 180640 | 한진칼 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2036 | 39.10% |
| 180640 | 한진칼 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2036 | 39.10% |
| 180640 | 한진칼 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2036 | 39.10% |
| 180640 | 한진칼 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 2036 | 39.10% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
