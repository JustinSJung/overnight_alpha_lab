# Learned-Rule Daily Candidate Report - 2026-10-15

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

- Total candidate rows: **100**
- Rows with active learned-rule adjustment: **75**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 56 |
| general_review | 24 |
| watchlist_candidate | 20 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 065420 | 에스아이리소스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 010400 | 우진아이엔에스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 064350 | 현대로템 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 097230 | HJ중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 017000 | 신원종합개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 351320 | 넥사다이내믹스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 351320 | 넥사다이내믹스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 351320 | 넥사다이내믹스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 351320 | 넥사다이내믹스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 351320 | 넥사다이내믹스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 351320 | 넥사다이내믹스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 351320 | 넥사다이내믹스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 452430 | 사피엔반도체 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 347700 | 스피어 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 351320 | 넥사다이내믹스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 005690 | 파미셀 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 000720 | 현대건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 805 | 27.33% |
| 068270 | 셀트리온 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 266 | 53.76% |
| 293780 | 압타바이오 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 266 | 53.76% |
| 078860 | 아이오케이이엔엠 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 266 | 53.76% |
| 027830 | 대성창투 | spin_off | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 60 | 35.00% |
| 033050 | 제이엠아이 | spin_off | volatile | 30.0 | 0.0 | 0.0 | -5.0 | 25.0 | general_review | mild_negative_learning | 60 | 35.00% |
| 199730 | 바이오인프라 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 276 | 21.01% |
| 290560 | 파라택시스이더리움 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 276 | 21.01% |
| 196170 | 알테오젠 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 276 | 21.01% |
| 122830 | 원포유 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 276 | 21.01% |
| 412540 | 제일엠앤에스 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1313 | 34.58% |
| 412540 | 제일엠앤에스 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1313 | 34.58% |
| 412540 | 제일엠앤에스 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1313 | 34.58% |
| 107590 | 미원홀딩스 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1313 | 34.58% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
