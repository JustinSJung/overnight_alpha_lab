# Learned-Rule Daily Candidate Report - 2026-10-29

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

- Total candidate rows: **136**
- Rows with active learned-rule adjustment: **129**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 55 |
| watchlist_candidate | 49 |
| risk_or_avoid_review | 32 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 017000 | 신원종합개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 032820 | 우리기술 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 097230 | HJ중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 032820 | 우리기술 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 014790 | HL D&I | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 060980 | HL홀딩스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 069920 | 엑시온그룹 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 017040 | 광명전기 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 089030 | 테크윙 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 131760 | 파인텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 420770 | 기가비스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 039740 | 한국정보공학 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 001260 | 남광토건 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 043220 | 티에스넥스젠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 001260 | 남광토건 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 295310 | 에이치브이엠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 295310 | 에이치브이엠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 295310 | 에이치브이엠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 295310 | 에이치브이엠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 295310 | 에이치브이엠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 295310 | 에이치브이엠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 295310 | 에이치브이엠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 295310 | 에이치브이엠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 010400 | 우진아이엔에스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 1085 | 32.63% |
| 052400 | 코나아이 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | -5.0 | 55.0 | watchlist_candidate | mild_negative_learning | 102 | 41.18% |
| 016450 | 한세예스24홀딩스 | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -10.0 | 40.0 | watchlist_candidate | negative_learning | 46 | 32.61% |
| 028260 | 삼성물산 | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -10.0 | 40.0 | watchlist_candidate | negative_learning | 46 | 32.61% |
| 016450 | 한세예스24홀딩스 | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -10.0 | 40.0 | watchlist_candidate | negative_learning | 46 | 32.61% |
| 105630 | 한세실업 | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -10.0 | 40.0 | watchlist_candidate | negative_learning | 46 | 32.61% |
| 105630 | 한세실업 | earnings_guidance | neutral_positive | 50.0 | 0.0 | 0.0 | -10.0 | 40.0 | watchlist_candidate | negative_learning | 46 | 32.61% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
