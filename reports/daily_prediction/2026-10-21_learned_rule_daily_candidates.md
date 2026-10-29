# Learned-Rule Daily Candidate Report - 2026-10-21

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

- Total candidate rows: **77**
- Rows with active learned-rule adjustment: **57**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| watchlist_candidate | 28 |
| risk_or_avoid_review | 27 |
| general_review | 22 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 095910 | 에스에너지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 010950 | S-Oil | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 329180 | HD현대중공업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 009540 | HD한국조선해양 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 009540 | HD한국조선해양 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 009540 | HD한국조선해양 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 009540 | HD한국조선해양 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 187870 | 디바이스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 217330 | 싸이토젠 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 058970 | 엠로 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 002290 | 삼일기업공사 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 122640 | 예스티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 950130 | 엑세스바이오 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 391710 | 코닉오토메이션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 200710 | 에이디테크놀로지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 277880 | 티에스아이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 921 | 30.73% |
| 117670 | 알파칩스 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | -5.0 | 55.0 | watchlist_candidate | mild_negative_learning | 100 | 42.00% |
| 023590 | 다우기술 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 287 | 54.70% |
| 444530 | 심플랫폼 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 287 | 54.70% |
| 088350 | 한화생명 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 287 | 54.70% |
| 097780 | 에코볼트 | spin_off | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 81 | 50.62% |
| 310210 | 보로노이 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 287 | 54.70% |
| 143240 | 사람인 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 287 | 54.70% |
| 028260 | 삼성물산 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 287 | 54.70% |
| 088350 | 한화생명 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 287 | 54.70% |
| 023590 | 다우기술 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 287 | 54.70% |
| 069640 | 한세엠케이 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 1509 | 35.19% |
| 025000 | KPX케미칼 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -5.0 | 5.0 | general_review | mild_negative_learning | 1509 | 35.19% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
